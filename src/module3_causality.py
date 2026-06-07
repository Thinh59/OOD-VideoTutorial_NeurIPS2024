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
        # Motion fillers: alternate between stable path and bad path fades
        for _ in range(4):
            self.play(Indicate(stable, color=BLUE_D, scale_factor=1.08), run_time=0.5)
            self.play(Indicate(good, color=BLUE_D), run_time=0.4)
            self.play(Circumscribe(xcore, color=BLUE_D), run_time=0.4)
            self.play(Flash(y.get_center(), color=GOLD, line_length=0.2, num_lines=8), run_time=0.35)
        self.wait(7.41)


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
        # Motion fillers: alternate between core feature and broken shortcut
        for _ in range(4):
            self.play(Indicate(stable, color=BLUE_D, scale_factor=1.07), run_time=0.5)
            self.play(Indicate(brittle, color=RED, scale_factor=1.07), run_time=0.5)
            self.play(Indicate(core, color=BLUE_D), run_time=0.4)
            self.play(Flash(shortcut.get_center(), color=RED, line_length=0.15, num_lines=6), run_time=0.35)
        self.wait(8.14)


class CausalVsSpuriousTest(OODScene):
    def construct(self):
        title = Text("The Ultimate Test: Generalization", font_size=36, color=WHITE, weight=BOLD).to_edge(UP, buff=0.35)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.8)
        
        # Split screen: Causal vs Spurious
        line = Line(UP * 2.5, DOWN * 2.5, color=GRAY_B)
        self.play(Create(line), run_time=0.8)
        
        causal_title = Text("Causal Model", font_size=28, color=BLUE_D).shift(LEFT * 3.5 + UP * 2.0)
        spur_title = Text("Spurious Model", font_size=28, color=RED).shift(RIGHT * 3.5 + UP * 2.0)
        self.play(FadeIn(causal_title), FadeIn(spur_title), run_time=0.8)
        
        # Train env
        train_lbl = Text("Train: E1", font_size=20, color=GREEN_D).shift(LEFT * 6.0 + UP * 0.5)
        self.play(FadeIn(train_lbl), run_time=0.5)
        
        causal_train = VGroup(simple_penguin(), Text("✓", color=GREEN_D)).arrange(RIGHT).shift(LEFT * 3.5 + UP * 0.5)
        spur_train = VGroup(Square(0.5, color=BLUE_E).set_fill(BLUE_E, 0.8), Text("✓", color=GREEN_D)).arrange(RIGHT).shift(RIGHT * 3.5 + UP * 0.5)
        
        self.play(FadeIn(causal_train), FadeIn(spur_train), run_time=0.8)
        self.wait(1.0)
        
        # Deploy env
        deploy_lbl = Text("Deploy: E2", font_size=20, color=ORANGE).shift(LEFT * 6.0 + DOWN * 1.5)
        self.play(FadeIn(deploy_lbl), run_time=0.5)
        
        causal_deploy = VGroup(simple_penguin(), Text("✓", color=GREEN_D)).arrange(RIGHT).shift(LEFT * 3.5 + DOWN * 1.5)
        spur_deploy = VGroup(Square(0.5, color=YELLOW_E).set_fill(YELLOW_E, 0.8), Text("✗", color=RED)).arrange(RIGHT).shift(RIGHT * 3.5 + DOWN * 1.5)
        
        self.play(FadeIn(causal_deploy), FadeIn(spur_deploy), run_time=0.8)
        self.play(Flash(spur_deploy[1], color=RED), run_time=0.5)
        
        conclusion = Text("Only causal models survive shifts!", font_size=24, color=GOLD, weight=BOLD).to_edge(DOWN, buff=0.3)
        self.play(FadeIn(conclusion, shift=UP * 0.1), run_time=0.8)
        
        for _ in range(3):
            self.play(Indicate(causal_deploy[1], color=GREEN_D), run_time=0.6)
            self.play(Indicate(spur_deploy[1], color=RED), run_time=0.6)
            self.play(Circumscribe(conclusion, color=GOLD), run_time=0.8)
        
        self.active_wait(VGroup(causal_deploy, spur_deploy, conclusion), 1.0, GOLD)
