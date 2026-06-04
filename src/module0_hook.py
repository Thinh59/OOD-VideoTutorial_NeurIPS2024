from manim import *
from common import *


class OpeningClinicalNotes(OODScene):
    def construct(self):
        def hospital_icon(label, color):
            building = RoundedRectangle(width=1.55, height=1.0, corner_radius=0.08, color=color, stroke_width=3).set_fill(color, 0.12)
            roof = Triangle(color=color, stroke_width=3).set_fill(color, 0.18).scale(0.4).next_to(building, UP, buff=-0.1)
            cross_v = Rectangle(width=0.1, height=0.38, color=WHITE).set_fill(WHITE, 0.9).move_to(building)
            cross_h = Rectangle(width=0.38, height=0.1, color=WHITE).set_fill(WHITE, 0.9).move_to(building)
            txt = Text(label, font_size=24, color=color, weight=BOLD).next_to(building, DOWN, buff=0.14)
            return VGroup(roof, building, cross_v, cross_h, txt)

        def record(keyword, color, mark_color=GREEN_D):
            paper = RoundedRectangle(width=2.7, height=1.25, corner_radius=0.08, color=WHITE, stroke_width=2).set_fill(WHITE, 0.05)
            avatar = Circle(radius=0.18, color=GRAY_B).set_fill(GRAY_B, 0.4).move_to(paper.get_left() + RIGHT * 0.45 + UP * 0.25)
            lines = VGroup(
                Line(ORIGIN, RIGHT * 1.25, color=GRAY_C, stroke_width=3),
                Line(ORIGIN, RIGHT * 1.05, color=GRAY_D, stroke_width=3),
                Line(ORIGIN, RIGHT * 1.35, color=GRAY_D, stroke_width=3),
            ).arrange(DOWN, buff=0.15).next_to(avatar, RIGHT, buff=0.22)
            tag = Text(keyword, font_size=24, color=RED, weight=BOLD).move_to(paper.get_bottom() + UP * 0.25)
            pulse = Circle(radius=0.12, color=mark_color, stroke_width=4).move_to(paper.get_right() + LEFT * 0.35 + DOWN * 0.33)
            return VGroup(paper, avatar, lines, tag, pulse)

        def disease_badge(label, color):
            icon = Circle(radius=0.34, color=color, stroke_width=3).set_fill(color, 0.15)
            label_m = Text(label, font_size=22, color=color, weight=BOLD).next_to(icon, DOWN, buff=0.16)
            return VGroup(icon, label_m)

        def accuracy_meter(value, color, label):
            base = RoundedRectangle(width=4.0, height=0.35, corner_radius=0.16, color=GRAY_D, stroke_width=0).set_fill(GRAY_D, 0.55)
            fill = RoundedRectangle(width=4.0 * value, height=0.35, corner_radius=0.16, color=color, stroke_width=0).set_fill(color, 0.95)
            fill.align_to(base, LEFT)
            pct = Text(f"{int(value * 100)}%", font_size=28, color=color, weight=BOLD).next_to(base, RIGHT, buff=0.22)
            lab = Text(label, font_size=20, color=GRAY_B).next_to(base, UP, buff=0.12).align_to(base, LEFT)
            return VGroup(lab, base, fill, pct)

        # ── Beat 1: Intro Title
        title = Text("EHR disease prediction", font_size=38, color=WHITE, weight=BOLD).to_edge(UP, buff=0.35)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.8)

        intro = VGroup(
            hospital_icon("Hospital A", GREEN_D).shift(LEFT * 4.4),
            labeled_box("AI", 1.15, 0.8, BLUE_D, 30),
            disease_badge("Disease", GOLD).shift(RIGHT * 4.4),
        ).move_to(UP * 1.75)
        arrows = VGroup(
            Arrow(intro[0].get_right(), intro[1].get_left(), color=GRAY_B, buff=0.25),
            Arrow(intro[1].get_right(), intro[2].get_left(), color=GRAY_B, buff=0.25),
        )
        self.play(
            FadeIn(intro[0]),
            FadeIn(intro[1]),
            FadeIn(intro[2]),
            LaggedStart(*[GrowArrow(arrow) for arrow in arrows], lag_ratio=0.2),
            run_time=1.3,
        )
        self.wait(1.5)

        # ── Beat 2: Training Set at Hospital A
        r1 = record("MAN", RED)
        r2 = record("GENTLEMAN", RED)
        d1 = disease_badge("Diabetes", BLUE_D)
        d2 = disease_badge("Arthritis", PURPLE)
        pairs = VGroup(
            VGroup(r1, Arrow(r1.get_right(), d1.get_left(), color=GREEN_D, buff=0.18), d1).arrange(RIGHT, buff=0.35),
            VGroup(r2, Arrow(r2.get_right(), d2.get_left(), color=GREEN_D, buff=0.18), d2).arrange(RIGHT, buff=0.35),
        ).arrange(DOWN, buff=0.55).shift(DOWN * 0.35)
        train_meter = accuracy_meter(0.95, GREEN_D, "Hospital A").to_edge(DOWN, buff=0.45)
        self.play(LaggedStart(FadeIn(pairs[0], shift=UP * 0.2), FadeIn(pairs[1], shift=UP * 0.2), lag_ratio=0.25), run_time=1.2)
        self.play(FadeIn(train_meter), run_time=0.7)
        self.play(Circumscribe(VGroup(r1[-2], r2[-2]), color=RED), run_time=1.2)
        self.wait(2.0)

        # ── Beat 3: Shortcut Highlight
        shortcut = VGroup(
            Text("shortcut", font_size=26, color=RED, weight=BOLD),
            Arrow(LEFT * 0.8, RIGHT * 0.8, color=RED, stroke_width=5),
        ).arrange(DOWN, buff=0.12).move_to(RIGHT * 2.25 + UP * 1.0)
        self.play(
            pairs[0][1].animate.set_color(RED).set_stroke(width=7),
            pairs[1][1].animate.set_color(RED).set_stroke(width=7),
            FadeIn(shortcut, scale=0.9),
            run_time=0.9,
        )
        self.wait(2.5)

        # ── Beat 4: Deployment to Hospital B
        self.play(
            VGroup(pairs, train_meter, intro, arrows, shortcut).animate.scale(0.66).to_edge(LEFT, buff=0.35).shift(DOWN * 0.15),
            title.animate.scale(0.78).to_edge(UP, buff=0.28),
            run_time=1.0,
        )
        self.wait(1.2)

        hosp_b = hospital_icon("Hospital B", RED).move_to(RIGHT * 4.0 + UP * 1.65)
        new_record = record("MAN", RED, mark_color=RED).move_to(RIGHT * 2.65 + DOWN * 0.25)
        arthritis_b = disease_badge("Arthritis", PURPLE).move_to(RIGHT * 5.3 + DOWN * 0.25)
        wrong_pred = disease_badge("Diabetes", BLUE_D).move_to(RIGHT * 5.3 + DOWN * 1.65)
        good_arrow = Arrow(new_record.get_right(), arthritis_b.get_left(), color=GRAY_D, buff=0.18)
        bad_arrow = Arrow(new_record.get_right(), wrong_pred.get_left(), color=RED, buff=0.18, stroke_width=7)
        cross = VGroup(
            Line(LEFT * 0.22 + DOWN * 0.22, RIGHT * 0.22 + UP * 0.22, color=RED, stroke_width=7),
            Line(LEFT * 0.22 + UP * 0.22, RIGHT * 0.22 + DOWN * 0.22, color=RED, stroke_width=7),
        ).move_to(wrong_pred[0])
        test_meter = accuracy_meter(0.72, RED, "Hospital B").move_to(RIGHT * 3.65 + DOWN * 2.75)
        
        self.play(FadeIn(hosp_b, shift=LEFT), FadeIn(new_record, shift=LEFT), FadeIn(arthritis_b), GrowArrow(good_arrow), run_time=1.0)
        self.wait(1.5)
        self.play(GrowArrow(bad_arrow), FadeIn(wrong_pred, shift=UP), FadeIn(cross), run_time=0.8)
        self.wait(1.5)
        self.play(TransformFromCopy(train_meter, test_meter), run_time=0.9)
        self.play(Flash(cross, color=RED), Indicate(test_meter[-1], color=RED), run_time=1.0)
        self.wait(2.0)

        # ── Beat 5: Wrong Signal Explanation
        self.play(*[FadeOut(m) for m in self.mobjects if m != title], run_time=0.7)
        core = Text("medical signal", font_size=34, color=BLUE_D, weight=BOLD).shift(LEFT * 2.8)
        spurious = Text("writing habit", font_size=34, color=RED, weight=BOLD).shift(RIGHT * 2.8)
        model = labeled_box("AI", 1.2, 0.8, WHITE, 30)
        good = Arrow(core.get_right(), model.get_left(), color=BLUE_D, buff=0.25, stroke_width=5)
        bad = Arrow(spurious.get_left(), model.get_right(), color=RED, buff=0.25, stroke_width=7)
        self.play(FadeIn(core), FadeIn(spurious), FadeIn(model))
        self.play(GrowArrow(good), GrowArrow(bad))
        self.play(bad.animate.set_stroke(width=11), spurious.animate.scale(1.12), run_time=0.8)
        aha = Text("wrong signal", font_size=42, color=GOLD, weight=BOLD).to_edge(DOWN, buff=0.55)
        self.play(FadeIn(aha, shift=UP), Circumscribe(spurious, color=RED), run_time=1.2)
        self.wait(1.5)

        # ── Beat 6: Summary Timeline & Narrative Beats
        timeline = VGroup(
            labeled_box("Hospital A\n95%", 2.0, 0.68, GREEN_D, 17),
            labeled_box("shortcut\nwriting style", 2.25, 0.68, RED, 17),
            labeled_box("Hospital B\n72%", 2.0, 0.68, ORANGE, 17),
            labeled_box("wrong\nsignal", 1.8, 0.68, GOLD, 17),
        ).arrange(RIGHT, buff=0.35).to_edge(DOWN, buff=0.28)
        links = VGroup(*[
            Arrow(timeline[i].get_right(), timeline[i + 1].get_left(), buff=0.08, color=GRAY_B, stroke_width=3)
            for i in range(3)
        ])
        
        self.play(
            FadeOut(aha),
            model.animate.shift(UP * 0.45).scale(0.8),
            core.animate.shift(UP * 0.45).scale(0.8),
            spurious.animate.shift(UP * 0.45).scale(0.8),
            good.animate.shift(UP * 0.45),
            bad.animate.shift(UP * 0.45),
            FadeIn(timeline[0], shift=UP * 0.1),
            run_time=0.9
        )
        self.play(GrowArrow(links[0]), FadeIn(timeline[1], shift=UP * 0.1), run_time=0.8)
        self.play(GrowArrow(links[1]), FadeIn(timeline[2], shift=UP * 0.1), run_time=0.8)
        self.play(GrowArrow(links[2]), FadeIn(timeline[3], shift=UP * 0.1), run_time=0.8)
        
        # Sequentially highlight each block according to the narrative recap
        self.play(Indicate(timeline[0], color=GREEN_D), run_time=0.9)
        self.play(Indicate(timeline[1], color=RED), run_time=0.9)
        self.play(Indicate(timeline[2], color=ORANGE), run_time=0.9)
        self.play(Indicate(timeline[3], color=GOLD), Flash(timeline[3], color=GOLD), run_time=1.0)
        self.wait(12.15)


class RoadMap(OODScene):
    def construct(self):
        self.title("Road Map")
        road = VGroup(Line(LEFT * 5.8, RIGHT * 5.8, color=GRAY_B), Line(LEFT * 5.8 + DOWN * 0.3, RIGHT * 5.8 + DOWN * 0.3, color=GRAY_B)).shift(UP * 0.25)
        
        # Expanded to 8 nodes to match SCM/Causality/DRO/JTT split voiceover beats
        labels = [
            "ERM\nShortcuts", "Causality", "SCM", "IRM",
            "Group\nDRO", "JTT", "Foundation\nModels", "Best\nPractices"
        ]
        colors = [ORANGE, BLUE_D, BLUE_D, GREEN_D, YELLOW_D, GOLD, PURPLE, GOLD]
        
        nodes = VGroup()
        for i, (lab, col) in enumerate(zip(labels, colors)):
            x = -5.25 + i * 1.5
            n = Circle(radius=0.22, color=col).set_fill(col, 0.3).move_to([x, 0.08, 0])
            t = Text(lab, font_size=15, color=WHITE, line_spacing=0.8).next_to(n, DOWN, buff=0.38)
            nodes.add(VGroup(n, t))
            
        sign = labeled_box("START", 1.0, 0.4, WHITE, 14).move_to(LEFT * 5.8 + UP * 0.65)
        car = Dot(color=WHITE, radius=0.08).move_to(nodes[0][0])
        self.play(Create(road), FadeIn(sign), run_time=1.0)
        self.play(LaggedStart(*[FadeIn(n, scale=0.8) for n in nodes], lag_ratio=0.12), run_time=0.7)
        self.play(FadeIn(car), run_time=0.3)
        
        icons = VGroup()
        for i, n in enumerate(nodes):
            icon_char = ["?", "->", "SCM", "=", "max", "x2", "AI", "WG"][i]
            icon = Text(icon_char, font_size=16, color=colors[i]).next_to(n[0], UP, buff=0.28)
            icons.add(icon)
            
            # Step nodes one by one to align with audio descriptions
            self.play(
                car.animate.move_to(n[0]),
                n[0].animate.scale(1.2),
                FadeIn(icon, scale=0.8),
                run_time=0.25
            )
            self.play(Flash(n[0], color=colors[i], line_length=0.2, num_lines=6), run_time=0.1)
            self.play(n[0].animate.scale(1 / 1.2), run_time=0.08)
            
        close = Text("From shortcuts to stability", font_size=30, color=GOLD).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(close, shift=UP), run_time=0.5)
        self.play(LaggedStart(*[Indicate(i, color=GOLD) for i in icons], lag_ratio=0.1), run_time=0.7)
        
        # Draw path connection
        route = VMobject(color=GOLD, stroke_width=5).set_points_as_corners([n[0].get_center() for n in nodes])
        self.play(Create(route), run_time=0.6)
        self.play(route.animate.set_stroke(width=8).set_opacity(0.35), Flash(close, color=GOLD), run_time=0.5)
        self.play(FadeOut(route), run_time=0.3)
        
        # Step-by-step active car sequence to align exactly with closing voiceover beats
        beat_notes = VGroup(
            Text("formalize shift", font_size=22, color=BLUE_D),
            Text("choose objective", font_size=22, color=GREEN_D),
            Text("evaluate robustness", font_size=22, color=GOLD),
        ).arrange(RIGHT, buff=0.55).to_edge(DOWN, buff=0.35)
        
        self.play(Transform(close, beat_notes[0]), run_time=0.35)
        self.play(car.animate.move_to(nodes[2][0]), Indicate(nodes[2], color=BLUE_D), run_time=0.4)
        self.wait(0.05)
        
        self.play(Transform(close, beat_notes[1]), run_time=0.25)
        self.play(car.animate.move_to(nodes[4][0]), Indicate(nodes[4], color=YELLOW_D), run_time=0.4)
        self.wait(0.05)
        
        self.play(Transform(close, beat_notes[2]), run_time=0.25)
        self.play(car.animate.move_to(nodes[6][0]), Indicate(nodes[6], color=PURPLE), run_time=0.4)
        self.wait(15.22)
        
        self.play(car.animate.move_to(nodes[7][0]), Flash(nodes[7][0], color=GOLD), run_time=0.4)
        self.play(Circumscribe(nodes, color=GOLD), run_time=0.4)
