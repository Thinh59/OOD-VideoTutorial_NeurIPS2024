import re
import subprocess
from pathlib import Path
import wave
import sys

ROOT = Path(__file__).resolve().parents[1]
NARRATION_DIR = ROOT / "assets" / "narration_en"
VIDEO_DIR = ROOT / "media" / "videos"
QUALITY_DIR = sys.argv[1] if len(sys.argv) > 1 else "480p15"

SCENE_MAP = {
    "FormalizingXYE": ("module1_erm", "src/module1_erm.py"),
    "OODShiftBreaks": ("module1_erm", "src/module1_erm.py"),
    "DistributionSetFamily": ("module1_erm", "src/module1_erm.py"),
    "GeometricSkewMaxMargin": ("module1_erm", "src/module1_erm.py"),
    "RiskAggregationFamilies": ("module2_framework", "src/module2_framework.py"),
    "IRMRepresentationSpace": ("module4_irm", "src/module4_irm.py"),
    "CausalVsSpuriousTest": ("module3_causality", "src/module3_causality.py"),
    "InvariancePrinciple": ("module4_irm", "src/module4_irm.py"),
    "NuRDDivergencePenalty": ("module4_irm", "src/module4_irm.py"),
    "AvoidingInterpolation": ("module4_irm", "src/module4_irm.py"),
    "JourneySummaryRemastered": ("module9_outro", "src/module9_outro.py"),
    "BigTriangleConclusion": ("module9_outro", "src/module9_outro.py"),

    "OpeningClinicalNotes": ("module0_hook", "src/module0_hook.py"),
    "RoadMap": ("module0_hook", "src/module0_hook.py"),
    "ERMAccuracyIllusion": ("module1_erm", "src/module1_erm.py"),
    "ERMAnatomy": ("module1_erm", "src/module1_erm.py"),
    "SpuriousDefinition": ("module1_erm", "src/module1_erm.py"),
    "FormalizingVariables": ("module2_framework", "src/module2_framework.py"),
    "IDOODDistributions": ("module2_framework", "src/module2_framework.py"),
    "EnvironmentFormalization": ("module2_framework", "src/module2_framework.py"),
    "DistributionSet": ("module2_framework", "src/module2_framework.py"),
    "GeometryInductiveBias": ("module1_erm", "src/module1_erm.py"),
    "RiskAggregation": ("module2_framework", "src/module2_framework.py"),
    "GroupStructure": ("module2_framework", "src/module2_framework.py"),
    "WorstGroupAccuracy": ("module2_framework", "src/module2_framework.py"),
    "DistributionShiftTypes": ("module2_framework", "src/module2_framework.py"),
    "StructuralCausalModel": ("module3_causality", "src/module3_causality.py"),
    "ShiftBreaksSpuriousLink": ("module3_causality", "src/module3_causality.py"),
    "ImportanceWeightingInterpolation": ("module4_irm", "src/module4_irm.py"),
    "IRMInvariantIdea": ("module4_irm", "src/module4_irm.py"),
    "IRMFormula": ("module4_irm", "src/module4_irm.py"),
    "IRMGradientVectors": ("module4_irm", "src/module4_irm.py"),
    "IRMLimitations": ("module4_irm", "src/module4_irm.py"),
    "NuRD": ("module4_irm", "src/module4_irm.py"),
    "GroupDRO": ("module5_dro", "src/module5_dro.py"),
    "SemanticCorruptions": ("module6_jtt", "src/module6_jtt.py"),
    "JTT": ("module6_jtt", "src/module6_jtt.py"),
    "ScaleDoesNotSolve": ("module7_foundation", "src/module7_foundation.py"),
    "CLIPSpuriousWeb": ("module7_foundation", "src/module7_foundation.py"),
    "ICLShortcuts": ("module7_foundation", "src/module7_foundation.py"),
    "ReverseScaling": ("module7_foundation", "src/module7_foundation.py"),
    "PromptingForRobustness": ("module7_foundation", "src/module7_foundation.py"),
    "CATO": ("module7_foundation", "src/module7_foundation.py"),
    "BenchmarksReality": ("module8_benchmarks", "src/module8_benchmarks.py"),
    "ModelSelectionParadox": ("module8_benchmarks", "src/module8_benchmarks.py"),
    "BestPractices": ("module8_benchmarks", "src/module8_benchmarks.py"),
    "JourneySummary": ("module9_outro", "src/module9_outro.py"),
    "OpenProblemsCredits": ("module9_outro", "src/module9_outro.py")
}

def get_wav_duration(path: Path) -> float:
    with wave.open(str(path), "rb") as w:
        frames = w.getnframes()
        rate = w.getframerate()
        return frames / float(rate)

def get_mp4_duration(path: Path) -> float:
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "csv=p=0", str(path)
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return float(res.stdout.strip())
    except Exception as e:
        print(f"Error getting duration for {path}: {e}")
        return 0.0

def adjust_scene_wait(file_path: Path, scene_name: str, delta: float):
    if not file_path.exists():
        print(f"Source file {file_path} not found.")
        return False
    
    content = file_path.read_text(encoding="utf-8")
    
    # Locate the class definition
    class_pattern = rf"(class\s+{scene_name}\b.*?)(?=\nclass\s+|\Z)"
    match = re.search(class_pattern, content, re.DOTALL)
    if not match:
        print(f"Class {scene_name} not found in {file_path}")
        return False
    
    class_body = match.group(1)
    
    # Look for self.wait(...) calls in the class body
    wait_pattern = r"self\.wait\(\s*([0-9\.]+)\s*\)"
    waits = list(re.finditer(wait_pattern, class_body))
    
    if waits:
        # Get the last self.wait call
        last_wait = waits[-1]
        old_val = float(last_wait.group(1))
        new_val = max(1.0, round(old_val + delta, 2))
        
        # Replace the last wait call with the new value
        new_wait_str = f"self.wait({new_val})"
        start_idx = last_wait.start()
        end_idx = last_wait.end()
        
        new_class_body = class_body[:start_idx] + new_wait_str + class_body[end_idx:]
        new_content = content[:match.start()] + new_class_body + content[match.end():]
        file_path.write_text(new_content, encoding="utf-8")
        print(f"Adjusted final wait in {scene_name} from {old_val} to {new_val} (delta {delta:+.2f}s)")
        return True
    else:
        # If no self.wait exists, append one
        lines = class_body.splitlines()
        indent = "        " # default fallback
        for line in lines:
            if "def construct" in line:
                m = re.match(r"^(\s+)", line)
                if m:
                    indent = m.group(1) + "    "
                break
        
        new_val = max(1.0, round(delta, 2))
        new_class_body = class_body.rstrip() + f"\n{indent}self.wait({new_val})\n"
        new_content = content[:match.start()] + new_class_body + content[match.end():]
        file_path.write_text(new_content, encoding="utf-8")
        print(f"Appended self.wait({new_val}) to {scene_name} (delta {delta:+.2f}s)")
        return True

def main():
    wav_files = sorted(NARRATION_DIR.glob("*.wav"))
    needs_rebuild = []
    
    for wav_path in wav_files:
        name = wav_path.stem
        # Extract scene name
        parts = name.split("_")
        if len(parts) < 3:
            continue
        scene_name = parts[-1]
        
        if scene_name not in SCENE_MAP:
            print(f"Warning: Scene {scene_name} not found in map.")
            continue
        
        module, py_rel = SCENE_MAP[scene_name]
        py_path = ROOT / py_rel
        mp4_path = VIDEO_DIR / module / QUALITY_DIR / f"{scene_name}.mp4"
        
        wav_dur = get_wav_duration(wav_path)
        target_dur = wav_dur + 1.0 # 1 second buffer at the end of audio
        
        if not mp4_path.exists():
            print(f"Scene {scene_name}: Video not rendered yet (Audio={wav_dur:.1f}s). Adding to build list.")
            needs_rebuild.append((py_rel, scene_name))
            continue
            
        mp4_dur = get_mp4_duration(mp4_path)
        delta = target_dur - mp4_dur
        
        if abs(delta) > 0.3:
            print(f"Scene {scene_name}: Audio={wav_dur:.1f}s, Target Video={target_dur:.1f}s, Current Video={mp4_dur:.1f}s. Adjusting...")
            adjust_scene_wait(py_path, scene_name, delta)
            needs_rebuild.append((py_rel, scene_name))
        else:
            print(f"Scene {scene_name}: OK (Audio={wav_dur:.1f}s, Target={target_dur:.1f}s, Video={mp4_dur:.1f}s, Delta={delta:+.2f}s)")
            
    if needs_rebuild:
        print("\nThe following scenes need to be (re-)rendered:")
        for py_rel, scene_name in needs_rebuild:
            print(f"  manim -ql {py_rel} {scene_name}")
        sys.exit(1)
    else:
        print("\nAll scene timings are aligned!")
        sys.exit(0)

if __name__ == "__main__":
    main()
