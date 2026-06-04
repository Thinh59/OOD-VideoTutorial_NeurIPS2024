# SCRIPT V3 — PART XI
## Benchmark Crisis

---

# PART XI — BENCHMARKS & REALITY CHECK

---

## Scene B1 — Gallery Benchmark: 4 Realistic Battlegrounds
**~2 minutes**

### VISUAL
- 2×2 grid showing four standard benchmarks. They appear one-by-one:

**[Waterbirds]** [BLUE_D frame]
- Icon: Bird + Water/Land background
- Task: Classify waterbird vs. landbird
- Spurious attribute: Background (water vs. land)
- Train size: 4,795 images. WG Gap: ~50%
- Note: "Synthetic correlation — background is perfectly controlled."

**[CelebA]** [GREEN_D frame]
- Icon: Human face
- Task: Classify hair color (blonde vs. non-blonde)
- Spurious attribute: Gender (female vs. male)
- Train size: 162,770 images. WG Gap: ~40%
- Note: "Real-world dataset — captures demographic biases in celebrity media."

**[CivilComments-WILDS]** [YELLOW_D frame]
- Icon: Text bubble
- Task: Toxicity detection
- Spurious attribute: Mention of demographic identities (race, religion, gender)
- Train size: 269,038 comments. WG Gap: ~35%
- Note: "High-stakes application — real-world content moderation."

**[Camelyon17-WILDS]** [PURPLE frame]
- Icon: Microscope slide
- Task: Tumor detection
- Spurious attribute: Hospital scanner artifacts
- Train size: 302,436 patches. WG Gap: ~30%
- Note: "Medical AI — different scanner profiles act as shortcuts."

### AUDIO
"To evaluate these robust algorithms, the machine learning community has established several standard benchmarks.

First: Waterbirds. This is a synthetic dataset where the correlation between the bird type and the background is controlled. It provides a clean testbed to evaluate algorithms under structured shifts.

Second: CelebA. This contains celebrity images. The task is to predict blonde hair, but because blonde hair is strongly correlated with female faces in the dataset, standard models learn that blonde equals female.

Third: CivilComments. This is a text dataset for online toxicity detection. Here, mentions of specific demographic groups — such as religions or races — are highly correlated with toxic labels, leading models to flag benign sentences containing these words.

Fourth: Camelyon17. A medical dataset for tumor detection. The shortcut here is the scanner model used at different hospitals. Instead of analyzing the tissue pathology, models learn to recognize the scanner signature of the training hospital."

---

## Scene B2 — Benchmark Disagreement: Mixed Results
**~2 minutes**

### VISUAL
- Grouped bar chart comparing 5 methods across the 4 datasets:
  ERM [GRAY], IRM [BLUE_D], Group DRO [GREEN_D], JTT [YELLOW_D], CORAL [PURPLE]
- Key findings are highlighted sequentially:
  1. A well-tuned ERM baseline is competitive with or outperforms robust methods on several datasets [ORANGE highlight].
  2. IRM performs well on Waterbirds but fails on CivilComments [RED dashes].
  3. Group DRO is strong when labels are available, but is highly sensitive to label noise.
  4. No single method consistently outperforms the others across all benchmarks [Large RED X].
- Pearson correlation heatmap between dataset performances:
  Mostly cool colors (low correlation) → "Performance on one benchmark does not predict performance on another."
- Text: "BENCHMARK DISAGREEMENT — No universal winner."

### AUDIO
"The empirical results on these benchmarks reveal a sobering truth: no single algorithm consistently outperforms the others.

In fact, a carefully tuned ERM baseline — where learning rates, weight decays, and data augmentations are optimized — often matches or exceeds the performance of more complex robust algorithms.

IRM performs well on Waterbirds but struggles on CivilComments. Group DRO is highly effective when group labels are clean, but is sensitive to noise. JTT is flexible but rarely leads the board.

A Pearson correlation analysis of model performance across these datasets shows very low correlation. Winning on Waterbirds does not predict success on CivilComments. The benchmarks are measuring distinct dimensions of robustness.

This inconsistency raises a deeper question: is the limitation in the algorithms themselves, or does it lie in the design of the benchmarks?"

---

## Scene B3 — Are Benchmarks Realistic?
**~90 seconds**

### VISUAL
- Waterbirds synthetic setup: Spurious correlation is fixed at exactly 95%.
  Question: "Are real-world shifts this structured and clean?"
- CelebA: Celebrity photos do not represent the demographics of the general population.
  "Celebrity bias ≠ real-world deployment bias."
- Plot: OOD gap in Waterbirds (lab) vs. OOD gap in clinical EHR (real world).
  Lab gap: structured and predictable. Real-world gap: messy, multi-source, and unpredictable.
- Text: "Benchmarks offer control, but oversimplify real-world shifts."
- Orange box: "Winning a benchmark does not guarantee safety in deployment."

### AUDIO
"To understand why algorithms fail to transfer, we must examine the realism of our benchmarks.

Waterbirds uses a synthetic spurious correlation fixed at ninety-five percent. In real-world deployments, distribution shifts are rarely this clean or structured. They are noisy, multi-source, and change unpredictably over time.

CelebA relies on celebrity images, which feature specific lighting, poses, and demographics that do not generalize to the general public.

As a result, an algorithm that is optimized to exploit the artificial structure of a benchmark may fail to generalize to real-world data. We are tuning models to win benchmarks, rather than to achieve true robustness."

---

## Scene B4 — Model Selection Paradox
**~90 seconds**

### VISUAL
- Circular flowchart (Model Selection Loop):
  "Select the best OOD model"
  → "Requires an OOD validation set"
  → "If we have an OOD validation set, why not train on it?"
  → "Training on it makes it in-distribution!"
  → Loop repeats.
- Center text in GOLD: "THE MODEL SELECTION PARADOX"
- Two imperfect choices are presented:
  - Option A: Use an in-distribution validation set → fails to guarantee OOD performance.
  - Option B: Assume access to the test distribution → unrealistic for real-world deployment.
- Text: "An open research problem with no simple solution."

### AUDIO
"This leads to a fundamental challenge in robust machine learning: the Model Selection Paradox.

To deploy a robust model, we must select the best candidate from our training runs. This selection requires an out-of-distribution validation set.

But if we have access to an OOD validation set, the most logical step is to include it in the training data to improve the model. Once we do, that data is no longer out-of-distribution.

Selecting models based on in-distribution validation sets does not correlate well with OOD performance. This paradox remains one of the most critical open problems in the field.

Given these limitations, how do we approach OOD generalization in practice? And do Foundation Models change this landscape?"

---

## Scene B5 — Best Practices: Practical Flowchart
**~2 minutes**

### VISUAL
- Decision flowchart, highlighting nodes sequentially:
  ```
  START
    ↓
  Identify the Shift Type
  (Covariate / Label / Spurious)
    ↓
  Are Group Labels Available?
    ├─ YES  → Use Group DRO
    └─ NO   → Use JTT or NuRD
    ↓
  Are Diverse Environments Available?
    ├─ YES  → Apply IRM Penalty
    └─ NO   → Focus on data collection
    ↓
  Are you using a Foundation Model?
    ├─ YES  → Apply Prompting for Robustness (PfR) or Last Layer Retraining
    └─ NO   → Optimize ERM baseline first
    ↓
  ALWAYS report Worst-Group Accuracy
  ```
- The entire flowchart glows in GOLD.

### AUDIO
"The tutorial distills these findings into seven practical recommendations.

First: identify the type of distribution shift before selecting an algorithm. Second: always report worst-group accuracy, not just the average. Third: optimize your ERM baseline thoroughly before implementing complex algorithms. Fourth: if group labels are available, Group DRO is your strongest starting point. Fifth: if group labels are missing, use JTT or NuRD. Sixth: when working with foundation models, evaluate last-layer retraining first. Seventh: prioritize collecting more diverse data — data diversity is often more effective than algorithmic interventions.

With this framework in place, we can address the latest shift in the machine learning landscape: how do foundation models change the nature of shortcut learning?"
