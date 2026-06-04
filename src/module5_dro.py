from manim import *
from common import *


class GroupDRO(OODScene):
    def construct(self):
        self.question("If averages hide failures, optimize the worst group?")
        erm = MathTex(r"\min_\theta \sum_g p_g R_g(\theta)", font_size=44).shift(UP * 1.15)
        dro = MathTex(r"\min_\theta \max_{g\in\mathcal{G}} R_g(\theta)", font_size=44).shift(UP * 1.15)
        self.play(Write(erm))
        self.wait(0.5)
        self.play(TransformMatchingTex(erm, dro))
        vals = [0.18, 0.42, 0.66, 0.82]
        bars = VGroup(*[bar(f"Group {i+1}", v, RED if i == 0 else GREEN_D, width=3.8).scale(0.78) for i, v in enumerate(vals)]).arrange(DOWN, buff=0.22).shift(DOWN * 0.7)
        self.play(FadeIn(bars))
        self.play(Indicate(bars[0], color=RED))
        self.play(bars[0].animate.scale(1.08), run_time=0.5)
        weights = VGroup(*[DecimalNumber(v, num_decimal_places=2, color=RED if i == 0 else GRAY_B, font_size=22).next_to(bars[i], RIGHT, buff=0.2) for i, v in enumerate([0.52, 0.18, 0.16, 0.14])])
        self.play(LaggedStart(*[FadeIn(w, shift=LEFT * 0.1) for w in weights], lag_ratio=0.1), run_time=0.8)
        note = Text("upweight the current worst group", font_size=28, color=GOLD).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(note))
        self.play(Circumscribe(bars[0], color=RED), run_time=0.8)
        for i, new_value in enumerate([0.28, 0.46, 0.63]):
            new_bar = bar("Group 1", new_value, ORANGE if i < 2 else GREEN_D, width=3.8).scale(0.78).move_to(bars[0])
            self.play(Transform(bars[0], new_bar), run_time=0.65)
        self.play(Indicate(note, color=GOLD), run_time=0.8)
        self.wait(2.6)
