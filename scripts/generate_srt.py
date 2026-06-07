import re
import os
import wave
from pathlib import Path
import math

ROOT = Path(r"d:\NA\Kì 6\Nhập Môn Học Máy\Lab01")
CONCAT_SCRIPT = ROOT / "scripts" / "concat_all.ps1"
MD_SCRIPT = ROOT / "bilingual_narration_script_v3.md"
AUDIO_DIR = ROOT / "assets" / "narration_en"

def get_audio_duration(scene_name):
    # Find the matching wav file
    for p in AUDIO_DIR.glob("*.wav"):
        if p.stem.endswith(f"_{scene_name}"):
            with wave.open(str(p), "rb") as w:
                frames = w.getnframes()
                rate = w.getframerate()
                return frames / float(rate)
    print(f"Warning: Audio for {scene_name} not found.")
    return 0.0

def format_timestamp(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds % 1) * 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

def split_into_sentences(text):
    text = text.replace('"', '').strip()
    text = text.replace('\n', ' ')
    # Add a space after punctuation if missing (but careful not to break decimals)
    text = re.sub(r'([.?!])([A-Z])', r'\1 \2', text)
    # Split by spaces following punctuation
    chunks = re.split(r'(?<=[.!?]) +', text)
    return [c.strip() for c in chunks if c.strip()]

def main():
    # 1. Parse order
    concat_content = CONCAT_SCRIPT.read_text(encoding="utf-8")
    order = []
    for line in concat_content.splitlines():
        m = re.search(r'\(\"[^\"]+\",\s*\"([^\"]+)\"\)', line)
        if m:
            order.append(m.group(1))
            
    # 2. Parse Markdown script
    md_content = MD_SCRIPT.read_text(encoding="utf-8")
    
    # Split by ## Scene
    scene_blocks = re.split(r'\n## Scene ', md_content)
    
    eng_dict = {}
    vie_dict = {}
    
    for block in scene_blocks[1:]:
        lines = block.splitlines()
        header = lines[0]
        m = re.search(r'\((.*?)\)', header)
        if not m:
            continue
        scene_name = m.group(1)
        
        # Extract English
        try:
            eng_start = lines.index("### English")
            vie_start = lines.index("### Tiếng Việt")
            eng_text = "\n".join(lines[eng_start+1:vie_start]).strip()
            
            # Find end of vie_text (could be --- or EOF)
            vie_end = len(lines)
            for i in range(vie_start+1, len(lines)):
                if lines[i].startswith("---"):
                    vie_end = i
                    break
            vie_text = "\n".join(lines[vie_start+1:vie_end]).strip()
            
            eng_dict[scene_name] = eng_text
            vie_dict[scene_name] = vie_text
        except ValueError:
            pass

    # 3. Generate SRTs
    eng_srt = []
    vie_srt = []
    
    current_time = 0.0
    eng_idx = 1
    vie_idx = 1
    
    for scene_name in order:
        duration = get_audio_duration(scene_name)
        if duration == 0:
            print(f"Skipping {scene_name} due to missing audio.")
            continue
            
        eng_text = eng_dict.get(scene_name, "")
        vie_text = vie_dict.get(scene_name, "")
        
        # Process English
        eng_sentences = split_into_sentences(eng_text)
        if eng_sentences:
            total_len = sum(len(s) for s in eng_sentences)
            scene_time = current_time
            for s in eng_sentences:
                s_len = len(s)
                s_dur = duration * (s_len / total_len) if total_len > 0 else 0
                end_time = scene_time + s_dur
                eng_srt.append(f"{eng_idx}")
                eng_srt.append(f"{format_timestamp(scene_time)} --> {format_timestamp(end_time)}")
                eng_srt.append(s)
                eng_srt.append("")
                scene_time = end_time
                eng_idx += 1
                
        # Process Vietnamese
        vie_sentences = split_into_sentences(vie_text)
        if vie_sentences:
            total_len = sum(len(s) for s in vie_sentences)
            scene_time = current_time
            for s in vie_sentences:
                s_len = len(s)
                s_dur = duration * (s_len / total_len) if total_len > 0 else 0
                end_time = scene_time + s_dur
                vie_srt.append(f"{vie_idx}")
                vie_srt.append(f"{format_timestamp(scene_time)} --> {format_timestamp(end_time)}")
                vie_srt.append(s)
                vie_srt.append("")
                scene_time = end_time
                vie_idx += 1
                
        current_time += duration
        
    # Write to files
    (ROOT / "subtitles_en.srt").write_text("\n".join(eng_srt), encoding="utf-8")
    (ROOT / "subtitles_vi.srt").write_text("\n".join(vie_srt), encoding="utf-8")
    
    print(f"Generated subtitles_en.srt ({eng_idx-1} lines)")
    print(f"Generated subtitles_vi.srt ({vie_idx-1} lines)")

if __name__ == "__main__":
    main()
