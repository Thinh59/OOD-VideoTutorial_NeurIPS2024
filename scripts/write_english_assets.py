from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "narration_en"


@dataclass
class SceneAudio:
    scene_id: str
    scene_name: str
    title: str
    audio: str


SCENES = [
    SceneAudio("0.1", "OpeningClinicalNotes", "Opening: Clinical Notes",
               "Start with a real clinical example. An AI system is trained to predict disease from electronic health records. At Hospital A, it reaches ninety five percent accuracy. But when the same model is moved to Hospital B, accuracy drops sharply. What happened? In the training hospital, one doctor often wrote the word man for diabetes cases, and gentleman for arthritis cases. The words are almost synonyms, but the model treated them as a shortcut. In Hospital B, that writing habit disappeared, and the shortcut collapsed. This is the core problem: the model did not learn medicine. It learned the wrong signal."),
    SceneAudio("0.2", "RoadMap", "Road Map",
               "This video follows six stops. First, why empirical risk minimization learns shortcuts. Then, how causality names the problem. After that, we cover IRM, Group DRO, and JTT. Finally, we look at foundation models, benchmarks, and practical best practices."),
    SceneAudio("1.1", "ERMAccuracyIllusion", "ERM and the Accuracy Illusion",
               "Imagine training a classifier for penguins and camels. In the training set, penguins are always on snow, and camels are always on sand. The model can get very high training accuracy by reading the background. But when a penguin appears on sand, the same rule predicts camel. The accuracy looked good, but the learned feature was wrong."),
    SceneAudio("1.2", "ERMAnatomy", "Why ERM Is Lazy",
               "Empirical risk minimization has one goal: reduce average loss on the training distribution. It does not know whether the loss drops because the model understands the animal, or because it found an easy background cue. Gradient descent often follows the fastest path to lower loss. If counting snow pixels is easier than recognizing body shape, ERM will happily use that shortcut."),
    SceneAudio("1.3", "SpuriousDefinition", "What Is a Spurious Feature?",
               "A spurious feature is a correlation that works in one environment but is not stable. A photographer chooses the Arctic because they want a penguin photo, so snow becomes correlated with penguins. The model reads the arrow backwards: snow means penguin. When the environment changes to a desert, that correlation breaks. Causal features remain stable; spurious features are brittle."),
    SceneAudio("1.4", "GeometryInductiveBias", "Geometry and Inductive Bias",
               "There is also a geometric reason shortcuts win. A simple model of the input is x equals y times the invariant feature, plus y times z times the nuisance feature, plus noise. Majority groups pull the max margin classifier toward the nuisance direction. The resulting boundary can cut through minority groups even when the invariant feature is present."),
    SceneAudio("2.1", "GroupStructure", "Group Structure",
               "To measure this failure, split the data into groups defined by the label and the spurious feature. Most examples may be natural combinations, such as cow on grass and camel on sand. The rare groups, such as cow on sand, are small but important. Average accuracy can look strong while the minority groups fail badly."),
    SceneAudio("2.2", "WorstGroupAccuracy", "Worst-Group Accuracy",
               "Worst-group accuracy asks how well the model performs on its weakest group. A model with higher average accuracy can still be unsafe if one group is almost always wrong. In deployment, the weakest group is often where the real harm appears."),
    SceneAudio("2.3", "DistributionShiftTypes", "Distribution Shift Types",
               "Not every distribution shift is the same. Covariate shift changes the input distribution. Label shift changes class proportions. Spurious shift changes or flips the relationship between the shortcut and the label. This tutorial focuses on that third case."),
    SceneAudio("3.1", "StructuralCausalModel", "Structural Causal Model",
               "A causal graph separates stable features from unstable context. Core features point to the label. The environment affects spurious features. If a representation depends on the stable path, it has a better chance of generalizing out of distribution."),
    SceneAudio("3.2", "ShiftBreaksSpuriousLink", "Shift Breaks Shortcut",
               "In the training environment, penguin and snow appear together. In a new environment, penguin and sand may appear together instead. A background shortcut cannot survive this change, while shape remains useful."),
    SceneAudio("4.0", "ImportanceWeightingInterpolation", "Importance Weighting and Interpolation",
               "A basic correction is importance weighting. Examples from rare combinations receive larger weights, using the ratio of the label probability to the conditional probability given the nuisance attribute. But in over parameterized neural networks, interpolation changes the story. Once the model can fit every training point with zero loss, weighting and penalties can be bypassed by memorization."),
    SceneAudio("4.1", "IRMInvariantIdea", "IRM Idea",
               "Invariant Risk Minimization asks for a representation where the same classifier works across environments. If the best decision rule changes from one environment to another, the model is probably using a spurious feature. If the rule stays fixed, it is more likely to rely on causal information."),
    SceneAudio("4.2", "IRMFormula", "IRM Formula",
               "IRM turns the invariance idea into a penalty. The objective still includes risk across environments, but adds a gradient penalty that encourages the same classifier to be optimal everywhere. In practice, this is hard to optimize, but the geometric idea is important."),
    SceneAudio("4.3", "IRMGradientVectors", "IRM Gradients",
               "One way to picture IRM is to look at gradients from different environments. If the gradients point in conflicting directions, one representation cannot satisfy them all. IRM tries to make those directions align."),
    SceneAudio("4.4", "IRMLimitations", "IRM Limits",
               "IRM is elegant, but not a silver bullet. It needs multiple diverse environments, it is sensitive to optimization details, and invariant solutions can still be wrong in some counterexamples."),
    SceneAudio("4.5", "NuRD", "NuRD",
               "NuRD stands for Nuisance Randomized Distillation. The goal is to learn a representation phi of X that filters out nuisance information Z. After filtering, the predictor should use only the clean representation. In notation, Y is independent of Z given phi of X."),
    SceneAudio("5.1", "GroupDRO", "Group DRO",
               "Group DRO changes the objective from average risk to worst-group risk. Instead of letting large groups dominate the loss, it puts extra weight on the group that is currently performing worst. This is powerful when group labels are available."),
    SceneAudio("6.0", "SemanticCorruptions", "Semantic Corruptions",
               "Semantic corruptions test whether a model still predicts after the real meaning is hidden. In an X ray, cover the heart region. If the model still predicts cardiomegaly, it may be using a shortcut outside the heart. In language, n gram randomization plays a similar role by damaging local semantic cues."),
    SceneAudio("6.1", "JTT", "Just Train Twice",
               "JTT works when group labels are missing. First train a standard ERM model. Then collect the examples it gets wrong, which often include minority or hard groups. Finally, upweight those examples and train again."),
    SceneAudio("7.1", "ScaleDoesNotSolve", "Scale Does Not Solve It",
               "Foundation models are larger and more capable, but scale alone does not remove shortcut learning. Large models can still rely on dataset artifacts, web correlations, or prompt patterns."),
    SceneAudio("7.2", "CLIPSpuriousWeb", "CLIP and Web Correlations",
               "CLIP learns from image and text pairs on the web. That gives it broad visual knowledge, but also exposes it to web correlations. Some correlations are useful. Others are spurious and can leak into the representation."),
    SceneAudio("7.3", "ICLShortcuts", "ICL Shortcuts",
               "In-context learning can create shortcuts inside the prompt itself. If every positive example in the prompt contains the word movie, the model may learn movie means positive instead of learning the sentiment task."),
    SceneAudio("7.4", "ReverseScaling", "Reverse Scaling",
               "Reverse scaling means a larger model can become more sensitive to a shortcut. For in-context learning, bigger models are better at reading patterns in the prompt, including patterns that are accidental."),
    SceneAudio("7.5", "PromptingForRobustness", "Prompting for Robustness",
               "Prompting for Robustness uses a large vision language model to label spurious attributes automatically. For Waterbirds, a VLM can describe whether the background is water or land. Those labels can then feed Group DRO, improving worst-group performance."),
    SceneAudio("7.6", "CATO", "CATO",
               "CATO uses causal reasoning and language models to create counterfactual data. If background is the spurious feature, the system can generate examples that flip the background while preserving the label. This helps balance rare groups."),
    SceneAudio("8.1", "BenchmarksReality", "Benchmarks",
               "Benchmarks such as Waterbirds, CelebA, Camelyon17, and CivilComments test robustness under real or realistic shifts. The results are mixed. No method wins everywhere, and a carefully tuned ERM baseline is often surprisingly competitive."),
    SceneAudio("8.2", "ModelSelectionParadox", "Model Selection Paradox",
               "Model selection is a practical open problem. To pick the best OOD model, you want an OOD validation set. But if you have that set, you might be tempted to train on it, and then it is no longer truly out of distribution."),
    SceneAudio("8.3", "BestPractices", "Best Practices",
               "The practical checklist is simple. Identify the shift type. Report worst-group accuracy. Tune ERM carefully. Use Group DRO when group labels exist. Use JTT or clustering when they do not. For foundation models, try the last layer first. And whenever possible, collect more diverse data."),
    SceneAudio("9.1", "JourneySummary", "Journey Summary",
               "The journey moves from correlation, to causation, to stability. ERM can learn shortcuts. Causal structure explains why those shortcuts fail. Robust methods try to force the model toward stable features. In foundation models, the problem does not disappear; it changes form."),
    SceneAudio("9.2", "OpenProblemsCredits", "Open Problems and Credits",
               "Open problems remain: OOD theory for foundation models, model selection without OOD validation, and robustness for multimodal and agentic AI. This video is based on the NeurIPS 2024 tutorial, Out-of-Distribution Generalization: Shortcuts, Spuriousness and Stability."),
]


def estimate_seconds(text: str) -> int:
    words = re.findall(r"\w+", text)
    return max(8, round(len(words) / 145 * 60 + 2))


def srt_time(total_seconds: int) -> str:
    h, rem = divmod(total_seconds, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02}:{m:02}:{s:02},000"


def chunks(text: str, max_chars: int = 84) -> list[str]:
    sentences = re.split(r"(?<=[.!?])\s+", text)
    out: list[str] = []
    cur = ""
    for sentence in sentences:
        if len(cur) + len(sentence) + 1 <= max_chars:
            cur = f"{cur} {sentence}".strip()
        else:
            if cur:
                out.append(cur)
            cur = sentence
    if cur:
        out.append(cur)
    return out


def write_srt(scene: SceneAudio, path: Path):
    total = estimate_seconds(scene.audio)
    parts = chunks(scene.audio)
    per = max(2, total // max(1, len(parts)))
    cursor = 0
    blocks = []
    for idx, text in enumerate(parts, start=1):
        end = total if idx == len(parts) else min(total, cursor + per)
        blocks.append(f"{idx}\n{srt_time(cursor)} --> {srt_time(end)}\n{text}\n")
        cursor = end
    path.write_text("\n".join(blocks), encoding="utf-8")


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    manifest = ["scene_id,scene_name,title,seconds,text_file,srt_file"]
    script = []
    for scene in SCENES:
        stem = f"scene_{scene.scene_id.replace('.', '_')}_{scene.scene_name}"
        text_file = OUT_DIR / f"{stem}.txt"
        srt_file = OUT_DIR / f"{stem}.srt"
        text_file.write_text(scene.audio + "\n", encoding="utf-8")
        write_srt(scene, srt_file)
        manifest.append(f'{scene.scene_id},{scene.scene_name},"{scene.title}",{estimate_seconds(scene.audio)},{text_file.name},{srt_file.name}')
        script.append(f"## Scene {scene.scene_id} - {scene.title}\n\n{scene.audio}")
    (OUT_DIR / "manifest.csv").write_text("\n".join(manifest) + "\n", encoding="utf-8")
    (OUT_DIR / "voiceover_script.md").write_text("\n\n".join(script) + "\n", encoding="utf-8")
    print(f"Wrote {len(SCENES)} English narration scenes to assets/narration_en")


if __name__ == "__main__":
    main()
