from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "kich_ban_v2_OOD_3b1b.md"
OUT_DIR = ROOT / "assets" / "narration"


@dataclass
class SceneAudio:
    scene_id: str
    title: str
    audio: str
    seconds: int


def clean_audio(raw: str) -> str:
    text = raw.strip()
    text = re.sub(r"^#+\s*AUDIO[^\n]*\n", "", text, flags=re.IGNORECASE).strip()
    text = text.strip().strip('"').strip()
    text = text.replace("—", "-")
    return re.sub(r"\n{3,}", "\n\n", text)


def estimate_seconds(text: str) -> int:
    words = re.findall(r"\w+", text, flags=re.UNICODE)
    # Vietnamese narration at about 135 words/minute, plus small pause margin.
    return max(8, round(len(words) / 135 * 60 + 2))


def parse_scenes(markdown: str) -> list[SceneAudio]:
    heading_pattern = re.compile(r"^## Scene ([\d.]+) — (.+)$", re.MULTILINE)
    matches = list(heading_pattern.finditer(markdown))
    scenes: list[SceneAudio] = []
    for idx, match in enumerate(matches):
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(markdown)
        block = markdown[start:end]
        audio_match = re.search(r"^### AUDIO[^\n]*\n(?P<audio>.*?)(?=\n---|\n## Scene|\Z)", block, flags=re.MULTILINE | re.DOTALL)
        if not audio_match:
            continue
        audio = clean_audio(audio_match.group("audio"))
        scenes.append(SceneAudio(match.group(1), match.group(2).strip(), audio, estimate_seconds(audio)))
    return scenes


def srt_time(total_seconds: int) -> str:
    h, rem = divmod(total_seconds, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02}:{m:02}:{s:02},000"


def chunk_text(text: str, max_chars: int = 92) -> list[str]:
    sentences = re.split(r"(?<=[.!?])\s+", text.replace("\n", " "))
    chunks: list[str] = []
    current = ""
    for sent in sentences:
        if not sent:
            continue
        if len(current) + len(sent) + 1 <= max_chars:
            current = f"{current} {sent}".strip()
        else:
            if current:
                chunks.append(current)
            current = sent
    if current:
        chunks.append(current)
    return chunks


def write_scene_srt(scene: SceneAudio, path: Path):
    chunks = chunk_text(scene.audio)
    per = max(2, scene.seconds // max(1, len(chunks)))
    cursor = 0
    lines: list[str] = []
    for i, chunk in enumerate(chunks, start=1):
        start = cursor
        end = scene.seconds if i == len(chunks) else min(scene.seconds, cursor + per)
        lines.append(f"{i}\n{srt_time(start)} --> {srt_time(end)}\n{chunk}\n")
        cursor = end
    path.write_text("\n".join(lines), encoding="utf-8")


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    scenes = parse_scenes(SCRIPT.read_text(encoding="utf-8"))
    (OUT_DIR / "voiceover_script.md").write_text(
        "\n\n".join(f"## Scene {s.scene_id} - {s.title}\n\n{s.audio}" for s in scenes),
        encoding="utf-8",
    )
    manifest = ["scene_id,title,seconds,text_file,srt_file"]
    for scene in scenes:
        stem = f"scene_{scene.scene_id.replace('.', '_')}"
        text_path = OUT_DIR / f"{stem}.txt"
        srt_path = OUT_DIR / f"{stem}.srt"
        text_path.write_text(scene.audio, encoding="utf-8")
        write_scene_srt(scene, srt_path)
        manifest.append(f'{scene.scene_id},"{scene.title.replace(chr(34), chr(34)*2)}",{scene.seconds},{text_path.name},{srt_path.name}')
    (OUT_DIR / "manifest.csv").write_text("\n".join(manifest) + "\n", encoding="utf-8")
    print(f"Extracted {len(scenes)} scenes to assets/narration")


if __name__ == "__main__":
    main()
