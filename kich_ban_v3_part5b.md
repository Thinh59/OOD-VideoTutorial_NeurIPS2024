# SCRIPT V3 — PART XII & XIII
## Foundation Models + AI Fixing AI + Outro

---

# PART XII — FOUNDATION MODELS: "Promise, Disillusionment, and Adaptation"

---

## Scene 7.0 — The Promise of Scale: Accuracy on the Line
**~2 minutes**

### VISUAL
- Scatter plot: x-axis = "In-Distribution (ID) Accuracy", y-axis = "Out-of-Distribution (OOD) Accuracy".
- Multiple models of varying sizes (represented by dots of increasing size) are plotted.
- A straight fit line passes through the dots: "Accuracy on the Line".
- High correlation: Higher ID accuracy corresponds directly to higher OOD accuracy.
- Text: "Does scaling model size solve OOD generalization?"
- Dot expansion animation: Larger models move up along the fit line.
- Evidence list: "Verified across 36 datasets including ImageNet shifts, CIFAR shifts, and NLP benchmarks."
- Gold box: "Scaling Law suggests OOD robustness is an emergent property."

### AUDIO
"Between twenty-twenty-one and twenty-twenty-two, researchers observed a compelling phenomenon known as Accuracy on the Line.

When plotting the in-distribution accuracy of various models against their out-of-distribution accuracy, the points fall along a straight line. Models that perform better on the training distribution also perform better on shifted test distributions.

Under the scaling laws of deep learning, larger models trained on more data yield higher in-distribution accuracy. If the linear relationship holds, scaling models should automatically resolve the OOD generalization problem.

This was verified across thirty-six distinct datasets, suggesting that robustness might simply emerge with scale.

However, as is often the case in machine learning, the reality is more nuanced."

---

## Scene 7.1 — Scale Does Not Solve: Empirical Evidence
**~2 minutes**

### VISUAL
- Plot: Worst-Group Accuracy vs. Model Size:
  - ERM [RED]: Increases slightly and then plateaus at ~55%.
  - Group DRO [BLUE_D]: Increases more significantly, peaking at ~75%.
- Large Models Region (>10B parameters): Both performance lines plateau.
  Icons representing large models (e.g., GPT, Gemini) are placed on the plateaued ERM line.
- Text: "Bigger models do not automatically yield higher worst-group accuracy."
- Chart: Average Accuracy vs. Worst-Group Accuracy for Large Models.
  Average accuracy increases with scale, while worst-group accuracy remains flat.
- Animation: A larger model expands, showing a complex web of learned shortcuts [RED, branching].
- Text: "Scale increases the capacity to memorize complex shortcuts, rather than ignoring them."

### AUDIO
"If we look at worst-group accuracy — the metric that matters most for safety — scaling tells a very different story.

As model size increases under standard ERM, worst-group accuracy plateaus. Scaling improves average performance, but does not eliminate spurious correlations.

In fact, larger models possess the capacity to learn and memorize more complex, subtle shortcuts. These are not simple background colors; they are high-dimensional, cross-modal patterns that are difficult to detect.

Accuracy on the Line holds for simple, uniform distribution shifts like ImageNet-Vtwo. But for spurious correlation shifts, scale alone is not enough.

However, contrastive vision-language models like CLIP exhibit unique properties."

---

## Scene 7.2 — CLIP and the Zero-Shot Promise
**~2 minutes**

### VISUAL
- CLIP architecture diagram:
  `[Image] → [Image Encoder] ─┐`
  `[Text] → [Text Encoder] ─┴→ Cosine Similarity → Prediction`
  Label: "Trained on 400M image-text pairs from the web."
- Zero-shot performance chart: CLIP vs. ERM on Waterbirds.
  CLIP zero-shot: ~75% worst-group accuracy [GREEN]. ERM: ~32% [RED].
- Gold box: "CLIP generalizes without seeing the target dataset."
- Intuition: Diverse web training exposes the model to varied contexts, reducing reliance on single shortcuts.
- Counterexample: Gender bias in CLIP.
  "doctor" → predicts male faces with higher probability.
  Histogram: Score distribution for "doctor" skewed toward male profiles.

### AUDIO
"CLIP represents a unique case study. It is trained on four hundred million image-text pairs from the web using contrastive learning, rather than standard supervised classification.

CLIP's zero-shot performance on the Waterbirds benchmark is remarkable: it achieves seventy-five percent worst-group accuracy without ever being trained on the dataset. Standard ERM achieves only thirty-two percent.

Because CLIP is exposed to diverse web data, it has seen penguins in many different contexts. The association between penguins and snow is not strong enough to dominate the representation.

At first glance, this suggests that large-scale contrastive training resolves OOD shifts.

However, CLIP still inherits biases from its training data. For example, the term 'doctor' is strongly associated with male faces in web media, and CLIP learns this correlation. With four hundred million examples, the model treats this bias as a true pattern."

---

## Scene 7.3 — Broken Promises: Vertical, Horizontal, and Negative Trends
**~2 minutes**

### VISUAL
- 4 small scatter plots (ID Accuracy vs. OOD Accuracy):

**Plot 1 — Vertical Line [GRAY]:**
- Models share the same ID accuracy but exhibit wide variance in OOD accuracy.
- "Scale increases ID accuracy while OOD remains unchanged."

**Plot 2 — Horizontal Line [ORANGE]:**
- OOD accuracy plateaus while ID accuracy continues to rise.
- "OOD performance saturates."

**Plot 3 — No Trend [RED]:**
- Random scatter of points with no correlation.
- "No linear relationship under complex spurious shifts."

**Plot 4 — Negative Correlation [Dark RED]:**
- Larger models exhibit lower OOD accuracy.
- "REVERSE SCALING — Larger models perform worse."
- Text: "Accuracy on the Line is a special case, not a general law."

### AUDIO
"A closer examination of the relationship between ID and OOD accuracy across different shifts reveals that the linear relationship often breaks down.

For some shifts, we observe a vertical trend: models with similar in-distribution performance vary widely in their out-of-distribution accuracy.

For other shifts, we see a horizontal trend: OOD performance saturates, and further scaling of ID accuracy yields no improvement.

Under complex spurious shifts, we find no correlation at all.

Most surprisingly, we sometimes observe negative correlation, or reverse scaling: larger models perform worse on OOD test sets.

Accuracy on the Line is a special case that occurs under simple, smooth shifts. It is not a general law of scaling."

---

## Scene 7.4 — In-Context Learning Shortcuts & Reverse Scaling
**~2 minutes**

### VISUAL
- ICL prompt example:
  ```
  "The movie was incredible!" → Positive
  "Best movie of the year!"   → Positive
  "I loved this movie!"       → Positive

  "The food was terrible."    → ???
  ```
- LLM predicts: "Positive" ✗. Highlight the word "movie" in ORANGE across the examples.
- Shortcut: "movie" → Positive (a spurious pattern created by the prompt design).
- Reverse Scaling plot:
  - x-axis = Model Size (2.7B → 7B → 13B), y-axis = % of predictions driven by the shortcut.
  - The line trends upward [RED]: 30% → 52% → 71%.
- Text: "Larger models are more sensitive to subtle patterns in the prompt."
- Text: "REVERSE SCALING: Scale amplifies shortcut learning."

### AUDIO
"In large language models, shortcuts can emerge dynamically within the prompt itself during in-context learning.

Consider a prompt where all positive examples happen to contain the word 'movie'. The model may learn a shortcut: the presence of 'movie' implies a positive label. When evaluated on a negative review about food, the model predicts 'positive'.

This is where we observe Reverse Scaling. A thirteen-billion parameter model is more likely to exploit this shortcut than a two-point-seven-billion parameter model.

Because larger models are highly capable of capturing patterns within the context window, they are also more sensitive to accidental correlations in the prompt.

Scale is not a universal solution for robustness. In the context of in-context learning, scaling can worsen the problem.

However, these same capabilities allow us to use large models to correct robustness failures. This leads to the paradigm of AI fixing AI."

---
---

# PART XIII — AI FIXING AI: "Leveraging Scale for Robustness"

---

## Scene 7.5 — PfR: Prompting for Robustness
**~2 minutes**

### VISUAL
- Question: "Group DRO requires group labels. Manual annotation is expensive. The solution?"
- PfR Pipeline (3 blocks):
  `[Waterbirds Image] → [VLM / GPT-4V + Prompt] → [Automated Group Labels]`
  Prompt text: "Describe the background: water or land?"
  Output: "water", "land", "water", ...
- Animation: Images pass through the VLM, and group labels are generated automatically.
- Setup:
  `[VLM Background Labels] + [Human Bird Labels] → [Group DRO]`
- Results comparison:
  - ERM baseline: 32% [RED]
  - Group DRO (manual labels): 91% [GREEN]
  - PfR (VLM-generated labels): 91.05% [GREEN+GOLD]
- Text: "PfR = Prompting for Robustness. Large models annotate for smaller models."

### AUDIO
"This is the concept of Prompting for Robustness, or PfR.

Group DRO is highly effective but requires group labels for all training data. Annotating thousands of backgrounds manually is expensive.

PfR resolves this by using a large Vision-Language Model to generate these labels automatically. We prompt the VLM to describe the background of each training image. The model provides accurate labels at minimal cost.

We then train Group DRO using these automated annotations.

On the Waterbirds benchmark, PfR achieves ninety-one point zero-five percent worst-group accuracy — matching the performance of Group DRO trained on manual labels, and tripling the ERM baseline.

This represents a clean narrative loop: while scaling introduces shortcuts in CLIP, we can leverage the capabilities of large VLMs to automate the annotations needed to train robust models. We are using AI to fix AI."

---

## Scene 7.6 — CATO: Counterfactual Data Generation
**~2 minutes**

### VISUAL
- Question: "What if minority groups are too small to train on, even if labeled?"
- CATO Pipeline:
  ```
  Step 1: Analyze SCM → Identify Z (spurious attribute)
           "Z = background (water/land)"

  Step 2: LLM + Causal Reasoning → Generate counterfactual text/images
           "A waterbird on land" (swap background)
           "A landbird on water" (swap background)

  Step 3: Augmented Dataset = Original + Counterfactual
           → Train robust model
  ```
- Animation: Minority groups expand as CATO generates synthetic examples.
- Pie chart: The group distribution balances from 5%/5%/45%/45% to equal quarters.
- Text: "CATO = Causal Augmentation via Language Models."
- Results: Worst-group accuracy increases by 3-5% compared to PfR alone.

### AUDIO
"PfR automates annotation. But we still face the challenge of data scarcity: minority groups are often too small to support effective training.

CATO, or Causal Augmentation, addresses this by using language models and causal reasoning to generate synthetic counterfactual data.

Using the SCM, we identify the spurious attribute — the background. CATO then prompts a generative model to synthesize counterfactual examples: placing a waterbird on land, or a landbird on water.

By augmenting the training set with these synthetic counterfactuals, we balance the group distributions. The model trained on this augmented dataset is significantly more robust.

CATO combines causal inference with generative AI, representing an active area of research.

This completes our narrative arc: scale initially promises robustness, fails under complex shifts, introduces new shortcuts, and is ultimately leveraged to automate annotations and generate counterfactual data to train robust models."

---
---

# PART XIV — CONCLUSION

---

## Scene 9.1 — Journey Summary
**~2 minutes**

### VISUAL
- Camera zooms out slowly. A conceptual map of the tutorial appears:
  ```
  [Intuition]          [Formalism]         [Risk Aggregation]
       ↓                    ↓                     ↓
  [ERM Failure] ───→ [OOD Definition] ───→ [Mean/Max/CVaR/DRO]
       ↓                                          ↓
  [Causal View]                           [Why Methods Differ]
  [SCM, Invariance]                               ↓
       ↓                              [Reweighting → fails]
  [Methods]                                       ↓
  [IRM → NuRD → DRO → JTT]                [IRM → NuRD → DRO]
       ↓                                          ↓
  [Benchmarks]               [Foundation Models]
  [Reality Check]            [Promise → Broken → Fix]
       ↓                            ↓
                 [PfR + CATO: AI Fixes AI]
  ```
- The map fades. Three words appear sequentially:
  CORRELATION [GRAY] → CAUSATION [BLUE_D] → STABILITY [GOLD, glowing]
- "STABILITY" is highlighted with a particle effect.
- Footer text: "The next frontier of Artificial Intelligence."

### AUDIO
"We have traveled a long path.

We began with a simple question: why do models learn shortcuts? We saw that ERM minimizes average loss, which can sacrifice minority groups to favor the majority.

We formalized this: OOD generalization requires performance to hold when distributions shift. We saw that robust algorithms are defined by their choice of risk aggregation — whether mean, max, CVaR, or DRO.

Simplicity bias explains why gradient descent prefers shortcuts: simple features present larger gradients at initialization.

Causal models clarify this structure: spurious features are environmental effects, while causal features are invariant properties of the object.

We examined five methods: Reweighting, IRM, NuRD, Group DRO, and JTT. Each represents a solution under specific mathematical assumptions.

Finally, we evaluated these on benchmarks, discussed the model selection paradox, and saw how foundation models fail and are then leveraged to improve robustness.

This leads to a single concept: Stability. Robust AI is not about predicting perfectly in every new environment. It is about identifying the core causal features and relying on them consistently, regardless of context."

---

## Scene 9.2 — Open Problems & Credits
**~45 seconds**

### VISUAL
- Three closed doors with light shining through the gaps:
  1. "OOD Theory for Foundation Models"
  2. "Model Selection without OOD Validation Sets"
  3. "OOD Generalization in Multimodal & Agentic AI"
- Fade to credits on a black screen:
  ```
  Based on:
  NeurIPS 2024 Tutorial
  "Out-of-Distribution Generalization: Shortcuts, Spuriousness & Stability"
  Maggie Makar · Aahlad Manas Puli · Yoav Wald

  Produced by:
  Phan Huỳnh Châu Thịnh (Na) · Mỹ Linh · Hồng Thanh · Trọng Hòa
  Machine Learning Course · HCMUS
  GitHub: https://github.com/Thinh59/OOD-VideoTutorial_NeurIPS2024.git
  ```

### AUDIO
"The tutorial concludes with three open research directions: developing OOD theory for foundation models, resolving model selection without OOD validation sets, and addressing robustness in multimodal and agentic systems.

This is the next frontier. Thank you for watching. The link to the original tutorial, slides, and Manim source code are in the description below."
