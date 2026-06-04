from manim import *
from common import *


class StructuralCausalModel(OODScene):
    def construct(self):
        title = Text("Stable path vs shortcut path", font_size=36, color=WHITE, weight=BOLD).to_edge(UP, buff=0.35)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.8)

        xcore = causal_node("Core", LEFT * 3.6 + DOWN * 0.2, BLUE_D)
        y = causal_node("Y", ORIGIN + DOWN * 0.2, GOLD)
        xspur = causal_node("Spur", RIGHT * 3.6 + DOWN * 0.2, RED)
        env = causal_node("Env", RIGHT * 3.6 + UP * 2.0, ORANGE)
        core_icon = VGroup(simple_penguin(), simple_camel()).arrange(RIGHT, buff=0.2).scale(0.65).next_to(xcore, DOWN, buff=0.25)
        bg_icon = VGroup(
            Square(0.32, color=BLUE_E).set_fill(BLUE_E, 0.8),
            Square(0.32, color=YELLOW_E).set_fill(YELLOW_E, 0.8),
        ).arrange(RIGHT, buff=0.18).next_to(xspur, DOWN, buff=0.35)
        self.play(FadeIn(xcore), FadeIn(y), FadeIn(xspur), FadeIn(env), FadeIn(core_icon), FadeIn(bg_icon), run_time=1.2)
        self.wait(2.0)

        stable = Arrow(xcore.get_right(), y.get_left(), color=BLUE_D, buff=0.1, stroke_width=7)
        label_to_spur = Arrow(y.get_right(), xspur.get_left(), color=RED, buff=0.1, stroke_width=5)
        env_to_spur = Arrow(env.get_bottom(), xspur.get_top(), color=ORANGE, buff=0.1, stroke_width=5)
        self.play(GrowArrow(stable), run_time=0.8)
        self.wait(1.8)
        self.play(GrowArrow(label_to_spur), GrowArrow(env_to_spur), run_time=1.0)
        self.wait(2.5)

        learner = labeled_box("AI", 1.1, 0.75, WHITE, 30).shift(DOWN * 2.3)
        good = Arrow(xcore.get_bottom(), learner.get_left(), color=BLUE_D, buff=0.15, stroke_width=6)
        bad = Arrow(xspur.get_bottom(), learner.get_right(), color=RED, buff=0.15, stroke_width=7)
        self.play(FadeIn(learner), GrowArrow(good), GrowArrow(bad), run_time=1.2)
        self.play(bad.animate.set_opacity(0.25), good.animate.set_stroke(width=10), Circumscribe(stable, color=BLUE_D), run_time=1.2)
        self.wait(6.4)


class ShiftBreaksSpuriousLink(OODScene):
    def construct(self):
        title = Text("A shift breaks the shortcut", font_size=36, color=WHITE, weight=BOLD).to_edge(UP, buff=0.35)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.8)

        train = VGroup(
            Text("E1", font_size=30, color=GREEN_D, weight=BOLD),
            simple_penguin(),
            Square(0.44, color=BLUE_E).set_fill(BLUE_E, 0.75),
        ).arrange(RIGHT, buff=0.28).shift(LEFT * 3.2 + UP * 0.65)
        test = VGroup(
            Text("E2", font_size=30, color=ORANGE, weight=BOLD),
            simple_penguin(),
            Square(0.44, color=YELLOW_E).set_fill(YELLOW_E, 0.75),
        ).arrange(RIGHT, buff=0.28).shift(RIGHT * 3.2 + UP * 0.65)
        self.play(FadeIn(train, shift=UP * 0.2), FadeIn(test, shift=UP * 0.2), run_time=1.1)
        self.wait(2.0)

        shortcut = DashedLine(train[2].get_bottom(), test[2].get_bottom(), color=RED, stroke_width=7).add_tip()
        core = Arrow(train[1].get_bottom() + DOWN * 0.2, test[1].get_bottom() + DOWN * 0.2, color=BLUE_D, stroke_width=7)
        self.play(Create(shortcut), run_time=0.9)
        self.play(Flash(shortcut.get_center(), color=RED), shortcut.animate.set_opacity(0.2), run_time=1.0)
        self.wait(2.5)

        self.play(GrowArrow(core), run_time=0.9)
        self.play(Indicate(core, color=BLUE_D), run_time=0.8)
        stable = Text("shape survives", font_size=38, color=BLUE_D, weight=BOLD).to_edge(DOWN, buff=0.5)
        brittle = Text("background flips", font_size=34, color=RED, weight=BOLD).next_to(stable, UP, buff=0.22)
        self.play(FadeIn(brittle, shift=UP), FadeIn(stable, shift=UP), run_time=1.0)
        self.wait(6.4)
