from manim import *
from common import *


class JourneySummary(OODScene):
    def construct(self):
        self.title("Journey Summary")
        boxes = {
            "ERM": labeled_box("ERM\nshortcuts", 2.2, 0.72, ORANGE, 17).move_to(LEFT * 4.2 + UP * 1.35),
            "SCM": labeled_box("SCM\ncausality", 2.2, 0.72, BLUE_D, 17).move_to(LEFT * 4.2 + DOWN * 0.05),
            "IRM": labeled_box("IRM", 1.45, 0.62, GREEN_D, 18).move_to(LEFT * 5.0 + DOWN * 1.65),
            "DRO": labeled_box("DRO", 1.45, 0.62, YELLOW_D, 18).move_to(LEFT * 3.55 + DOWN * 1.65),
            "JTT": labeled_box("JTT", 1.45, 0.62, GOLD, 18).move_to(LEFT * 2.1 + DOWN * 1.65),
            "FM": labeled_box("Foundation\nmodels", 2.45, 0.72, PURPLE, 17).move_to(RIGHT * 3.7 + UP * 1.35),
            "Scale": labeled_box("Scale !=\nrobustness", 2.45, 0.72, RED, 17).move_to(RIGHT * 3.7 + DOWN * 0.05),
            "Bench": labeled_box("Benchmarks\nbest practices", 2.9, 0.72, GOLD, 16).move_to(RIGHT * 2.15 + DOWN * 1.65),
        }
        left_path = VGroup(boxes["ERM"], boxes["SCM"], boxes["IRM"], boxes["DRO"], boxes["JTT"])
        right_path = VGroup(boxes["FM"], boxes["Scale"], boxes["Bench"])
        arrows = VGroup(
            Arrow(boxes["ERM"].get_bottom(), boxes["SCM"].get_top(), buff=0.08, color=BLUE_D),
            Arrow(boxes["SCM"].get_bottom(), boxes["DRO"].get_top(), buff=0.08, color=GREEN_D),
            Arrow(boxes["IRM"].get_right(), boxes["DRO"].get_left(), buff=0.08, color=GREEN_D),
            Arrow(boxes["DRO"].get_right(), boxes["JTT"].get_left(), buff=0.08, color=YELLOW_D),
            Arrow(boxes["FM"].get_bottom(), boxes["Scale"].get_top(), buff=0.08, color=RED),
            Arrow(boxes["Scale"].get_bottom(), boxes["Bench"].get_top(), buff=0.08, color=GOLD),
            Arrow(boxes["Scale"].get_left(), boxes["SCM"].get_right(), buff=0.1, color=PURPLE, stroke_width=3),
            Arrow(boxes["JTT"].get_right(), boxes["Bench"].get_left(), buff=0.08, color=GOLD),
        )
        words = VGroup(
            Text("CORRELATION", font_size=32, color=GRAY_B),
            Text("CAUSATION", font_size=32, color=BLUE_D),
            Text("STABILITY", font_size=42, color=GOLD, weight=BOLD),
        ).arrange(RIGHT, buff=0.4).shift(DOWN * 0.2)
        links = VGroup(
            Arrow(words[0].get_right(), words[1].get_left(), buff=0.1, color=BLUE_D),
            Arrow(words[1].get_right(), words[2].get_left(), buff=0.1, color=GOLD),
        )
        self.play(FadeIn(words[0], shift=UP * 0.1), run_time=0.4)
        self.play(GrowArrow(links[0]), FadeIn(words[1], shift=UP * 0.1), run_time=0.4)
        self.play(GrowArrow(links[1]), FadeIn(words[2], scale=1.1), run_time=0.5)
        self.play(Flash(words[2].get_center(), color=GOLD, line_length=0.35, num_lines=10), Circumscribe(words[2], color=GOLD), run_time=0.5)
        self.wait(0.1)

        self.play(FadeOut(VGroup(words, links)), run_time=0.3)

        left_path = VGroup(boxes["ERM"], boxes["SCM"], boxes["IRM"], boxes["DRO"], boxes["JTT"])
        right_path = VGroup(boxes["FM"], boxes["Scale"], boxes["Bench"])
        
        self.play(FadeIn(boxes["ERM"], shift=RIGHT * 0.1), run_time=0.3)
        self.play(Indicate(boxes["ERM"], color=ORANGE), run_time=0.3)
        self.play(GrowArrow(arrows[0]), FadeIn(boxes["SCM"], shift=DOWN * 0.1), run_time=0.4)
        self.play(Indicate(boxes["SCM"], color=BLUE_D), run_time=0.3)
        
        self.play(
            GrowArrow(arrows[1]),
            FadeIn(boxes["IRM"], shift=UP * 0.1),
            FadeIn(boxes["DRO"], shift=UP * 0.1),
            FadeIn(boxes["JTT"], shift=UP * 0.1),
            run_time=0.4,
        )
        self.play(GrowArrow(arrows[2]), GrowArrow(arrows[3]), run_time=0.3)
        self.play(
            Indicate(boxes["IRM"], color=GREEN_D),
            Indicate(boxes["DRO"], color=YELLOW_D),
            Indicate(boxes["JTT"], color=GOLD),
            run_time=0.4,
        )
        left_label = Text("small-data robust learning", font_size=24, color=GRAY_B).next_to(left_path, DOWN, buff=0.22)
        self.play(FadeIn(left_label, shift=UP * 0.08), Circumscribe(left_path, color=BLUE_D), run_time=0.5)

        self.play(FadeIn(boxes["FM"], shift=LEFT * 0.1), run_time=0.3)
        self.play(GrowArrow(arrows[4]), FadeIn(boxes["Scale"], shift=DOWN * 0.1), run_time=0.4)
        self.play(Indicate(boxes["Scale"], color=RED), run_time=0.3)
        self.play(GrowArrow(arrows[5]), FadeIn(boxes["Bench"], shift=UP * 0.1), run_time=0.4)
        self.play(GrowArrow(arrows[6]), GrowArrow(arrows[7]), run_time=0.4)
        self.play(Indicate(boxes["Bench"], color=GOLD), run_time=0.3)
        
        bridge = Text("foundation models & scale", font_size=24, color=GRAY_B).next_to(right_path, DOWN, buff=0.22)
        self.play(FadeIn(bridge, shift=UP * 0.08), Circumscribe(right_path, color=PURPLE), run_time=0.5)
        
        # Instead of self.wait(72.95), we walk through each concept dynamically

        # Stop 1: ERM
        self.play(Indicate(boxes["ERM"], color=ORANGE), run_time=0.5)
        self.wait(0.1)

        # Stop 2: SCM
        self.play(Indicate(boxes["SCM"], color=BLUE_D), run_time=0.5)
        self.wait(0.1)

        # Stop 3: DRO / IRM / JTT
        self.play(
            Indicate(boxes["IRM"], color=GREEN_D),
            Indicate(boxes["DRO"], color=YELLOW_D),
            Indicate(boxes["JTT"], color=GOLD),
            run_time=0.6
        )
        self.wait(0.1)

        # Stop 4: Foundation Models & Scale
        self.play(
            Indicate(boxes["FM"], color=PURPLE),
            Indicate(boxes["Scale"], color=RED),
            run_time=0.6
        )
        self.wait(0.1)

        # Stop 5: Benchmarks
        self.play(Indicate(boxes["Bench"], color=GOLD), run_time=0.5)
        self.wait(0.1)

        # Clear everything for the final grand message of STABILITY
        self.play(
            FadeOut(VGroup(
                boxes["ERM"], boxes["SCM"], boxes["IRM"], boxes["DRO"], boxes["JTT"],
                boxes["FM"], boxes["Scale"], boxes["Bench"],
                arrows, left_label, bridge
            )),
            run_time=0.5
        )

        stability_word = Text("STABILITY", font_size=56, color=GOLD, weight=BOLD).shift(UP * 0.5)
        stability_desc = Text(
            "Identify the core causal features and rely on them consistently.",
            font_size=24,
            color=WHITE
        ).next_to(stability_word, DOWN, buff=0.4)
        
        self.play(FadeIn(stability_word, scale=1.2), run_time=0.5)
        self.play(Flash(stability_word.get_center(), color=GOLD, line_length=0.45, num_lines=12), run_time=0.5)
        self.play(FadeIn(stability_desc, shift=UP * 0.1), run_time=0.5)
        self.play(Circumscribe(stability_word, color=GOLD), run_time=0.5)
        self.wait(7.59)


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
