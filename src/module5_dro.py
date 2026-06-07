from manim import *
from common import *


class GroupDRO(OODScene):
    def construct(self):
        self.question("If averages hide failures, optimize the worst group?")
        self.wait(3.0)
        
        erm = MathTex(r"\min_\theta \sum_g p_g R_g(\theta)", font_size=44).shift(UP * 1.15)
        dro = MathTex(r"\min_h\ \max_{g\in\mathcal{G}} R_g(h)", font_size=48).shift(UP * 1.15)
        self.play(Write(erm))
        self.wait(2.0)
        
        self.play(TransformMatchingTex(erm, dro))
        self.wait(2.0)
        
        inner = Text("inner max: find worst group", font_size=24, color=RED).next_to(dro, DOWN, buff=0.22)
        outer = Text("outer min: update h for that group", font_size=24, color=GREEN_D).next_to(inner, DOWN, buff=0.14)
        self.play(FadeIn(inner, shift=UP * 0.08), run_time=0.6)
        self.play(FadeIn(outer, shift=UP * 0.08), run_time=0.6)
        self.wait(3.0)
        
        vals = [0.18, 0.42, 0.66, 0.82]
        bars = VGroup(*[bar(f"Group {i+1}", v, RED if i == 0 else GREEN_D, width=3.8).scale(0.78) for i, v in enumerate(vals)]).arrange(DOWN, buff=0.22).shift(DOWN * 0.7)
        self.play(FadeOut(VGroup(inner, outer), shift=UP * 0.05), FadeIn(bars))
        self.play(Indicate(bars[0], color=RED))
        self.play(bars[0].animate.scale(1.08), run_time=0.5)
        self.wait(2.5)
        
        weights = VGroup(*[DecimalNumber(v, num_decimal_places=2, color=RED if i == 0 else GRAY_B, font_size=22).next_to(bars[i], RIGHT, buff=0.2) for i, v in enumerate([0.52, 0.18, 0.16, 0.14])])
        self.play(LaggedStart(*[FadeIn(w, shift=LEFT * 0.1) for w in weights], lag_ratio=0.1), run_time=0.8)
        
        note = Text("upweight the current worst group", font_size=28, color=GOLD).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(note))
        self.play(Circumscribe(bars[0], color=RED), run_time=0.8)
        self.wait(2.5)
        
        for i, new_value in enumerate([0.28, 0.46, 0.63]):
            new_bar = bar("Group 1", new_value, ORANGE if i < 2 else GREEN_D, width=3.8).scale(0.78).move_to(bars[0])
            self.play(Transform(bars[0], new_bar), run_time=0.65)
        self.play(Indicate(note, color=GOLD), run_time=0.8)
        self.wait(2.5)

        loop_nodes = VGroup(
            labeled_box("compute\nR_g(h)", 1.75, 0.72, BLUE_D, 16),
            labeled_box("select\nmax group", 1.75, 0.72, RED, 16),
            labeled_box("update\nmodel h", 1.75, 0.72, GREEN_D, 16),
        ).arrange(RIGHT, buff=0.55).to_edge(DOWN, buff=0.35)
        loop_arrows = VGroup(
            Arrow(loop_nodes[0].get_right(), loop_nodes[1].get_left(), color=GRAY_B, buff=0.08),
            Arrow(loop_nodes[1].get_right(), loop_nodes[2].get_left(), color=GRAY_B, buff=0.08),
            CurvedArrow(loop_nodes[2].get_top(), loop_nodes[0].get_top(), angle=-TAU / 4, color=GOLD),
        )
        self.play(FadeOut(note), FadeIn(loop_nodes[0], shift=UP * 0.1), run_time=0.6)
        self.play(GrowArrow(loop_arrows[0]), FadeIn(loop_nodes[1], shift=UP * 0.1), run_time=0.7)
        self.play(GrowArrow(loop_arrows[1]), FadeIn(loop_nodes[2], shift=UP * 0.1), run_time=0.7)
        self.play(Create(loop_arrows[2]), run_time=0.8)
        for idx in [0, 1, 2, 1]:
            self.play(Indicate(loop_nodes[idx], color=loop_nodes[idx][0].get_color()), run_time=0.42)
        self.wait(3.5)

        oracle = labeled_box("requires oracle\ngroup labels", 2.75, 0.72, ORANGE, 17).to_corner(UL, buff=0.45).shift(DOWN * 0.45)
        tags = VGroup(*[Text(f"g{i+1}", font_size=20, color=ORANGE).next_to(bars[i], LEFT, buff=0.18) for i in range(4)])
        self.play(FadeIn(oracle, shift=RIGHT * 0.12), LaggedStart(*[FadeIn(t, shift=RIGHT * 0.08) for t in tags], lag_ratio=0.08), run_time=1.0)
        self.play(Circumscribe(VGroup(tags, oracle), color=ORANGE), run_time=0.9)
        self.wait(1.3)

        limitation = Text("limitation: if groups are unknown, max cannot target them", font_size=25, color=RED).to_edge(DOWN, buff=0.28)
        crossed = VGroup(
            Line(oracle.get_corner(UL), oracle.get_corner(DR), color=RED, stroke_width=5),
            Line(oracle.get_corner(DL), oracle.get_corner(UR), color=RED, stroke_width=5),
        )
        self.play(FadeOut(loop_nodes), FadeOut(loop_arrows), FadeIn(limitation, shift=UP * 0.1), Create(crossed), run_time=1.0)
        self.play(Indicate(dro, color=GOLD), Flash(limitation, color=RED), run_time=0.9)
        
        self.active_wait(VGroup(dro, bars, limitation), 1.0, RED)
