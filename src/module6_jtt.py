from manim import *
from common import *


class JTT(OODScene):
    def construct(self):
        q = self.question("Without group labels, how do we find weak groups?")
        def step_node(num: str, label: str, col: str):
            circ = Circle(radius=0.34, color=col).set_fill(col, 0.22)
            n_txt = Text(num, font_size=22, color=WHITE, weight=BOLD).move_to(circ)
            l_txt = Text(label, font_size=17, color=col).next_to(circ, DOWN, buff=0.15)
            return VGroup(circ, n_txt, l_txt)

        step1 = step_node("1", "Train ERM", GRAY_B).shift(LEFT * 4.1 + UP * 1.3)
        step2 = step_node("2", "Find Errors", GOLD).shift(ORIGIN + UP * 1.3)
        step3 = step_node("3", "Upweight & Retrain", GREEN_D).shift(RIGHT * 4.1 + UP * 1.3)
        arrows = VGroup(
            Arrow(step1[0].get_right(), step2[0].get_left(), buff=0.12, color=GRAY_B),
            Arrow(step2[0].get_right(), step3[0].get_left(), buff=0.12, color=GOLD)
        )
        self.play(FadeIn(step1), FadeIn(step2), FadeIn(step3), LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.2))
        self.wait(2.5)
        
        dots = VGroup(*[Dot(LEFT * 4 + DOWN * 1 + RIGHT * (i % 8) * 0.25 + UP * (i // 8) * 0.25, color=RED if i in [3, 5, 12, 17] else BLUE_D) for i in range(24)])
        bucket = RoundedRectangle(width=2.4, height=2.0, corner_radius=0.12, color=GOLD).set_fill(GOLD, 0.12).shift(DOWN * 1.2)
        self.play(FadeIn(dots), Create(bucket))
        self.wait(1.5)
        
        wrong = [dots[i] for i in [3, 5, 12, 17]]
        self.play(*[d.animate.move_to(bucket.get_center() + RIGHT * (j - 1.5) * 0.35) for j, d in enumerate(wrong)], run_time=0.6)
        self.play(Flash(bucket, color=GOLD))
        copies = VGroup(*[d.copy().set_color(GOLD) for d in wrong])
        copies_target = VGroup(*[Dot(color=GOLD) for _ in wrong]).arrange(UP, buff=0.15).shift(bucket.get_center() + RIGHT * 2.6)
        self.play(Transform(copies, copies_target), run_time=0.5)
        k = Text("K copies", font_size=28, color=GOLD).next_to(copies, RIGHT, buff=0.35)
        self.play(FadeIn(k, shift=LEFT * 0.1), Indicate(step3[0], color=GREEN_D), run_time=0.5)
        self.wait(2.0)
        
        after = bar("worst group", 0.71, GREEN_D, width=3.0).scale(0.75).to_edge(DOWN, buff=0.35)
        before = bar("ERM", 0.32, RED, width=3.0).scale(0.75).next_to(after, UP, buff=0.18)
        self.play(FadeIn(before, shift=UP * 0.1), run_time=0.3)
        self.play(FadeIn(after, shift=UP * 0.1), run_time=0.35)
        self.play(Circumscribe(after, color=GREEN_D), run_time=0.4)
        self.wait(2.0)
        
        # Fade out step diagram to transition to dataset walkthrough
        self.wait(2.0)
        self.play(
            FadeOut(VGroup(step1, step2, step3, arrows, dots, bucket, copies, k, before, after, q)),
            run_time=0.5
        )
        self.wait(0.5)
        
        # Concrete dataset visualization
        db_title = Text("Stage 1: Identify ERM Weaknesses", font_size=24, color=WHITE).shift(UP * 2.4)
        self.play(FadeIn(db_title), run_time=0.4)
        
        # Draw 4 sample cards representing majority and minority
        def sample_card(animal, background, group_type, correct=True):
            card_obj = RoundedRectangle(width=2.2, height=1.7, corner_radius=0.1, color=GRAY_B, stroke_width=2).set_fill(GRAY_D, 0.2)
            bg_rect = Rectangle(width=2.0, height=1.5, color=BLUE_E if background == "snow" else YELLOW_E, stroke_width=0).set_fill(BLUE_E if background == "snow" else YELLOW_E, 0.35).move_to(card_obj)
            anim = simple_penguin() if animal == "penguin" else simple_camel()
            anim.scale(0.65).move_to(card_obj)
            
            lbl = Text(group_type, font_size=14, color=GRAY_B).next_to(card_obj, UP, buff=0.06)
            marker = Text("✓" if correct else "✗", font_size=26, color=GREEN_D if correct else RED, weight=BOLD).next_to(card_obj, DOWN, buff=0.08)
            
            return VGroup(card_obj, bg_rect, anim, lbl, marker)
        
        # Positions for 4 cards
        cards = VGroup(
            sample_card("penguin", "snow", "Majority (95%)", correct=True).shift(LEFT * 4.2 + UP * 0.1),
            sample_card("camel", "sand", "Majority (95%)", correct=True).shift(LEFT * 1.4 + UP * 0.1),
            sample_card("penguin", "sand", "Minority (5%)", correct=False).shift(RIGHT * 1.4 + UP * 0.1),
            sample_card("camel", "snow", "Minority (5%)", correct=False).shift(RIGHT * 4.2 + UP * 0.1),
        )
        
        self.play(LaggedStart(*[FadeIn(c, scale=0.85) for c in cards], lag_ratio=0.12), run_time=0.5)
        self.wait(2.0)
        
        # Highlight why the minority is wrong
        explanation = Text("Minority cards are misclassified because the shortcut points in the wrong direction!", font_size=20, color=GOLD).shift(DOWN * 1.8)
        self.play(FadeIn(explanation, shift=UP * 0.1), run_time=0.3)
        self.play(Circumscribe(cards[2], color=RED), Circumscribe(cards[3], color=RED), run_time=0.4)
        self.wait(2.0)
        
        # Show that these mistakes are a natural proxy for the minority group
        proxy_title = Text("Mistakes = Natural Proxy for Minority Groups", font_size=22, color=GOLD).move_to(db_title.get_center())
        self.play(
            FadeOut(explanation),
            Transform(db_title, proxy_title),
            cards[0].animate.set_opacity(0.25),
            cards[1].animate.set_opacity(0.25),
            cards[2].animate.scale(1.15).shift(LEFT * 0.8),
            cards[3].animate.scale(1.15).shift(RIGHT * 0.8),
            run_time=0.5
        )
        self.wait(1.5)
        
        # Stage 2: Upweighting
        s2_title = Text("Stage 2: Upweight Mistakes (K = 20)", font_size=24, color=WHITE).move_to(db_title.get_center())
        self.play(
            Transform(db_title, s2_title),
            FadeOut(cards[0]), FadeOut(cards[1]),
            run_time=0.5
        )
        self.wait(0.2)
        
        # Draw the copies multiplication visual
        copies_grid_left = VGroup(*[cards[2][0:3].copy().move_to(ORIGIN).scale(0.35) for _ in range(9)]).arrange_in_grid(3, 3, buff=0.08).shift(LEFT * 2.5 + DOWN * 0.3)
        copies_grid_right = VGroup(*[cards[3][0:3].copy().move_to(ORIGIN).scale(0.35) for _ in range(9)]).arrange_in_grid(3, 3, buff=0.08).shift(RIGHT * 2.5 + DOWN * 0.3)
        
        self.play(
            ReplacementTransform(cards[2][0:3], copies_grid_left),
            ReplacementTransform(cards[3][0:3], copies_grid_right),
            FadeOut(cards[2][3:]), FadeOut(cards[3][3:]),
            run_time=0.7
        )
        self.play(Flash(copies_grid_left, color=GOLD), Flash(copies_grid_right, color=GOLD), run_time=0.3)
        self.wait(2.5)
        
        # Retrain on balanced data
        retrain_lbl = Text("Retraining forces the model to ignore the shortcut", font_size=20, color=GREEN_D).shift(DOWN * 2.1)
        self.play(FadeIn(retrain_lbl, shift=UP * 0.1), run_time=0.3)
        self.wait(2.5)
        
        # Show results
        self.play(FadeOut(VGroup(db_title, copies_grid_left, copies_grid_right, retrain_lbl)), run_time=0.5)
        
        result_title = Text("JTT Performance on Waterbirds", font_size=26, color=WHITE).shift(UP * 1.5)
        self.play(FadeIn(result_title), run_time=0.4)
        
        after = bar("JTT Worst-Group", 0.71, GREEN_D, width=3.5).scale(0.85).shift(DOWN * 0.4)
        before = bar("ERM Worst-Group", 0.32, RED, width=3.5).scale(0.85).next_to(after, UP, buff=0.25)
        
        self.play(FadeIn(before, shift=UP * 0.1), run_time=0.5)
        self.play(Indicate(before, color=RED), run_time=0.3)
        self.wait(2.0)
        self.play(FadeIn(after, shift=UP * 0.1), run_time=0.3)
        self.play(Circumscribe(after, color=GREEN_D), run_time=0.3)
        self.wait(1.5)
        
        # Concluding tag
        final_tag = Text("Robustness achieved without manual group labels!", font_size=22, color=GOLD, weight=BOLD).to_edge(DOWN, buff=0.3)
        self.play(FadeIn(final_tag, shift=UP * 0.1), run_time=0.3)
        self.play(Circumscribe(final_tag, color=GOLD), run_time=0.3)
        # Motion fillers: cycle through result bars and final tag
        for _ in range(2):
            self.play(Indicate(after, color=GREEN_D, scale_factor=1.06), run_time=0.5)
            self.play(Indicate(before, color=RED, scale_factor=1.06), run_time=0.5)
            self.play(Indicate(final_tag, color=GOLD), run_time=0.4)
        self.active_wait(VGroup(after, before, final_tag), 1.0, GOLD)
        self.wait(1.0)


class SemanticCorruptions(OODScene):
    def construct(self):
        main_title = self.title("Semantic Corruptions", "Hide the meaning, test the shortcut")
        
        # --- STEP 1: CV Intuition (X-ray) ---
        xray = RoundedRectangle(width=2.3, height=2.3, corner_radius=0.12, color=GRAY_B).set_fill(GRAY_D, 0.35).shift(LEFT * 3.7 + UP * 0.2)
        heart = Circle(radius=0.42, color=RED).set_fill(RED, 0.35).move_to(xray)
        cover = Square(side_length=0.95, color=GRAY_B).set_fill(GRAY_B, 0.95).move_to(heart)
        model = labeled_box("model", 1.6, 0.72, BLUE_D, 20)
        pred = labeled_box("cardiomegaly\nstill predicted", 2.8, 0.78, RED, 17).shift(RIGHT * 3.7 + UP * 0.2)
        a1 = Arrow(xray.get_right(), model.get_left(), buff=0.12, color=BLUE_D)
        a2 = Arrow(model.get_right(), pred.get_left(), buff=0.12, color=RED)
        
        self.play(FadeIn(VGroup(xray, heart)), run_time=0.4)
        self.play(FadeIn(cover, scale=0.8), Flash(cover, color=GRAY_B), run_time=0.4)
        self.play(GrowArrow(a1), FadeIn(model), GrowArrow(a2), FadeIn(pred), run_time=0.5)
        
        warning = Text("prediction survives after semantics are hidden", font_size=24, color=GOLD).to_edge(DOWN, buff=0.5)
        shortcut = Text("shortcut outside the heart", font_size=22, color=RED).next_to(xray, DOWN, buff=0.25)
        
        self.play(FadeIn(warning, shift=UP * 0.1), FadeIn(shortcut, shift=UP * 0.1), Circumscribe(pred, color=RED), run_time=0.6)
        self.wait(1.5)
        
        # Fade out step 1
        self.play(FadeOut(VGroup(xray, heart, cover, model, pred, a1, a2, warning, shortcut)), run_time=0.4)
        
        # --- STEP 2: NLP Intuition (Word Shuffling) ---
        nlp_title = Text("NLP Word Shuffling", font_size=28, color=WHITE).shift(UP * 2.2)
        orig_text = Text('"I loved this movie, it was fantastic!"', font_size=22, color=BLUE_D).shift(UP * 0.8)
        orig_lbl = Text("Original Sentence -> Predicts POSITIVE", font_size=16, color=GRAY_B).next_to(orig_text, DOWN, buff=0.15)
        
        self.play(FadeIn(nlp_title, shift=DOWN * 0.1), FadeIn(orig_text), FadeIn(orig_lbl), run_time=0.5)
        self.wait(1.0)
        
        shuf_text = Text('"movie was fantastic I this loved!"', font_size=22, color=RED).shift(DOWN * 0.4)
        shuf_lbl = Text("Shuffled Sentence -> Predicts POSITIVE (same prediction!)", font_size=16, color=GRAY_B).next_to(shuf_text, DOWN, buff=0.15)
        
        self.play(FadeIn(shuf_text), FadeIn(shuf_lbl), run_time=0.5)
        self.play(Flash(shuf_text, color=RED), run_time=0.4)
        
        explain_nlp = Text("Model merely counts keywords (ignores syntax/order)", font_size=20, color=GOLD).shift(DOWN * 2.0)
        self.play(FadeIn(explain_nlp, shift=UP * 0.1), run_time=0.4)
        self.wait(1.8)
        
        # Fade out step 2
        self.play(FadeOut(VGroup(nlp_title, orig_text, orig_lbl, shuf_text, shuf_lbl, explain_nlp)), run_time=0.4)
        
        # --- STEP 3: Testing Loop & Variants ---
        loop_title = Text("Semantic Corruption Pipeline", font_size=28, color=WHITE).shift(UP * 2.2)
        variants = VGroup(
            labeled_box("mask object", 2.0, 0.65, GRAY_B, 15),
            labeled_box("shuffle patch", 2.0, 0.65, ORANGE, 15),
            labeled_box("randomize n-grams", 2.2, 0.65, PURPLE, 15),
        ).arrange(RIGHT, buff=0.35).shift(UP * 0.5)
        
        self.play(FadeIn(loop_title, shift=DOWN * 0.1), LaggedStart(*[FadeIn(v, scale=0.85) for v in variants], lag_ratio=0.15), run_time=0.6)
        
        verdict = Text("if prediction survives, inspect the shortcut", font_size=22, color=GOLD).shift(DOWN * 0.6)
        test_loop = VGroup(
            Text("corrupt", font_size=20, color=ORANGE),
            Text("predict", font_size=20, color=BLUE_D),
            Text("compare", font_size=20, color=GREEN_D),
        ).arrange(RIGHT, buff=0.55).next_to(verdict, DOWN, buff=0.3)
        loop_arrows = VGroup(
            Arrow(test_loop[0].get_right(), test_loop[1].get_left(), buff=0.08, color=GRAY_B),
            Arrow(test_loop[1].get_right(), test_loop[2].get_left(), buff=0.08, color=GRAY_B),
        )
        
        self.play(FadeIn(verdict, shift=UP * 0.1), run_time=0.4)
        self.play(
            FadeIn(test_loop[0]),
            GrowArrow(loop_arrows[0]), FadeIn(test_loop[1]),
            GrowArrow(loop_arrows[1]), FadeIn(test_loop[2]),
            run_time=0.8
        )
        self.play(Circumscribe(VGroup(test_loop, loop_arrows), color=GOLD), run_time=0.5)
        self.wait(1.5)
        
        # Fade out step 3
        self.play(FadeOut(VGroup(loop_title, variants, verdict, test_loop, loop_arrows)), run_time=0.4)
        
        # --- FINAL SCENE: Side-by-side CV/NLP Summary (No black gaps!) ---
        self.play(FadeOut(main_title), run_time=0.3)
        sum_title = Text("Semantic corruption exposes brittle spurious shortcuts", font_size=28, color=WHITE).shift(UP * 2.8)
        self.play(FadeIn(sum_title, shift=DOWN * 0.1), run_time=0.5)
        
        # Left card (NLP Shuffling Summary)
        nlp_card = RoundedRectangle(width=5.5, height=3.5, corner_radius=0.12, color=BLUE_D, stroke_width=2).set_fill(GRAY_D, 0.2).shift(LEFT * 3.3 + DOWN * 0.2)
        nlp_card_lbl = Text("NLP Word Shuffling", font_size=18, color=BLUE_D).next_to(nlp_card, UP, buff=0.15)
        nlp_card_text = Text('"movie was fantastic I this loved!"\n\n-> Predicts POSITIVE\n(Keyword counting shortcut)', font_size=14, color=WHITE).move_to(nlp_card)
        left_group = VGroup(nlp_card, nlp_card_lbl, nlp_card_text)
        
        # Right card (CV Masking Summary)
        cv_card = RoundedRectangle(width=5.5, height=3.5, corner_radius=0.12, color=GREEN_D, stroke_width=2).set_fill(GRAY_D, 0.2).shift(RIGHT * 3.3 + DOWN * 0.2)
        cv_card_lbl = Text("CV Patch Masking", font_size=18, color=GREEN_D).next_to(cv_card, UP, buff=0.15)
        
        # Small xray inside CV card
        sum_xray = RoundedRectangle(width=1.6, height=1.6, corner_radius=0.08, color=GRAY_B, stroke_width=1).set_fill(GRAY_D, 0.35).move_to(cv_card.get_center() + LEFT * 1.3)
        sum_heart = Circle(radius=0.3, color=RED).set_fill(RED, 0.35).move_to(sum_xray)
        sum_mask = Square(side_length=0.6, color=GRAY_B).set_fill(GRAY_B, 1.0).move_to(sum_heart)
        sum_tag = Text("HOSPITAL-A-SCAN-01", font_size=7, color=GOLD).move_to(sum_xray.get_top() + DOWN * 0.12)
        
        cv_card_text = Text("Cardiomegaly\nstill predicted!\n\n(Relies on scanner\nsignature shortcut)", font_size=14, color=WHITE).move_to(cv_card.get_center() + RIGHT * 1.4)
        right_group = VGroup(cv_card, cv_card_lbl, sum_xray, sum_heart, sum_mask, sum_tag, cv_card_text)
        
        self.play(
            FadeIn(left_group, scale=0.9),
            FadeIn(right_group, scale=0.9),
            run_time=0.8
        )
        
        final_verdict = Text("Semantic corruption exposes brittle spurious shortcuts.", font_size=22, color=GOLD, weight=BOLD).to_edge(DOWN, buff=0.3)
        self.play(FadeIn(final_verdict, shift=UP * 0.1), run_time=0.5)
        self.play(Circumscribe(final_verdict, color=GOLD), run_time=0.5)
        # Motion fillers: alternate between NLP card and CV card highlights
        for _ in range(3):
            self.play(Indicate(left_group[0], color=BLUE_D, scale_factor=1.04), run_time=0.5)
            self.play(Indicate(right_group[0], color=GREEN_D, scale_factor=1.04), run_time=0.5)
            self.play(Indicate(final_verdict, color=GOLD), run_time=0.4)
        self.active_wait(VGroup(left_group, right_group, final_verdict), 1.0, GOLD)
        self.wait(8.73)
