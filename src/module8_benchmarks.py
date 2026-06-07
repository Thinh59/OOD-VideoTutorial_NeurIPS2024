from manim import *
from common import *


class BenchmarksReality(OODScene):
    def construct(self):
        self.title("Benchmarks", "No silver bullet")
        
        # --- STEP 1: Benchmarks Introduction ---
        names = [
            "Waterbirds\nbackground\nWG gap 50%",
            "CelebA\ngender\nWG gap 40%",
            "Camelyon17\nhospital\nWG gap 30%",
            "CivilComments\nidentity\nWG gap 35%",
        ]
        
        # Shift slightly less left (LEFT * 2.8) and keep cards compact to prevent off-screen overflow
        cards = VGroup(*[card(n, 2.7, 1.1, c, font_size=14) for n, c in zip(names, [BLUE_D, PURPLE, GREEN_D, ORANGE])]).arrange_in_grid(2, 2, buff=0.25).shift(UP * 0.9 + LEFT * 2.8)
        
        self.play(FadeIn(cards[0], scale=0.9), run_time=0.4)
        self.play(Indicate(cards[0], color=GOLD), run_time=0.3)
        for c in cards[1:]:
            self.play(FadeIn(c, scale=0.9), run_time=0.4)
            self.play(Indicate(c, color=GOLD), run_time=0.3)
            
        stress = Text("Each benchmark breaks a different shortcut.", font_size=20, color=GRAY_B).next_to(cards, DOWN, buff=0.25)
        self.play(FadeIn(stress, shift=UP * 0.1), run_time=0.4)
        self.play(Circumscribe(cards, color=GOLD), run_time=0.45)
        self.wait(1.5)
        
        methods = ["ERM", "IRM", "DRO", "JTT", "CORAL"]
        values = [0.78, 0.73, 0.81, 0.79, 0.72]
        colors = [GRAY_B, BLUE_D, GREEN_D, YELLOW_D, PURPLE]
        
        bars = VGroup(*[bar(m, v, col, width=3.0).scale(0.72) for m, v, col in zip(methods, values, colors)]).arrange(DOWN, buff=0.16).shift(RIGHT * 3.0 + DOWN * 0.15)
        chart_title = Text("Tuned baselines mix with robust methods", font_size=18, color=GRAY_B).next_to(bars, UP, buff=0.25)
        
        self.play(FadeIn(chart_title), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(b, shift=RIGHT * 0.1) for b in bars], lag_ratio=0.12), run_time=0.5)
        self.play(LaggedStart(*[Indicate(b, color=GOLD) for b in bars], lag_ratio=0.08), run_time=0.4)
        self.wait(1.5)
        
        self.play(Indicate(bars[2], color=GREEN_D), Indicate(bars[0], color=GRAY_B), run_time=0.5)
        
        swap = Text("Rankings change with dataset, groups, and tuning budget.", font_size=20, color=ORANGE).next_to(bars, DOWN, buff=0.3)
        self.play(FadeIn(swap, shift=UP * 0.1), run_time=0.4)
        self.play(Circumscribe(bars, color=ORANGE), run_time=0.45)
        self.wait(1.5)
        
        note = Text("No method wins every dataset", font_size=26, color=GOLD, weight=BOLD).to_edge(DOWN, buff=0.3)
        self.play(FadeIn(note, shift=UP * 0.12), run_time=0.4)
        self.play(Circumscribe(note, color=GOLD), run_time=0.4)
        self.wait(2.0)
        
        # --- STEP 2: Clear screen for Gallery & Grid (Resolves title and block overlap!) ---
        self.play(FadeOut(VGroup(cards, stress, bars, chart_title, swap, note)), run_time=0.5)
        self.clear_scene()
        
        gallery_title = Text("Benchmark crisis: every dataset encodes a different shortcut", font_size=24, color=GOLD, weight=BOLD).to_edge(UP, buff=0.4)
        self.play(FadeIn(gallery_title, shift=DOWN * 0.1), run_time=0.5)
        
        gallery = VGroup(
            labeled_box("Waterbirds\nbird x background", 2.2, 0.78, BLUE_D, 14),
            labeled_box("CelebA\nhair x gender", 2.0, 0.78, PURPLE, 14),
            labeled_box("CivilComments\nidentity terms", 2.2, 0.78, ORANGE, 14),
            labeled_box("Camelyon17\nhospital scanner", 2.2, 0.78, GREEN_D, 14),
            labeled_box("WILDS\nreal distribution shifts", 2.3, 0.78, GOLD, 14),
        ).arrange(RIGHT, buff=0.2).shift(UP * 0.6)
        
        self.play(LaggedStart(*[FadeIn(g, scale=0.88) for g in gallery], lag_ratio=0.12), run_time=0.8)
        self.wait(2.5)
        
        # Fade out the gallery blocks first to prevent them overlapping the performance grid!
        self.play(FadeOut(gallery), run_time=0.5)
        
        # --- STEP 3: Performance Matrix Grid ---
        rows = ["Waterbirds", "CelebA", "Civil", "Camelyon", "WILDS"]
        cols = ["ERM", "IRM", "DRO", "JTT"]
        vals = [
            [0.32, 0.61, 0.89, 0.71],
            [0.47, 0.51, 0.88, 0.81],
            [0.58, 0.55, 0.70, 0.66],
            [0.64, 0.62, 0.68, 0.60],
            [0.50, 0.48, 0.57, 0.53],
        ]
        
        grid = VGroup()
        for r, row in enumerate(vals):
            for c, v in enumerate(row):
                color = interpolate_color(RED, GREEN_D, v)
                cell = Square(side_length=0.48, color=color, stroke_width=1.5).set_fill(color, 0.72)
                txt = Text(str(int(v * 100)), font_size=13, color=WHITE).move_to(cell)
                grid.add(VGroup(cell, txt))
                
        # Center the grid vertically since gallery is gone
        grid.arrange_in_grid(rows=5, cols=4, buff=0.07).shift(DOWN * 0.4 + RIGHT * 0.8)
        
        row_labels = VGroup(*[Text(r, font_size=16, color=GRAY_B).next_to(grid[i * 4], LEFT, buff=0.2) for i, r in enumerate(rows)])
        col_labels = VGroup(*[Text(name, font_size=16, color=GRAY_B).next_to(grid[i], UP, buff=0.2) for i, name in enumerate(cols)])
        
        self.play(FadeIn(row_labels), FadeIn(col_labels), LaggedStart(*[FadeIn(cell, scale=0.75) for cell in grid], lag_ratio=0.025), run_time=0.8)
        self.wait(1.5)
        
        scan = SurroundingRectangle(VGroup(grid[0], grid[1], grid[2], grid[3]), color=GOLD, buff=0.06)
        self.play(Create(scan), run_time=0.4)
        for r in range(1, 5):
            self.play(scan.animate.move_to(VGroup(grid[r * 4], grid[r * 4 + 1], grid[r * 4 + 2], grid[r * 4 + 3])), run_time=0.35)
        self.play(FadeOut(scan), run_time=0.25)
        
        warning = Text("A robust method is judged by the shift it survives, not by one leaderboard.", font_size=22, color=ORANGE).to_edge(DOWN, buff=0.25)
        self.play(FadeIn(warning, shift=UP * 0.1), run_time=0.5)
        self.play(Circumscribe(VGroup(grid, row_labels, col_labels), color=ORANGE), run_time=0.5)
        
        self.wait(9.21)


class ModelSelectionParadox(OODScene):
    def construct(self):
        self.title("Model Selection Paradox")
        
        items = ["Choose best\nOOD model", "Need OOD\nvalidation", "Use it for\ntraining?", "Then it is\nnot OOD"]
        positions = [UP * 2.0, RIGHT * 3.8, DOWN * 2.0, LEFT * 3.8]
        colors = [GOLD, ORANGE, BLUE_D, RED]
        
        nodes = VGroup(*[labeled_box(t, 2.65, 0.78, c, 18).move_to(p) for t, p, c in zip(items, positions, colors)])
        arrows = VGroup(*[Arrow(nodes[i].get_center(), nodes[(i + 1) % 4].get_center(), buff=0.72, color=ORANGE, stroke_width=4) for i in range(4)])
        center = labeled_box("Open\nProblem", 1.7, 0.85, RED, 18)
        
        self.play(FadeIn(nodes[0], scale=0.9), run_time=0.4)
        self.wait(0.5)
        for i in range(4):
            self.play(GrowArrow(arrows[i]), FadeIn(nodes[(i + 1) % 4], scale=0.9), run_time=0.4)
            self.play(Indicate(nodes[(i + 1) % 4], color=colors[(i + 1) % 4]), run_time=0.25)
            self.wait(0.5)
            
        self.play(FadeIn(center, scale=1.1), run_time=0.4)
        self.wait(1.0)
        
        cursor = Dot(nodes[0].get_center(), color=WHITE, radius=0.09)
        loop_path = VMobject().set_points_smoothly([n.get_center() for n in nodes] + [nodes[0].get_center()])
        self.play(FadeIn(cursor), run_time=0.25)
        
        for label, col in [("validation leaks into selection", RED), ("test shift becomes a design choice", ORANGE), ("ID accuracy hides worst-group failure", BLUE_D)]:
            note = Text(label, font_size=24, color=col).to_edge(DOWN, buff=0.42)
            self.play(FadeIn(note, shift=UP * 0.1), run_time=0.4)
            self.play(MoveAlongPath(cursor, loop_path), Rotate(arrows, angle=TAU, about_point=ORIGIN), run_time=0.8)
            self.play(FadeOut(note, shift=DOWN * 0.1), run_time=0.3)
            
        opts = VGroup(
            labeled_box("ID validation\ncan miss OOD failure", 3.25, 0.78, BLUE_D, 17),
            labeled_box("Assume test shift\nis usually unrealistic", 3.25, 0.78, ORANGE, 17),
        ).arrange(RIGHT, buff=0.45).to_edge(DOWN, buff=0.35)
        
        self.play(FadeOut(cursor), FadeIn(opts[0], shift=UP * 0.1), run_time=0.4)
        self.play(Indicate(opts[0], color=BLUE_D), run_time=0.4)
        self.wait(1.0)
        
        self.play(FadeIn(opts[1], shift=UP * 0.1), Indicate(center, color=RED), run_time=0.4)
        self.play(Indicate(opts[1], color=ORANGE), run_time=0.4)
        self.wait(1.0)
        
        warning = Text("Selection protocol is part of the method.", font_size=28, color=GOLD, weight=BOLD).next_to(center, DOWN, buff=0.25)
        self.play(FadeIn(warning, shift=UP * 0.1), run_time=0.5)
        self.play(Circumscribe(warning, color=GOLD), run_time=0.5)
        
        self.active_wait(VGroup(nodes, center, opts, warning), 1.0, GOLD)
        self.wait(4.73)


class BestPractices(OODScene):
    def construct(self):
        self.title("Best Practices", "Choose the method from the shift")

        # Make flowchart boxes slightly wider and font smaller to completely resolve text overflows!
        start = labeled_box("START", 1.8, 0.5, GOLD, 16).move_to(UP * 2.05)
        shift = labeled_box("What kind of shift?", 3.5, 0.58, BLUE_D, 16).next_to(start, DOWN, buff=0.22)
        shift_types = VGroup(
            labeled_box("Covariate", 1.5, 0.43, GRAY_B, 13),
            labeled_box("Label", 1.2, 0.43, GRAY_B, 13),
            labeled_box("Spurious", 1.5, 0.43, RED, 13),
        ).arrange(RIGHT, buff=0.14).next_to(shift, DOWN, buff=0.16)

        group_q = labeled_box("Group labels?", 2.8, 0.52, ORANGE, 15).move_to(LEFT * 3.05 + DOWN * 0.22)
        dro = labeled_box("YES: Group DRO", 2.8, 0.48, GREEN_D, 13).next_to(group_q, DOWN, buff=0.18)
        jtt = labeled_box("NO: JTT / clustering", 2.9, 0.48, YELLOW_D, 13).next_to(dro, DOWN, buff=0.14)

        fm_q = labeled_box("Foundation model?", 3.1, 0.52, PURPLE, 15).move_to(RIGHT * 3.05 + DOWN * 0.22)
        last_layer = labeled_box("YES: last-layer first", 3.0, 0.48, PURPLE, 13).next_to(fm_q, DOWN, buff=0.18)
        erm = labeled_box("NO: tune ERM baseline", 3.1, 0.48, BLUE_D, 13).next_to(last_layer, DOWN, buff=0.14)

        diversity = labeled_box("Increase environment diversity", 4.3, 0.52, GREEN_D, 13).move_to(DOWN * 2.18)
        report = labeled_box("Always report Worst-Group Accuracy", 4.9, 0.54, GOLD, 13).move_to(DOWN * 2.82)

        arrows = VGroup(
            Arrow(start.get_bottom(), shift.get_top(), buff=0.08, color=GRAY_B),
            Arrow(shift.get_bottom(), shift_types.get_top(), buff=0.08, color=GRAY_B),
            Arrow(shift_types[0].get_bottom(), group_q.get_top(), buff=0.1, color=ORANGE, stroke_width=3),
            Arrow(shift_types[2].get_bottom(), fm_q.get_top(), buff=0.1, color=PURPLE, stroke_width=3),
            Arrow(group_q.get_bottom(), dro.get_top(), buff=0.08, color=GREEN_D),
            Arrow(dro.get_bottom(), jtt.get_top(), buff=0.08, color=YELLOW_D),
            Arrow(fm_q.get_bottom(), last_layer.get_top(), buff=0.08, color=PURPLE),
            Arrow(last_layer.get_bottom(), erm.get_top(), buff=0.08, color=BLUE_D),
            Arrow(jtt.get_bottom(), diversity.get_left(), buff=0.12, color=GREEN_D),
            Arrow(erm.get_bottom(), diversity.get_right(), buff=0.12, color=BLUE_D),
            Arrow(diversity.get_bottom(), report.get_top(), buff=0.08, color=GOLD),
        )

        self.play(FadeIn(start, shift=DOWN * 0.15), GrowArrow(arrows[0]), run_time=0.4)
        self.play(FadeIn(shift, shift=DOWN * 0.15), run_time=0.35)
        self.play(LaggedStart(*[FadeIn(item, shift=UP * 0.08) for item in shift_types], lag_ratio=0.1), GrowArrow(arrows[1]), run_time=0.5)
        self.play(Indicate(shift_types[2], color=RED), run_time=0.4)
        self.wait(0.5)

        self.play(GrowArrow(arrows[2]), GrowArrow(arrows[3]), run_time=0.35)
        self.play(FadeIn(group_q, shift=RIGHT * 0.15), FadeIn(fm_q, shift=LEFT * 0.15), run_time=0.4)
        self.play(Indicate(group_q, color=ORANGE), run_time=0.3)
        self.play(GrowArrow(arrows[4]), FadeIn(dro, shift=UP * 0.1), run_time=0.3)
        self.play(Flash(dro.get_center(), color=GREEN_D), run_time=0.3)
        self.play(GrowArrow(arrows[5]), FadeIn(jtt, shift=UP * 0.1), run_time=0.35)
        self.play(Indicate(jtt, color=YELLOW_D), run_time=0.3)
        self.wait(0.5)

        self.play(Indicate(fm_q, color=PURPLE), run_time=0.3)
        self.play(GrowArrow(arrows[6]), FadeIn(last_layer, shift=UP * 0.1), run_time=0.35)
        self.play(Flash(last_layer.get_center(), color=PURPLE), run_time=0.3)
        self.play(GrowArrow(arrows[7]), FadeIn(erm, shift=UP * 0.1), run_time=0.35)
        self.play(Indicate(erm, color=BLUE_D), run_time=0.3)
        self.wait(0.5)

        self.play(GrowArrow(arrows[8]), GrowArrow(arrows[9]), run_time=0.4)
        self.play(FadeIn(diversity, shift=UP * 0.12), run_time=0.35)
        
        env_dots = VGroup(
            Dot(color=GREEN_D).move_to(diversity.get_left() + RIGHT * 0.55),
            Dot(color=YELLOW_D).move_to(diversity.get_center()),
            Dot(color=PURPLE).move_to(diversity.get_right() + LEFT * 0.55),
        )
        self.play(LaggedStart(*[GrowFromCenter(dot) for dot in env_dots], lag_ratio=0.15), run_time=0.4)
        self.play(env_dots.animate.arrange(RIGHT, buff=0.45).next_to(diversity, UP, buff=0.18), run_time=0.4)
        self.wait(1.0)

        self.play(GrowArrow(arrows[10]), FadeIn(report, shift=UP * 0.12), run_time=0.4)
        
        flow_group = VGroup(
            start, shift, shift_types, group_q, dro, jtt,
            fm_q, last_layer, erm, arrows, env_dots
        )
        self.play(
            FadeOut(flow_group, shift=UP * 0.12),
            diversity.animate.move_to(UP * 0.25).scale(1.08),
            report.animate.move_to(DOWN * 0.95).scale(1.08),
            run_time=0.6,
        )
        
        bars = VGroup(
            bar("avg", 0.88, GREEN_D, width=2.4).scale(0.76),
            bar("worst", 0.42, RED, width=2.4).scale(0.76),
        ).arrange(DOWN, buff=0.2).next_to(report, DOWN, buff=0.25)
        
        self.play(FadeIn(bars[0], shift=UP * 0.1), run_time=0.35)
        self.play(FadeIn(bars[1], shift=UP * 0.1), Indicate(report, color=GOLD), run_time=0.4)
        self.play(Flash(report.get_center(), color=GOLD), run_time=0.4)
        
        self.active_wait(VGroup(diversity, report, bars), 1.0, GOLD)
        self.wait(9.39)
