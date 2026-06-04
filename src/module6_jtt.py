from manim import *
from common import *


class JTT(OODScene):
    def construct(self):
        self.question("Without group labels, how do we find weak groups?")
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
        self.wait(3)
        dots = VGroup(*[Dot(LEFT * 4 + DOWN * 1 + RIGHT * (i % 8) * 0.25 + UP * (i // 8) * 0.25, color=RED if i in [3, 5, 12, 17] else BLUE_D) for i in range(24)])
        bucket = RoundedRectangle(width=2.4, height=2.0, corner_radius=0.12, color=GOLD).set_fill(GOLD, 0.12).shift(DOWN * 1.2)
        self.play(FadeIn(dots), Create(bucket))
        wrong = [dots[i] for i in [3, 5, 12, 17]]
        self.play(*[d.animate.move_to(bucket.get_center() + RIGHT * (j - 1.5) * 0.35) for j, d in enumerate(wrong)], run_time=1.2)
        self.play(Flash(bucket, color=GOLD))
        copies = VGroup(*[d.copy().set_color(GOLD) for d in wrong])
        self.play(LaggedStart(*[c.animate.shift(RIGHT * 2.2 + UP * (i - 1.5) * 0.18) for i, c in enumerate(copies)], lag_ratio=0.1), run_time=1.0)
        k = Text("K copies", font_size=28, color=GOLD).next_to(bucket, RIGHT, buff=0.35)
        self.play(FadeIn(k, shift=LEFT * 0.1), Indicate(step3[0], color=GREEN_D), run_time=0.9)
        after = bar("worst group", 0.71, GREEN_D, width=3.0).scale(0.75).to_edge(DOWN, buff=0.35)
        before = bar("ERM", 0.32, RED, width=3.0).scale(0.75).next_to(after, UP, buff=0.18)
        self.play(FadeIn(before, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(after, shift=UP * 0.1), run_time=0.7)
        self.play(Circumscribe(after, color=GREEN_D), run_time=0.8)
        self.wait(2.5)


class SemanticCorruptions(OODScene):
    def construct(self):
        self.title("Semantic Corruptions", "Hide the meaning, test the shortcut")
        xray = RoundedRectangle(width=2.3, height=2.3, corner_radius=0.12, color=GRAY_B).set_fill(GRAY_D, 0.35).shift(LEFT * 3.7 + UP * 0.2)
        heart = Circle(radius=0.42, color=RED).set_fill(RED, 0.35).move_to(xray)
        cover = Square(side_length=0.95, color=GRAY_B).set_fill(GRAY_B, 0.95).move_to(heart)
        model = labeled_box("model", 1.6, 0.72, BLUE_D, 20)
        pred = labeled_box("cardiomegaly\nstill predicted", 2.8, 0.78, RED, 17).shift(RIGHT * 3.7 + UP * 0.2)
        a1 = Arrow(xray.get_right(), model.get_left(), buff=0.12, color=BLUE_D)
        a2 = Arrow(model.get_right(), pred.get_left(), buff=0.12, color=RED)
        self.play(FadeIn(VGroup(xray, heart)), run_time=0.8)
        self.play(FadeIn(cover, scale=0.8), Flash(cover, color=GRAY_B), run_time=0.8)
        self.play(GrowArrow(a1), FadeIn(model), GrowArrow(a2), FadeIn(pred), run_time=1.0)
        warning = Text("prediction survives after semantics are hidden", font_size=26, color=GOLD).to_edge(DOWN, buff=0.45)
        self.play(FadeIn(warning, shift=UP * 0.1), run_time=0.8)
        nlp = labeled_box("NGRAM-RND:\nshuffle local words", 3.2, 0.78, PURPLE, 17).next_to(warning, UP, buff=0.35)
        self.play(FadeIn(nlp, shift=UP * 0.1), Circumscribe(pred, color=RED), run_time=1.0)
        shortcut = Text("shortcut outside the heart", font_size=24, color=RED).next_to(xray, DOWN, buff=0.25)
        self.play(FadeIn(shortcut, shift=UP * 0.1), Flash(pred, color=RED), run_time=0.9)
        words = VGroup(*[Text(t, font_size=18, color=WHITE) for t in ["toxic", "identity", "word", "order"]]).arrange(RIGHT, buff=0.18).next_to(nlp, DOWN, buff=0.25)
        self.play(LaggedStart(*[FadeIn(w) for w in words], lag_ratio=0.1), run_time=0.7)
        self.play(words.animate.arrange(RIGHT, buff=0.18).shift(RIGHT * 0.45), Indicate(nlp, color=PURPLE), run_time=0.9)
        self.play(Circumscribe(warning, color=GOLD), run_time=0.8)
        variants = VGroup(
            labeled_box("mask object", 2.0, 0.55, GRAY_B, 15),
            labeled_box("shuffle patch", 2.0, 0.55, ORANGE, 15),
            labeled_box("randomize n-grams", 2.2, 0.55, PURPLE, 15),
        ).arrange(RIGHT, buff=0.25).to_edge(DOWN, buff=0.2)
        self.play(LaggedStart(*[FadeIn(v, shift=UP * 0.1) for v in variants], lag_ratio=0.12), run_time=1.0)
        for v in variants:
            self.play(Indicate(v, color=GOLD), run_time=0.45)
        verdict = Text("if prediction survives, inspect the shortcut", font_size=24, color=GOLD).next_to(variants, UP, buff=0.2)
        self.play(FadeIn(verdict, shift=UP * 0.1), run_time=0.8)
        self.play(Circumscribe(verdict, color=GOLD), run_time=0.8)
        test_loop = VGroup(
            Text("corrupt", font_size=22, color=ORANGE),
            Text("predict", font_size=22, color=BLUE_D),
            Text("compare", font_size=22, color=GREEN_D),
        ).arrange(RIGHT, buff=0.45).next_to(verdict, UP, buff=0.25)
        loop_arrows = VGroup(
            Arrow(test_loop[0].get_right(), test_loop[1].get_left(), buff=0.08, color=GRAY_B),
            Arrow(test_loop[1].get_right(), test_loop[2].get_left(), buff=0.08, color=GRAY_B),
        )
        self.play(FadeIn(test_loop[0]), run_time=0.5)
        self.play(GrowArrow(loop_arrows[0]), FadeIn(test_loop[1]), run_time=0.6)
        self.play(GrowArrow(loop_arrows[1]), FadeIn(test_loop[2]), run_time=0.6)
        self.play(Indicate(test_loop[2], color=GREEN_D), Flash(pred, color=RED), run_time=0.9)
        self.play(Circumscribe(VGroup(test_loop, loop_arrows), color=GOLD), run_time=0.9)
        self.play(Indicate(warning, color=GOLD), run_time=0.8)
        self.wait(6.1)
