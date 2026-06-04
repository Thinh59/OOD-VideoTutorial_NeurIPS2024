# SCRIPT V3 — PART VIII, IX, X
## NuRD + Group DRO + JTT

---

# PART VIII — NuRD: "Filtering out the Nuisance"

---

## Scene N1 — NuRD: Core Idea
**~90 seconds**

### VISUAL
- Title: "NuRD — Nuisance-Randomized Distillation"
- Simple pipeline:
  `[X] → [Φ: Encoder] → [Φ(X): Representation] → [w] → [Ŷ]`
- Central question: "How do we know if Φ(X) still contains the nuisance variable Z?"
- Independence condition appears in GOLD:
  `Y ⊥ Z | Φ(X)`
- Component explanation:
  - Y ⊥ Z: "Y and Z are independent..."
  - | Φ(X): "...given the learned representation."
  - Intuition: "Φ(X) contains no information about Z beyond what is already captured by Y."
- Diagram: Z is filtered out of Φ(X), leaving only the Y-relevant causal information.

### AUDIO
"Because Invariant Risk Minimization faces practical challenges when environments lack diversity, Nuisance-Randomized Distillation, or NuRD, approaches the problem from a different angle. Instead of searching for invariance across environments, NuRD directly filters out the nuisance features from the representation.

The core condition of NuRD is that the label Y must be independent of the nuisance attribute Z, conditioned on the representation Phi of X.

In simple terms, once we extract the representation Phi of X, it should contain no residual information about the nuisance attribute Z that could be exploited by a classifier.

If this condition holds, any model trained on Phi of X is mathematically prevented from using Z as a shortcut.

But how do we identify the nuisance attribute Z in practice?"

---

## Scene N2 — Detecting Nuisance: Semantic Corruption
**~90 seconds**

### VISUAL
- NLP example: Original sentence: "The movie was incredible and the acting superb."
- Step 1 — N-gram randomization: The words are shuffled:
  "incredible was The movie and superb acting the."
  Label: "N-gram randomized — semantics destroyed, n-gram bias preserved"
- Step 2 — Feed the corrupted sentence to the model.
  If the model still predicts positive with high confidence → it is relying on n-gram shortcuts, not semantic understanding.
- Animation: Original sentence [BLUE_D] → Shuffled [ORANGE] → Model prediction → High accuracy [RED flash].
- Text: "Semantic Corruption = Physical intervention to expose shortcuts."
- Parallel vision example: X-ray image → masking random patches → model still predicts cardiomegaly.
  "Model relies on scanner artifacts, not clinical indicators."

### AUDIO
"To filter out a nuisance feature, we must first detect it.

We do this using a technique called Semantic Corruption. The intuition is straightforward: if we destroy the semantic meaning of the input while preserving the spurious shortcut, and the model still predicts successfully, it is relying on the shortcut.

In natural language processing, we shuffle the word order. The semantic meaning is lost, but the word frequencies and n-gram statistics remain. If a sentiment classifier maintains eighty percent accuracy on this shuffled text, it is merely counting words, not understanding sentiment.

In computer vision, we apply random patch masking. If a medical classifier still detects a disease after the diagnostic region is masked, it is likely reading scanner artifacts or hospital-specific markers.

Semantic corruption exposes the specific shortcuts our models are exploiting."

---

## Scene N3 — Vision Masking: Diagnostic through Occlusion
**~90 seconds**

### VISUAL
- Image of a bird on water [BLUE_D frame].
- Attention map / GradCAM: Highlight that the ERM model focuses primarily on the background water, not the bird [RED glow].
- Masking Step: The background is masked, leaving only the bird.
  The model's prediction drops to 60% accuracy.
  "Evidence: model relies on background."
- Reverse Masking Step: The bird is masked, leaving only the background.
  The model predicts "Waterbird" with high accuracy.
  [RED flash] "Confirmation: background is the primary shortcut."
- Text: "Vision Masking = Semantic Corruption for images."

### AUDIO
"For visual data, semantic corruption takes the form of Vision Masking.

Consider an ERM model trained on the Waterbirds dataset. By examining its attention map or GradCAM outputs, we can see where the model is looking. Often, it focuses almost entirely on the background rather than the bird.

We verify this by masking the background. When evaluated on the bird alone, the model's accuracy drops significantly.

Conversely, if we mask the bird and leave only the background, the model still classifies the image correctly. This confirms that the background is acting as the primary shortcut.

Vision masking is a diagnostic tool: it tells us both that a shortcut is being used, and exactly what that shortcut is."

---

## Scene N4 — Teacher-Student Distillation
**~2 minutes**

### VISUAL
- Two models side-by-side:
  - Teacher [ORANGE, large]: Trained on corrupted inputs (e.g., shuffled text or masked images).
    → "Teacher only learns shortcuts (Z) because semantics are destroyed."
  - Student [BLUE_D, smaller]: Trained on original inputs.
- Distillation process:
  `Teacher(X_corrupted) → soft labels [p₁, p₂, ...]`
  `Student objective: predict Y AND diverge from Teacher`
- Formula:
  `L_student = L_CE(ŷ, y) + α · L_KL(f_student(X) ‖ f_teacher(X_corrupted))`
  Note the positive sign: the Student is penalized for mimicking the Teacher.
- Animation: The Teacher is confident about the background. The Student is forced to look elsewhere, learning the animal's shape.
- Text: "The Teacher teaches the Student what NOT to learn."

### AUDIO
"NuRD exploits this diagnostic via a Teacher-Student distillation framework.

First, we train a Teacher model exclusively on corrupted inputs, where the semantic features have been destroyed. Because the semantic signal is gone, the Teacher is forced to rely entirely on spurious shortcuts.

Next, we train a Student model on the original, clean inputs with a dual objective: predict the ground-truth label Y, while simultaneously diverging from the predictions of the Teacher.

Because the Teacher has captured the shortcuts, the divergence penalty forces the Student to ignore those same shortcuts. The Student must find alternative predictive signals — the invariant, causal features.

Rather than teaching the Student what is correct, the Teacher defines what is spurious, guiding the Student to look elsewhere."

---

## Scene N5 — Mutual Information Intuition
**~90 seconds**

### VISUAL
- Venn diagram showing three overlapping circles:
  - I(Φ(X); Y) [BLUE_D] — Information about the label
  - I(Φ(X); Z) [RED] — Information about the nuisance
  - I(Φ(X); X) [GRAY] — Total information
- Visualizing NuRD's objective:
  - `maximize I(Φ(X); Y)` → expands the BLUE_D circle
  - `minimize I(Φ(X); Z)` → shrinks the RED circle
- Overlapping region: "Nuisance information not needed for Y → Spurious"
- Complete formulation:
  `max_Φ  I(Φ(X); Y)  −  β · I(Φ(X); Z)`
- Text: "NuRD = Directed Information Bottleneck."

### AUDIO
"We can also understand NuRD through the lens of information theory.

Our goal is to maximize the mutual information between the representation Phi of X and the label Y, while minimizing the mutual information between Phi of X and the nuisance attribute Z.

This is a directed information bottleneck. Instead of compressing all information generally, we compress specifically along the dimension of the nuisance variable Z.

The hyperparameter beta controls this trade-off. A large beta aggressively filters out Z, but risks losing some features relevant to Y. A small beta preserves performance on Y, but may allow some shortcuts to leak through.

Combined with semantic corruption and distillation, NuRD provides a complete pipeline: detect the nuisance, model the shortcut, and filter it out of the representation.

While NuRD is highly effective for text and images, other settings provide explicit group structures, allowing us to optimize for the worst-case scenario directly. This brings us to Group DRO."

---
---

# PART IX — GROUP DRO: "Optimizing for the Weakest Group"

---

## Scene 5.1 — Group DRO: Complete Formula
**~2.5 minutes**

### VISUAL
- Waterbirds pie chart (4 groups):
  - Waterbird+Water: 45% [BLUE_D]
  - Landbird+Land: 45% [GREEN_D]
  - Waterbird+Land: 5% [RED pulsing]
  - Landbird+Water: 5% [RED pulsing]
- ERM formulation: `min_θ Σ_g p_g · 𝔼_g[ℓ]`
  Arrow: "Small p_g → group is ignored."
- The equation transforms: `Σ_g p_g` is replaced by `max_g`:
  ```
  min_h  max_{g∈G}  𝔼_{(x,y)~P_g} [ℓ(h(x), y)]
  ```
- The word "max" appears in GOLD with a glow effect. Text: "Optimize for the worst-performing group."
- Expanding the objective:
  - **Inner maximization**: `max_{g∈G} R_g(h)` → Identify the group with the highest risk.
  - **Outer minimization**: `min_h` → Update the model to reduce risk on that group.
- Loop animation:
  Step 1: Calculate R_g for all groups → Highlight the worst group.
  Step 2: Increase the weight of the worst group → Update model h.
  Step 3: Repeat.

### AUDIO
"Group Distributionally Robust Optimization, or Group DRO, modifies the ERM objective with a single operator: max.

Standard ERM minimizes the average loss. Since minority groups have small weights, they contribute very little to the average and are effectively ignored.

Group DRO reframes this as a minimax game: minimize over the model parameters, maximize over the groups.

The inner maximization identifies the group currently experiencing the highest risk — the worst-group.

The outer minimization updates the model parameters specifically to reduce the risk of this worst group.

As training progresses, the weights dynamically shift: whichever group performs worst is upweighted, forcing the model to focus on it. The model is prevented from sacrificing any single group to improve the average."

---

## Scene 5.2 — Oracle vs Practical: Limits of Group DRO
**~90 seconds**

### VISUAL
- Two columns: "Oracle Setting" [GOLD] vs "Practical Setting" [GRAY].
- Oracle column:
  - Precise group labels (g) are available for all training points.
  - Group DRO performs optimally.
- Practical column:
  - Group labels require manual annotation → prohibitively expensive.
  - Waterbirds: annotating every background.
  - CivilComments: identifying demographics for every comment.
- Cost comparison table:
  | Dataset | Size | Estimated Annotation Cost |
  |---------|------|---------------------------|
  | Waterbirds | 4,795 | ~$500 |
  | CelebA | 202,599 | ~$20,000 |
  | CivilComments | 448,000 | ~$45,000 |
- Text: "Group DRO is powerful, but requires expensive group labels."

### AUDIO
"When group labels are fully available, Group DRO consistently achieves the highest worst-group accuracy across most benchmarks.

However, this requirement is also its primary limitation. Group DRO needs to know the group membership of every training point. In real-world applications, annotating thousands of examples with demographic or environmental metadata is often too expensive or logistically impossible.

Furthermore, human annotations are prone to noise and bias.

To address this constraint, researchers have pursued two directions: automating group annotation using foundation models, or designing algorithms that function without group labels. Let's look at the latter first: JTT."

---
---

# PART X — JTT: "Letting ERM Identify Its Own Weakness"

---

## Scene 6.1 — JTT: Two-Stage Training
**~2.5 minutes**

### VISUAL
- Central question: "If we don't have group labels, how do we identify the minority groups?"
- Text: "Let the ERM model tell us."
- Two-stage timeline:

**STAGE 1 — Identification (5 epochs):**
- A brief training progress bar.
- The training set is split into two bins:
  - Bin 1 GRAY: "Correctly classified (Easy — shortcut holds)"
  - Bin 2 GOLD (pulsing): "Misclassified (Hard — shortcut fails!)"
- Explanation: (Penguin, snow) → shortcut works → Bin 1. (Penguin, sand) → shortcut fails → Bin 2.

**STAGE 2 — Robust Training:**
- The examples in Bin 2 are upweighted by a factor of K=20 (a large K=20 icon appears).
- The final model is trained on this upweighted dataset.

**Results on Waterbirds:**
- ERM: Worst-Group = 32% [RED]
- JTT: Worst-Group = 71% [GREEN]
- Label: "No group annotations required!"

### AUDIO
"Just Train Twice, or JTT, offers a simple and elegant solution: let a standard model identify its own weaknesses.

In the first stage, we train a standard ERM model for only a few epochs — enough for it to capture easy shortcuts, but not long enough to memorize exceptions. We then identify the examples this model classifies incorrectly.

Why do these mistakes matter? Because a quickly trained ERM model relies almost entirely on shortcuts. It correctly classifies majority examples where the shortcut aligns with the label. It misclassifies minority examples where the shortcut points in the wrong direction — such as a penguin on sand.

These early mistakes are a natural proxy for the minority groups.

In the second stage, we take these misclassified examples, upweight them by a factor of K equals twenty, and train a new model from scratch.

On the Waterbirds benchmark, this simple two-stage process increases worst-group accuracy from thirty-two percent to seventy-one percent — without requiring a single manual group label. JTT leverages the model's own simplicity bias to identify what it needs to correct."

---

## Scene 6.2 — Comparison of Methods: Which is Best When?
**~90 seconds**

### VISUAL
- Comparison table of 5 methods:
  | Method | Needs Group Labels? | Needs Environments? | Worst-Group Acc | Ideal Context |
  |--------|---------------------|---------------------|-----------------|---------------|
  | ERM | No | No | Low | Baseline |
  | Reweighting | Yes (or estimated) | No | Moderate | Small datasets |
  | IRM | No | Yes (diverse) | High (with good envs)| Clear environments |
  | NuRD | No | No | High (NLP/Vision) | Corruptible inputs |
  | Group DRO | Yes | No | Highest | Oracle labels available |
  | JTT | No | No | High | No labels or environments |
- Gold highlight box: "Choosing a method is about choosing the assumptions that fit your data."

### AUDIO
"Now that we have covered these five core methods, we can see that no single approach dominates.

Reweighting is simple but vulnerable to memorization in deep networks. IRM is theoretically grounded but requires high-quality, diverse environments. NuRD is effective for text and images but requires designing domain-specific corruptions. Group DRO is the top performer when group labels are available. JTT is the most flexible when we lack metadata.

Selecting the right method requires matching the algorithm's mathematical assumptions with the constraints of your dataset.

But how do these algorithms perform under real-world conditions? Let's look at the reality of OOD benchmarks."
