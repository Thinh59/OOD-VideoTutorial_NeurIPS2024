# Ká»CH Báº¢N V3 â€” PART I & II
## Out-of-Distribution Generalization: Shortcuts, Spuriousness & Stability
### NeurIPS 2024 Tutorial â€” Makar, Puli, Wald

---

# PART I â€” INTUITION: "Khi AI tá»± tin mĂ  sai"

---

## Scene 0.1 â€” Opening: Bá»‡nh Ă¡n cá»§a BĂ¡c sÄ©
**~90 giĂ¢y**

### VISUAL
- MĂ n hĂ¬nh Ä‘en â†’ text tráº¯ng: "Má»™t AI Ä‘Æ°á»£c huáº¥n luyá»‡n Ä‘á»ƒ dá»± Ä‘oĂ¡n bá»‡nh tá»« há»“ sÆ¡ bá»‡nh Ă¡n Ä‘iá»‡n tá»­."
- 2 bá»‡nh Ă¡n xuáº¥t hiá»‡n (há»™p viá»n tráº¯ng):
  - BA1: "89 yr old MAN, polyuria..." â†’ AI: Diabetes âœ“
  - BA2: "70 yr old GENTLEMAN, joint pain..." â†’ AI: Arthritis âœ“
  - Thanh accuracy: Hospital A â€” 95% [GREEN]
- Pan sang pháº£i â†’ Hospital B:
  - BA3: "65 yr old MAN, joint pain..." â†’ AI: Diabetes âœ—
  - Thanh: Hospital B â€” 72% [RED]. Dáº¥u "?" GOLD nháº¥p nhĂ¡y.
- Zoom vĂ o BA1, BA2. Highlight RED: "MAN" â†’ Diabetes, "GENTLEMAN" â†’ Arthritis.
- Text: "AI khĂ´ng Ä‘á»c chá»‰ sá»‘ y khoa. NĂ³ há»c thĂ³i quen viáº¿t cá»§a bĂ¡c sÄ©."

### AUDIO
"HĂ£y báº¯t Ä‘áº§u vá»›i má»™t vĂ­ dá»¥ thá»±c táº¿. Má»™t AI Ä‘Æ°á»£c huáº¥n luyá»‡n Ä‘á»ƒ dá»± Ä‘oĂ¡n bá»‡nh tá»« há»“ sÆ¡ bá»‡nh Ă¡n Ä‘iá»‡n tá»­. Táº¡i Bá»‡nh viá»‡n A, nĂ³ Ä‘áº¡t 95 pháº§n trÄƒm â€” áº¥n tÆ°á»£ng.

NhÆ°ng khi chuyá»ƒn sang Bá»‡nh viá»‡n B, accuracy rá»›t xuá»‘ng 72 pháº§n trÄƒm.

Äiá»u gĂ¬ Ä‘Ă£ xáº£y ra? NhĂ¬n ká»¹ vĂ o dá»¯ liá»‡u huáº¥n luyá»‡n. Táº¡i Viá»‡n A, má»™t bĂ¡c sÄ© cá»¥ thá»ƒ cĂ³ thĂ³i quen: Ă´ng ta viáº¿t 'man' khi ghi há»“ sÆ¡ bá»‡nh nhĂ¢n tiá»ƒu Ä‘Æ°á»ng, vĂ  'gentleman' khi ghi bá»‡nh nhĂ¢n viĂªm khá»›p. Hai tá»« Ä‘á»“ng nghÄ©a â€” nhÆ°ng AI Ä‘Ă£ há»c Ä‘Æ°á»£c sá»± phĂ¢n biá»‡t nĂ y vĂ  dĂ¹ng nĂ³ nhÆ° má»™t Ä‘Æ°á»ng táº¯t.

Khi sang Viá»‡n B, bĂ¡c sÄ© má»›i khĂ´ng cĂ³ thĂ³i quen Ä‘Ă³. Shortcut biáº¿n máº¥t. MĂ´ hĂ¬nh sá»¥p Ä‘á»•.

ÄĂ¢y chĂ­nh lĂ  váº¥n Ä‘á» trá»ng tĂ¢m cá»§a tutorial nĂ y. KhĂ´ng pháº£i AI thiáº¿u dá»¯ liá»‡u hay thiáº¿u tham sá»‘. MĂ  lĂ  AI Ä‘ang há»c sai thá»©."

---

## Scene 0.2 â€” Road Map
**~50 giĂ¢y**

### VISUAL
- ÄÆ°á»ng ngang trĂ¡iâ†’pháº£i, 2 lane GRAY. Biá»ƒn "XUáº¤T PHĂT" bĂªn trĂ¡i.
- 8 tráº¡m dá»«ng xuáº¥t hiá»‡n láº§n lÆ°á»£t:
  [Intuition] â†’ [Formalism] â†’ [Risk] â†’ [Causality] â†’ [Methods] â†’ [Benchmarks] â†’ [Foundation Models] â†’ [AI Fixing AI]
  ORANGE â†’ GOLD â†’ RED â†’ BLUE_D â†’ GREEN_D â†’ YELLOW_D â†’ PURPLE â†’ TEAL
- Xe WHITE cháº¡y tá»« trĂ¡i, dá»«ng á»Ÿ node 1, node sĂ¡ng lĂªn.

### AUDIO
"Trong video nĂ y chĂºng ta sáº½ Ä‘i qua tĂ¡m cháº·ng. Báº¯t Ä‘áº§u báº±ng trá»±c giĂ¡c vá» váº¥n Ä‘á», sau Ä‘Ă³ hĂ¬nh thá»©c hĂ³a báº±ng toĂ¡n há»c, Ä‘á»‹nh nghÄ©a risk vĂ  cĂ¡ch Ä‘o lÆ°á»ng robustness, nhĂ¬n qua lÄƒng kĂ­nh nhĂ¢n quáº£, khĂ¡m phĂ¡ cĂ¡c phÆ°Æ¡ng phĂ¡p giáº£i quyáº¿t tá»« reweighting Ä‘áº¿n IRM vĂ  DRO, Ä‘Ă¡nh giĂ¡ thá»±c táº¿ qua benchmark, rá»“i xem foundation models thay Ä‘á»•i bĂ i toĂ¡n nhÆ° tháº¿ nĂ o. VĂ  cuá»‘i cĂ¹ng, liá»‡u AI cĂ³ thá»ƒ tá»± sá»­a lá»—i cá»§a chĂ­nh mĂ¬nh. Äi thĂ´i."

---

## Scene 1.1 â€” ERM vĂ  áº¢o áº£nh Accuracy Cao
**~2 phĂºt**

### VISUAL
- KhĂ´ng gian 2D: trá»¥c x = "mĂ u ná»n" (tráº¯ngâ†’vĂ ng), trá»¥c y = "hĂ¬nh dĂ¡ng con váº­t".
- 20 Ä‘iá»ƒm xuáº¥t hiá»‡n: 10 BLUE_D (penguin, gĂ³c trĂªn-trĂ¡i) + 10 YELLOW_D (camel, gĂ³c dÆ°á»›i-pháº£i).
- ÄÆ°á»ng phĂ¢n loáº¡i WHITE 45Â° trÆ°á»£t vĂ o. Text: "Train Accuracy = 98% âœ“" [GREEN].
- Zoom vĂ o Ä‘Æ°á»ng â†’ mÅ©i tĂªn Ä‘á»: Ä‘Æ°á»ng Ä‘i theo trá»¥c x (mĂ u ná»n), khĂ´ng theo trá»¥c y.
- Äiá»ƒm BLUE_D má»›i á»Ÿ gĂ³c dÆ°á»›i-pháº£i (penguin trĂªn cĂ¡t). Model predict Camel. âœ— RED.
- ÄÆ°á»ng Ä‘á»•i RED, pulsing. Text: "ÄÆ°á»ng nĂ y Ä‘á»c MĂ€U Ná»€N â€” khĂ´ng pháº£i CON Váº¬T"

### AUDIO
"HĂ£y báº¯t Ä‘áº§u báº±ng vĂ­ dá»¥ kinh Ä‘iá»ƒn trong tutorial. Báº¡n xĂ¢y dá»±ng AI phĂ¢n loáº¡i chim cĂ¡nh cá»¥t vĂ  láº¡c Ä‘Ă .

Táº­p dá»¯ liá»‡u huáº¥n luyá»‡n: chim cĂ¡nh cá»¥t luĂ´n Ä‘á»©ng trĂªn tuyáº¿t tráº¯ng, láº¡c Ä‘Ă  luĂ´n Ä‘á»©ng trĂªn cĂ¡t vĂ ng. Trong khĂ´ng gian Ä‘áº·c trÆ°ng hai chiá»u, dá»¯ liá»‡u chia thĂ nh hai cá»¥m tĂ¡ch biá»‡t hoĂ n háº£o.

Thuáº­t toĂ¡n há»c vĂ  váº½ Ä‘Æ°á»£c má»™t Ä‘Æ°á»ng phĂ¢n loáº¡i. Accuracy 98 pháº§n trÄƒm. Tuyá»‡t vá»i.

NhÆ°ng chĂº Ă½ ká»¹ Ä‘Æ°á»ng nĂ y Ä‘ang lĂ m gĂ¬. NĂ³ Ä‘i theo trá»¥c ngang â€” Ä‘á»c mĂ u ná»n. KhĂ´ng pháº£i trá»¥c dá»c â€” hĂ¬nh dĂ¡ng con váº­t.

Khi má»™t chĂº chim cĂ¡nh cá»¥t bá»‹ Ä‘áº·t trĂªn cĂ¡t vĂ ng, Ä‘Æ°á»ng phĂ¢n loáº¡i khĂ´ng ngáº§n ngáº¡i: Ä‘Ă¢y lĂ  láº¡c Ä‘Ă . Sai hoĂ n toĂ n.

Äá»ƒ hiá»ƒu táº¡i sao, chĂºng ta cáº§n nhĂ¬n vĂ o trĂ¡i tim cá»§a má»i thuáº­t toĂ¡n há»c mĂ¡y hiá»‡n Ä‘áº¡i."

---

## Scene 1.2 â€” Giáº£i pháº«u ERM: Táº¡i sao nĂ³ lÆ°á»i?
**~2.5 phĂºt**

### VISUAL
- CĂ´ng thá»©c ERM xuáº¥t hiá»‡n tá»«ng pháº§n:
  1. `min_Î¸` â†’ "TĂ¬m bá»™ tham sá»‘ tá»‘t nháº¥t..."
  2. `đ”¼_{(x,y)âˆ¼P_train}` â†’ há»™p ORANGE bao P_train â†’ "...trĂªn train data..."
  3. `[â„“(f_Î¸(x), y)]` â†’ "...giáº£m sai sá»‘ trung bĂ¬nh."
- Zoom vĂ o P_train: "ERM chá»‰ tháº¥y P_train. KhĂ´ng hÆ¡n. KhĂ´ng kĂ©m."
- 2 con Ä‘Æ°á»ng INPUTâ†’OUTPUT:
  - ÄÆ°á»ng 1 BLUE_D (dĂ y): "PhĂ¢n tĂ­ch cáº¥u trĂºc hĂ¬nh thĂ¡i" + Ä‘á»“ng há»“ cĂ¡t dĂ i
  - ÄÆ°á»ng 2 RED (Ä‘á»©t, â¡): "Äáº¿m pixel tráº¯ng/vĂ ng" + tia chá»›p, 1 bÆ°á»›c
- ViĂªn bi WHITE lao vĂ o ÄÆ°á»ng 2. Text: "Gradient Descent chá»n con Ä‘Æ°á»ng giáº£m Loss nhanh nháº¥t"
- ÄÆ°á»ng 2 sĂ¡ng, ÄÆ°á»ng 1 má». Text lá»›n: "SPURIOUS FEATURE" [RED viá»n GOLD]

### AUDIO
"ERM, Empirical Risk Minimization, lĂ  thuáº­t toĂ¡n há»c mĂ¡y tiĂªu chuáº©n. Ă tÆ°á»Ÿng Ä‘Æ¡n giáº£n: tĂ¬m bá»™ tham sá»‘ theta Ä‘á»ƒ minimize sai sá»‘ trung bĂ¬nh trĂªn táº­p train.

NhÆ°ng chĂº Ă½: ERM chá»‰ cĂ³ má»™t má»¥c tiĂªu duy nháº¥t â€” giáº£m Loss. NĂ³ khĂ´ng biáº¿t, khĂ´ng quan tĂ¢m, liá»‡u sá»± giáº£m Ä‘Ă³ Ä‘áº¿n tá»« hiá»ƒu tháº­t sá»± hay tá»« Ä‘Æ°á»ng táº¯t.

HĂ£y hĂ¬nh dung tá»« gĂ³c nhĂ¬n Gradient Descent. CĂ³ hai con Ä‘Æ°á»ng: phĂ¢n tĂ­ch hĂ¬nh thĂ¡i há»c â€” tá»‘n nhiá»u bÆ°á»›c, khĂ³ há»c. Hoáº·c Ä‘áº¿m pixel ná»n â€” má»™t phĂ©p tĂ­nh Ä‘Æ¡n giáº£n.

Gradient Descent luĂ´n chá»n con Ä‘Æ°á»ng hai. KhĂ´ng pháº£i vĂ¬ nĂ³ xáº¥u xa, mĂ  vĂ¬ Ä‘Ă³ lĂ  chiá»u gradient giáº£m nhanh nháº¥t.

ChĂºng ta gá»i nhá»¯ng Ä‘áº·c trÆ°ng nhÆ° mĂ u ná»n Ä‘Ă³ lĂ  Spurious Features â€” Ä‘áº·c trÆ°ng áº£o. ChĂºng trĂ´ng giá»‘ng tĂ­n hiá»‡u há»¯u Ă­ch trong train data, nhÆ°ng chá»‰ lĂ  sá»± trĂ¹ng há»£p cá»§a ngá»¯ cáº£nh.

VĂ  cĂ¢u há»i tá»± nhiĂªn tiáº¿p theo lĂ : lĂ m sao ta phĂ¢n biá»‡t chĂ­nh xĂ¡c giá»¯a Ä‘áº·c trÆ°ng tháº­t vĂ  Ä‘áº·c trÆ°ng áº£o?"

---

## Scene 1.3 â€” Spurious Feature: ChĂ­nh xĂ¡c lĂ  gĂ¬?
**~1.5 phĂºt**

### VISUAL
- Timeline trĂ¡iâ†’pháº£i:
  [Nhiáº¿p áº£nh gia chá»¥p PENGUIN] â†’ [Chá»n: Báº¯c Cá»±c â€” Tuyáº¿t] â†’ [áº¢nh: ná»n tráº¯ng + penguin]
- MÅ©i tĂªn BLUE_D: "PENGUIN (Y)" â†’ "Ná»€N TRáº®NG (X_spur)" = nhĂ¢n quáº£ tháº­t
- MÅ©i tĂªn RED Ä‘á»©t ngÆ°á»£c: Ná»€N TRáº®NG â†’ PENGUIN. Label: "AI Ä‘ang há»c Ä‘iá»u nĂ y â€” NgÆ°á»£c chiá»u nhĂ¢n quáº£!"
- Animate: E thay Ä‘á»•i "Báº¯c Cá»±c"â†’"Sa máº¡c". MÅ©i tĂªn RED vá»¡ vá»¥n. MÅ©i tĂªn BLUE_D sĂ¡ng lĂªn.
- Text: "Causal Features = INVARIANT (báº¥t biáº¿n) | Spurious Features = BRITTLE (dá»… vá»¡)"

### AUDIO
"Váº­y spurious feature lĂ  gĂ¬, chĂ­nh xĂ¡c?

HĂ£y nghÄ© vá» chuá»—i sá»± kiá»‡n táº¡o ra dá»¯ liá»‡u. Nhiáº¿p áº£nh gia muá»‘n chá»¥p chim cĂ¡nh cá»¥t, há» Ä‘áº¿n Báº¯c Cá»±c. Con chim lĂ  nguyĂªn nhĂ¢n, ná»n tuyáº¿t tráº¯ng lĂ  káº¿t quáº£. MÅ©i tĂªn nhĂ¢n quáº£ Ä‘i tá»« nhĂ£n sang ná»n.

NhÆ°ng AI Ä‘ang Ä‘á»c ngÆ°á»£c láº¡i: tháº¥y ná»n tráº¯ng, káº¿t luáº­n chim cĂ¡nh cá»¥t. ÄĂ¢y lĂ  dá»± Ä‘oĂ¡n ngÆ°á»£c chiá»u nhĂ¢n quáº£.

Khi mĂ´i trÆ°á»ng thay Ä‘á»•i â€” chim cĂ¡nh cá»¥t xuáº¥t hiá»‡n á»Ÿ sa máº¡c â€” tÆ°Æ¡ng quan Ä‘Ă³ tan biáº¿n. NhÆ°ng má»‘i quan há»‡ nhĂ¢n quáº£ tháº­t váº«n cĂ²n: chim cĂ¡nh cá»¥t cĂ³ hĂ¬nh dĂ¡ng chim cĂ¡nh cá»¥t dĂ¹ Ä‘á»©ng á»Ÿ Ä‘Ă¢u.

Causal features á»•n Ä‘á»‹nh qua má»i mĂ´i trÆ°á»ng. Spurious features chá»‰ tá»“n táº¡i á»Ÿ má»™t hoĂ n cáº£nh cá»¥ thá»ƒ.

NhÆ°ng cho Ä‘áº¿n giá», táº¥t cáº£ nhá»¯ng gĂ¬ ta nĂ³i váº«n lĂ  trá»±c giĂ¡c. Äá»ƒ thá»±c sá»± giáº£i quyáº¿t váº¥n Ä‘á», ta cáº§n má»™t ngĂ´n ngá»¯ toĂ¡n há»c chĂ­nh xĂ¡c."

---
---

# PART II â€” FORMALIZING THE PROBLEM: "Äáº·t tĂªn cho trá»±c giĂ¡c"

---

## Scene F1 â€” Tá»« VĂ­ Dá»¥ LĂ¢m SĂ ng Ä‘áº¿n ToĂ¡n Há»c
**~90 giĂ¢y**

### VISUAL
- Báº£ng 3 cá»™t xuáº¥t hiá»‡n tá»«ng hĂ ng:
  | KĂ½ hiá»‡u | Ă nghÄ©a | VĂ­ dá»¥ Bá»‡nh viá»‡n |
  |----------|---------|-----------------|
  | X | Input (Ä‘áº§u vĂ o) | Bá»‡nh Ă¡n Ä‘iá»‡n tá»­ |
  | Y | Label (nhĂ£n) | Bá»‡nh (Diabetes/Arthritis) |
  | E | Environment (mĂ´i trÆ°á»ng) | Bá»‡nh viá»‡n (A hoáº·c B) |
- Há»™p ORANGE bao "E": "ÄĂ¢y lĂ  biáº¿n mĂ  ERM bá» qua hoĂ n toĂ n"
- VĂ­ dá»¥ penguin xuáº¥t hiá»‡n song song:
  X = áº£nh, Y = loĂ i (penguin/camel), E = Ä‘á»‹a Ä‘iá»ƒm (Báº¯c Cá»±c/Sa máº¡c)
- MÅ©i tĂªn ná»‘i 2 vĂ­ dá»¥ â†’ text: "CĂ¹ng má»™t cáº¥u trĂºc toĂ¡n há»c"

### AUDIO
"VĂ­ dá»¥ bá»‡nh viá»‡n vĂ  chim cĂ¡nh cá»¥t vá»«a rá»“i nghe trá»±c giĂ¡c. NhÆ°ng Ä‘á»ƒ giáº£i quyáº¿t váº¥n Ä‘á», ta cáº§n Ä‘áº·t tĂªn chĂ­nh xĂ¡c cho tá»«ng thĂ nh pháº§n.

Ba kĂ½ hiá»‡u cÆ¡ báº£n. X lĂ  input â€” bá»‡nh Ă¡n Ä‘iá»‡n tá»­, hoáº·c bá»©c áº£nh. Y lĂ  label â€” loáº¡i bá»‡nh, hoáº·c loĂ i Ä‘á»™ng váº­t. VĂ  E lĂ  environment â€” mĂ´i trÆ°á»ng â€” bá»‡nh viá»‡n A hay B, Báº¯c Cá»±c hay sa máº¡c.

ChĂº Ă½: ERM truyá»n thá»‘ng gá»™p táº¥t cáº£ dá»¯ liá»‡u tá»« má»i mĂ´i trÆ°á»ng láº¡i vĂ  tá»‘i Æ°u trung bĂ¬nh. NĂ³ khĂ´ng bao giá» nhĂ¬n tháº¥y biáº¿n E. VĂ  chĂ­nh sá»± mĂ¹ quĂ¡ng Ä‘Ă³ lĂ  nguá»“n gá»‘c cá»§a váº¥n Ä‘á».

BĂ¢y giá» ta Ä‘Ă£ cĂ³ kĂ½ hiá»‡u, hĂ£y Ä‘á»‹nh nghÄ©a chĂ­nh xĂ¡c tháº¿ nĂ o lĂ  'há»c tá»‘t ngoĂ i phĂ¢n phá»‘i'."

---

## Scene F2 â€” OOD Generalization lĂ  gĂ¬?
**~90 giĂ¢y**

### VISUAL
- Hai há»™p lá»›n cáº¡nh nhau:
  - Há»™p trĂ¡i BLUE_D: "IN-DISTRIBUTION (ID)" â†’ `(X,Y) ~ P_train`
  - Há»™p pháº£i GREEN_D: "OUT-OF-DISTRIBUTION (OOD)" â†’ `(X,Y) ~ P_test`
- Dáº¥u "â‰ " lá»›n RED giá»¯a hai há»™p: `P_train â‰  P_test`
- Animate: Ä‘Ă¡m mĂ¢y Ä‘iá»ƒm train (BLUE_D) á»Ÿ trĂ¡i. ÄĂ¡m mĂ¢y test (GREEN_D) á»Ÿ pháº£i, hĂ¬nh dáº¡ng khĂ¡c.
- ÄÆ°á»ng phĂ¢n loáº¡i fit train â†’ kĂ©o sang test â†’ sai nhiá»u. Flash RED.
- Text: "OOD Generalization = hoáº¡t Ä‘á»™ng tá»‘t khi P_test â‰  P_train"

### AUDIO
"Trong machine learning truyá»n thá»‘ng, ta giáº£ Ä‘á»‹nh train vĂ  test Ä‘áº¿n tá»« cĂ¹ng má»™t phĂ¢n phá»‘i. ÄĂ¢y gá»i lĂ  In-Distribution.

NhÆ°ng trong thá»±c táº¿, phĂ¢n phá»‘i test luĂ´n khĂ¡c train. Bá»‡nh viá»‡n má»›i, quá»‘c gia má»›i, nÄƒm má»›i. ÄĂ¢y lĂ  Out-of-Distribution.

OOD Generalization lĂ  kháº£ nÄƒng mĂ´ hĂ¬nh hoáº¡t Ä‘á»™ng tá»‘t khi phĂ¢n phá»‘i test khĂ¡c phĂ¢n phá»‘i train. KhĂ´ng pháº£i khĂ¡c má»™t chĂºt â€” mĂ  khĂ¡c vá» cáº¥u trĂºc.

VĂ  Ä‘á»ƒ nĂ³i chĂ­nh xĂ¡c 'khĂ¡c nhÆ° tháº¿ nĂ o', ta cáº§n khĂ¡i niá»‡m mĂ´i trÆ°á»ng."

---

## Scene F3 â€” PhĂ¢n Phá»‘i theo MĂ´i TrÆ°á»ng
**~90 giĂ¢y**

### VISUAL
- Node "e" xuáº¥t hiá»‡n giá»¯a. Text: "e âˆˆ E (environment)"
- 3 Ä‘Ă¡m mĂ¢y phĂ¢n phá»‘i xuáº¥t hiá»‡n xung quanh, má»—i cĂ¡i khĂ¡c hĂ¬nh:
  - eâ‚ [GREEN_D]: P_{eâ‚}(X,Y) â€” Ä‘Ă¡m mĂ¢y háº¹p, nghiĂªng trĂ¡i
  - eâ‚‚ [YELLOW_D]: P_{eâ‚‚}(X,Y) â€” Ä‘Ă¡m mĂ¢y rá»™ng, Ä‘á»‘i xá»©ng
  - eâ‚ƒ [PURPLE]: P_{eâ‚ƒ}(X,Y) â€” Ä‘Ă¡m mĂ¢y nhá», nghiĂªng pháº£i
- CĂ´ng thá»©c: "Má»—i mĂ´i trÆ°á»ng e táº¡o ra phĂ¢n phá»‘i P_e(X,Y) riĂªng"
- VĂ­ dá»¥ cá»¥ thá»ƒ:
  eâ‚ = Bá»‡nh viá»‡n A, eâ‚‚ = Bá»‡nh viá»‡n B, eâ‚ƒ = Bá»‡nh viá»‡n C
- MÅ©i tĂªn tá»« e â†’ P_e: "CĂ¹ng bá»‡nh, cĂ¹ng triá»‡u chá»©ng, khĂ¡c ngá»¯ cáº£nh"

### AUDIO
"Má»—i mĂ´i trÆ°á»ng e thuá»™c táº­p E táº¡o ra má»™t phĂ¢n phá»‘i dá»¯ liá»‡u riĂªng: P_e cá»§a X vĂ  Y.

Bá»‡nh viá»‡n A cĂ³ phĂ¢n phá»‘i bá»‡nh nhĂ¢n khĂ¡c Bá»‡nh viá»‡n B. KhĂ´ng pháº£i vĂ¬ bá»‡nh khĂ¡c, mĂ  vĂ¬ ngá»¯ cáº£nh khĂ¡c â€” cĂ¡ch ghi há»“ sÆ¡, thiáº¿t bá»‹ cháº©n Ä‘oĂ¡n, nhĂ¢n kháº©u há»c vĂ¹ng miá»n.

Quan trá»ng lĂ : má»‘i quan há»‡ nhĂ¢n quáº£ giá»¯a triá»‡u chá»©ng tháº­t vĂ  bá»‡nh khĂ´ng Ä‘á»•i qua cĂ¡c mĂ´i trÆ°á»ng. Chá»‰ cĂ³ má»‘i quan há»‡ giá»¯a spurious features vĂ  nhĂ£n má»›i thay Ä‘á»•i.

VĂ  khi ta cĂ³ nhiá»u mĂ´i trÆ°á»ng, cĂ¢u há»i trá»Ÿ thĂ nh: ta muá»‘n mĂ´ hĂ¬nh tá»‘t trĂªn Má»˜T phĂ¢n phá»‘i cá»¥ thá»ƒ, hay trĂªn Táº¤T Cáº¢ phĂ¢n phá»‘i cĂ³ thá»ƒ?"

---

## Scene F4 â€” Táº­p Há»£p Má»i Tháº¿ Giá»›i CĂ³ Thá»ƒ
**~90 giĂ¢y**

### VISUAL
- Táº­p há»£p P xuáº¥t hiá»‡n (hĂ¬nh oval lá»›n GOLD viá»n):
  P = {pâ‚, pâ‚‚, pâ‚ƒ, ...}
- BĂªn trong: nhiá»u Ä‘Ă¡m mĂ¢y nhá», má»—i cĂ¡i = 1 phĂ¢n phá»‘i, dao Ä‘á»™ng nháº¹.
- ERM: mÅ©i tĂªn chá»‰ vĂ o 1 Ä‘Ă¡m mĂ¢y duy nháº¥t (p_train). Text: "ERM chá»‰ tá»‘i Æ°u trĂªn Ä‘Ă¢y"
- Robust Learning: vĂ²ng trĂ²n bao TOĂ€N Bá»˜ P. Text: "Ta muá»‘n tá»‘t trĂªn Cáº¢ Há»Œ phĂ¢n phá»‘i"
- CĂ´ng thá»©c xuáº¥t hiá»‡n:
  `ERM:  min_Î¸ R_{p_train}(Î¸)`
  `Robust: min_Î¸ sup_{pâˆˆP} R_p(Î¸)`
- Há»™p highlight GOLD: "ÄĂ¢y lĂ  sá»± khĂ¡c biá»‡t cá»‘t lĂµi"

### AUDIO
"ÄĂ¢y lĂ  slide then chá»‘t. Gá»i P lĂ  táº­p há»£p táº¥t cáº£ phĂ¢n phá»‘i cĂ³ thá»ƒ xáº£y ra â€” táº¥t cáº£ bá»‡nh viá»‡n, táº¥t cáº£ quá»‘c gia, táº¥t cáº£ ngá»¯ cáº£nh mĂ  mĂ´ hĂ¬nh cĂ³ thá»ƒ gáº·p.

ERM tá»‘i Æ°u trĂªn Ä‘Ăºng má»™t phĂ¢n phá»‘i: p train. NĂ³ khĂ´ng biáº¿t vĂ  khĂ´ng quan tĂ¢m Ä‘áº¿n pháº§n cĂ²n láº¡i cá»§a P.

Robust Learning thay Ä‘á»•i má»¥c tiĂªu: ta muá»‘n tĂ¬m mĂ´ hĂ¬nh hoáº¡t Ä‘á»™ng tá»‘t trĂªn má»i phĂ¢n phá»‘i trong P. KhĂ´ng pháº£i tá»‘t trung bĂ¬nh â€” mĂ  tá»‘t ngay cáº£ trong trÆ°á»ng há»£p xáº¥u nháº¥t.

NhÆ°ng 'tá»‘t' nghÄ©a lĂ  gĂ¬? Ta cáº§n má»™t cĂ¡ch Ä‘o lÆ°á»ng chĂ­nh xĂ¡c. VĂ  Ä‘Ă³ chĂ­nh lĂ  khĂ¡i niá»‡m Risk â€” rá»§i ro."

---
---

# PART III â€” RISK AGGREGATION: "Äo lÆ°á»ng Robustness"

---

## Scene R1 â€” Expected Risk: Rá»§i ro trĂªn Má»™t PhĂ¢n Phá»‘i
**~60 giĂ¢y**

### VISUAL
- CĂ´ng thá»©c xuáº¥t hiá»‡n tá»«ng pháº§n:
  `R(h) = đ”¼_{(X,Y)~P} [L(h(X), Y)]`
- Giáº£i thĂ­ch dÆ°á»›i má»—i pháº§n:
  R(h) = "Rá»§i ro cá»§a mĂ´ hĂ¬nh h"
  đ”¼ = "Trung bĂ¬nh trĂªn..."
  P = "...má»™t phĂ¢n phá»‘i cá»¥ thá»ƒ"
  L = "...cá»§a hĂ m máº¥t mĂ¡t"
- VĂ­ dá»¥: náº¿u P = bá»‡nh viá»‡n A, R(h) = tá»‰ lá»‡ cháº©n Ä‘oĂ¡n sai trung bĂ¬nh táº¡i viá»‡n A.
- Animate: scatter plot, má»—i Ä‘iá»ƒm sĂ¡ng khi Ä‘Æ°á»£c tĂ­nh, R(h) cáº­p nháº­t dáº§n.

### AUDIO
"Risk, hay rá»§i ro, lĂ  thÆ°á»›c Ä‘o cÆ¡ báº£n. Vá»›i má»™t phĂ¢n phá»‘i P cá»¥ thá»ƒ, Risk cá»§a mĂ´ hĂ¬nh h báº±ng ká»³ vá»ng cá»§a hĂ m máº¥t mĂ¡t.

NĂ³i Ä‘Æ¡n giáº£n: R of h lĂ  xĂ¡c suáº¥t mĂ´ hĂ¬nh máº¯c lá»—i trung bĂ¬nh trĂªn phĂ¢n phá»‘i P. Náº¿u P lĂ  bá»‡nh viá»‡n A, Risk lĂ  tá»‰ lá»‡ cháº©n Ä‘oĂ¡n sai trung bĂ¬nh táº¡i viá»‡n Ä‘Ă³.

NhÆ°ng ta cĂ³ nhiá»u mĂ´i trÆ°á»ng, nhiá»u phĂ¢n phá»‘i. CĂ¢u há»i lĂ : khi cĂ³ nhiá»u Risk khĂ¡c nhau, ta gá»™p chĂºng láº¡i báº±ng cĂ¡ch nĂ o?"

---

## Scene R2 â€” Average Risk: CĂ¡ch ERM Gá»™p
**~60 giĂ¢y**

### VISUAL
- 3 thanh bar ngang: R_{eâ‚}=10%, R_{eâ‚‚}=15%, R_{eâ‚ƒ}=60%
  MĂ u GREEN_D, YELLOW_D, PURPLE
- CĂ´ng thá»©c ERM: `R_avg = (1/n) Î£áµ¢ â„“áµ¢ = (1/m) Î£_e R_e`
- Animate: trung bĂ¬nh â†’ R_avg = 28% [ORANGE]
- Há»™p: "28% â€” nghe cháº¥p nháº­n Ä‘Æ°á»£c?"
- Zoom vĂ o R_{eâ‚ƒ} = 60% [RED, nháº¥p nhĂ¡y]: "NhÆ°ng nhĂ³m nĂ y Ä‘ang chá»‹u 60%!"
- Text: "Average Risk che giáº¥u tháº£m há»a á»Ÿ nhĂ³m thiá»ƒu sá»‘"

### AUDIO
"ERM gá»™p risk báº±ng trung bĂ¬nh. Ba mĂ´i trÆ°á»ng: risk 10, 15, vĂ  60 pháº§n trÄƒm. Trung bĂ¬nh lĂ  28 â€” nghe cháº¥p nháº­n Ä‘Æ°á»£c.

NhÆ°ng nhĂ¬n ká»¹: mĂ´i trÆ°á»ng thá»© ba Ä‘ang chá»‹u 60 pháº§n trÄƒm lá»—i. Trong y táº¿, Ä‘Ă³ cĂ³ thá»ƒ lĂ  má»™t nhĂ³m dĂ¢n sá»‘ Ä‘ang bá»‹ cháº©n Ä‘oĂ¡n sai hÆ¡n má»™t ná»­a.

Average Risk cho phĂ©p mĂ´ hĂ¬nh hy sinh nhĂ³m thiá»ƒu sá»‘ Ä‘á»ƒ giáº£m lá»—i á»Ÿ nhĂ³m Ä‘a sá»‘. ÄĂ¢y chĂ­nh xĂ¡c lĂ  váº¥n Ä‘á» cá»§a ERM.

Váº­y thay vĂ¬ trung bĂ¬nh, náº¿u ta nhĂ¬n vĂ o trÆ°á»ng há»£p tá»‡ nháº¥t thĂ¬ sao?"

---

## Scene R3 â€” Worst-Case Risk: Báº£o vá»‡ NhĂ³m Yáº¿u Nháº¥t
**~90 giĂ¢y**

### VISUAL
- Giá»¯ 3 thanh bar tá»« R2.
- TransformMatchingTex: `(1/m) Î£_e R_e` â†’ `max_e R_e(h)`
- Chá»¯ "max" xuáº¥t hiá»‡n GOLD, glow.
- Animate: thanh R_{eâ‚ƒ}=60% sĂ¡ng lĂªn, 2 thanh kia má» Ä‘i.
- Text: "Worst-Case Risk = max_e R_e(h) = 60%"
- So sĂ¡nh 2 mĂ´ hĂ¬nh:
  Model A: R_avg=28%, R_worst=60% [ORANGE/RED]
  Model B: R_avg=35%, R_worst=38% [ORANGE/GREEN]
- CĂ¢u há»i: "Model nĂ o deploy cho bá»‡nh nhĂ¢n tháº­t?"
- Há»™p GOLD: "Worst-Case Risk â†’ báº£o vá»‡ nhĂ³m bá»‹ tá»•n thÆ°Æ¡ng nháº¥t"

### AUDIO
"Worst-Case Risk thay trung bĂ¬nh báº±ng max: tĂ¬m mĂ´i trÆ°á»ng mĂ  mĂ´ hĂ¬nh tá»‡ nháº¥t, vĂ  dĂ¹ng Ä‘Ă³ lĂ m thÆ°á»›c Ä‘o.

So sĂ¡nh hai mĂ´ hĂ¬nh. Model A cĂ³ average risk 28 nhÆ°ng worst-case 60 pháº§n trÄƒm. Model B average 35 nhÆ°ng worst-case chá»‰ 38. Model nĂ o báº¡n muá»‘n deploy cho bá»‡nh nhĂ¢n tháº­t?

Táº¡i sao worst-case quan trá»ng? Bá»Ÿi vĂ¬ trong y táº¿, trong tĂ i chĂ­nh, trong luáº­t phĂ¡p â€” bá»‡nh nhĂ¢n thiá»ƒu sá»‘, nhĂ³m dĂ¢n tá»™c Ă­t, trÆ°á»ng há»£p hiáº¿m â€” chĂ­nh lĂ  nhá»¯ng ngÆ°á»i bá»‹ tá»•n thÆ°Æ¡ng khi AI tháº¥t báº¡i. VĂ  há» xá»©ng Ä‘Ă¡ng Ä‘Æ°á»£c báº£o vá»‡.

NhÆ°ng worst-case chá»‰ lĂ  Má»˜T cĂ¡ch gá»™p risk. Thá»±c táº¿ cĂ³ cáº£ má»™t há» cĂ¡c phÆ°Æ¡ng phĂ¡p."

---

## Scene R4 â€” Risk Aggregation Families
**~2 phĂºt**

### VISUAL
- Báº£ng/heatmap 4 hĂ ng xuáº¥t hiá»‡n láº§n lÆ°á»£t:

| PhÆ°Æ¡ng phĂ¡p | CĂ´ng thá»©c | Ă nghÄ©a |
|-------------|-----------|----------|
| Mean | `(1/m) Î£_e R_e` | ERM tá»‘i Æ°u cĂ¡i nĂ y |
| Max | `max_e R_e` | Group DRO tá»‘i Æ°u cĂ¡i nĂ y |
| CVaR | `E[R_e | R_e â‰¥ VaR_Î±]` | Táº­p trung vĂ o Ä‘uĂ´i phĂ¢n phá»‘i |
| DRO | `sup_{PâˆˆP} R_P(h)` | Robust vá»›i má»i phĂ¢n phá»‘i |

- Má»—i hĂ ng sĂ¡ng lĂªn khi Ä‘Æ°á»£c giáº£i thĂ­ch. Cá»™t pháº£i: link Ä‘áº¿n thuáº­t toĂ¡n.
- Há»™p insight GOLD: "CĂ¡c thuáº­t toĂ¡n khĂ¡c nhau chá»‰ khĂ¡c nhau á»Ÿ cĂ¡ch gá»™p rá»§i ro"
- MÅ©i tĂªn: Mean â†’ Max â†’ CVaR â†’ DRO (má»©c Ä‘á»™ báº£o thá»§ tÄƒng dáº§n).

### AUDIO
"ÄĂ¢y lĂ  má»™t trong nhá»¯ng insight quan trá»ng nháº¥t cá»§a tutorial: cĂ¡c thuáº­t toĂ¡n robust khĂ¡c nhau thá»±c cháº¥t chá»‰ khĂ¡c nhau á»Ÿ cĂ¡ch gá»™p rá»§i ro.

Mean â€” trung bĂ¬nh bĂ¬nh thÆ°á»ng. ERM tá»‘i Æ°u cĂ¡i nĂ y. Nhanh, Ä‘Æ¡n giáº£n, nhÆ°ng hy sinh thiá»ƒu sá»‘.

Max â€” worst-case. Group DRO tá»‘i Æ°u cĂ¡i nĂ y. Báº£o vá»‡ nhĂ³m yáº¿u nháº¥t, nhÆ°ng cĂ³ thá»ƒ quĂ¡ bi quan.

CVaR â€” Conditional Value at Risk. KhĂ´ng cá»±c Ä‘oan nhÆ° max, nhÆ°ng táº­p trung vĂ o Ä‘uĂ´i phĂ¢n phá»‘i â€” nhá»¯ng trÆ°á»ng há»£p tá»‡ nháº¥t, khĂ´ng pháº£i tá»‡ nháº¥t tuyá»‡t Ä‘á»‘i.

Distributionally Robust â€” báº£o vá»‡ trÆ°á»›c má»i phĂ¢n phá»‘i trong má»™t táº­p há»£p. Máº¡nh nháº¥t vá» lĂ½ thuyáº¿t, nhÆ°ng táº­p há»£p pháº£i Ä‘Æ°á»£c chá»n cáº©n tháº­n.

Khi báº¡n chá»n má»™t thuáº­t toĂ¡n robust, thá»±c cháº¥t báº¡n Ä‘ang chá»n cĂ¡ch gá»™p risk. Hiá»ƒu Ä‘iá»u nĂ y giĂºp báº¡n khĂ´ng bá»‹ láº¡c trong rá»«ng thuáº­t toĂ¡n.

BĂ¢y giá» ta Ä‘Ă£ cĂ³ ngĂ´n ngá»¯ toĂ¡n há»c. CĂ¢u há»i tiáº¿p theo: táº¡i sao ERM â€” tá»‘i Æ°u mean risk â€” láº¡i chá»n spurious features? CĂ³ pháº£i chá»‰ vĂ¬ thá»‘ng kĂª, hay cĂ²n lĂ½ do sĂ¢u hÆ¡n?"
# Ká»CH Báº¢N V3 â€” PART IV, V, VI
## (Mathematical Assumptions â†’ Causal View â†’ Reweighting)

---

# PART IV â€” MATHEMATICAL ASSUMPTIONS: "MĂ´ hĂ¬nh toĂ¡n há»c cá»§a Shortcut"

---

## Scene 1.4A â€” Generative Model cá»§a Spurious Features
**~2 phĂºt**

### VISUAL
- MĂ n hĂ¬nh Ä‘en. CĂ´ng thá»©c xuáº¥t hiá»‡n tá»«ng sá»‘ háº¡ng:
  `x = yÂ·Ï†* + yÂ·zÂ·Ïˆ* + Î¾`
- Báº£ng giáº£i thĂ­ch tá»«ng thĂ nh pháº§n xuáº¥t hiá»‡n tá»«ng dĂ²ng:
  | KĂ½ hiá»‡u | TĂªn | Ă nghÄ©a |
  |---------|-----|---------|
  | x | Input | Bá»‡nh Ă¡n / Bá»©c áº£nh |
  | y | Label | Bá»‡nh / LoĂ i váº­t |
  | Ï†* | Causal feature direction | HÆ°á»›ng Ä‘áº·c trÆ°ng nhĂ¢n quáº£ |
  | z | Spurious attribute | Thuá»™c tĂ­nh áº£o (bá»‡nh viá»‡n A/B) |
  | Ïˆ* | Spurious feature direction | HÆ°á»›ng Ä‘áº·c trÆ°ng áº£o |
  | Î¾ | Noise | Nhiá»…u ngáº«u nhiĂªn |
- Animate: x bá»‹ phĂ¢n tĂ­ch thĂ nh 3 vector trong khĂ´ng gian: Ï†* [BLUE_D], Ïˆ* [RED], Î¾ [GRAY]
- Highlight RED `yÂ·zÂ·Ïˆ*`: "ÄĂ¢y lĂ  pháº§n spurious â€” phá»¥ thuá»™c VĂ€O cáº£ nhĂ£n Y VĂ€ mĂ´i trÆ°á»ng Z"

### AUDIO
"Äá»ƒ hiá»ƒu táº¡i sao gradient descent luĂ´n chá»n shortcut, ta cáº§n má»™t mĂ´ hĂ¬nh toĂ¡n há»c chĂ­nh xĂ¡c cho dá»¯ liá»‡u.

MĂ´ hĂ¬nh tuyáº¿n tĂ­nh Ä‘Æ¡n giáº£n nháº¥t: x báº±ng y nhĂ¢n phi-star, cá»™ng y nhĂ¢n z nhĂ¢n psi-star, cá»™ng nhiá»…u xi.

Phi-star lĂ  hÆ°á»›ng cá»§a causal feature trong khĂ´ng gian Ä‘áº·c trÆ°ng â€” hĂ¬nh dĂ¡ng con váº­t, triá»‡u chá»©ng tháº­t. Psi-star lĂ  hÆ°á»›ng cá»§a spurious feature â€” mĂ u ná»n, phong cĂ¡ch viáº¿t bĂ¡c sÄ©. Z lĂ  biáº¿n mĂ´i trÆ°á»ng â€” bá»‡nh viá»‡n A hay B, Báº¯c Cá»±c hay sa máº¡c.

ChĂº Ă½ sá»‘ háº¡ng spurious: nĂ³ phá»¥ thuá»™c vĂ o cáº£ Y vĂ  Z. Khi Z báº±ng 1, spurious feature vĂ  causal feature Ä‘á»u há»¯u Ă­ch Ä‘á»ƒ dá»± Ä‘oĂ¡n Y. Khi Z thay Ä‘á»•i giá»¯a cĂ¡c mĂ´i trÆ°á»ng, spurious feature trá»Ÿ nĂªn khĂ´ng Ä‘Ă¡ng tin.

CĂ¢u há»i lĂ : trong mĂ´ hĂ¬nh nĂ y, gradient descent sáº½ há»c Ï†* hay Ïˆ* trÆ°á»›c?"

---

## Scene 1.4B â€” NhĂ³m Äa Sá»‘ vĂ  NhĂ³m Thiá»ƒu Sá»‘
**~90 giĂ¢y**

### VISUAL
- Pie chart xuáº¥t hiá»‡n vá»›i 2 pháº§n:
  - 95% BLUE_D: "Majority: Z = Y (spurious khá»›p nhĂ£n)"
  - 5% RED: "Minority: Z â‰  Y (spurious trĂ¡i nhĂ£n)"
- CĂ´ng thá»©c:
  `P(Z = Y) = 0.95`
  `P(Z â‰  Y) = 0.05`
- VĂ­ dá»¥ cá»¥ thá»ƒ:
  - Majority (95%): penguin trĂªn tuyáº¿t + camel trĂªn cĂ¡t â†’ shortcut Ä‘Ăºng
  - Minority (5%): penguin trĂªn cĂ¡t + camel trĂªn tuyáº¿t â†’ shortcut sai
- Animate: cháº¥m RED nhá» á»Ÿ minority, ráº¥t khĂ³ nhĂ¬n tháº¥y trong Ä‘Ă¡m Ä‘Ă´ng BLUE_D.
- Text: "95-5 split â€” khĂ´ng báº¥t thÆ°á»ng. ÄĂ¢y lĂ  cáº¥u trĂºc cá»§a háº§u háº¿t dataset thá»±c táº¿."

### AUDIO
"Trong dataset thá»±c táº¿, spurious correlation hiáº¿m khi hoĂ n háº£o 100 pháº§n trÄƒm. Cáº¥u trĂºc phá»• biáº¿n: 95 pháº§n trÄƒm dá»¯ liá»‡u lĂ  nhĂ³m Ä‘a sá»‘ â€” spurious attribute khá»›p vá»›i nhĂ£n. Chá»‰ 5 pháº§n trÄƒm lĂ  nhĂ³m thiá»ƒu sá»‘ â€” spurious attribute trĂ¡i chiá»u nhĂ£n.

Penguin trĂªn tuyáº¿t vĂ  camel trĂªn cĂ¡t chiáº¿m 95 pháº§n trÄƒm. Penguin trĂªn cĂ¡t vĂ  camel trĂªn tuyáº¿t chá»‰ 5 pháº§n trÄƒm.

Vá»›i ERM, 5 pháº§n trÄƒm thiá»ƒu sá»‘ nĂ y háº§u nhÆ° vĂ´ hĂ¬nh. ChĂºng Ä‘Ă³ng gĂ³p quĂ¡ nhá» vĂ o average loss Ä‘á»ƒ buá»™c model há»c Ä‘áº·c trÆ°ng Ä‘Ăºng.

NhÆ°ng khi test distribution thay Ä‘á»•i â€” bá»‡nh viá»‡n má»›i, quá»‘c gia má»›i â€” nhĂ³m thiá»ƒu sá»‘ Ä‘Ă³ Ä‘á»™t nhiĂªn chiáº¿m Ä‘a sá»‘. VĂ  model sá»¥p Ä‘á»•."

---

## Scene 1.4C â€” Simplicity Bias: Táº¡i sao GD chá»n Z trÆ°á»›c
**~2 phĂºt**

### VISUAL
- KhĂ´ng gian tham sá»‘ 2D: trá»¥c x = "trá»ng sá»‘ theo Ï†* (causal)", trá»¥c y = "trá»ng sá»‘ theo Ïˆ* (spurious)"
- Äiá»ƒm xuáº¥t phĂ¡t: origin (0,0).
- Loss landscape: Ä‘Æ°á»ng Ä‘á»“ng má»©c (contour). Quan trá»ng: Ïˆ* cĂ³ gradient Dá»C HÆ N so vá»›i Ï†* á»Ÿ gáº§n origin.
- Animate: gradient descent step Ä‘áº§u tiĂªn â†’ bÆ°á»›c lá»›n hÆ¡n theo trá»¥c Ïˆ* (spurious).
- Sau nhiá»u bÆ°á»›c: mĂ´ hĂ¬nh náº±m gáº§n trá»¥c Ïˆ*, Ă­t dĂ¹ng Ï†*.
- Text: "Spurious feature cĂ³ gradient lá»›n hÆ¡n â†’ Gradient Descent chá»n nĂ³ trÆ°á»›c"
- Há»™p giáº£i thĂ­ch:
  Ïˆ* dá»… há»c vĂ¬: signal máº¡nh (95% data), feature Ä‘Æ¡n giáº£n (1 bit: bá»‡nh viá»‡n A hay B)
  Ï†* khĂ³ há»c vĂ¬: cáº§n káº¿t há»£p nhiá»u chiá»u, phá»©c táº¡p hÆ¡n

### AUDIO
"ÄĂ¢y lĂ  Simplicity Bias â€” má»™t trong nhá»¯ng insight quan trá»ng nháº¥t cá»§a tutorial.

Trong khĂ´ng gian tham sá»‘, gradient descent báº¯t Ä‘áº§u tá»« Ä‘iá»ƒm khá»Ÿi táº¡o ngáº«u nhiĂªn. NĂ³ di chuyá»ƒn theo hÆ°á»›ng giáº£m loss nhanh nháº¥t.

CĂ¢u há»i: hÆ°á»›ng nĂ o nhanh hÆ¡n â€” theo phi-star hay psi-star?

Spurious feature psi-star cĂ³ gradient lá»›n hÆ¡n á»Ÿ gáº§n origin vĂ¬ hai lĂ½ do. Thá»© nháº¥t, signal cá»§a nĂ³ máº¡nh: 95 pháº§n trÄƒm dá»¯ liá»‡u cĂ³ spurious correlation. Thá»© hai, feature nĂ y Ä‘Æ¡n giáº£n â€” chá»‰ cáº§n 1 bit thĂ´ng tin: bá»‡nh viá»‡n A hay B.

Causal feature phi-star phá»©c táº¡p hÆ¡n nhiá»u â€” cáº§n tá»•ng há»£p nhiá»u chiá»u Ä‘á»ƒ nháº­n dáº¡ng hĂ¬nh thĂ¡i há»c cá»§a penguin.

Káº¿t quáº£: gradient descent chá»n psi-star trÆ°á»›c, Ä‘áº·t nhiá»u trá»ng sá»‘ vĂ o spurious direction. NĂ³ cĂ³ thá»ƒ bao giá» quay láº¡i há»c phi-star khĂ´ng? CĂ³ â€” nhÆ°ng chá»‰ khi spurious feature khĂ´ng Ä‘á»§ Ä‘á»ƒ giáº£m loss ná»¯a. VĂ  vá»›i 95 pháº§n trÄƒm data á»§ng há»™ nĂ³, Ä‘iá»u Ä‘Ă³ hiáº¿m khi xáº£y ra.

ÄĂ¢y khĂ´ng pháº£i lá»—i ká»¹ thuáº­t. ÄĂ¢y lĂ  thuá»™c tĂ­nh cÆ¡ báº£n cá»§a gradient-based optimization. VĂ  chĂ­nh vĂ¬ váº­y, ta cáº§n can thiá»‡p cĂ³ chá»§ Ä‘Ă­ch."

---
---

# PART V â€” CAUSAL VIEW: "Táº¡i sao, khĂ´ng chá»‰ lĂ  NhÆ° tháº¿ nĂ o"

---

## Scene 3.1 â€” Structural Causal Model
**~2.5 phĂºt**

### VISUAL
- Node GOLD á»Ÿ trung tĂ¢m: Y (NhĂ£n)
- Node BLUE_D bĂªn trĂ¡i: X_core (Causal features â€” hĂ¬nh dĂ¡ng con váº­t)
  MÅ©i tĂªn dĂ y BLUE_D: X_core â†’ Y. Label: "NhĂ¢n quáº£ tháº­t"
- Node ORANGE gĂ³c trĂªn: E (MĂ´i trÆ°á»ng)
  MÅ©i tĂªn ORANGE: E â†’ X_spur
- Node RED bĂªn pháº£i: X_spur (Spurious features â€” mĂ u ná»n)
  MÅ©i tĂªn RED: Y â†’ X_spur. Label: "Y gĂ¢y ra ngá»¯ cáº£nh â†’ ngá»¯ cáº£nh gĂ¢y ra ná»n"
- ToĂ n bá»™ SCM:
  ```
       E (MĂ´i trÆ°á»ng)
      â†™              â†˜
  X_core â”€â”€â†’ Y â”€â”€â†’ X_spur
  [BLUE_D]  [GOLD]  [RED]
  ```
- MÅ©i tĂªn Ä‘á»©t RED tá»« X_spur â†’ Y: "AI Ä‘ang há»c Ä‘iá»u nĂ y â†" + kĂ½ hiá»‡u gáº¡ch chĂ©o

### AUDIO
"HĂ£y xĂ¢y dá»±ng Structural Causal Model cho bĂ i toĂ¡n nĂ y.

Báº¯t Ä‘áº§u tá»« Y â€” nhĂ£n. Con váº­t lĂ  penguin hay camel. Y quyáº¿t Ä‘á»‹nh Ä‘áº·c trÆ°ng váº­t lĂ½: X_core. Bá»‘n chĂ¢n hay hai chĂ¢n, lÆ°ng tháº³ng hay lÆ°ng bÆ°á»›u. ÄĂ¢y lĂ  mÅ©i tĂªn nhĂ¢n quáº£ tháº­t.

NhÆ°ng mĂ u ná»n Ä‘áº¿n tá»« Ä‘Ă¢u? Khi nhiáº¿p áº£nh gia chá»¥p penguin, há» Ä‘áº¿n Báº¯c Cá»±c. ÄĂ¢y lĂ  quyáº¿t Ä‘á»‹nh cá»§a mĂ´i trÆ°á»ng E. MĂ´i trÆ°á»ng E táº¡o ra X_spur â€” mĂ u ná»n tráº¯ng. KhĂ´ng pháº£i penguin trá»±c tiáº¿p chá»n mĂ u ná»n.

Tuy nhiĂªn vĂ¬ trong train data penguin Ä‘i vá»›i E lĂ  Báº¯c Cá»±c, cĂ³ tÆ°Æ¡ng quan giá»¯a Y vĂ  X_spur. AI nhĂ¬n tháº¥y tÆ°Æ¡ng quan nĂ y vĂ  há»c nĂ³. ÄĂ¢y lĂ  báº«y: AI Ä‘ang dá»± Ä‘oĂ¡n ngÆ°á»£c chiá»u nhĂ¢n quáº£ â€” tá»« há»‡ quáº£ suy ra nguyĂªn nhĂ¢n.

Khi E thay Ä‘á»•i â€” penguin á»Ÿ sa máº¡c â€” tÆ°Æ¡ng quan Ä‘Ă³ biáº¿n máº¥t. Chá»‰ mÅ©i tĂªn X_core Ä‘áº¿n Y lĂ  khĂ´ng bao giá» thay Ä‘á»•i."

---

## Scene 3.2 â€” MĂ´i TrÆ°á»ng thay Ä‘á»•i, LiĂªn Káº¿t áº£o vá»¡ tan
**~1.5 phĂºt**

### VISUAL
- Giá»¯ SCM tá»« 3.1. Node E sĂ¡ng lĂªn. Text E thay Ä‘á»•i 3 láº§n:
  "Äá»“ng cá»" â†’ "BĂ£i biá»ƒn" â†’ "Sa máº¡c"
- Má»—i láº§n E Ä‘á»•i: mÅ©i tĂªn Yâ†’X_spur nháº¥p nhĂ¡y RED, sau Ä‘Ă³ fracture (vá»¡ vá»¥n, máº£nh fly out).
- Sau 3 láº§n: mÅ©i tĂªn RED biáº¿n máº¥t. Chá»‰ cĂ²n X_coreâ†’Y [BLUE_D sĂ¡ng, glow].
- Text: "Causal Features = INVARIANT | Spurious Features = BRITTLE"
- CĂ¢u há»i xuáº¥t hiá»‡n: "LĂ m tháº¿ nĂ o Ä‘á»ƒ buá»™c AI chá»‰ há»c nhá»¯ng thá»© báº¥t biáº¿n?"

### AUDIO
"HĂ£y xem Ä‘iá»u gĂ¬ xáº£y ra khi mĂ´i trÆ°á»ng thay Ä‘á»•i.

E báº±ng Ä‘á»“ng cá»: má»‘i liĂªn há»‡ giá»¯a Y vĂ  X_spur tá»“n táº¡i â€” penguin Ä‘i vá»›i ná»n tráº¯ng. E báº±ng bĂ£i biá»ƒn: má»‘i liĂªn há»‡ Ä‘Ă³ lung lay. E báº±ng sa máº¡c: biáº¿n máº¥t hoĂ n toĂ n.

NhÆ°ng mÅ©i tĂªn tá»« X_core Ä‘áº¿n Y khĂ´ng bao giá» thay Ä‘á»•i. DĂ¹ á»Ÿ Ä‘á»“ng cá», bĂ£i biá»ƒn, hay sa máº¡c â€” penguin váº«n cĂ³ hĂ¬nh dĂ¡ng penguin.

SCM cho ta tháº¥y rĂµ: spurious features lĂ  há»‡ quáº£ cá»§a mĂ´i trÆ°á»ng, khĂ´ng pháº£i nguyĂªn nhĂ¢n cá»§a nhĂ£n. Khi mĂ´i trÆ°á»ng thay Ä‘á»•i, chĂºng thay Ä‘á»•i theo. Causal features thĂ¬ khĂ´ng.

CĂ¢u há»i lĂ : lĂ m tháº¿ nĂ o buá»™c mĂ´ hĂ¬nh chá»‰ há»c X_core? ChĂ­nh vĂ¬ bĂ i toĂ¡n cĂ³ cáº¥u trĂºc nhĂ¢n quáº£ rĂµ rĂ ng nhÆ° váº­y, ta cĂ³ nhiá»u hÆ°á»›ng tiáº¿p cáº­n. VĂ  hÆ°á»›ng Ä‘áº§u tiĂªn â€” Ä‘Æ¡n giáº£n nháº¥t â€” lĂ  reweighting."

---
---

# PART VI â€” REWEIGHTING FAMILY: "CĂ¢n báº±ng láº¡i Trá»ng sá»‘"

---

## Scene RW1 â€” Reweighting Principle: Ă tÆ°á»Ÿng cÆ¡ báº£n
**~90 giĂ¢y**

### VISUAL
- CĂ´ng thá»©c ERM gá»‘c: `L = (1/n) Î£áµ¢ â„“áµ¢`
- TransformMatchingTex: `(1/n)` â†’ `wáµ¢`:
  `L = Î£áµ¢ wáµ¢ Â· â„“áµ¢`
- Scatter plot: Ä‘iá»ƒm majority [BLUE_D, nhá»] vĂ  minority [RED, nhá»].
- Animate: Ä‘iá»ƒm minority Ä‘Æ°á»£c "phĂ³ng to" (glow, circle to ra xung quanh).
  Trá»ng sá»‘ wáµ¢: majority = 0.5, minority = 10.
- Text: "Reweighting = cho thiá»ƒu sá»‘ tiáº¿ng nĂ³i lá»›n hÆ¡n trong loss function"
- Constraint: `Î£áµ¢ wáµ¢ = 1` (váº«n lĂ  xĂ¡c suáº¥t há»£p lá»‡)

### AUDIO
"Ă tÆ°á»Ÿng Ä‘Æ¡n giáº£n nháº¥t Ä‘á»ƒ chá»‘ng shortcut: thay vĂ¬ Ä‘á»ƒ má»i Ä‘iá»ƒm dá»¯ liá»‡u Ä‘Ă³ng gĂ³p báº±ng nhau vĂ o loss, ta gĂ¡n trá»ng sá»‘ lá»›n hÆ¡n cho nhĂ³m thiá»ƒu sá»‘.

CĂ´ng thá»©c thay Ä‘á»•i tá»« trung bĂ¬nh Ä‘á»u sang trung bĂ¬nh cĂ³ trá»ng sá»‘: L báº±ng tá»•ng wáµ¢ nhĂ¢n â„“áµ¢.

Náº¿u minority chá»‰ chiáº¿m 5 pháº§n trÄƒm nhÆ°ng ta gĂ¡n trá»ng sá»‘ 10 láº§n lá»›n hÆ¡n, chĂºng chiáº¿m 50 pháº§n trÄƒm contribution vĂ o loss. Model bĂ¢y giá» pháº£i quan tĂ¢m Ä‘áº¿n nhĂ³m Ä‘Ă³.

NhÆ°ng váº¥n Ä‘á» lĂ : lĂ m sao ta biáº¿t trá»ng sá»‘ Ä‘Ăºng pháº£i lĂ  bao nhiĂªu?"

---

## Scene RW2 â€” Oracle Reweighting: Náº¿u biáº¿t táº¥t cáº£
**~60 giĂ¢y**

### VISUAL
- Há»™p GOLD: "Oracle setting â€” giáº£ sá»­ ta biáº¿t phĂ¢n phá»‘i tháº­t"
- CĂ´ng thá»©c trá»ng sá»‘ tá»‘i Æ°u:
  `wáµ¢ = P_test(Xáµ¢, Yáµ¢) / P_train(Xáµ¢, Yáµ¢)`
  hoáº·c Ä‘Æ¡n giáº£n hÆ¡n:
  `wáµ¢ âˆ 1 / P_train(Z=záµ¢ | Y=yáµ¢)`
- Giáº£i thĂ­ch: Ä‘iá»ƒm nĂ o hiáº¿m trong train (P_train nhá») â†’ trá»ng sá»‘ lá»›n
- VĂ­ dá»¥: penguin trĂªn cĂ¡t (P_train = 5%) â†’ w = 20 láº§n
- Text: "Náº¿u biáº¿t P(Z|Y), oracle reweighting loáº¡i bá» hoĂ n toĂ n spurious correlation"

### AUDIO
"Trong trÆ°á»ng há»£p lĂ½ tÆ°á»Ÿng â€” oracle setting â€” náº¿u ta biáº¿t phĂ¢n phá»‘i tháº­t, trá»ng sá»‘ tá»‘i Æ°u lĂ  tá»‰ lá»‡ giá»¯a phĂ¢n phá»‘i test vĂ  train.

ÄÆ¡n giáº£n hÆ¡n: Ä‘iá»ƒm nĂ o hiáº¿m trong táº­p train â€” tá»©c lĂ  khĂ´ng Ä‘Æ°á»£c Ä‘áº¡i diá»‡n Ä‘á»§ â€” nháº­n trá»ng sá»‘ lá»›n hÆ¡n. Penguin trĂªn cĂ¡t, xuáº¥t hiá»‡n chá»‰ 5 pháº§n trÄƒm trong train, nháº­n trá»ng sá»‘ 20 láº§n so vá»›i trung bĂ¬nh.

Vá»›i oracle reweighting hoĂ n háº£o, spurious correlation bá»‹ loáº¡i bá» hoĂ n toĂ n vá» máº·t lĂ½ thuyáº¿t. NhÆ°ng Ä‘Ă¢y lĂ  oracle â€” ta khĂ´ng biáº¿t P_train(Z|Y) trong thá»±c táº¿.

VĂ  ngay cáº£ khi ta Æ°á»›c lÆ°á»£ng Ä‘Æ°á»£c trá»ng sá»‘ tá»‘t, váº«n cĂ²n má»™t váº¥n Ä‘á» cÄƒn báº£n hÆ¡n."

---

## Scene RW3 â€” Táº¡i sao Reweighting Tháº¥t báº¡i: Interpolation
**~2 phĂºt**

### VISUAL
- Scatter plot: minority dots [RED] vá»›i trá»ng sá»‘ lá»›n (circles to).
- MĂ´ hĂ¬nh nhá» (3-4 neurons): loss landscape cĂ³ valley rĂµ rĂ ng theo minority.
  Model há»c Ä‘Æ°á»£c minority Ä‘Ăºng. âœ“
- Animate: model size tÄƒng (nhiá»u layers hÆ¡n, connections nhiá»u hÆ¡n) [PURPLE].
- Loss landscape má»›i: model lá»›n cĂ³ thá»ƒ "uá»‘n" Ä‘Æ°á»ng quyáº¿t Ä‘á»‹nh qua tá»«ng Ä‘iá»ƒm.
- Animate: loss â†’ 0 tá»«ng bÆ°á»›c. Text: "Loss = 0 â€” mĂ´ hĂ¬nh interpolate hoĂ n háº£o"
- Há»™p RED: "Khi loss = 0 â†’ gradient = 0 â†’ trá»ng sá»‘ wáµ¢ khĂ´ng cĂ³ Ă½ nghÄ©a gĂ¬ ná»¯a"
- Text: "INTERPOLATION: Neural network Ä‘á»§ lá»›n luĂ´n fit má»i Ä‘iá»ƒm â†’ Reweighting máº¥t tĂ¡c dá»¥ng"

### AUDIO
"ÄĂ¢y lĂ  váº¥n Ä‘á» cÆ¡ báº£n cá»§a reweighting vá»›i neural networks hiá»‡n Ä‘áº¡i.

Vá»›i mĂ´ hĂ¬nh nhá», trá»ng sá»‘ lá»›n cho minority thá»±c sá»± Ă©p model há»c nhĂ³m Ä‘Ă³. Loss landscape cĂ³ cáº¥u trĂºc rĂµ rĂ ng, valley sĂ¢u nháº¥t náº±m á»Ÿ nÆ¡i model hoáº¡t Ä‘á»™ng tá»‘t cáº£ majority láº«n minority.

NhÆ°ng vá»›i neural networks lá»›n â€” vĂ  trong thá»±c táº¿ ta luĂ´n dĂ¹ng máº¡ng Ä‘á»§ lá»›n â€” cĂ³ má»™t hiá»‡n tÆ°á»£ng gá»i lĂ  interpolation: máº¡ng Ä‘á»§ capacity Ä‘á»ƒ fit HOĂ€N Háº¢O má»i Ä‘iá»ƒm training, ká»ƒ cáº£ minority.

Khi loss báº±ng 0, gradient báº±ng 0. Trá»ng sá»‘ wáµ¢ lá»›n nhĂ¢n vá»›i gradient báº±ng 0 váº«n báº±ng 0. Reweighting hoĂ n toĂ n máº¥t tĂ¡c dá»¥ng.

MĂ´ hĂ¬nh váº«n há»c shortcut â€” vĂ¬ shortcut cho loss tháº¥p nháº¥t nhanh nháº¥t â€” rá»“i sau Ä‘Ă³ dĂ¹ng capacity dÆ° Ä‘á»ƒ memorize cĂ¡c Ä‘iá»ƒm minority mĂ  khĂ´ng thá»±c sá»± há»c Ä‘áº·c trÆ°ng Ä‘Ăºng.

ÄĂ¢y lĂ  lĂ½ do reweighting Ä‘Æ¡n thuáº§n khĂ´ng Ä‘á»§. Ta cáº§n can thiá»‡p vĂ o cáº¥u trĂºc há»c, khĂ´ng chá»‰ trá»ng sá»‘. VĂ  Ä‘Ă³ chĂ­nh lĂ  Ă½ tÆ°á»Ÿng Ä‘áº±ng sau IRM vĂ  DRO.

NhÆ°ng trÆ°á»›c khi Ä‘áº¿n cĂ¡c phÆ°Æ¡ng phĂ¡p Ä‘Ă³, ta cáº§n hiá»ƒu má»™t nhĂ¡nh khĂ¡c: lĂ m tháº¿ nĂ o phĂ¡t hiá»‡n chĂ­nh xĂ¡c Ä‘áº·c trÆ°ng nĂ o lĂ  nuisance Ä‘á»ƒ loáº¡i bá». ÄĂ¢y lĂ  bĂ i toĂ¡n mĂ  NuRD giáº£i quyáº¿t."

---

## Scene RW4 â€” Group Balancing vĂ  JTT Preview
**~60 giĂ¢y**

### VISUAL
- 4 Ă´ grid (2Ă—2): Majority+ [lá»›n, BLUE_D], Majority- [lá»›n, YELLOW_D], Minority+ [nhá», RED], Minority- [nhá», ORANGE]
- Animate: ERM â†’ chá»‰ Ă´ lá»›n Ä‘Æ°á»£c tá»‘i Æ°u. Minority bá»‹ bá» qua.
- Group Balancing: má»—i Ă´ Ä‘Æ°á»£c upweight Ä‘áº¿n báº±ng nhau.
- Text: "Group Balancing = extreme reweighting: má»i nhĂ³m Ä‘Ă³ng gĂ³p báº±ng nhau"
- Preview: "NhÆ°ng náº¿u khĂ´ng biáº¿t nhĂ³m nĂ o lĂ  thiá»ƒu sá»‘? â†’ JTT (sau)"

### AUDIO
"Má»™t biáº¿n thá»ƒ cá»§a reweighting lĂ  Group Balancing: thay vĂ¬ trá»ng sá»‘ liĂªn tá»¥c, ta Ä‘Æ¡n giáº£n Ä‘áº£m báº£o má»—i nhĂ³m Ä‘Ă³ng gĂ³p báº±ng nhau vĂ o loss â€” 25 pháº§n trÄƒm má»—i nhĂ³m, dĂ¹ kĂ­ch thÆ°á»›c thá»±c táº¿ khĂ¡c nhau nhiá»u.

Group Balancing máº¡nh hÆ¡n reweighting thĂ´ng thÆ°á»ng trong nhiá»u setting. NhÆ°ng nĂ³ váº«n cáº§n biáº¿t nhĂ³m nĂ o lĂ  thiá»ƒu sá»‘.

Sau nĂ y ta sáº½ tháº¥y JTT â€” Just Train Twice â€” má»™t cĂ¡ch thĂ´ng minh Ä‘á»ƒ tĂ¬m minority mĂ  khĂ´ng cáº§n nhĂ£n nhĂ³m. NhÆ°ng trÆ°á»›c tiĂªn, hĂ£y Ä‘áº¿n phÆ°Æ¡ng phĂ¡p cĂ³ ná»n táº£ng lĂ½ thuyáº¿t vá»¯ng cháº¯c nháº¥t: IRM."
# Ká»CH Báº¢N V3 â€” PART VII
## IRM: Invariant Risk Minimization (Äáº§y Ä‘á»§ + Failure Cases)

---

# PART VII â€” IRM: "Báº¥t biáº¿n lĂ  chĂ¬a khĂ³a"

---

## Scene 4.1 â€” IRM: Trá»±c giĂ¡c cá»‘t lĂµi
**~2 phĂºt**

### VISUAL
- 3 khĂ´ng gian 2D cáº¡nh nhau, viá»n GREEN_D, YELLOW_D, PURPLE. Label: eâ‚, eâ‚‚, eâ‚ƒ.
- Trong má»—i khĂ´ng gian: scatter plot vá»›i phĂ¢n phá»‘i trĂ´ng KHĂC nhau.
  NhÆ°ng ranh giá»›i quyáº¿t Ä‘á»‹nh tá»‘i Æ°u tháº­t (BLUE_D) thĂ¬ GIá»NG nhau trong cáº£ ba.
- CĂ¢u há»i xuáº¥t hiá»‡n á»Ÿ trung tĂ¢m:
  "Náº¿u mĂ´i trÆ°á»ng thay Ä‘á»•i mĂ  Ä‘Æ°á»ng phĂ¢n loáº¡i Ä‘Ăºng váº«n giá»‘ng nhau...
   thĂ¬ Ä‘Æ°á»ng Ä‘Ă³ pháº£i dá»±a vĂ o Äáº¶C TRÆ¯NG KHĂ”NG Äá»”I."
- Pause 2 giĂ¢y. Text: "â†’ ÄĂ¢y lĂ  Ă½ tÆ°á»Ÿng cá»‘t lĂµi cá»§a IRM"
- Váº½ kiáº¿n trĂºc máº¡ng chia 2 pháº§n:
  `[Input x] â†’ [Î¦: Feature Extractor] â†’ [w: Linear Classifier] â†’ [Output]`
  BLUE_D (Î¦), GREEN_D (w)
- Text: "Î¦ trĂ­ch xuáº¥t Ä‘áº·c trÆ°ng. w phĂ¢n loáº¡i. IRM Ă©p Î¦ chá»‰ giá»¯ causal features."

### AUDIO
"ChĂºng ta vá»«a tháº¥y reweighting tháº¥t báº¡i vá»›i máº¡ng lá»›n. IRM â€” Invariant Risk Minimization â€” tiáº¿p cáº­n tá»« má»™t gĂ³c Ä‘á»™ hoĂ n toĂ n khĂ¡c.

HĂ£y nhĂ¬n vĂ o ba mĂ´i trÆ°á»ng. Dá»¯ liá»‡u phĂ¢n phá»‘i khĂ¡c nhau â€” mĂ u ná»n khĂ¡c, ngá»¯ cáº£nh khĂ¡c. NhÆ°ng ranh giá»›i quyáº¿t Ä‘á»‹nh Ä‘Ăºng â€” Ä‘Æ°á»ng phĂ¢n chia penguin vĂ  camel theo hĂ¬nh dĂ¡ng tháº­t â€” giá»‘ng há»‡t nhau trong cáº£ ba.

Táº¡i sao? VĂ¬ hĂ¬nh dĂ¡ng con váº­t khĂ´ng thay Ä‘á»•i theo mĂ´i trÆ°á»ng. ÄĂ¢y lĂ  causal feature.

IRM Ä‘áº·t ra má»™t yĂªu cáº§u thanh lá»‹ch: tĂ¬m cĂ¡ch biá»ƒu diá»…n dá»¯ liá»‡u Phi, sao cho cĂ¹ng má»™t bá»™ phĂ¢n loáº¡i tuyáº¿n tĂ­nh w sáº½ tá»‘i Æ°u á»Ÿ táº¥t cáº£ cĂ¡c mĂ´i trÆ°á»ng Ä‘á»“ng thá»i.

Náº¿u tá»“n táº¡i Phi nhÆ° váº­y, Phi pháº£i Ä‘Ă£ loáº¡i bá» háº¿t spurious features â€” vĂ¬ chĂºng khĂ´ng nháº¥t quĂ¡n giá»¯a cĂ¡c mĂ´i trÆ°á»ng. Phi chá»‰ giá»¯ láº¡i causal features, vá»‘n báº¥t biáº¿n.

Nghe thanh lá»‹ch. NhÆ°ng viáº¿t thĂ nh toĂ¡n há»c nhÆ° tháº¿ nĂ o?"

---

## Scene 4.2 â€” IRM Objective: Bi-level Optimization
**~2 phĂºt**

### VISUAL
- CĂ´ng thá»©c bi-level xuáº¥t hiá»‡n tá»«ng dĂ²ng:
  ```
  min_{Î¦,w}  Î£_{eâˆˆE}  R_e(wâˆ˜Î¦)

  subject to  w âˆˆ argmin_{ẁ„} R_e(ẁ„âˆ˜Î¦),  âˆ€eâˆˆE
  ```
- Há»™p RED bao constraint. Label: "RĂ ng buá»™c: w pháº£i lĂ  minimum cá»§a Má»ŒI environment"
- Giáº£i thĂ­ch dĂ²ng 1: "Minimize tá»•ng risk trĂªn má»i mĂ´i trÆ°á»ng"
- Giáº£i thĂ­ch constraint: "w pháº£i tá»‘i Æ°u riĂªng cho Tá»ªNG mĂ´i trÆ°á»ng â€” khĂ´ng chá»‰ tá»•ng"
- Visualize constraint: 3 parabola Loss_e(w) vá»›i Ä‘Ă¡y á»Ÿ vá»‹ trĂ­ khĂ¡c nhau.
  Constraint nĂ³i: w=1.0 pháº£i lĂ  Ä‘Ă¡y cá»§a Cáº¢ BA. NhÆ°ng Ä‘Ă¡y á»Ÿ w=0.8, w=1.3, w=1.1 â€” khĂ´ng thá»ƒ thá»a mĂ£n cĂ¹ng lĂºc.
- Há»™p ORANGE: "NP-Hard â€” khĂ´ng giáº£i trá»±c tiáº¿p báº±ng Gradient Descent"

### AUDIO
"IRM viáº¿t bĂ i toĂ¡n tá»‘i Æ°u bi-level: minimize tá»•ng risk trĂªn má»i mĂ´i trÆ°á»ng, vá»›i rĂ ng buá»™c ráº±ng w pháº£i lĂ  classifier tá»‘i Æ°u cho tá»«ng mĂ´i trÆ°á»ng riĂªng láº».

Táº¡i sao rĂ ng buá»™c nĂ y quan trá»ng? Náº¿u w tá»‘i Æ°u á»Ÿ environment eâ‚ nhÆ°ng khĂ´ng tá»‘i Æ°u á»Ÿ eâ‚‚, nghÄ©a lĂ  Phi Ä‘ang dĂ¹ng má»™t Ä‘áº·c trÆ°ng há»¯u Ă­ch á»Ÿ eâ‚ nhÆ°ng háº¡i á»Ÿ eâ‚‚ â€” tá»©c lĂ  spurious feature.

RĂ ng buá»™c nĂ y báº£o Ä‘áº£m Phi trĂ­ch xuáº¥t Ä‘áº·c trÆ°ng Ä‘á»§ báº¥t biáº¿n Ä‘á»ƒ má»™t w duy nháº¥t lĂ m viá»‡c Ä‘Æ°á»£c á»Ÿ táº¥t cáº£ nÆ¡i.

Váº¥n Ä‘á»: bĂ i toĂ¡n nĂ y lĂ  NP-Hard. KhĂ´ng giáº£i trá»±c tiáº¿p báº±ng Gradient Descent. HĂ¬nh dung: ba parabola vá»›i Ä‘Ă¡y á»Ÿ ba vá»‹ trĂ­ khĂ¡c nhau â€” khĂ´ng cĂ³ w nĂ o lĂ  Ä‘Ă¡y cá»§a cáº£ ba cĂ¹ng lĂºc.

ChĂºng ta cáº§n má»™t xáº¥p xá»‰. VĂ  Ä‘Ă¢y lĂ  nÆ¡i má»™t trick toĂ¡n há»c Ä‘áº¹p xuáº¥t hiá»‡n."

---

## Scene 4.2B â€” Tá»« Constraint Ä‘áº¿n Gradient Penalty
**~2 phĂºt**

### VISUAL
- Nháº¯c láº¡i: constraint cá»©ng lĂ  `w âˆˆ argmin_{ẁ„} R_e(ẁ„âˆ˜Î¦)`
- Text: "Náº¿u w=1.0 lĂ  minimum cá»§a R_e thĂ¬ âˆ‡_{w|w=1.0} R_e(wâˆ˜Î¦) = 0"
  ÄĂ¢y lĂ  Ä‘á»‹nh nghÄ©a toĂ¡n há»c cá»§a minimum.
- "â†’ Gradient lá»›n = w chÆ°a pháº£i minimum = vi pháº¡m báº¥t biáº¿n"
- "â†’ Äo vi pháº¡m báº±ng Ä‘á»™ lá»›n gradient!"
- TransformMatchingTex: constraint biáº¿n thĂ nh penalty:
  ```
  min_{Î¦,w}  Î£_e R_e(wâˆ˜Î¦)  +  Î»Â·Î£_e â€–âˆ‡_{w|w=1.0} R_e(wâˆ˜Î¦)â€–Â²
             â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€    â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
             fit má»i mĂ´i trÆ°á»ng    penalty vi pháº¡m báº¥t biáº¿n
  ```
- Penalty term xuáº¥t hiá»‡n tá»« bĂªn pháº£i, mĂ u ORANGE.
- ValueTracker: Î» tÄƒng tá»« 0 â†’ 10 trong 3 giĂ¢y.
  Ba parabola dáº§n dá»‹ch chuyá»ƒn, Ä‘Ă¡y há»™i tá»¥ vá» w=1.0.
- Text: "IRMv1 â€” phiĂªn báº£n thá»±c táº¿ cĂ³ thá»ƒ train báº±ng Gradient Descent"

### AUDIO
"Trick toĂ¡n há»c: náº¿u w báº±ng 1.0 lĂ  minimum cá»§a hĂ m loss, thĂ¬ gradient cá»§a hĂ m loss táº¡i w báº±ng 1.0 pháº£i báº±ng 0. ÄĂ³ lĂ  Ä‘á»‹nh nghÄ©a cá»§a minimum.

Váº­y thay vĂ¬ rĂ ng buá»™c cá»©ng â€” w pháº£i lĂ  argmin â€” ta thay báº±ng penalty má»m: pháº¡t khi gradient lá»›n.

Gradient lá»›n táº¡i w=1.0 nghÄ©a lĂ  w chÆ°a pháº£i minimum á»Ÿ environment Ä‘Ă³, Phi Ä‘ang dĂ¹ng shortcut. Gradient nhá» nghÄ©a lĂ  Phi Ä‘Ă£ há»c Ä‘áº·c trÆ°ng báº¥t biáº¿n.

ÄĂ¢y lĂ  IRMv1. Khi lambda tÄƒng, optimizer bá»‹ Ă©p pháº£i tĂ¬m Phi sao cho má»i mĂ´i trÆ°á»ng Ä‘á»“ng thuáº­n. Spurious features bá»‹ loáº¡i vĂ¬ chĂºng lĂ  nguyĂªn nhĂ¢n cá»§a sá»± báº¥t Ä‘á»“ng.

NhÆ°ng cĂ³ má»™t Ä‘iá»ƒm tinh táº¿: táº¡i sao dĂ¹ng w=1 cá»‘ Ä‘á»‹nh thay vĂ¬ w tá»•ng quĂ¡t?"

---

## Scene 4.3 â€” Táº¡i sao w=1? Geometry cá»§a IRMv1
**~90 giĂ¢y**

### VISUAL
- KhĂ´ng gian Ä‘áº·c trÆ°ng Î¦(x) 2D.
- Vá»›i w=1 scalar: classifier lĂ  hyperplane qua origin vá»›i há»‡ sá»‘ do Î¦ quyáº¿t Ä‘á»‹nh.
- Giáº£i thĂ­ch: "w=1 khĂ´ng máº¥t tĂ­nh tá»•ng quĂ¡t â€” Î¦ cĂ³ thá»ƒ há»c scale"
- Váº½ 3 environment: má»—i environment cĂ³ gradient vector táº¡i Ä‘iá»ƒm w=1.
  - Vá»›i spurious feature: gradient vectors chá»‰ vá» 3 hÆ°á»›ng KHĂC nhau (phĂ¢n ká»³)
  - Vá»›i causal feature: gradient vectors gáº§n nhÆ° cĂ¹ng hÆ°á»›ng (há»™i tá»¥)
- Animation: penalty Ă©p gradient há»™i tá»¥ â†’ spurious bá»‹ Ä‘áº©y ra khá»i Î¦.
- Text: "Invariant representation = gradient Ä‘á»“ng thuáº­n qua má»i environment"

### AUDIO
"Táº¡i sao chá»n w báº±ng 1 cá»‘ Ä‘á»‹nh? VĂ¬ vá»›i classifier tuyáº¿n tĂ­nh, w chá»‰ lĂ  scalar scale â€” Phi cĂ³ thá»ƒ há»c scale Ä‘Ă³ vĂ o trong representation cá»§a mĂ¬nh. NĂªn w=1 khĂ´ng máº¥t tĂ­nh tá»•ng quĂ¡t, nhÆ°ng Ä‘Æ¡n giáº£n hĂ³a bĂ i toĂ¡n Ä‘Ă¡ng ká»ƒ.

NhĂ¬n trá»±c quan: vá»›i spurious feature, gradient táº¡i w=1 trá» vá» hÆ°á»›ng khĂ¡c nhau á»Ÿ má»—i environment â€” vĂ¬ spurious há»¯u Ă­ch á»Ÿ environment nĂ y nhÆ°ng háº¡i á»Ÿ environment kia. Penalty pháº¡t sá»± phĂ¢n ká»³ nĂ y.

Vá»›i causal feature, gradient gáº§n nhÆ° Ä‘á»“ng hÆ°á»›ng qua má»i environment. Penalty gáº§n nhÆ° báº±ng khĂ´ng. Phi Ä‘Æ°á»£c phĂ©p giá»¯ causal feature.

Káº¿t quáº£: Phi há»™i tá»¥ vá» invariant representation â€” chá»‰ chá»©a nhá»¯ng gĂ¬ nháº¥t quĂ¡n qua má»i mĂ´i trÆ°á»ng."

---

## Scene 4.4 â€” Gradient Vectors Há»™i tá»¥ (Visualization)
**~90 giĂ¢y**

### VISUAL
- KhĂ´ng gian tham sá»‘ w (trá»¥c sá»‘). Ba parabola vá»›i Ä‘Ă¡y á»Ÿ vá»‹ trĂ­ khĂ¡c nhau.
- Táº¡i Ä‘iá»ƒm w=1.0: 3 vector gradient (mÅ©i tĂªn) chá»‰ vá» 3 hÆ°á»›ng khĂ¡c nhau (phĂ¢n ká»³).
  Label: "3 mĂ´i trÆ°á»ng báº¥t Ä‘á»“ng â†’ shortcut Ä‘ang Ä‘Æ°á»£c dĂ¹ng!"
- ValueTracker Î» tÄƒng dáº§n. Ba vector gradient xoay tá»«ng bÆ°á»›c vá» cĂ¹ng hÆ°á»›ng, nhá» dáº§n, tiáº¿n vá» 0.
  Label: "Penalty Ă©p Ä‘á»“ng thuáº­n â†’ shortcut bá»‹ loáº¡i"
- Final state: cáº£ 3 gradient â‰ˆ 0. Ba parabola cĂ³ Ä‘Ă¡y gáº§n nhau.
  Text: "Phi Ä‘Ă£ há»c invariant features âœ“"

### AUDIO
"HĂ¬nh dung trá»±c quan. Náº¿u Phi Ä‘ang dĂ¹ng spurious feature, Ä‘áº·c trÆ°ng Ä‘Ă³ há»¯u Ă­ch á»Ÿ má»™t sá»‘ mĂ´i trÆ°á»ng nhÆ°ng háº¡i á»Ÿ mĂ´i trÆ°á»ng khĂ¡c. Má»—i mĂ´i trÆ°á»ng muá»‘n w dá»‹ch chuyá»ƒn theo hÆ°á»›ng khĂ¡c nhau. Ba vector gradient chá»‰ vá» ba hÆ°á»›ng khĂ¡c nhau â€” báº¥t Ä‘á»“ng.

Khi penalty lambda tÄƒng, optimizer bá»‹ pháº¡t náº¿u cĂ¡c gradient cĂ²n phĂ¢n ká»³. NĂ³ buá»™c pháº£i tĂ¬m Phi mĂ  táº¥t cáº£ mĂ´i trÆ°á»ng Ä‘á»“ng thuáº­n. Spurious features bá»‹ loáº¡i khá»i Phi vĂ¬ chĂºng lĂ  nguyĂªn nhĂ¢n cá»§a sá»± báº¥t Ä‘á»“ng.

Pháº§n cĂ²n láº¡i trong Phi â€” nhá»¯ng chiá»u mĂ  má»i environment Ä‘á»“ng Ă½ â€” chĂ­nh lĂ  causal features."

---

## Scene 4.5 â€” IRM Failure Cases: Khi Báº¥t biáº¿n KhĂ´ng Äá»§
**~2.5 phĂºt**

### VISUAL
- TiĂªu Ä‘á» lá»›n: "IRM is NOT a Silver Bullet" [ORANGE]
- 3 counterexample, má»—i cĂ¡i cĂ³ SCM diagram nhá» + dáº¥u âœ— RED:

**Counterexample 1: Invariant Feature giáº£**
- SCM: X_spur tĂ¬nh cá» báº¥t biáº¿n qua táº¥t cáº£ environments trong táº­p train.
- VĂ­ dá»¥: táº¥t cáº£ bá»‡nh viá»‡n trong train Ä‘á»u cĂ³ cĂ¹ng thĂ³i quen viáº¿t "man/gentleman".
- Text: "Spurious feature báº¥t biáº¿n trong train â‰  causal. IRM khĂ´ng phĂ¢n biá»‡t Ä‘Æ°á»£c."

**Counterexample 2: Environments khĂ´ng Ä‘á»§ Ä‘a dáº¡ng**
- 2 environment vá»›i cĂ¹ng spurious correlation (P(Z=Y)=0.95 á»Ÿ Cáº¢ HAI).
- IRM khĂ´ng cĂ³ báº¥t Ä‘á»“ng Ä‘á»ƒ detect â†’ khĂ´ng loáº¡i Ä‘Æ°á»£c spurious.
- Text: "IRM cáº§n diversity. KhĂ´ng Ä‘á»§ diversity â†’ gradient penalty = 0 á»Ÿ cáº£ hai."

**Counterexample 3: Shortcut tá»“n táº¡i á»Ÿ má»i environment**
- SCM: spurious feature Z khĂ´ng phá»¥ thuá»™c vĂ o E â€” Z tá»“n táº¡i á»Ÿ má»i nÆ¡i.
- VĂ­ dá»¥: race/gender bias trong ngĂ´n ngá»¯ â€” tá»“n táº¡i á»Ÿ má»i dataset.
- IRM khĂ´ng thá»ƒ loáº¡i Z vĂ¬ Z khĂ´ng "vi pháº¡m" báº¥t biáº¿n.

### AUDIO
"ChĂ­nh vĂ¬ nhá»¯ng Ä‘áº·c Ä‘iá»ƒm trĂªn, IRM nghe ráº¥t thanh lá»‹ch vá» lĂ½ thuyáº¿t. NhÆ°ng thá»±c táº¿ kháº¯c nghiá»‡t hÆ¡n nhiá»u.

Ba trÆ°á»ng há»£p IRM tháº¥t báº¡i.

Thá»© nháº¥t: invariant feature giáº£. Náº¿u má»™t spurious feature tĂ¬nh cá» báº¥t biáº¿n qua táº¥t cáº£ environments trong táº­p train â€” vĂ­ dá»¥ táº¥t cáº£ bá»‡nh viá»‡n train Ä‘á»u cĂ³ cĂ¹ng thĂ³i quen ghi chĂ©p â€” IRM sáº½ giá»¯ spurious feature Ä‘Ă³ vĂ¬ nĂ³ 'vÆ°á»£t qua' bĂ i kiá»ƒm tra báº¥t biáº¿n.

Thá»© hai: environments khĂ´ng Ä‘á»§ Ä‘a dáº¡ng. IRM hoáº¡t Ä‘á»™ng báº±ng cĂ¡ch phĂ¡t hiá»‡n Báº¤T Äá»’NG giá»¯a environments. Náº¿u hai environments cĂ³ cĂ¹ng spurious correlation máº¡nh, gradient penalty á»Ÿ cáº£ hai Ä‘á»u nhá» â€” IRM khĂ´ng phĂ¡t hiá»‡n váº¥n Ä‘á».

Thá»© ba: shortcut tá»“n táº¡i á»Ÿ má»i environment. Bias vá» race hay gender trong ngĂ´n ngá»¯ khĂ´ng pháº£i lĂ  spurious correlation phá»¥ thuá»™c environment â€” chĂºng xuáº¥t hiá»‡n á»Ÿ má»i nÆ¡i. IRM khĂ´ng cĂ³ cÆ¡ cháº¿ loáº¡i bá» chĂºng.

Nhiá»u nghiĂªn cá»©u thá»±c nghiá»‡m cho tháº¥y ERM Ä‘Æ°á»£c tuning tá»‘t Ä‘Ă´i khi cĂ²n vÆ°á»£t trá»™i IRMv1 trĂªn benchmark thá»±c táº¿. IRM máº¡nh vá» lĂ½ thuyáº¿t, nhÆ°ng fragile trong practice.

Váº­y náº¿u khĂ´ng cĂ³ Ä‘á»§ mĂ´i trÆ°á»ng rĂµ rĂ ng, hoáº·c shortcut khĂ´ng pháº£i environment-dependent, ta cáº§n hÆ°á»›ng tiáº¿p cáº­n khĂ¡c. VĂ  Ä‘Ă³ lĂ  khi ta quay láº¡i vá»›i cáº¥u trĂºc nhĂ³m â€” nhÆ°ng láº§n nĂ y vá»›i má»™t cĂ´ng thá»©c cháº·t cháº½ hÆ¡n."

---

## Scene 4.6 â€” IRM trong Thá»±c táº¿: Khi nĂ o dĂ¹ng?
**~60 giĂ¢y**

### VISUAL
- Báº£ng tĂ³m táº¯t:
  | Äiá»u kiá»‡n | IRM phĂ¹ há»£p? |
  |-----------|--------------|
  | CĂ³ nhiá»u environments Ä‘a dáº¡ng | âœ“ Tá»‘t |
  | Spurious khĂ¡c nhau rĂµ giá»¯a environments | âœ“ Tá»‘t |
  | Chá»‰ 2 environments giá»‘ng nhau | âœ— Yáº¿u |
  | Spurious tá»“n táº¡i má»i nÆ¡i | âœ— Yáº¿u |
  | Neural network ráº¥t lá»›n | âœ— Yáº¿u (interpolation) |
- Há»™p GOLD: "IRM: ná»n táº£ng lĂ½ thuyáº¿t nhĂ¢n quáº£ vá»¯ng, nhÆ°ng cáº§n environments cháº¥t lÆ°á»£ng cao"
- Arrow chá»‰ sang: "Náº¿u khĂ´ng cĂ³ environments â†’ NuRD hoáº·c Group DRO"

### AUDIO
"TĂ³m láº¡i vá» IRM: nĂ³ hoáº¡t Ä‘á»™ng tá»‘t khi báº¡n cĂ³ nhiá»u environments Ä‘á»§ Ä‘a dáº¡ng vĂ  spurious correlation thay Ä‘á»•i Ä‘Ă¡ng ká»ƒ giá»¯a cĂ¡c environments. ÄĂ¢y lĂ  setting lĂ½ tÆ°á»Ÿng nháº¥t.

NhÆ°ng trong nhiá»u bĂ i toĂ¡n thá»±c táº¿ â€” y táº¿, ngĂ´n ngá»¯, khoa há»c â€” báº¡n khĂ´ng cĂ³ luxury Ä‘Ă³. Environments khĂ´ng Ä‘á»§ hoáº·c khĂ´ng Ä‘á»§ Ä‘a dáº¡ng.

ChĂ­nh vĂ¬ nhá»¯ng tháº¥t báº¡i nĂ y, cá»™ng Ä‘á»“ng Ä‘Ă£ phĂ¡t triá»ƒn hai hÆ°á»›ng song song. Má»™t lĂ  NuRD â€” tĂ¬m vĂ  loáº¡i bá» nuisance features má»™t cĂ¡ch trá»±c tiáº¿p. Hai lĂ  Group DRO â€” thay vĂ¬ báº¥t biáº¿n, tá»‘i Æ°u trá»±c tiáº¿p worst-case group. Ta sáº½ Ä‘áº¿n cáº£ hai."
# Ká»CH Báº¢N V3 â€” PART VIII, IX, X
## NuRD + Group DRO + JTT

---

# PART VIII â€” NuRD: "Lá»c Sáº¡ch Nuisance"

---

## Scene N1 â€” NuRD: Ă tÆ°á»Ÿng cá»‘t lĂµi
**~90 giĂ¢y**

### VISUAL
- TiĂªu Ä‘á»: "NuRD â€” Nuisance-Randomized Distillation"
- Pipeline Ä‘Æ¡n giáº£n:
  `[X] â†’ [Î¦: Encoder] â†’ [Î¦(X): Representation] â†’ [w] â†’ [Å¶]`
- CĂ¢u há»i: "LĂ m sao biáº¿t Î¦(X) cĂ³ cĂ²n chá»©a Z (nuisance) khĂ´ng?"
- Äiá»u kiá»‡n Ä‘á»™c láº­p xuáº¥t hiá»‡n:
  `Y â¥ Z | Î¦(X)`
- Giáº£i thĂ­ch tá»«ng pháº§n:
  - Y â¥ Z: "Y vĂ  Z Ä‘á»™c láº­p..."
  - | Î¦(X): "...khi Ä‘Ă£ biáº¿t representation"
  - NghÄ©a lĂ : "Î¦(X) khĂ´ng cĂ²n thĂ´ng tin vá» Z ngoĂ i nhá»¯ng gĂ¬ cáº§n Ä‘á»ƒ predict Y"
- Diagram: Z bá»‹ lá»c ra khá»i Î¦(X). Chá»‰ cĂ²n Y-relevant information.

### AUDIO
"ChĂ­nh vĂ¬ IRM gáº·p khĂ³ khÄƒn khi environment khĂ´ng Ä‘á»§ Ä‘a dáº¡ng, NuRD â€” Nuisance-Randomized Distillation â€” tiáº¿p cáº­n váº¥n Ä‘á» tá»« má»™t gĂ³c khĂ¡c: thay vĂ¬ tĂ¬m invariance qua environments, hĂ£y trá»±c tiáº¿p loáº¡i bá» nuisance khá»i representation.

Äiá»u kiá»‡n cá»‘t lĂµi cá»§a NuRD: Y Ä‘á»™c láº­p vá»›i Z khi Ä‘Ă£ cĂ³ Î¦(X). NĂ³i dá»… hiá»ƒu: representation Î¦(X) khĂ´ng Ä‘Æ°á»£c chá»©a thĂªm thĂ´ng tin vá» nuisance Z ngoĂ i nhá»¯ng gĂ¬ Ä‘Ă£ Ä‘Æ°á»£c encode vĂ o Y.

Náº¿u Ä‘iá»u kiá»‡n nĂ y thá»a mĂ£n, báº¥t ká»³ bá»™ phĂ¢n loáº¡i nĂ o train trĂªn Î¦(X) cÅ©ng khĂ´ng thá»ƒ khai thĂ¡c Z â€” vĂ¬ Z Ä‘Ă£ bá»‹ lá»c ra.

NhÆ°ng cĂ¢u há»i thá»±c táº¿ lĂ : lĂ m sao phĂ¡t hiá»‡n Ä‘Æ°á»£c Z lĂ  gĂ¬ Ä‘á»ƒ mĂ  lá»c?"

---

## Scene N2 â€” PhĂ¡t hiá»‡n Nuisance: Semantic Corruption
**~90 giĂ¢y**

### VISUAL
- VĂ­ dá»¥ NLP: cĂ¢u gá»‘c "The movie was incredible and the acting superb."
- BÆ°á»›c 1 â€” N-gram randomization: xĂ¡o trá»™n thá»© tá»± tá»«:
  "incredible was The movie and superb acting the."
  Label: "N-gram randomized â€” ngá»¯ nghÄ©a máº¥t, n-gram bias cĂ²n"
- BÆ°á»›c 2 â€” Cho model dá»± Ä‘oĂ¡n trĂªn cĂ¢u bá»‹ xĂ¡o trá»™n.
  Náº¿u model váº«n predict Ä‘Ăºng â†’ Ä‘ang dĂ¹ng n-gram shortcut, khĂ´ng pháº£i ngá»¯ nghÄ©a.
- Animate: cĂ¢u gá»‘c [BLUE_D] â†’ xĂ¡o trá»™n [ORANGE] â†’ model predict â†’ accuracy váº«n cao [RED flash]
- Text: "Semantic Corruption = can thiá»‡p váº­t lĂ½ Ä‘á»ƒ lá»™ shortcut"
- Bá»• sung vĂ­ dá»¥ vision: áº£nh X-ray â†’ che patch ngáº«u nhiĂªn â†’ model váº«n predict ung thÆ°.
  "Model Ä‘ang nhĂ¬n vĂ o artifact cá»§a mĂ¡y, khĂ´ng pháº£i khá»‘i u."

### AUDIO
"CĂ¢u há»i cÄƒn báº£n: lĂ m sao biáº¿t model Ä‘ang dĂ¹ng spurious feature nĂ o?

Ká»¹ thuáº­t Ä‘áº§u tiĂªn: Semantic Corruption. Ă tÆ°á»Ÿng: náº¿u ta phĂ¡ há»§y ngá»¯ nghÄ©a thá»±c sá»± cá»§a input nhÆ°ng giá»¯ láº¡i spurious feature, model váº«n predict tá»‘t thĂ¬ nĂ³ Ä‘ang dĂ¹ng shortcut.

Trong NLP: xĂ¡o trá»™n thá»© tá»± tá»«. CĂ¢u vÄƒn máº¥t ngá»¯ nghÄ©a hoĂ n toĂ n â€” nhÆ°ng n-gram statistics, táº§n suáº¥t tá»«, váº«n cĂ²n. Náº¿u model sentiment analysis váº«n Ä‘Ăºng 80 pháº§n trÄƒm sau khi xĂ¡o trá»™n, nĂ³ Ä‘ang Ä‘áº¿m tá»«, khĂ´ng hiá»ƒu cĂ¢u.

Trong vision: che random patches cá»§a áº£nh X-ray. Náº¿u model váº«n detect ung thÆ° â€” vĂ  khá»‘i u náº±m trong patch bá»‹ che â€” model Ä‘ang dĂ¹ng artifact cá»§a thiáº¿t bá»‹ chá»¥p, khĂ´ng pháº£i khá»‘i u tháº­t.

Semantic Corruption cho ta map: shortcut nĂ o Ä‘ang Ä‘Æ°á»£c khai thĂ¡c."

---

## Scene N3 â€” Vision Masking: PhĂ¡t hiá»‡n báº±ng Che
**~90 giĂ¢y**

### VISUAL
- áº¢nh chim trĂªn ná»n nÆ°á»›c [BLUE_D frame].
- GradCAM / Attention map: model ERM táº­p trung vĂ o Ná»€N, khĂ´ng pháº£i con chim.
  Highlight vĂ¹ng ná»n [RED glow].
- BÆ°á»›c Masking: che ná»n â†’ chá»‰ cĂ²n con chim.
  Model má»›i predict: "Waterbird" â†’ nhÆ°ng accuracy DROP xuá»‘ng 60%.
  "Báº±ng chá»©ng: model Ä‘ang dĂ¹ng ná»n."
- BÆ°á»›c ngÆ°á»£c: che con chim â†’ chá»‰ cĂ²n ná»n.
  Model cÅ© váº«n predict Ä‘Ăºng vá»›i accuracy cao.
  [RED flash] "Confirmational: ná»n = spurious feature chĂ­nh"
- Text: "Vision Masking = Semantic Corruption cho áº£nh"

### AUDIO
"Vá»›i dá»¯ liá»‡u hĂ¬nh áº£nh, Semantic Corruption cĂ³ dáº¡ng Vision Masking â€” che Ä‘i cĂ¡c pháº§n cá»§a áº£nh.

CĂ¡ch lĂ m: láº¥y model ERM Ä‘Ă£ train, xem attention map hoáº·c GradCAM â€” báº£n Ä‘á»“ cho tháº¥y model Ä‘ang nhĂ¬n vĂ o vĂ¹ng nĂ o. Vá»›i Waterbirds, model ERM chá»§ yáº¿u nhĂ¬n vĂ o ná»n â€” nÆ°á»›c hay Ä‘áº¥t â€” chá»© khĂ´ng pháº£i con chim.

Kiá»ƒm chá»©ng: che ná»n Ä‘i, chá»‰ Ä‘á»ƒ láº¡i con chim. Accuracy model ERM giáº£m máº¡nh â€” báº±ng chá»©ng nĂ³ Ä‘ang dĂ¹ng ná»n.

Che con chim Ä‘i, chá»‰ Ä‘á»ƒ láº¡i ná»n. Accuracy váº«n cao â€” xĂ¡c nháº­n ná»n lĂ  shortcut chĂ­nh.

Vision Masking lĂ  cĂ´ng cá»¥ diagnostic máº¡nh: nĂ³ khĂ´ng chá»‰ nĂ³i 'model Ä‘ang dĂ¹ng shortcut' mĂ  cĂ²n nĂ³i 'shortcut náº±m á»Ÿ Ä‘Ă¢u'."

---

## Scene N4 â€” Teacher-Student Distillation
**~2 phĂºt**

### VISUAL
- Hai mĂ´ hĂ¬nh song song:
  - Teacher [ORANGE, lá»›n]: Ä‘Æ°á»£c train trĂªn corrupted input (n-gram shuffled / masked)
    â†’ Teacher chá»‰ cĂ³ thá»ƒ há»c shortcut Z, khĂ´ng cĂ³ ngá»¯ nghÄ©a tháº­t
  - Student [BLUE_D, nhá» hÆ¡n]: Ä‘Æ°á»£c train trĂªn original input
- QuĂ¡ trĂ¬nh distillation:
  `Teacher(X_corrupted) â†’ soft labels [pâ‚, pâ‚‚, ...]`
  `Student há»c: predict Y AND diverge from Teacher`
- CĂ´ng thá»©c:
  `L_student = L_CE(Å·, y) + Î± Â· L_KL(f_student(X) â€– f_teacher(X_corrupted))`
  Vá»›i dáº¥u NGÆ¯á»¢C: student bá»‹ pháº¡t khi GIá»NG teacher â†’ Ă©p student há»c Ä‘iá»u KHĂC teacher.
- Animate: Teacher confident vá» ná»n â†’ Student bá»‹ Ă©p pháº£i tĂ¬m signal khĂ¡c â†’ há»c hĂ¬nh dĂ¡ng con váº­t.
- Text: "Teacher dáº¡y student nhá»¯ng gĂ¬ KHĂ”NG nĂªn há»c"

### AUDIO
"NuRD dĂ¹ng má»™t ká»¹ thuáº­t tinh táº¿: Teacher-Student distillation ngÆ°á»£c.

Ă tÆ°á»Ÿng: train má»™t Teacher model trĂªn corrupted input â€” vĂ­ dá»¥ cĂ¢u vÄƒn Ä‘Ă£ bá»‹ xĂ¡o trá»™n, hoáº·c áº£nh Ä‘Ă£ che máº¥t semantic content. Teacher nĂ y CHá»ˆ cĂ³ thá»ƒ há»c shortcuts vĂ¬ semantic content Ä‘Ă£ bá»‹ phĂ¡ há»§y.

Student model Ä‘Æ°á»£c train trĂªn input gá»‘c, vá»›i hai má»¥c tiĂªu Ä‘á»“ng thá»i: má»™t, predict Ä‘Ăºng nhĂ£n Y. Hai, vĂ  Ä‘Ă¢y lĂ  pháº§n quan trá»ng, diverge khá»i Teacher â€” tá»©c lĂ  Ä‘Æ°a ra prediction KHĂC Teacher khi cĂ³ thá»ƒ.

VĂ¬ Teacher Ä‘Ă£ há»c háº¿t shortcuts, divergence penalty Ă©p Student pháº£i tĂ¬m signal khĂ¡c â€” nhá»¯ng gĂ¬ Teacher khĂ´ng thá»ƒ há»c tá»« corrupted input. ÄĂ³ chĂ­nh lĂ  semantic signal, causal features.

ÄĂ¢y lĂ  má»™t cÆ¡ cháº¿ elegant: Teacher khĂ´ng dáº¡y Student nhá»¯ng gĂ¬ Ä‘Ăºng, mĂ  dáº¡y nhá»¯ng gĂ¬ sai Ä‘á»ƒ Student trĂ¡nh."

---

## Scene N5 â€” Mutual Information Intuition
**~90 giĂ¢y**

### VISUAL
- Diagram Venn: 3 vĂ²ng trĂ²n chá»“ng nhau:
  I(Î¦(X); Y) [BLUE_D] â€” thĂ´ng tin vá» nhĂ£n
  I(Î¦(X); Z) [RED] â€” thĂ´ng tin vá» nuisance
  I(Î¦(X); X) [GRAY] â€” tá»•ng thĂ´ng tin
- Má»¥c tiĂªu NuRD Ä‘Æ°á»£c visualize:
  `maximize I(Î¦(X); Y)` â†’ vĂ²ng BLUE_D lá»›n ra
  `minimize I(Î¦(X); Z)` â†’ vĂ²ng RED nhá» láº¡i
- VĂ¹ng chá»“ng láº¥p: "ThĂ´ng tin vá» Z mĂ  khĂ´ng cáº§n Ä‘á»ƒ predict Y â†’ Ä‘Ă¢y lĂ  spurious"
- CĂ´ng thá»©c Ä‘áº§y Ä‘á»§:
  `max_Î¦  I(Î¦(X); Y)  âˆ’  Î² Â· I(Î¦(X); Z)`
- Text: "NuRD = Information Bottleneck cĂ³ Ä‘á»‹nh hÆ°á»›ng"

### AUDIO
"NhĂ¬n NuRD qua lÄƒng kĂ­nh information theory cho tháº¥y bá»©c tranh Ä‘áº§y Ä‘á»§ hÆ¡n.

Má»¥c tiĂªu: maximize thĂ´ng tin mĂ  Î¦(X) chá»©a vá» Y â€” Ä‘á»ƒ predict tá»‘t â€” trong khi minimize thĂ´ng tin mĂ  Î¦(X) chá»©a vá» Z â€” Ä‘á»ƒ khĂ´ng dĂ¹ng shortcut.

ÄĂ¢y lĂ  dáº¡ng Information Bottleneck cĂ³ Ä‘á»‹nh hÆ°á»›ng: thay vĂ¬ chá»‰ compress thĂ´ng tin tá»•ng quĂ¡t, ta compress theo hÆ°á»›ng loáº¡i bá» Z cá»¥ thá»ƒ.

Tham sá»‘ Î² kiá»ƒm soĂ¡t trade-off: Î² lá»›n â†’ loáº¡i Z triá»‡t Ä‘á»ƒ hÆ¡n nhÆ°ng cĂ³ thá»ƒ máº¥t má»™t sá»‘ thĂ´ng tin vá» Y. Î² nhá» â†’ an toĂ n hÆ¡n nhÆ°ng Z cĂ³ thá»ƒ lá»t qua.

Káº¿t há»£p vá»›i Teacher-Student distillation vĂ  Semantic Corruption, NuRD táº¡o thĂ nh má»™t pipeline hoĂ n chá»‰nh: phĂ¡t hiá»‡n nuisance â†’ loáº¡i bá» nuisance â†’ train representation sáº¡ch.

ChĂ­nh vĂ¬ nhá»¯ng káº¿t quáº£ Ä‘áº§y há»©a háº¹n cá»§a NuRD trĂªn NLP, cá»™ng Ä‘á»“ng báº¯t Ä‘áº§u tĂ¬m kiáº¿m phÆ°Æ¡ng phĂ¡p tÆ°Æ¡ng tá»± cho structured data â€” nÆ¡i mĂ  group labels Ä‘Ă´i khi cĂ³ thá»ƒ thu tháº­p Ä‘Æ°á»£c. VĂ  Ä‘Ă³ lĂ  bá»‘i cáº£nh ra Ä‘á»i cá»§a Group DRO."

---
---

# PART IX â€” GROUP DRO: "Tá»‘i Æ°u cho Káº» Yáº¿u Nháº¥t"

---

## Scene 5.1 â€” Group DRO: CĂ´ng thá»©c Äáº§y Ä‘á»§
**~2.5 phĂºt**

### VISUAL
- Pie chart Waterbirds (4 máº£nh):
  Waterbird+Water: 45% [BLUE_D], Landbird+Land: 45% [GREEN_D]
  Waterbird+Land: 5% [RED nháº¥p nhĂ¡y], Landbird+Water: 5% [RED nháº¥p nhĂ¡y]
- CĂ´ng thá»©c ERM: `min_Î¸ Î£_g p_g Â· đ”¼_g[â„“]`
  MÅ©i tĂªn: "p_g nhá» â†’ bá»‹ bá» qua"
- TransformMatchingTex: `Î£_g p_g` â†’ `max_g`:
  ```
  min_h  max_{gâˆˆG}  đ”¼_{(x,y)~P_g} [â„“(h(x), y)]
  ```
- "max" xuáº¥t hiá»‡n GOLD, glow. Text: "Thay trung bĂ¬nh báº±ng worst-case"
- Expand cĂ´ng thá»©c thĂ nh 2 pháº§n:
  - **Inner maximization**: `max_{gâˆˆG} R_g(h)` â†’ tĂ¬m group Ä‘ang tá»‡ nháº¥t
  - **Outer minimization**: `min_h` â†’ tá»‘i Æ°u model cho group Ä‘Ă³
- VĂ²ng láº·p animate:
  Step 1: tĂ­nh R_g cho má»i group â†’ highlight group tá»‡ nháº¥t
  Step 2: upweight group Ä‘Ă³ â†’ update h
  Step 3: quay láº¡i Step 1

### AUDIO
"Group DRO thay Ä‘á»•i má»¥c tiĂªu báº±ng má»™t tá»«: max.

ERM minimize trung bĂ¬nh cĂ³ trá»ng sá»‘. NhĂ³m nhá» cĂ³ trá»ng sá»‘ nhá» â€” tá»± Ä‘á»™ng bá»‹ bá» qua.

Group DRO viáº¿t láº¡i bĂ i toĂ¡n hoĂ n toĂ n: minimize over h, maximize over g. Hai lá»›p tá»‘i Æ°u lá»“ng nhau.

Inner maximization: vá»›i mĂ´ hĂ¬nh h hiá»‡n táº¡i, tĂ¬m group nĂ o Ä‘ang cĂ³ risk cao nháº¥t. ÄĂ¢y lĂ  worst-case group.

Outer minimization: cáº­p nháº­t h Ä‘á»ƒ giáº£m risk cá»§a worst-case group Ä‘Ă³.

Thuáº­t toĂ¡n láº·p láº¡i: group nĂ o tá»‡ nháº¥t thĂ¬ Ä‘Æ°á»£c upweight, h pháº£i quan tĂ¢m Ä‘áº¿n group Ä‘Ă³. VĂ²ng tiáº¿p theo, cĂ³ thá»ƒ group khĂ¡c tá»‡ hÆ¡n â€” láº¡i upweight group má»›i.

Káº¿t quáº£: má»i group Ä‘á»u Ä‘Æ°á»£c báº£o vá»‡. KhĂ´ng group nĂ o bá»‹ bá» láº¡i phĂ­a sau."

---

## Scene 5.2 â€” Oracle vs Practical: Giá»›i háº¡n cá»§a Group DRO
**~90 giĂ¢y**

### VISUAL
- Hai cá»™t: "Oracle Setting" [GOLD] vs "Practical Setting" [GRAY]
- Oracle:
  - Biáº¿t chĂ­nh xĂ¡c group label (g) cá»§a má»i Ä‘iá»ƒm training
  - Biáº¿t R_g cho má»i g
  - Group DRO hoáº¡t Ä‘á»™ng hoĂ n háº£o
- Practical:
  - Group label cáº§n annotation thá»§ cĂ´ng â†’ tá»‘n kĂ©m
  - Vá»›i Waterbirds: pháº£i gĂ¡n nhĂ£n "ná»n lĂ  nÆ°á»›c hay Ä‘áº¥t" cho hĂ ng váº¡n áº£nh
  - Vá»›i CivilComments: pháº£i gĂ¡n nhĂ£n demographic identity cho má»i comment
- Báº£ng chi phĂ­ annotation:
  | Dataset | Sá»‘ máº«u | Chi phĂ­ Æ°á»›c tĂ­nh |
  |---------|--------|-----------------|
  | Waterbirds | 4,795 | ~$500 |
  | CelebA | 202,599 | ~$20,000 |
  | CivilComments | 448,000 | ~$45,000 |
- Text: "Oracle Group DRO ráº¥t máº¡nh. NhÆ°ng ai tráº£ tiá»n annotation?"

### AUDIO
"Group DRO cĂ³ má»™t Ä‘iá»ƒm máº¡nh rĂµ rĂ ng: khi group labels Ä‘áº§y Ä‘á»§, nĂ³ consistently lĂ  phÆ°Æ¡ng phĂ¡p tá»‘t nháº¥t trĂªn háº§u háº¿t benchmark.

NhÆ°ng Ä‘Ă¢y lĂ  váº¥n Ä‘á» thá»±c táº¿. Group DRO cáº§n biáº¿t group label cá»§a tá»«ng Ä‘iá»ƒm training. Vá»›i Waterbirds: má»—i áº£nh cáº§n nhĂ£n 'ná»n lĂ  nÆ°á»›c hay Ä‘áº¥t'. Vá»›i CelebA: má»—i khuĂ´n máº·t cáº§n nhĂ£n giá»›i tĂ­nh. Vá»›i CivilComments: má»—i comment cáº§n nhĂ£n demographic.

Annotation thá»§ cĂ´ng cho hĂ ng trÄƒm nghĂ¬n máº«u khĂ´ng kháº£ thi. VĂ  ká»ƒ cáº£ khi cĂ³ ngĂ¢n sĂ¡ch, annotation con ngÆ°á»i cĂ³ sai sá»‘ vĂ  bias.

ChĂ­nh vĂ¬ limitation nĂ y, cá»™ng Ä‘á»“ng Ä‘Ă£ phĂ¡t triá»ƒn hai hÆ°á»›ng: má»™t lĂ  tá»± Ä‘á»™ng hĂ³a annotation báº±ng Foundation Models â€” Ä‘Ă³ lĂ  PfR ta sáº½ tháº¥y sau. Hai lĂ  khĂ´ng cáº§n annotation group â€” Ä‘Ă³ lĂ  JTT ngay bĂ¢y giá»."

---
---

# PART X â€” JTT: "Äá»ƒ ERM Tá»± Chá»‰ Ra Äiá»ƒm Yáº¿u"

---

## Scene 6.1 â€” JTT: Hai vĂ²ng Train
**~2.5 phĂºt**

### VISUAL
- CĂ¢u há»i lá»›n: "Náº¿u khĂ´ng biáº¿t má»—i Ä‘iá»ƒm thuá»™c nhĂ³m nĂ o... lĂ m sao tĂ¬m Ä‘Æ°á»£c nhĂ³m thiá»ƒu sá»‘?"
- Text xuáº¥t hiá»‡n: "HĂ£y Ä‘á»ƒ ERM tá»± chá»‰ ra."
- Timeline 2 giai Ä‘oáº¡n:

**GIAI ÄOáº N 1 â€” ERM sÆ¡ bá»™ (5 epochs):**
- Thanh progress ngáº¯n.
- Káº¿t quáº£: 2 rá»• xuáº¥t hiá»‡n:
  - Rá»• GRAY (Ä‘Ăºng): má». "Dá»… â€” shortcut hoáº¡t Ä‘á»™ng"
  - Rá»• GOLD (sai): sĂ¡ng, nháº¥p nhĂ¡y. "KhĂ³ â€” shortcut sai hÆ°á»›ng!"
- Giáº£i thĂ­ch: (Penguin, tuyáº¿t) â†’ shortcut Ä‘Ăºng â†’ rá»• GRAY. (Penguin, cĂ¡t) â†’ shortcut sai â†’ rá»• GOLD.

**GIAI ÄOáº N 2 â€” Train robust:**
- Láº¥y rá»• GOLD. NhĂ¢n báº£n K=20 láº§n (animate: con sá»‘ K=20 xuáº¥t hiá»‡n to).
- Dataset má»›i: rá»• GOLD chiáº¿m tá»‰ lá»‡ lá»›n hÆ¡n. Train mĂ´ hĂ¬nh thá»© 2.

**Káº¿t quáº£:**
- ERM: Worst-Group = 32% [RED]
- JTT: Worst-Group = 71% [GREEN]
- Label: "â† KhĂ´ng cáº§n má»™t nhĂ£n nhĂ³m nĂ o!"

### AUDIO
"JTT â€” Just Train Twice â€” cĂ³ cĂ¢u tráº£ lá»i thanh lá»‹ch: hĂ£y Ä‘á»ƒ ERM tá»± chá»‰ ra Ä‘iá»ƒm yáº¿u.

BÆ°á»›c má»™t: train má»™t mĂ´ hĂ¬nh ERM nhá» trong vĂ i epochs â€” Ä‘á»§ Ä‘á»ƒ nĂ³ há»c shortcuts, nhÆ°ng chÆ°a memorize. NhĂ¬n vĂ o nhá»¯ng Ä‘iá»ƒm mĂ  mĂ´ hĂ¬nh nĂ y dá»± Ä‘oĂ¡n sai.

Táº¡i sao nhá»¯ng Ä‘iá»ƒm bá»‹ sai láº¡i quan trá»ng? VĂ¬ mĂ´ hĂ¬nh ERM há»c shortcuts ngay láº­p tá»©c. Äiá»ƒm nĂ o thuá»™c nhĂ³m Ä‘a sá»‘ â€” shortcut hoáº¡t Ä‘á»™ng â€” dá»± Ä‘oĂ¡n Ä‘Ăºng. Äiá»ƒm nĂ o thuá»™c nhĂ³m thiá»ƒu sá»‘ â€” shortcut sai hÆ°á»›ng â€” dá»± Ä‘oĂ¡n sai.

Nhá»¯ng Ä‘iá»ƒm bá»‹ sai chĂ­nh xĂ¡c lĂ  minority: penguin trĂªn cĂ¡t, bĂ² trĂªn cĂ¡t â€” nhá»¯ng trÆ°á»ng há»£p mĂ  shortcut 'ná»n mĂ u gĂ¬' chá»‰ sai hÆ°á»›ng.

BÆ°á»›c hai: gom nhá»¯ng Ä‘iá»ƒm sai Ä‘Ă³, nhĂ¢n báº£n K=20 láº§n, táº¡o dataset má»›i cĂ¢n báº±ng hÆ¡n. Train mĂ´ hĂ¬nh thá»© hai trĂªn dataset nĂ y.

Káº¿t quáº£ trĂªn Waterbirds: Worst-group accuracy tÄƒng tá»« 32 lĂªn 71 pháº§n trÄƒm â€” mĂ  khĂ´ng cáº§n má»™t nhĂ£n nhĂ³m thá»§ cĂ´ng nĂ o.

ERM Ä‘Ă£ tá»± lá»™ ra Ä‘iá»ƒm yáº¿u cá»§a chĂ­nh mĂ¬nh."

---

## Scene 6.2 â€” So sĂ¡nh Methods: Ai tá»‘t khi nĂ o?
**~90 giĂ¢y**

### VISUAL
- Báº£ng so sĂ¡nh 5 methods:

| Method | Cáº§n group labels? | Cáº§n environments? | Worst-Group Acc | PhĂ¹ há»£p khi |
|--------|------------------|-------------------|-----------------|-------------|
| ERM | KhĂ´ng | KhĂ´ng | Tháº¥p | Baseline |
| Reweighting | CĂ³ (hoáº·c Æ°á»›c lÆ°á»£ng) | KhĂ´ng | Trung bĂ¬nh | Dataset nhá» |
| IRM | KhĂ´ng | CĂ“ (Ä‘a dáº¡ng) | Cao (náº¿u environments tá»‘t) | Environments rĂµ |
| NuRD | KhĂ´ng | KhĂ´ng | Cao (NLP) | NLP, vision cĂ³ corruption |
| Group DRO | CĂ“ | KhĂ´ng | Cao nháº¥t | CĂ³ oracle labels |
| JTT | KhĂ´ng | KhĂ´ng | Cao | KhĂ´ng cĂ³ labels/environments |

- Highlight: khĂ´ng cĂ³ phÆ°Æ¡ng phĂ¡p nĂ o win táº¥t cáº£.
- Há»™p GOLD: "Chá»n method = chá»n giáº£ Ä‘á»‹nh phĂ¹ há»£p vá»›i bĂ i toĂ¡n cá»§a báº¡n"

### AUDIO
"Sau khi Ä‘i qua nÄƒm phÆ°Æ¡ng phĂ¡p, cáº§n nhĂ¬n toĂ n cáº£nh: khĂ´ng cĂ³ silver bullet.

Reweighting Ä‘Æ¡n giáº£n nhÆ°ng tháº¥t báº¡i vá»›i máº¡ng lá»›n. IRM thanh lá»‹ch vá» lĂ½ thuyáº¿t nhÆ°ng cáº§n environments cháº¥t lÆ°á»£ng cao. NuRD máº¡nh vá»›i NLP nhÆ°ng cáº§n thiáº¿t káº¿ corruption cáº©n tháº­n. Group DRO máº¡nh nháº¥t khi cĂ³ labels. JTT linh hoáº¡t nháº¥t khi khĂ´ng cĂ³ gĂ¬.

Chá»n phÆ°Æ¡ng phĂ¡p nĂ o phá»¥ thuá»™c vĂ o giáº£ Ä‘á»‹nh báº¡n cĂ³ thá»ƒ lĂ m: báº¡n cĂ³ environments khĂ´ng? Báº¡n cĂ³ group labels khĂ´ng? Báº¡n cĂ³ thá»ƒ thiáº¿t káº¿ corruption khĂ´ng?

Hiá»ƒu Ä‘iá»u nĂ y quan trá»ng hÆ¡n lĂ  nhá»› cĂ´ng thá»©c. Má»—i phÆ°Æ¡ng phĂ¡p lĂ  lá»i giáº£i cho má»™t bĂ i toĂ¡n cĂ³ giáº£ Ä‘á»‹nh cá»¥ thá»ƒ.

NhÆ°ng trong thá»±c táº¿ â€” ká»ƒ cáº£ khi báº¡n chá»n Ä‘Ăºng phÆ°Æ¡ng phĂ¡p â€” cĂ²n má»™t cĂ¢u há»i lá»›n hÆ¡n: cĂ¡c benchmark ta Ä‘ang dĂ¹ng Ä‘á»ƒ Ä‘Ă¡nh giĂ¡ cĂ³ thá»±c sá»± pháº£n Ă¡nh robustness tháº­t khĂ´ng? ÄĂ¢y lĂ  cĂ¢u há»i mĂ  pháº§n tiáº¿p theo sáº½ tráº£ lá»i, vĂ  cĂ¢u tráº£ lá»i khĂ´ng dá»… chá»‹u."
# Ká»CH Báº¢N V3 â€” PART XI
## Benchmark Crisis

---

# PART XI â€” BENCHMARKS & REALITY CHECK

---

## Scene B1 â€” Gallery Benchmark: 4 Chiáº¿n trÆ°á»ng Thá»±c táº¿
**~2 phĂºt**

### VISUAL
- Grid 2Ă—2, má»—i Ă´ lĂ  má»™t benchmark. Xuáº¥t hiá»‡n láº§n lÆ°á»£t:

**[Waterbirds]** [BLUE_D frame]
- Icon: chim + nÆ°á»›c/Ä‘áº¥t
- Task: phĂ¢n loáº¡i waterbird vs landbird
- Spurious: background (water vs land)
- Train: 4,795 áº£nh. WG Gap: ~50%
- Note: "ÄÆ°á»£c táº¡o nhĂ¢n táº¡o â€” spurious correlation kiá»ƒm soĂ¡t Ä‘Æ°á»£c"

**[CelebA]** [GREEN_D frame]
- Icon: khuĂ´n máº·t
- Task: hair color (blonde vs non-blonde)
- Spurious: gender
- Train: 162,770 áº£nh. WG Gap: ~40%
- Note: "Dataset thá»±c táº¿ â€” bias gender thá»±c trong celebrity photos"

**[CivilComments-WILDS]** [YELLOW_D frame]
- Icon: text bubble
- Task: toxicity detection
- Spurious: demographic identity (race, religion, gender)
- Train: 269,038 comments. WG Gap: ~35%
- Note: "High stakes â€” AI moderation thá»±c táº¿"

**[Camelyon17-WILDS]** [PURPLE frame]
- Icon: kĂ­nh hiá»ƒn vi
- Task: tumor detection
- Spurious: hospital (scanner artifacts)
- Train: 302,436 patches. WG Gap: ~30%
- Note: "Medical AI â€” different hospitals = different scanners"

### AUDIO
"Cá»™ng Ä‘á»“ng xĂ¢y dá»±ng bá»‘n benchmark chuáº©n Ä‘á»ƒ Ä‘Ă¡nh giĂ¡ cĂ¡c phÆ°Æ¡ng phĂ¡p robust.

Waterbirds: dataset nhĂ¢n táº¡o, spurious correlation Ä‘Æ°á»£c kiá»ƒm soĂ¡t chĂ­nh xĂ¡c. LĂ½ tÆ°á»Ÿng Ä‘á»ƒ test phÆ°Æ¡ng phĂ¡p trong mĂ´i trÆ°á»ng clean.

CelebA: khuĂ´n máº·t celebrity. Task lĂ  phĂ¡t hiá»‡n tĂ³c vĂ ng, nhÆ°ng trong dataset, tĂ³c vĂ ng tÆ°Æ¡ng quan máº¡nh vá»›i giá»›i tĂ­nh ná»¯. AI há»c Ä‘Æ°á»£c: blonde equals female, vĂ  ngÆ°á»£c láº¡i.

CivilComments: moderation ná»™i dung Ä‘á»™c háº¡i online. NhÆ°ng tá»« ngá»¯ nháº­n diá»‡n nhĂ³m dĂ¢n sá»‘ â€” nhÆ° tĂªn tĂ´n giĂ¡o hay chá»§ng tá»™c â€” tÆ°Æ¡ng quan vá»›i viá»‡c bá»‹ gĂ¡n nhĂ£n toxic, dĂ¹ khĂ´ng pháº£i nguyĂªn nhĂ¢n. AI há»c bias nguy hiá»ƒm.

Camelyon17: phĂ¡t hiá»‡n khá»‘i u tá»« áº£nh kĂ­nh hiá»ƒn vi. Spurious lĂ  artifact cá»§a mĂ¡y scanner tá»« cĂ¡c bá»‡nh viá»‡n khĂ¡c nhau. AI há»c cĂ¡ch nháº­n ra mĂ¡y, khĂ´ng pháº£i khá»‘i u."

---

## Scene B2 â€” Benchmark Disagreement: Káº¿t quáº£ Láº«n lá»™n
**~2 phĂºt**

### VISUAL
- Grouped bar chart: 5 phÆ°Æ¡ng phĂ¡p Ă— 4 datasets
  ERM [GRAY], IRM [BLUE_D], Group DRO [GREEN_D], JTT [YELLOW_D], CORAL [PURPLE]
- Quan sĂ¡t quan trá»ng â€” animate tá»«ng Ä‘iá»ƒm:
  1. ERM Ä‘Æ°á»£c tuning tá»‘t â‰ˆ state-of-the-art á»Ÿ 2/4 datasets [ORANGE highlight]
  2. IRM win á»Ÿ Waterbirds nhÆ°ng thua á»Ÿ CivilComments [RED dashes]
  3. Group DRO win khi cĂ³ labels, nhÆ°ng khĂ´ng pháº£i luĂ´n [GREEN]
  4. KhĂ´ng cĂ³ phÆ°Æ¡ng phĂ¡p nĂ o win táº¥t cáº£ 4 [RED X lá»›n]
- Pearson correlation heatmap giá»¯a performance trĂªn cĂ¡c dataset:
  Nhiá»u Ă´ mĂ u Láº NH (correlation tháº¥p) â†’ "Win á»Ÿ dataset nĂ y khĂ´ng Ä‘áº£m báº£o win á»Ÿ dataset kia"
- Text: "BENCHMARK DISAGREEMENT â€” khĂ´ng cĂ³ silver bullet"

### AUDIO
"VĂ  Ä‘Ă¢y lĂ  sá»± tháº­t phÅ© phĂ ng tá»« benchmark.

NhĂ¬n vĂ o káº¿t quáº£ thá»±c nghiá»‡m: khĂ´ng cĂ³ phÆ°Æ¡ng phĂ¡p nĂ o thá»‘ng trá»‹ tuyá»‡t Ä‘á»‘i. Tá»‡ hÆ¡n: ERM Ä‘Æ°á»£c tuning cáº©n tháº­n â€” chá»n learning rate, weight decay vĂ  augmentation tá»‘t â€” thÆ°á»ng cáº¡nh tranh Ä‘Æ°á»£c vá»›i cĂ¡c phÆ°Æ¡ng phĂ¡p phá»©c táº¡p hÆ¡n nhiá»u.

IRM win á»Ÿ Waterbirds nhÆ°ng thua á»Ÿ CivilComments. Group DRO máº¡nh khi cĂ³ labels Ä‘áº§y Ä‘á»§ nhÆ°ng fragile khi labels á»“n. JTT á»•n Ä‘á»‹nh hÆ¡n nhÆ°ng khĂ´ng Ä‘á»‰nh cao.

Pearson correlation heatmap giá»¯a performance trĂªn cĂ¡c dataset: correlation tháº¥p. Win á»Ÿ Waterbirds khĂ´ng bĂ¡o hiá»‡u win á»Ÿ CivilComments. Hai benchmark Ä‘ang Ä‘o hai thá»© khĂ¡c nhau.

Äiá»u nĂ y Ä‘áº·t ra cĂ¢u há»i sĂ¢u hÆ¡n: cĂ³ pháº£i phÆ°Æ¡ng phĂ¡p khĂ´ng tá»‘t, hay chĂ­nh benchmark Ä‘ang cĂ³ váº¥n Ä‘á»?"

---

## Scene B3 â€” Are Benchmarks Realistic?
**~90 giĂ¢y**

### VISUAL
- Waterbirds Ä‘Æ°á»£c táº¡o nhĂ¢n táº¡o: correlation 95% Ä‘Æ°á»£c set thá»§ cĂ´ng.
  CĂ¢u há»i: "Trong thá»±c táº¿, correlation cĂ³ máº¡nh Ä‘áº¿n 95% khĂ´ng?"
- CelebA: celebrity photos â€” khĂ´ng Ä‘áº¡i diá»‡n cho dĂ¢n sá»‘ tháº­t.
  "Bias cá»§a celebrity â‰  bias trong á»©ng dá»¥ng tháº­t"
- Biá»ƒu Ä‘á»“: OOD gap á»Ÿ Waterbirds (lab) vs OOD gap á»Ÿ hospital EHR (real).
  Lab gap: predictable, structured. Real gap: messy, multi-source.
- Text: "Benchmark tá»‘t vá» kiá»ƒm soĂ¡t, nhÆ°ng Ä‘Æ¡n giáº£n hĂ³a quĂ¡ má»©c"
- Há»™p ORANGE: "Algorithms win benchmark â‰  algorithms work in deployment"

### AUDIO
"Má»™t cĂ¢u há»i quan trá»ng thÆ°á»ng bá»‹ bá» qua: liá»‡u cĂ¡c benchmark nĂ y cĂ³ thá»±c sá»± pháº£n Ă¡nh váº¥n Ä‘á» ngoĂ i Ä‘á»i thá»±c khĂ´ng?

Waterbirds cĂ³ spurious correlation 95 pháº§n trÄƒm Ä‘Æ°á»£c set thá»§ cĂ´ng. Trong thá»±c táº¿, distribution shift khĂ´ng Ä‘Æ¡n giáº£n vĂ  cĂ³ cáº¥u trĂºc nhÆ° váº­y. NĂ³ noisy, multi-source, vĂ  thay Ä‘á»•i khĂ´ng theo quy luáº­t rĂµ rĂ ng.

CelebA dĂ¹ng áº£nh celebrity â€” má»™t nhĂ³m dĂ¢n sá»‘ ráº¥t Ä‘áº·c biá»‡t, khĂ´ng Ä‘áº¡i diá»‡n cho deployment thá»±c táº¿.

Káº¿t quáº£: thuáº­t toĂ¡n Ä‘Æ°á»£c thiáº¿t káº¿ Ä‘á»ƒ win benchmark cĂ³ thá»ƒ khai thĂ¡c cáº¥u trĂºc nhĂ¢n táº¡o cá»§a benchmark, khĂ´ng pháº£i há»c robustness tháº­t sá»±. ÄĂ¢y lĂ  model selection problem á»Ÿ cáº¥p Ä‘á»™ meta: benchmark selection."

---

## Scene B4 â€” Model Selection Paradox
**~90 giĂ¢y**

### VISUAL
- VĂ²ng láº·p luáº©n quáº©n (circular arrows, xoay):
  "Muá»‘n chá»n model OOD tá»‘t nháº¥t"
  â†’ "Cáº§n validation set OOD"
  â†’ "Náº¿u cĂ³ OOD val set â†’ sao khĂ´ng train trá»±c tiáº¿p?"
  â†’ "ÄÆ°a vĂ o train â†’ khĂ´ng cĂ²n lĂ  OOD ná»¯a!"
  â†’ (quay láº¡i Ä‘áº§u)
- Text trung tĂ¢m: "MODEL SELECTION PARADOX" [GOLD]
- Hai lá»±a chá»n khĂ´ng hoĂ n háº£o:
  A: DĂ¹ng ID validation â†’ khĂ´ng Ä‘áº£m báº£o OOD performance
  B: Giáº£ Ä‘á»‹nh biáº¿t test distribution â†’ khĂ´ng thá»±c táº¿
- Text: "Open Problem â€” chÆ°a cĂ³ lá»i giáº£i hoĂ n háº£o"

### AUDIO
"Má»™t nghá»‹ch lĂ½ thá»±c tiá»…n khĂ´ng cĂ³ lá»i giáº£i hoĂ n háº£o.

Sau khi train ERM, IRM, vĂ  Group DRO, báº¡n cáº§n chá»n model nĂ o Ä‘á»ƒ deploy. Báº¡n cáº§n validation set OOD Ä‘á»ƒ Ä‘Ă¡nh giĂ¡.

NhÆ°ng náº¿u Ä‘Ă£ cĂ³ OOD validation set, táº¡i sao khĂ´ng dĂ¹ng nĂ³ Ä‘á»ƒ train? VĂ  náº¿u dĂ¹ng Ä‘á»ƒ train, nĂ³ khĂ´ng cĂ²n lĂ  OOD ná»¯a.

DĂ¹ng ID validation set thÆ°á»ng khĂ´ng tÆ°Æ¡ng quan tá»‘t vá»›i OOD performance. Tutorial gá»i Ä‘Ă¢y lĂ  má»™t trong nhá»¯ng open problems quan trá»ng nháº¥t cá»§a lÄ©nh vá»±c.

VĂ  ká»ƒ cáº£ khi giáº£i quyáº¿t Ä‘Æ°á»£c model selection â€” váº«n cĂ²n má»™t cĂ¢u há»i lá»›n hÆ¡n: liá»‡u Foundation Models cĂ³ thay Ä‘á»•i toĂ n bá»™ bá»©c tranh nĂ y khĂ´ng? CĂ¢u tráº£ lá»i phá»©c táº¡p hÆ¡n ta nghÄ©."

---

## Scene B5 â€” Best Practices: Flowchart Thá»±c tiá»…n
**~2 phĂºt**

### VISUAL
- Decision flowchart, tá»«ng nhĂ¡nh sĂ¡ng lĂªn theo lá»i Ä‘á»c:
  ```
  START
    â†“
  Loáº¡i Distribution Shift?
  (Covariate / Label / Spurious)
    â†“
  CĂ³ Group Labels khĂ´ng?
    â”œâ”€ CĂ“  â†’ Group DRO
    â””â”€ KHĂ”NG â†’ JTT hoáº·c NuRD
    â†“
  CĂ³ Environments Ä‘a dáº¡ng?
    â”œâ”€ CĂ“  â†’ ThĂªm IRM penalty
    â””â”€ KHĂ”NG â†’ Táº­p trung vĂ o data collection
    â†“
  Äang dĂ¹ng Foundation Model?
    â”œâ”€ CĂ“  â†’ PfR / Last Layer Retraining trÆ°á»›c
    â””â”€ KHĂ”NG â†’ Tune ERM ká»¹ lĂ m baseline
    â†“
  LUĂ”N report Worst-Group Accuracy
  ```
- Cuá»‘i cĂ¹ng toĂ n bá»™ cĂ¢y sĂ¡ng [GOLD glow].

### AUDIO
"Tutorial Ä‘Ăºc káº¿t thĂ nh báº£y nguyĂªn táº¯c thá»±c tiá»…n.

Má»™t: hiá»ƒu rĂµ loáº¡i distribution shift trÆ°á»›c khi chá»n phÆ°Æ¡ng phĂ¡p. Hai: luĂ´n report Worst-Group Accuracy, khĂ´ng chá»‰ average. Ba: tune ERM tháº­t ká»¹ lĂ m baseline â€” Ä‘á»«ng bá» qua bÆ°á»›c nĂ y. Bá»‘n: náº¿u cĂ³ group labels, Group DRO lĂ  lá»±a chá»n máº¡nh nháº¥t. NÄƒm: náº¿u khĂ´ng, JTT hoáº·c NuRD lĂ  Ä‘iá»ƒm khá»Ÿi Ä‘áº§u tá»‘t. SĂ¡u: vá»›i foundation models, thá»­ Last Layer Retraining trÆ°á»›c khi fine-tune toĂ n bá»™. Báº£y: thu tháº­p thĂªm dá»¯ liá»‡u Ä‘a dáº¡ng mĂ´i trÆ°á»ng â€” data collection thÆ°á»ng hiá»‡u quáº£ hÆ¡n má»i algorithmic fix.

BĂ¢y giá» ta Ä‘Ă£ cĂ³ bá»©c tranh Ä‘áº§y Ä‘á»§ vá» cĂ¡c phÆ°Æ¡ng phĂ¡p vĂ  benchmark. CĂ¢u há»i cuá»‘i cĂ¹ng: trong thá»i Ä‘áº¡i cá»§a GPT, CLIP, vĂ  Gemini â€” Foundation Models cĂ³ thay Ä‘á»•i má»i thá»© khĂ´ng?"
# Ká»CH Báº¢N V3 â€” PART XII & XIII
## Foundation Models + AI Fixing AI + Káº¿t luáº­n

---

# PART XII â€” FOUNDATION MODELS: "Há»©a háº¹n, Vá»¡ má»™ng, vĂ  TĂ¡i sinh"

---

## Scene 7.0 â€” The Promise of Scale: Accuracy on the Line
**~2 phĂºt**

### VISUAL
- Äá»“ thá»‹ scatter: trá»¥c x = ID accuracy, trá»¥c y = OOD accuracy.
  Nhiá»u model khĂ¡c nhau (cháº¥m) â€” nhá» Ä‘áº¿n lá»›n.
- ÄÆ°á»ng tháº³ng fit qua cĂ¡c cháº¥m: "Accuracy on the Line"
  Correlation cao: ID tá»‘t â†’ OOD tá»‘t.
- Text: "Náº¿u scale model â†’ ID accuracy tÄƒng â†’ OOD accuracy tÄƒng theo?"
- Animate: cháº¥m lá»›n dáº§n (model lá»›n hÆ¡n) di chuyá»ƒn lĂªn Ä‘Æ°á»ng tháº³ng.
- Evidence bars: "Verified across 36 datasets â€” ImageNet shifts, CIFAR shifts, NLP benchmarks"
- Há»™p GOLD: "Scale Law â†’ OOD cÅ©ng Ä‘Æ°á»£c? Cá»™ng Ä‘á»“ng hĂ o há»©ng."

### AUDIO
"NÄƒm 2021-2022, má»™t hiá»‡n tÆ°á»£ng thĂº vá»‹ Ä‘Æ°á»£c phĂ¡t hiá»‡n: Accuracy on the Line.

Khi váº½ scatter plot giá»¯a ID accuracy vĂ  OOD accuracy cá»§a nhiá»u model khĂ¡c nhau, chĂºng náº±m gáº§n nhÆ° trĂªn má»™t Ä‘Æ°á»ng tháº³ng. Model nĂ o tá»‘t hÆ¡n trong distribution thĂ¬ cÅ©ng tá»‘t hÆ¡n ngoĂ i distribution.

VĂ  scale law nĂ³i ráº±ng: model lá»›n hÆ¡n, train lĂ¢u hÆ¡n, data nhiá»u hÆ¡n sáº½ cĂ³ ID accuracy cao hÆ¡n. Náº¿u Ä‘Æ°á»ng tháº³ng Ä‘Ă³ Ä‘Ăºng â€” scale cÅ©ng giáº£i quyáº¿t OOD.

Evidence tá»« 36 datasets khĂ¡c nhau. Cá»™ng Ä‘á»“ng báº¯t Ä‘áº§u hĂ o há»©ng: cĂ³ pháº£i chĂºng ta chá»‰ cáº§n scale lĂ  xong?

CĂ¢u tráº£ lá»i â€” nhÆ° thÆ°á»ng lá»‡ trong machine learning â€” phá»©c táº¡p hÆ¡n nhiá»u."

---

## Scene 7.1 â€” Scale KhĂ´ng Giáº£i Quyáº¿t ÄÆ°á»£c: Báº±ng Chá»©ng Thá»±c
**~2 phĂºt**

### VISUAL
- Äá»“ thá»‹ Worst-Group Accuracy vs Model Size:
  ERM [RED]: tÄƒng nháº¹ rá»“i plateau á»Ÿ ~55%
  Group DRO [BLUE_D]: tÄƒng Ä‘Ă¡ng ká»ƒ hÆ¡n, Ä‘áº¡t ~75%
- VĂ¹ng Large Models (>10B params): cáº£ hai Ä‘Æ°á»ng Ä‘á»u plateau.
  Icon GPT/Gemini náº±m trĂªn Ä‘Æ°á»ng plateau ERM.
- Text: "Bigger â‰  More Robust (for worst-group)"
- ThĂªm biá»ƒu Ä‘á»“: Average Accuracy vs Worst-Group Accuracy cho Large Models.
  Average tÄƒng máº¡nh theo scale. Worst-Group gáº§n nhÆ° khĂ´ng tÄƒng.
- Animation: model lá»›n hÆ¡n â†’ nhiá»u shortcut tinh vi hÆ¡n xuáº¥t hiá»‡n [RED, nhiá»u nhĂ¡nh].
  "Scale amplifies capacity to memorize spurious, not to ignore them"

### AUDIO
"NhĂ¬n vĂ o Worst-Group Accuracy â€” thÆ°á»›c Ä‘o ta thá»±c sá»± quan tĂ¢m â€” bá»©c tranh ráº¥t khĂ¡c.

Khi model size tÄƒng nhÆ°ng váº«n train theo ERM, worst-group accuracy gáº§n nhÆ° khĂ´ng tÄƒng sau má»™t Ä‘iá»ƒm nháº¥t Ä‘á»‹nh. Scale giĂºp average accuracy â€” nhÆ°ng khĂ´ng giáº£i quyáº¿t spurious correlations.

Tá»‡ hÆ¡n: mĂ´ hĂ¬nh lá»›n hÆ¡n cĂ³ capacity lá»›n hÆ¡n Ä‘á»ƒ memorize spurious features tinh vi hÆ¡n. ChĂºng khĂ´ng Ä‘Æ¡n giáº£n lĂ  mĂ u ná»n â€” chĂºng lĂ  cĂ¡c pattern phá»©c táº¡p, cross-modal, khĂ³ detect hÆ¡n.

Accuracy on the Line Ä‘Ăºng cho distribution shifts Ä‘Æ¡n giáº£n â€” nhÆ° ImageNet-V2. NhÆ°ng vá»›i spurious correlation shift â€” loáº¡i shift ta thá»±c sá»± lo â€” scale khĂ´ng giĂºp Ă­ch.

NhÆ°ng Ä‘iá»u thĂº vá»‹ lĂ  vá»›i CLIP â€” model Ä‘Æ°á»£c train theo cĂ¡ch ráº¥t khĂ¡c â€” cĂ¢u chuyá»‡n cĂ³ váº» khĂ¡c."

---

## Scene 7.2 â€” CLIP vĂ  Há»©a háº¹n Zero-Shot
**~2 phĂºt**

### VISUAL
- Kiáº¿n trĂºc CLIP:
  `[áº¢nh] â†’ [Image Encoder] â”€â”`
  `[Text] â†’ [Text Encoder] â”€â”´â†’ Cosine Similarity â†’ Score`
  "Train trĂªn 400M cáº·p áº£nh-vÄƒn báº£n tá»« internet"
- Zero-shot performance: CLIP vs ERM trĂªn Waterbirds.
  CLIP zero-shot: ~75% worst-group. ERM: ~32%. [GREEN vs RED]
- Há»™p GOLD: "CLIP khĂ´ng tháº¥y Waterbirds trong train â€” váº«n robust hÆ¡n?"
- Giáº£i thĂ­ch trá»±c giĂ¡c: CLIP há»c tá»« diverse web data â†’ Ă­t bá»‹ anchor vĂ o spurious correlation Ä‘Æ¡n láº».
- NhÆ°ng... thĂªm counter-example:
  Gender bias trong CLIP: "doctor" â†’ predict nam máº¡nh hÆ¡n ná»¯.
  Histogram: score "doctor" theo gender â€” lá»‡ch sang nam rĂµ rĂ ng.

### AUDIO
"CLIP lĂ  má»™t case study thĂº vá»‹. ÄÆ°á»£c train trĂªn 400 triá»‡u cáº·p áº£nh-vÄƒn báº£n tá»« internet vá»›i contrastive learning â€” khĂ´ng pháº£i supervised classification thĂ´ng thÆ°á»ng.

Zero-shot performance cá»§a CLIP trĂªn Waterbirds Ä‘Ă¡ng kinh ngáº¡c: 75 pháº§n trÄƒm worst-group accuracy mĂ  khĂ´ng train má»™t láº§n nĂ o trĂªn dataset Ä‘Ă³. ERM chá»‰ Ä‘áº¡t 32 pháº§n trÄƒm.

Táº¡i sao? VĂ¬ web data Ä‘a dáº¡ng hÆ¡n nhiá»u. CLIP Ä‘Ă£ tháº¥y penguin á»Ÿ nhiá»u ngá»¯ cáº£nh khĂ¡c nhau â€” khĂ´ng chá»‰ trĂªn tuyáº¿t. Spurious correlation 'penguin equals tuyáº¿t' khĂ´ng Ä‘á»§ máº¡nh Ä‘á»ƒ dominate.

Nghe nhÆ° scale tháº­t sá»± cá»©u Ä‘Æ°á»£c OOD â€” Ă­t nháº¥t vá»›i CLIP?

NhÆ°ng nhĂ¬n vĂ o gender bias: tá»« 'doctor' trong vÄƒn báº£n Ä‘i kĂ¨m áº£nh ngÆ°á»i trĂªn web â€” pháº§n lá»›n lĂ  nam. CLIP há»c tÆ°Æ¡ng quan nĂ y. Vá»›i 400 triá»‡u vĂ­ dá»¥, Ä‘Ă¢y trĂ´ng nhÆ° pattern tháº­t."

---

## Scene 7.3 â€” Broken Promises: Vertical, Horizontal, No Trend
**~2 phĂºt**

### VISUAL
- 4 scatter plots nhá» cáº¡nh nhau (ID acc vs OOD acc):

**Plot 1 â€” Vertical Line [GRAY]:**
Nhiá»u model cĂ¹ng ID accuracy nhÆ°ng OOD accuracy khĂ¡c nhau nhiá»u.
"Scale ID accuracy â†’ OOD khĂ´ng Ä‘á»•i"

**Plot 2 â€” Horizontal Line [ORANGE]:**
Nhiá»u model cĂ¹ng OOD accuracy dĂ¹ ID accuracy khĂ¡c.
"OOD bĂ£o hĂ²a â€” scale khĂ´ng giĂºp"

**Plot 3 â€” No Trend [RED]:**
Scatter ngáº«u nhiĂªn, khĂ´ng cĂ³ correlation.
"Vá»›i spurious shift cá»¥ thá»ƒ: khĂ´ng cĂ³ relationship"

**Plot 4 â€” Negative Correlation [RED Ä‘áº­m]:**
Model lá»›n hÆ¡n â†’ OOD Tá»† HÆ N.
"REVERSE SCALING â€” Ä‘Ă¢y lĂ  cĂ¡i gĂ¢y sá»‘c nháº¥t"

- Text lá»›n: "Accuracy on the Line lĂ  trÆ°á»ng há»£p Ä‘áº·c biá»‡t, khĂ´ng pháº£i quy luáº­t chung"

### AUDIO
"NhĂ¬n ká»¹ hÆ¡n vĂ o Accuracy on the Line trĂªn nhiá»u loáº¡i shift khĂ¡c nhau â€” bá»©c tranh vá»¡ vá»¥n.

Vá»›i má»™t sá»‘ loáº¡i shift: scale ID accuracy trong khi OOD khĂ´ng Ä‘á»•i â€” vertical line. Model lá»›n hÆ¡n chá»‰ memorize training distribution tá»‘t hÆ¡n.

Vá»›i loáº¡i khĂ¡c: OOD accuracy bĂ£o hĂ²a á»Ÿ má»™t má»©c â€” horizontal line. Scale khĂ´ng giĂºp gĂ¬ thĂªm.

Vá»›i spurious shift cá»¥ thá»ƒ: khĂ´ng cĂ³ correlation nĂ o cáº£. ÄÆ°á»ng tháº³ng khĂ´ng tá»“n táº¡i.

VĂ  Ä‘Ă¢y lĂ  phĂ¡t hiá»‡n gĂ¢y sá»‘c nháº¥t: vá»›i má»™t sá»‘ loáº¡i spurious shift â€” Ä‘áº·c biá»‡t lĂ  ICL shortcuts trong LLMs â€” model lá»›n hÆ¡n cĂ³ OOD accuracy Tá»† HÆ N.

Accuracy on the Line lĂ  trÆ°á»ng há»£p Ä‘áº·c biá»‡t khi shift Ä‘Æ¡n giáº£n vĂ  smooth. KhĂ´ng pháº£i quy luáº­t chung."

---

## Scene 7.4 â€” In-Context Learning Shortcuts & Reverse Scaling
**~2 phĂºt**

### VISUAL
- Prompt ICL:
  ```
  "The movie was incredible!" â†’ Positive
  "Best movie of the year!"   â†’ Positive
  "I loved this movie!"       â†’ Positive

  "The food was terrible."    â†’ ???
  ```
- LLM predict: "Positive" âœ—. Highlight ORANGE: tá»« "movie" trong 3 vĂ­ dá»¥ Positive.
- Shortcut: "movie" â†’ Positive (spurious, chá»‰ do cĂ¡ch viáº¿t prompt)
- Äá»“ thá»‹ Reverse Scaling:
  x = Model Size (2.7B â†’ 7B â†’ 13B), y = % bá»‹ shortcut chi phá»‘i
  ÄÆ°á»ng Ä‘i LĂN [RED]: 30% â†’ 52% â†’ 71%
- Giáº£i thĂ­ch: "Model lá»›n hÆ¡n Ä‘á»c context tá»‘t hÆ¡n â†’ nháº¡y hÆ¡n vá»›i pattern trong prompt â†’ dá»… bá»‹ lá»«a hÆ¡n"
- Text lá»›n: "REVERSE SCALING â€” Scale lĂ m má»i thá»© Tá»† HÆ N"

### AUDIO
"Trong tháº¿ giá»›i LLMs, spurious shortcuts xuáº¥t hiá»‡n á»Ÿ nÆ¡i báº¥t ngá»: trong chĂ­nh prompt báº¡n viáº¿t.

Táº¥t cáº£ ba vĂ­ dá»¥ Positive Ä‘á»u chá»©a tá»« 'movie'. LLM há»c: 'movie' trong prompt â†’ Positive. Khi gáº·p cĂ¢u vá» food â€” khĂ´ng pháº£i movie â€” LLM váº«n bá»‹ áº£nh hÆ°á»Ÿng bá»Ÿi absence cá»§a 'movie'.

VĂ  Ä‘Ă¢y lĂ  Reverse Scaling: mĂ´ hĂ¬nh 13 tá»· tham sá»‘ bá»‹ áº£nh hÆ°á»Ÿng bá»Ÿi shortcut nĂ y nhiá»u hÆ¡n mĂ´ hĂ¬nh 2.7 tá»·.

Táº¡i sao? VĂ¬ mĂ´ hĂ¬nh lá»›n hÆ¡n ráº¥t giá»i Ä‘á»c vĂ  náº¯m báº¯t pattern trong context. ÄĂ¢y chĂ­nh lĂ  kháº£ nÄƒng táº¡o nĂªn ICL. NhÆ°ng nĂ³ cÅ©ng cĂ³ nghÄ©a mĂ´ hĂ¬nh lá»›n hÆ¡n 'quĂ¡ nháº¡y' vá»›i má»i pattern â€” ká»ƒ cáº£ pattern khĂ´ng liĂªn quan.

Scale khĂ´ng pháº£i thuá»‘c chá»¯a bĂ¡ch bá»‡nh. Trong trÆ°á»ng há»£p ICL, scale cĂ²n lĂ m bá»‡nh náº·ng hÆ¡n.

Váº­y lĂ  ta cĂ³ má»™t nghá»‹ch lĂ½ Ä‘áº¹p: scale táº¡o ra váº¥n Ä‘á» má»›i. NhÆ°ng chĂ­nh scale cÅ©ng cĂ³ thá»ƒ lĂ  chĂ¬a khĂ³a Ä‘á»ƒ giáº£i quyáº¿t â€” chá»‰ cáº§n dĂ¹ng Ä‘Ăºng cĂ¡ch."

---

# PART XIII â€” AI FIXING AI: "DĂ¹ng Scale Ä‘á»ƒ Sá»­a Scale"

---

## Scene 7.5 â€” PfR: Prompting for Robustness
**~2 phĂºt**

### VISUAL
- CĂ¢u há»i: "Group DRO cáº§n nhĂ£n nhĂ³m. Annotation tá»‘n kĂ©m. Giáº£i phĂ¡p?"
- Pipeline PfR (3 khá»‘i):
  `[áº¢nh Waterbirds] â†’ [VLM/GPT-4V + Prompt] â†’ [NhĂ£n phĂ´ng ná»n tá»± Ä‘á»™ng]`
  Prompt: "Describe the background: water or land?"
  Output: "water", "land", "water", ...
- Animate: áº£nh Ä‘i vĂ o VLM, nhĂ£n báº¯n ra nhÆ° conveyor belt.
- Káº¿t há»£p:
  `[NhĂ£n phĂ´ng ná»n tá»« VLM] + [NhĂ£n bird type thá»§ cĂ´ng] â†’ [Group DRO]`
- Káº¿t quáº£:
  ```
  ERM baseline:          32%  [RED]
  Group DRO (manual):    91%  [GREEN]
  PfR (VLM labels):      91.05% [GREEN+GOLD]
  ```
- Text: "PfR = Prompting for Robustness. AI lá»›n gĂ¡n nhĂ£n cho AI nhá»."

### AUDIO
"ÄĂ¢y lĂ  giáº£i phĂ¡p Ä‘á»™t phĂ¡: PfR â€” Prompting for Robustness.

Váº¥n Ä‘á» cá»‘t lĂµi: Group DRO cáº§n nhĂ£n nhĂ³m â€” pháº£i biáº¿t ná»n má»—i áº£nh lĂ  nÆ°á»›c hay Ä‘áº¥t. GĂ¡n nhĂ£n thá»§ cĂ´ng cho hĂ ng váº¡n áº£nh ráº¥t tá»‘n kĂ©m.

Giáº£i phĂ¡p: dĂ¹ng chĂ­nh má»™t Foundation Model lá»›n nhÆ° GPT-4V Ä‘á»ƒ gĂ¡n nhĂ£n phĂ´ng ná»n. Prompt Ä‘Æ¡n giáº£n: 'HĂ£y mĂ´ táº£ background cá»§a áº£nh nĂ y.' VLM tráº£ vá» nhĂ£n chĂ­nh xĂ¡c vá»›i chi phĂ­ gáº§n nhÆ° báº±ng khĂ´ng.

Káº¿t quáº£ trĂªn Waterbirds: PfR Ä‘áº¡t 91.05 pháº§n trÄƒm worst-group accuracy â€” gáº§n báº±ng Group DRO vá»›i oracle labels thá»§ cĂ´ng, vĂ  gáº¥p gáº§n 3 láº§n ERM baseline.

ÄĂ¢y lĂ  arc Ä‘áº¹p nháº¥t cá»§a cĂ¢u chuyá»‡n: Scale táº¡o ra spurious correlation trong CLIP. NhÆ°ng chĂ­nh Scale â€” dÆ°á»›i dáº¡ng VLM máº¡nh â€” láº¡i giĂºp ta gĂ¡n nhĂ£n Ä‘á»ƒ cháº¡y Group DRO. DĂ¹ng AI Ä‘á»ƒ sá»­a AI."

---

## Scene 7.6 â€” CATO: Counterfactual Data Generation
**~2 phĂºt**

### VISUAL
- CĂ¢u há»i: "Ngay cáº£ khi biáº¿t group, náº¿u minority quĂ¡ Ă­t Ä‘á»ƒ train hiá»‡u quáº£?"
- Pipeline CATO:
  ```
  BÆ°á»›c 1: PhĂ¢n tĂ­ch SCM â†’ xĂ¡c Ä‘á»‹nh Z (spurious)
           "Z = background (water/land)"

  BÆ°á»›c 2: LLM + Causal Reasoning â†’ sinh counterfactual
           "Waterbird trĂªn Ä‘áº¥t" (Ä‘áº£o ngÆ°á»£c ná»n)
           "Landbird trĂªn nÆ°á»›c" (Ä‘áº£o ngÆ°á»£c ná»n)

  BÆ°á»›c 3: Dataset má»›i = Original + Counterfactual
           â†’ Train model robust hÆ¡n
  ```
- Animate: tá»« 2 nhĂ³m nhá» (5% má»—i loáº¡i), CATO sinh thĂªm data.
  Pie chart cĂ¢n báº±ng: tá»« 5%/5%/45%/45% â†’ gáº§n Ä‘á»u 4 nhĂ³m.
- Text: "CATO = Causal Augmentation + LLM"
- Káº¿t quáº£: Worst-group accuracy tÄƒng thĂªm 3-5% so vá»›i PfR Ä‘Æ¡n thuáº§n.

### AUDIO
"PfR giáº£i quyáº¿t váº¥n Ä‘á» annotation. NhÆ°ng cĂ²n má»™t váº¥n Ä‘á» khĂ¡c: dĂ¹ biáº¿t group, sá»‘ lÆ°á»£ng minority samples váº«n quĂ¡ Ă­t Ä‘á»ƒ train hiá»‡u quáº£.

CATO â€” Causal Augmentation â€” giáº£i quyáº¿t Ä‘iá»u nĂ y báº±ng cĂ¡ch dĂ¹ng LLM vĂ  suy luáº­n nhĂ¢n quáº£ Ä‘á»ƒ SINH ra dá»¯ liá»‡u counterfactual.

Tá»« SCM Ä‘Ă£ xĂ¢y dá»±ng, ta biáº¿t spurious feature lĂ  phĂ´ng ná»n. CATO yĂªu cáº§u LLM: hĂ£y tÆ°á»Ÿng tÆ°á»£ng waterbird nĂ y Ä‘á»©ng trĂªn Ä‘áº¥t thay vĂ¬ nÆ°á»›c. MĂ´ táº£ láº¡i cáº£nh Ä‘Ă³.

LLM sinh ra mĂ´ táº£ â€” hoáº·c tháº­m chĂ­ áº£nh tá»•ng há»£p â€” cá»§a cĂ¡c trÆ°á»ng há»£p counterfactual. Dataset má»›i cĂ¢n báº±ng hÆ¡n nhiá»u. Model Ä‘Æ°á»£c train trĂªn dataset augmented nĂ y robust hÆ¡n Ä‘Ă¡ng ká»ƒ.

CATO lĂ  hÆ°á»›ng káº¿t há»£p giá»¯a nhĂ¢n quáº£ vĂ  generative AI â€” má»™t trong nhá»¯ng xu hÆ°á»›ng nghiĂªn cá»©u nĂ³ng nháº¥t nÄƒm 2024.

VĂ  Ä‘Ă¢y chĂ­nh lĂ  arc hoĂ n chá»‰nh: Scale há»©a háº¹n giáº£i quyáº¿t OOD â†’ Scale táº¡o ra spurious má»›i vĂ  phá»©c táº¡p hÆ¡n â†’ Scale tháº­m chĂ­ lĂ m váº¥n Ä‘á» tá»‡ hÆ¡n trong ICL â†’ NhÆ°ng ta dĂ¹ng chĂ­nh Scale Ä‘á»ƒ gĂ¡n nhĂ£n vĂ  sinh dá»¯ liá»‡u â†’ Scale sá»­a lá»—i cá»§a Scale."

---
---

# PART XIV â€” Káº¾T LUáº¬N

---

## Scene 9.1 â€” HĂ nh trĂ¬nh Tá»•ng há»£p
**~2 phĂºt**

### VISUAL
- Camera zoom lĂ¹i cháº­m. Báº£n Ä‘á»“ khĂ¡i niá»‡m toĂ n bá»™ xuáº¥t hiá»‡n:
  ```
  [Intuition]         [Formalism]        [Risk Aggregation]
       â†“                   â†“                    â†“
  [ERM Failure] â”€â”€â†’ [OOD Definition] â”€â”€â†’ [Mean/Max/CVaR/DRO]
       â†“                                         â†“
  [Causal View]                          [Why Methods Differ]
  [SCM, Invariant]                              â†“
       â†“                              [Reweighting â†’ fails]
  [Methods]                                     â†“
  [IRM â†’ NuRD â†’ DRO â†’ JTT]              [IRM â†’ NuRD â†’ DRO]
       â†“                                         â†“
  [Benchmarks]              [Foundation Models]
  [Reality Check]           [Promise â†’ Broken â†’ Fix]
       â†“                          â†“
               [PfR + CATO: AI Fixes AI]
  ```
- Má»i thá»© má» dáº§n. 3 tá»« xuáº¥t hiá»‡n láº§n lÆ°á»£t:
  CORRELATION [GRAY] â†’ CAUSATION [BLUE_D] â†’ STABILITY [GOLD, glow]
- STABILITY to nháº¥t, particle effect nháº¹ xung quanh.
- DÆ°á»›i cĂ¹ng: "ÄĂ¢y lĂ  ranh giá»›i tiáº¿p theo cá»§a TrĂ­ tuá»‡ NhĂ¢n táº¡o."

### AUDIO
"ChĂºng ta Ä‘Ă£ Ä‘i má»™t hĂ nh trĂ¬nh dĂ i.

Báº¯t Ä‘áº§u tá»« má»™t cĂ¢u há»i Ä‘Æ¡n giáº£n: táº¡i sao AI há»c sai? ERM tá»‘i Æ°u trung bĂ¬nh, vĂ  trung bĂ¬nh cho phĂ©p hy sinh thiá»ƒu sá»‘ Ä‘á»ƒ Ä‘á»•i láº¥y majority.

ChĂºng ta hĂ¬nh thá»©c hĂ³a váº¥n Ä‘á»: OOD generalization lĂ  há»c tá»‘t khi phĂ¢n phá»‘i thay Ä‘á»•i. Risk aggregation cho tháº¥y cĂ¡c thuáº­t toĂ¡n khĂ¡c nhau chá»‰ khĂ¡c nhau á»Ÿ cĂ¡ch gá»™p rá»§i ro â€” mean, max, CVaR, hay DRO.

Simplicity bias giáº£i thĂ­ch táº¡i sao gradient descent luĂ´n chá»n shortcut: Ä‘áº·c trÆ°ng Ä‘Æ¡n giáº£n cĂ³ gradient lá»›n hÆ¡n.

SCM cho tháº¥y cáº¥u trĂºc nhĂ¢n quáº£: spurious features lĂ  há»‡ quáº£ cá»§a mĂ´i trÆ°á»ng, causal features lĂ  báº¥t biáº¿n.

NÄƒm phÆ°Æ¡ng phĂ¡p â€” Reweighting, IRM, NuRD, Group DRO, JTT â€” má»—i cĂ¡i lĂ  lá»i giáº£i cho má»™t giáº£ Ä‘á»‹nh cá»¥ thá»ƒ. KhĂ´ng cĂ³ silver bullet.

Benchmark cho tháº¥y thá»±c táº¿ phá»©c táº¡p hÆ¡n lĂ½ thuyáº¿t. VĂ  Foundation Models â€” Scale tháº¥t báº¡i nhÆ°ng Scale cá»©u Ä‘Æ°á»£c báº±ng cĂ¡ch khĂ¡c.

Táº¥t cáº£ dáº«n vá» má»™t tá»«: Stability. AI á»•n Ä‘á»‹nh khĂ´ng pháº£i AI khĂ´ng bao giá» gáº·p phĂ¢n phá»‘i má»›i. MĂ  lĂ  AI biáº¿t Ä‘iá»u gĂ¬ thá»±c sá»± quan trá»ng vĂ  giá»¯ vá»¯ng Ä‘iá»u Ä‘Ă³ dĂ¹ hoĂ n cáº£nh thay Ä‘á»•i."

---

## Scene 9.2 â€” Open Problems & Credits
**~45 giĂ¢y**

### VISUAL
- 3 cĂ¡nh cá»­a chÆ°a má»Ÿ (Ă¡nh sĂ¡ng hĂ© ra tá»« khe):
  1. "LĂ½ thuyáº¿t OOD cho Foundation Models"
  2. "Model Selection khĂ´ng cáº§n OOD validation"
  3. "OOD trong Multimodal & Agentic AI"
- Fade in credits trĂªn ná»n Ä‘en:
  ```
  Based on:
  NeurIPS 2024 Tutorial
  "Out-of-Distribution Generalization: Shortcuts, Spuriousness & Stability"
  Maggie Makar Â· Aahlad Manas Puli Â· Yoav Wald

  Produced by:
  Phan Huá»³nh ChĂ¢u Thá»‹nh (Na) Â· Má»¹ Linh Â· Há»“ng Thanh Â· Trá»ng HĂ²a
  Nháº­p MĂ´n Há»c MĂ¡y Â· HCMUS
  GitHub: [link]
  ```

### AUDIO
"Tutorial Ä‘á»ƒ láº¡i ba cĂ¡nh cá»­a má»Ÿ: lĂ½ thuyáº¿t OOD cho foundation models, model selection khĂ´ng cáº§n OOD validation, vĂ  OOD trong tháº¿ giá»›i multimodal vĂ  agentic AI.

ÄĂ¢y lĂ  biĂªn giá»›i tiáº¿p theo. Cáº£m Æ¡n cĂ¡c báº¡n Ä‘Ă£ theo dĂµi. Link tutorial gá»‘c, slides, vĂ  source code Manim Ä‘á»u cĂ³ trong pháº§n mĂ´ táº£."
