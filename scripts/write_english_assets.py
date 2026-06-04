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
               """Consider this. An AI is trained to predict diseases from electronic health records.
At Hospital A, it reaches ninety-five percent accuracy. Incredible, right?
But when we test it at Hospital B, the accuracy collapses to seventy-two percent.

Why?

Let's look at the training data.
At Hospital A, a specific doctor wrote the word man for diabetes, and gentleman for arthritis.
The AI exploited this stylistic habit as a shortcut.
At Hospital B, new doctors did not share this habit.
The shortcut disappeared, and the model failed.

The AI didn't fail from lack of data. It failed because it learned the wrong signal."""),
    SceneAudio("0.2", "RoadMap", "Road Map",
               """In this video, we trace eight key stops.
First: the intuition of shortcut learning.
Second: the mathematical formalization of out-of-distribution shifts.
Third: causal graphs.
Fourth: robust methods like IRM and Group DRO.
Finally, we cover benchmarks, foundation models, and how to use AI to fix AI.

Let us begin."""),
    SceneAudio("1.1", "ERMAccuracyIllusion", "ERM and the Accuracy Illusion",
               """Suppose you train a classifier to distinguish penguins from camels.
In your dataset, all penguins are on snow, and camels are on sand.
The classes are perfectly separable.
The model easily achieves ninety-eight percent training accuracy.

But look closely.
The decision boundary only aligns with the background color. It ignores the animal shape.
So, when we place a penguin on sand, the model predicts camel.

The prediction is wrong.
The model relied on a shortcut."""),
    SceneAudio("1.2", "ERMAnatomy", "Why ERM Is Lazy",
               """Empirical Risk Minimization, or ERM, is standard.
Its objective is simple: minimize the average training loss.

But here's the catch.
ERM is lazy. It is indifferent to whether it learns semantic features or simple shortcuts.
From a gradient perspective, counting background pixels is easy, while learning shape features is hard.
Gradient descent takes the path of steepest descent, choosing the shortcut first.

We call these unstable backgrounds spurious features."""),
    SceneAudio("1.3", "SpuriousDefinition", "What Is a Spurious Feature?",
               """What exactly is a spurious feature?

Think about it.
A photographer travels to the Arctic. The penguin is the cause, and the snowy background is the effect.
The causal arrow points from the label to the background.
But the AI reads this arrow in reverse. It sees the background and infers the penguin.

This is anti-causal prediction.
When the environment shifts, this shortcut shatters.
Causal features are stable. Spurious features are brittle."""),
    SceneAudio("1.31", "FormalizingVariables", "Formalizing Variables",
               """Let's formalize this.
X is the input observation, like an image or clinical note.
Y is the target label to predict.
E is the environment or context that generated the data.

A training example is a triplet: X, Y, and E.
Environment labels are the key to separating stable signals from brittle shortcuts."""),
    SceneAudio("1.32", "IDOODDistributions", "ID and OOD Distributions",
               """In standard learning, training and testing data come from the same distribution.
Out-of-distribution generalization breaks this assumption.

The training distribution, P train, is not equal to the test distribution, P test.

The challenge? The classifier must perform well even after this shift occurs."""),
    SceneAudio("1.33", "EnvironmentFormalization", "Environment Formalization",
               """An environment e belongs to the set of possible contexts E.
Each environment induces its own distribution, P-e, over X and Y.

Think of different hospitals using different scanners.
The task is the same, but the data-generating contexts differ.
This is why environment labels are so valuable."""),
    SceneAudio("1.34", "DistributionSet", "Distribution Set",
               """Rather than one train and one test distribution, we look at a family of distributions, script P.

Training exposes us to only a few members.
Deployment might sample from an entirely unseen member.
The goal is not to memorize one distribution. It is to remain stable across the entire set."""),
    SceneAudio("1.4", "GeometryInductiveBias", "Geometry and Inductive Bias",
               """Why does gradient descent consistently prefer shortcuts?

Consider the majority group, where background and label match.
This group represents ninety-five percent of the training data.
The minority group is only five percent.

For ERM, this minority is virtually invisible.
The average loss is dominated by the majority.
Geometrically, the max-margin boundary is pulled toward the majority geometry.
The minority is left with insufficient margin.

The invariant feature is present, but underused."""),
    SceneAudio("2.0", "RiskAggregation", "Risk Aggregation Families",
               """The core of robust learning is risk aggregation.
ERM minimizes average risk.
Group DRO minimizes the worst-case risk over groups.
CVaR focuses on the average of the high-loss tail.

This choice of aggregation operator is the key difference between robust methods."""),
    SceneAudio("2.1", "GroupStructure", "Group Structure",
               """To measure this, we split the training distribution into groups.
We cross the label Y with the spurious attribute Z.

Cows on grass and camels on sand are large majority groups.
Cows on sand and camels on grass are small minority groups.
ERM averages the risk across all groups.
Because the majority dominates, the average risk remains low.

The model sacrifices the minority to minimize average loss."""),
    SceneAudio("2.2", "WorstGroupAccuracy", "Worst-Group Accuracy",
               """To expose this failure, we measure worst-group accuracy.

A standard model might reach eighty-two percent average accuracy, but only eighteen percent worst-group accuracy.
In medicine, the worst-group accuracy represents the real deployment risk.
A model that is wrong on a minority group is unsafe.
We need stability for all groups."""),
    SceneAudio("2.3", "DistributionShiftTypes", "Distribution Shift Types",
               """Not all shifts are the same.
Covariate shift changes the input distribution, P of X.
Label shift changes class proportions, P of Y.

But spurious shift alters the correlation between the shortcut and the label.
This is the hardest shift.
The model's reliance on the shortcut actively leads it astray."""),
    SceneAudio("3.1", "StructuralCausalModel", "Structural Causal Model",
               """Let's build a Structural Causal Model.
The label Y determines the causal features, X-core. This is the stable path.
The environment E determines the background, X-spurious.

During training, Y and E are correlated, creating a spurious link.
The model exploits this link.
But when the environment shifts, this correlation shatters."""),
    SceneAudio("3.2", "ShiftBreaksSpuriousLink", "Shift Breaks Shortcut",
               """When the environment shifts, the link between the label and the background is fractured.
The background changes, and shortcut predictions fail.

But the causal features are invariant.
A penguin still looks like a penguin on a beach.
Causal features are stable. Spurious features are brittle.
We must force the model to rely only on invariant features."""),
    SceneAudio("4.0", "ImportanceWeightingInterpolation", "Importance Weighting and Interpolation",
               """The simplest way to balance groups is importance weighting.
We upweight rare groups in the loss function.

But there's a problem.
Modern networks easily interpolate all training points, reaching zero loss.
When loss is zero, gradients are zero.
Multiplying by weights has no effect.

The model simply memorizes the minority while using the shortcut for the rest."""),
    SceneAudio("4.1", "IRMInvariantIdea", "IRM Idea",
               """Invariant Risk Minimization, or IRM, approaches this differently.
We seek a representation where the optimal classifier is identical across all environments.

If a representation relies on shortcuts, the optimal classifier must change as correlations shift.
If the classifier remains optimal everywhere, it must have discarded spurious features.
This is the core idea of IRM."""),
    SceneAudio("4.2", "IRMFormula", "IRM Formula",
               """IRM translates this into a bi-level optimization problem.
We minimize the risk across all environments, subject to the classifier being optimal in each.

This prevents the model from exploiting local shortcuts.
But this constraint is NP-hard. We need a practical approximation."""),
    SceneAudio("4.3", "IRMGradientVectors", "IRM Gradients",
               """IRMv1 approximates this using a gradient penalty.
If the classifier is optimal, its gradient must be zero.
We add a penalty measuring the squared norm of the gradient at a dummy classifier.

A large penalty indicates the representation relies on shortcuts.
The optimizer is forced to find a representation where gradients from all environments agree."""),
    SceneAudio("4.4", "IRMLimitations", "IRM Limits",
               """IRM faces severe practical limits.
It requires multiple, clearly defined environments.
The gradient penalty is highly sensitive and makes training unstable.
In practice, standard ERM often outperforms IRM.

IRM is elegant in theory, but fragile in practice."""),
    SceneAudio("4.5", "NuRD", "NuRD",
               """Because IRM requires diverse environments, NuRD takes a different approach.
Instead of searching for invariance, it directly filters out nuisance features.

The key condition: the label Y must be independent of the nuisance Z, given the representation.
This mathematically prevents the model from using Z as a shortcut."""),
    SceneAudio("5.1", "GroupDRO", "Group DRO",
               """Group DRO modifies the objective with a single operator: max.
Standard ERM minimizes the average loss, ignoring minority groups.
Group DRO reframes this as a minimax game: minimize model parameters, maximize group loss.

The inner loop identifies the worst group, and the outer loop updates parameters to reduce its risk.
Weights dynamically shift, preventing the model from sacrificing any group.

But here is the catch.
Group DRO requires oracle group labels during training.
If we do not know these groups in advance, the max operator cannot target them.
This is a major practical limitation."""),
    SceneAudio("6.0", "SemanticCorruptions", "Semantic Corruptions",
               """To filter out a nuisance feature, we must detect it.
We use Semantic Corruption.

Think about it.
In NLP, we shuffle word order. If a classifier remains accurate on scrambled text, it is only counting words.
In CV, we apply random patch masking. If a medical model still predicts, it is reading scanner artifacts.
Semantic corruption exposes our shortcuts."""),
    SceneAudio("6.1", "JTT", "Just Train Twice",
               """Just Train Twice, or JTT, lets a standard model identify its own weaknesses.

In Stage One, we train an ERM model for only a few epochs.
It learns easy shortcuts, but doesn't memorize exceptions.
The mistakes it makes are minority examples where the shortcut fails.

In Stage Two, we upweight these mistakes and train a new model.
This simple process massively improves worst-group accuracy, without manual group labels."""),
    SceneAudio("7.1", "ScaleDoesNotSolve", "Scale Does Not Solve It",
               """Does scaling solve this?

If we look at worst-group accuracy, standard ERM plateaus.
Scaling improves average performance but does not eliminate shortcuts.
In fact, larger models have the capacity to learn more complex, high-dimensional shortcuts.

Scale alone is not enough."""),
    SceneAudio("7.2", "CLIPSpuriousWeb", "CLIP and Web Correlations",
               """CLIP represents a unique case.
It is trained on four hundred million image-text pairs using contrastive learning.
It achieves seventy-five percent worst-group accuracy on Waterbirds zero-shot.

Why? Because web data is highly diverse.
But CLIP still inherits web biases, strongly associating terms like doctor with male faces.
With four hundred million examples, the model treats this bias as a true pattern."""),
    SceneAudio("7.3", "ICLShortcuts", "ICL Shortcuts",
               """In large language models, shortcuts emerge dynamically within the prompt during in-context learning.
If all positive examples contain the word movie, the model learns this shortcut.

Here's the catch.
Larger models are more likely to exploit this shortcut, showing reverse scaling.
They are highly sensitive to accidental correlations in the prompt."""),
    SceneAudio("7.4", "ReverseScaling", "Reverse Scaling",
               """Under complex spurious shifts, the linear relationship between ID and OOD accuracy breaks.
We see reverse scaling: larger models perform worse on OOD test sets.

Accuracy on the Line is a special case for simple shifts.
It is not a general law of scaling."""),
    SceneAudio("7.5", "PromptingForRobustness", "Prompting for Robustness",
               """Prompting for Robustness, or PfR, uses a Vision-Language Model to generate group labels automatically.
We prompt the VLM to describe the background of each image.

This avoids expensive manual annotation.
Group DRO trained on these automated labels matches manual label performance, tripling the ERM baseline.
We are using AI to fix AI."""),
    SceneAudio("7.6", "CATO", "CATO",
               """PfR automates annotation, but data scarcity remains.
CATO addresses this by using language models to generate synthetic counterfactual data.

We identify the spurious background and prompt a model to generate counterfactuals: a waterbird on land, or a landbird on water.
Training on this balanced dataset significantly improves robustness.
This completes our narrative: we use large models to fix shortcuts."""),
    SceneAudio("8.1", "BenchmarksReality", "Benchmarks",
               """We evaluate robust algorithms on four standard benchmarks.
First: Waterbirds. It controls bird and background correlations.
Second: CelebA. The task is blonde hair, which strongly correlates with gender.
Third: CivilComments. Toxicity detection, where demographic terms correlate with toxic labels.
Fourth: Camelyon17. Tumor detection, where the scanner model shifts across hospitals."""),
    SceneAudio("8.2", "ModelSelectionParadox", "Model Selection Paradox",
               """This leads to a fundamental challenge: the Model Selection Paradox.
To select a robust model, we need an OOD validation set.
But if we have one, we should train on it.

Selecting models using in-distribution validation sets does not correlate with OOD performance.
This remains an open problem."""),
    SceneAudio("8.3", "BestPractices", "Best Practices",
               """The practical checklist is simple.
Identify the shift type. Report worst-group accuracy. Tune ERM carefully.
Use Group DRO when group labels exist, and JTT when they do not.
For foundation models, tune the last layer first.
And always collect more diverse data."""),
    SceneAudio("9.1", "JourneySummary", "Journey Summary",
               """We have traveled a long path.
From ERM limitations to causal models and foundation model robustness.

This is the key idea.
Robust AI is not about predicting perfectly in every new environment.
It is about identifying the core causal features and relying on them consistently, regardless of context."""),
    SceneAudio("9.2", "OpenProblemsCredits", "Open Problems and Credits",
               """We conclude with three open research directions.
Developing OOD theory for foundation models.
Resolving model selection without OOD validation.
And addressing robustness in multimodal systems.

Thank you for watching."""),
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
