from manim import *
from common import *


def simple_cow(color=WHITE):
    body = RoundedRectangle(width=0.64, height=0.32, corner_radius=0.08, color=color).set_fill(color, 0.65)
    head = Circle(radius=0.15, color=color).set_fill(color, 0.65).next_to(body, RIGHT, buff=-0.04)
    horns = VGroup(
        Line(head.get_top(), head.get_top() + LEFT * 0.12 + UP * 0.14, color=color, stroke_width=3),
        Line(head.get_top(), head.get_top() + RIGHT * 0.12 + UP * 0.14, color=color, stroke_width=3),
    )
    legs = VGroup(*[
        Line(body.get_bottom() + RIGHT * x, body.get_bottom() + RIGHT * x + DOWN * 0.2, color=color, stroke_width=4)
        for x in [-0.22, 0.18]
    ])
    return VGroup(body, head, horns, legs).scale(0.8)


def group_tile(animal, bg_color, count, label_color, pos, scale=1.0):
    box = RoundedRectangle(width=2.35, height=1.55, corner_radius=0.08, color=label_color, stroke_width=3).set_fill(bg_color, 0.18)
    icons = VGroup(*[animal.copy().scale(0.72).shift(RIGHT * (i % 4) * 0.35 + DOWN * (i // 4) * 0.32) for i in range(count)])
    icons.move_to(box)
    return VGroup(box, icons).scale(scale).move_to(pos)


class GroupStructure(OODScene):
    def construct(self):
        title = Text("Average hides groups", font_size=36, color=WHITE, weight=BOLD).to_edge(UP, buff=0.35)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.8)

        cow = simple_cow(WHITE)
        camel = simple_camel(YELLOW_D)
        tiles = VGroup(
            group_tile(cow, GREEN_D, 8, GREEN_D, LEFT * 2.0 + UP * 0.95),
            group_tile(cow, YELLOW_D, 2, RED, RIGHT * 2.0 + UP * 0.95),
            group_tile(camel, GREEN_D, 2, RED, LEFT * 2.0 + DOWN * 1.05),
            group_tile(camel, YELLOW_D, 8, YELLOW_D, RIGHT * 2.0 + DOWN * 1.05),
        )
        self.play(LaggedStart(*[FadeIn(t, scale=0.85) for t in tiles], lag_ratio=0.15), run_time=1.4)
        self.wait(2.5)

        braces = VGroup(
            SurroundingRectangle(tiles[1], color=RED, buff=0.12),
            SurroundingRectangle(tiles[2], color=RED, buff=0.12),
        )
        small = Text("small groups", font_size=30, color=RED, weight=BOLD).to_edge(DOWN, buff=0.45)
        self.play(Create(braces), FadeIn(small, shift=UP), run_time=1.0)
        self.wait(3.4)

        overall = bar("overall", 0.92, GREEN_D, width=3.2).scale(0.88).to_corner(UR).shift(DOWN * 0.45)
        worst = bar("weakest", 0.18, RED, width=3.2).scale(0.88).next_to(overall, DOWN, buff=0.35)
        self.play(FadeIn(overall), run_time=0.7)
        self.play(FadeIn(worst), Indicate(braces, color=RED), run_time=1.0)
        self.wait(4.8)

        cover = Rectangle(width=14, height=8, color=BLACK, stroke_width=0).set_fill(BLACK, 0.72)
        reveal = Text("minority failure", font_size=44, color=GOLD, weight=BOLD).move_to(ORIGIN)
        self.play(FadeIn(cover), FadeIn(reveal, scale=1.05), run_time=1.0)
        self.wait(6.0)


class WorstGroupAccuracy(OODScene):
    def construct(self):
        title = Text("Worst-group accuracy", font_size=36, color=WHITE, weight=BOLD).to_edge(UP, buff=0.35)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.8)

        labels = ["g1", "g2", "g3", "g4", "avg"]
        erm_vals = [0.96, 0.18, 0.21, 0.94, 0.82]
        robust_vals = [0.78, 0.75, 0.72, 0.80, 0.76]

        def chart(name, vals, x):
            rows = VGroup(Text(name, font_size=30, color=GOLD, weight=BOLD))
            for lab, val in zip(labels, vals):
                col = RED if val < 0.3 else GREEN_D
                rows.add(bar(lab, val, col, width=2.6).scale(0.82))
            rows.arrange(DOWN, aligned_edge=LEFT, buff=0.22).move_to(x)
            return rows

        erm = chart("ERM", erm_vals, LEFT * 3.2)
        robust = chart("Robust", robust_vals, RIGHT * 3.2)
        self.play(FadeIn(erm, shift=RIGHT * 0.2), FadeIn(robust, shift=LEFT * 0.2), run_time=1.2)
        self.wait(2.0)

        self.play(Indicate(erm[2], color=RED), Indicate(erm[3], color=RED), run_time=1.1)
        self.wait(2.2)
        floor_erm = DashedLine(LEFT * 5.5 + DOWN * 1.8, LEFT * 1.0 + DOWN * 1.8, color=RED)
        floor_robust = DashedLine(RIGHT * 1.0 + DOWN * 0.28, RIGHT * 5.5 + DOWN * 0.28, color=GREEN_D)
        self.play(Create(floor_erm), Create(floor_robust), run_time=1.0)
        self.wait(2.2)

        weak = Text("weakest group = deployment risk", font_size=34, color=GOLD, weight=BOLD).to_edge(DOWN, buff=0.45)
        self.play(FadeIn(weak, shift=UP), run_time=0.8)
        self.wait(7.0)


class DistributionShiftTypes(OODScene):
    def construct(self):
        title = Text("Distribution shift", font_size=36, color=WHITE, weight=BOLD).to_edge(UP, buff=0.35)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.8)

        names = ["covariate", "label", "spurious"]
        panels = VGroup()
        for i, name in enumerate(names):
            ax = Axes(
                x_range=[-3, 3],
                y_range=[0, 1],
                x_length=3.2,
                y_length=1.8,
                axis_config={"include_ticks": False, "color": GRAY_B},
            )
            train = ax.plot(lambda x: math.exp(-x * x), color=BLUE_D)
            if i == 0:
                test = ax.plot(lambda x: math.exp(-(x - 1.0) ** 2), color=GREEN_D)
            elif i == 1:
                test = ax.plot(lambda x: 0.55 * math.exp(-x * x), color=GREEN_D)
            else:
                test = ax.plot(lambda x: math.exp(-x * x), color=RED).rotate(PI, about_point=ax.c2p(0, 0.5))
            label = Text(name, font_size=28, color=GOLD if i == 2 else WHITE, weight=BOLD).next_to(ax, UP, buff=0.18)
            panels.add(VGroup(label, ax, train, test))
        panels.arrange(RIGHT, buff=0.72).shift(DOWN * 0.1)
        self.play(LaggedStart(*[FadeIn(p, shift=UP * 0.15) for p in panels], lag_ratio=0.18), run_time=1.5)
        self.wait(3.0)

        arrows = VGroup(
            Arrow(panels[0][2].get_center(), panels[0][3].get_center(), color=GREEN_D, buff=0.15),
            Arrow(panels[1][2].get_center(), panels[1][3].get_center(), color=GREEN_D, buff=0.15),
            Arrow(panels[2][2].get_center(), panels[2][3].get_center(), color=RED, buff=0.15),
        )
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.2), run_time=1.1)
        self.wait(3.2)
        self.play(panels[2].animate.scale(1.13), Indicate(arrows[2], color=GOLD), run_time=1.2)
        focus = Text("shortcut relation flips", font_size=34, color=RED, weight=BOLD).to_edge(DOWN, buff=0.45)
        self.play(FadeIn(focus, shift=UP), run_time=0.8)
        self.wait(9.0)
