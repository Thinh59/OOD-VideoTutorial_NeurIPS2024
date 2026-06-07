from manim import *
from common import *


class JourneySummaryRemastered(OODScene):
    def construct(self):
        title = Text("The Journey Remastered", font_size=36, color=WHITE, weight=BOLD).to_edge(UP, buff=0.35)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.8)
        
        # Flowchart
        boxes = VGroup(
            labeled_box("1. Shortcut\nLearning", 2.2, 0.8, ORANGE, 18),
            labeled_box("2. ERM\nFailures", 2.2, 0.8, RED, 18),
            labeled_box("3. Invariance\n(DRO/IRM)", 2.4, 0.8, GREEN_D, 18),
            labeled_box("4. Foundation\nModels", 2.4, 0.8, PURPLE, 18),
        ).arrange(RIGHT, buff=0.6).shift(UP * 0.5)
        
        arrows = VGroup(*[
            Arrow(boxes[i].get_right(), boxes[i+1].get_left(), color=GRAY_B)
            for i in range(3)
        ])
        
        self.play(FadeIn(boxes[0], shift=RIGHT * 0.2), run_time=0.6)
        self.play(GrowArrow(arrows[0]), FadeIn(boxes[1], shift=RIGHT * 0.2), run_time=0.6)
        self.play(GrowArrow(arrows[1]), FadeIn(boxes[2], shift=RIGHT * 0.2), run_time=0.6)
        self.play(GrowArrow(arrows[2]), FadeIn(boxes[3], shift=RIGHT * 0.2), run_time=0.6)
        self.wait(1.0)
        
        # Shortcuts STILL
        still_lbl = Text("Shortcuts STILL exist!", font_size=28, color=RED, weight=BOLD).next_to(boxes[3], DOWN, buff=0.5)
        self.play(FadeIn(still_lbl, shift=UP * 0.2), Flash(boxes[3], color=RED), run_time=0.8)
        
        # Text
        quote = Text("AI inherently seeks the easiest path.\nOur job is to redefine what's easy.", font_size=24, color=GOLD, line_spacing=1.5).shift(DOWN * 2.0)
        self.play(Write(quote), run_time=1.5)
        
        for _ in range(3):
            self.play(Indicate(boxes[3], color=PURPLE), run_time=0.5)
            self.play(Indicate(still_lbl, color=RED), run_time=0.5)
            self.play(Circumscribe(quote, color=GOLD), run_time=0.6)
        self.active_wait(VGroup(boxes, arrows, still_lbl, quote), 1.0, GOLD)


class BigTriangleConclusion(OODScene):
    def construct(self):
        title = Text("The Robustness Triangle", font_size=36, color=WHITE, weight=BOLD).to_edge(UP, buff=0.35)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.8)
        
        # Triangle vertices
        top = ORIGIN + UP * 1.5
        left = ORIGIN + LEFT * 3.0 + DOWN * 1.5
        right = ORIGIN + RIGHT * 3.0 + DOWN * 1.5
        
        # Nodes
        erm = VGroup(
            Circle(radius=0.6, color=BLUE_D).set_fill(BLUE_D, 0.2),
            Text("ERM", font_size=24, color=BLUE_D, weight=BOLD)
        ).move_to(top)
        
        dro = VGroup(
            Circle(radius=0.6, color=RED).set_fill(RED, 0.2),
            Text("DRO", font_size=24, color=RED, weight=BOLD)
        ).move_to(left)
        
        inv = VGroup(
            Circle(radius=0.6, color=GREEN_D).set_fill(GREEN_D, 0.2),
            Text("Invariance", font_size=20, color=GREEN_D, weight=BOLD)
        ).move_to(right)
        
        # Edges
        e1 = Line(erm.get_bottom(), dro.get_top(), color=GRAY_B)
        e2 = Line(erm.get_bottom(), inv.get_top(), color=GRAY_B)
        e3 = Line(dro.get_right(), inv.get_left(), color=GRAY_B)
        
        self.play(Create(e1), Create(e2), Create(e3), run_time=1.0)
        self.play(FadeIn(erm), FadeIn(dro), FadeIn(inv), run_time=1.0)
        
        # Formulas
        f_erm = MathTex(r"\min \mathbb{E}[L]", font_size=24, color=BLUE_D).next_to(erm, UP)
        f_dro = MathTex(r"\min \max \mathbb{E}[L]", font_size=24, color=RED).next_to(dro, DOWN)
        f_inv = MathTex(r"\min \mathbb{E}[L] + \lambda \text{Pen}", font_size=24, color=GREEN_D).next_to(inv, DOWN)
        
        self.play(FadeIn(f_erm), FadeIn(f_dro), FadeIn(f_inv), run_time=1.0)
        self.wait(1.0)
        
        center_text = Text("STABILITY", font_size=36, color=GOLD, weight=BOLD).move_to(ORIGIN + DOWN * 0.2)
        self.play(FadeIn(center_text, scale=0.5), run_time=0.8)
        self.play(Flash(center_text, color=GOLD, num_lines=12), run_time=0.6)
        
        for _ in range(3):
            self.play(Indicate(erm, color=BLUE_D), run_time=0.4)
            self.play(Indicate(dro, color=RED), run_time=0.4)
            self.play(Indicate(inv, color=GREEN_D), run_time=0.4)
            self.play(Indicate(center_text, color=GOLD, scale_factor=1.2), run_time=0.6)
        self.active_wait(VGroup(erm, dro, inv, center_text), 1.0, GOLD)



class OpenProblemsCredits(OODScene):
    def construct(self):
        self.title("Open Problems")
        doors = VGroup(
            labeled_box("OOD theory\nfor foundation models", 3.25, 0.95, BLUE_D, 18),
            labeled_box("Model selection\nwithout OOD val", 3.25, 0.95, ORANGE, 18),
            labeled_box("OOD in multimodal\nand agentic AI", 3.45, 0.95, PURPLE, 18),
        ).arrange(RIGHT, buff=0.28).shift(UP * 0.95)
        glows = VGroup(*[SurroundingRectangle(d, color=c, buff=0.08) for d, c in zip(doors, [BLUE_D, ORANGE, PURPLE])])
        self.play(FadeIn(doors[0], shift=UP * 0.1), run_time=0.5)
        self.play(Create(glows[0]), FadeOut(glows[0]), run_time=0.4)
        self.wait(0.1)
        self.play(FadeIn(doors[1], shift=UP * 0.1), run_time=0.5)
        self.play(Create(glows[1]), FadeOut(glows[1]), run_time=0.4)
        self.wait(0.1)
        self.play(FadeIn(doors[2], shift=UP * 0.1), run_time=0.5)
        self.play(Create(glows[2]), FadeOut(glows[2]), run_time=0.4)
        self.wait(0.1)

        questions = VGroup(
            Text("How do we select models without peeking at the shift?", font_size=23, color=ORANGE),
            Text("Which correlations are useful, and which are brittle?", font_size=23, color=BLUE_D),
            Text("How do multimodal agents fail outside deployment data?", font_size=23, color=PURPLE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22).shift(DOWN * 0.65)
        self.play(LaggedStart(*[FadeIn(q, shift=UP * 0.08) for q in questions], lag_ratio=0.15), run_time=1.0)
        self.play(Indicate(questions[0], color=ORANGE), run_time=0.5)
        self.play(Indicate(questions[1], color=BLUE_D), run_time=0.5)
        self.play(Indicate(questions[2], color=PURPLE), run_time=0.5)
        self.wait(0.2)

        takeaway = Text("Robustness is a deployment question.", font_size=34, color=GOLD, weight=BOLD).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(takeaway, shift=UP * 0.12), run_time=0.5)
        self.play(Circumscribe(takeaway, color=GOLD), run_time=0.6)
        self.wait(0.2)

        self.play(FadeOut(questions, shift=DOWN * 0.1), doors.animate.shift(UP * 0.25).set_opacity(0.5), FadeOut(takeaway), run_time=0.5)
        credits = paragraph(
            'Based on: NeurIPS 2024 Tutorial\n"Out-of-Distribution Generalization: Shortcuts, Spuriousness & Stability"\nMaggie Makar, Aahlad Manas Puli, Yoav Wald\n\nProduced by:\nPhan Huynh Chau Thinh\nLai Nguyen Hong Thanh\nNguyen Gia Bao',
            23,
            WHITE,
            58,
        ).shift(DOWN * 1.15)
        self.play(FadeIn(credits, shift=UP * 0.18), run_time=0.8)
        self.play(doors.animate.set_opacity(0.28), run_time=0.5)
        self.wait(7.6)
