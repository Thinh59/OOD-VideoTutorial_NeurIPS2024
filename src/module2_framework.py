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


class FormalizingVariables(OODScene):
    def construct(self):
        self.title("Formalizing OOD", "Name the objects before optimizing")
        clinical = labeled_box("clinical note", 2.8, 0.75, BLUE_D, 20).shift(LEFT * 4.3 + UP * 0.65)
        model = labeled_box("h", 1.0, 0.7, GOLD, 28).shift(ORIGIN + UP * 0.65)
        label = labeled_box("diagnosis", 2.25, 0.75, GREEN_D, 20).shift(RIGHT * 4.2 + UP * 0.65)
        env = labeled_box("hospital / doctor", 2.65, 0.7, ORANGE, 19).shift(DOWN * 1.35)
        arrows = VGroup(
            Arrow(clinical.get_right(), model.get_left(), buff=0.1, color=BLUE_D),
            Arrow(model.get_right(), label.get_left(), buff=0.1, color=GREEN_D),
            Arrow(env.get_top(), clinical.get_bottom(), buff=0.12, color=ORANGE),
        )
        self.play(FadeIn(clinical), FadeIn(model), FadeIn(label), LaggedStart(*[GrowArrow(a) for a in arrows[:2]], lag_ratio=0.2), run_time=1.4)
        self.play(FadeIn(env, shift=UP * 0.12), GrowArrow(arrows[2]), run_time=0.9)

        symbols = VGroup(
            MathTex(r"X=\mathrm{input}", font_size=42, color=BLUE_D),
            MathTex(r"Y=\mathrm{label}", font_size=42, color=GREEN_D),
            MathTex(r"E=\mathrm{environment}", font_size=42, color=ORANGE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28).to_edge(RIGHT, buff=0.65).shift(DOWN * 0.55)
        targets = [clinical, label, env]
        for symbol, target in zip(symbols, targets):
            self.play(Write(symbol), Circumscribe(target, color=symbol.get_color()), run_time=0.85)
        sample = MathTex(r"(X,Y,E)", font_size=58, color=GOLD).to_edge(DOWN, buff=0.45)
        self.play(Write(sample), run_time=0.8)
        self.play(
            clinical.animate.set_stroke(width=5),
            label.animate.set_stroke(width=5),
            env.animate.set_stroke(width=5),
            Indicate(sample, color=GOLD),
            run_time=1.0,
        )
        self.wait(16.45)


class IDOODDistributions(OODScene):
    def construct(self):
        self.title("ID versus OOD", "The distribution changes")
        train = MathTex(r"(X,Y)\sim P_{\mathrm{train}}", font_size=48, color=BLUE_D).shift(LEFT * 3.05 + UP * 1.2)
        test = MathTex(r"(X,Y)\sim P_{\mathrm{test}}", font_size=48, color=GREEN_D).shift(RIGHT * 3.05 + UP * 1.2)
        neq = MathTex(r"P_{\mathrm{train}}\ne P_{\mathrm{test}}", font_size=58, color=RED).shift(DOWN * 1.95)
        self.play(Write(train), run_time=0.9)
        self.play(Write(test), run_time=0.9)

        ax_l = Axes(x_range=[-3, 3], y_range=[0, 1], x_length=4.0, y_length=2.0, axis_config={"include_ticks": False, "color": GRAY_B}).shift(LEFT * 3.05 + DOWN * 0.35)
        ax_r = ax_l.copy().shift(RIGHT * 6.1)
        curve_l = ax_l.plot(lambda x: math.exp(-x * x), color=BLUE_D)
        curve_r = ax_r.plot(lambda x: math.exp(-(x - 1.25) ** 2), color=GREEN_D)
        dot_l = Dot(ax_l.c2p(-2.4, 0.05), color=BLUE_D)
        dot_r = Dot(ax_r.c2p(-1.2, 0.05), color=GREEN_D)
        self.play(Create(ax_l), Create(ax_r), run_time=0.7)
        self.play(Create(curve_l), Create(curve_r), run_time=1.2)
        self.play(dot_l.animate.move_to(ax_l.c2p(0, 1.0)), dot_r.animate.move_to(ax_r.c2p(1.25, 1.0)), FadeIn(dot_l), FadeIn(dot_r), run_time=1.1)
        self.play(Write(neq), run_time=0.8)
        bridge = Arrow(train.get_bottom(), test.get_bottom(), color=RED, buff=0.25, stroke_width=5)
        self.play(GrowArrow(bridge), Indicate(neq, color=RED), run_time=1.0)
        self.play(curve_r.animate.shift(RIGHT * 0.35), dot_r.animate.shift(RIGHT * 0.35), Flash(test, color=GREEN_D), run_time=1.1)
        self.wait(14.4)


class EnvironmentFormalization(OODScene):
    def construct(self):
        self.title("Environment", "Each context has its own distribution")
        envs = VGroup(*[
            labeled_box(lbl, 2.0, 0.68, col, 18)
            for lbl, col in [("e1: snow", BLUE_D), ("e2: sand", YELLOW_D), ("e3: hospital", PURPLE)]
        ]).arrange(RIGHT, buff=0.55).shift(UP * 1.45)
        formula = MathTex(r"e\in\mathcal{E}", font_size=54, color=GOLD).to_edge(UP, buff=1.25)
        self.play(Write(formula), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(e, shift=DOWN * 0.1) for e in envs], lag_ratio=0.18), run_time=1.2)
        dists = VGroup()
        for env, col in zip(envs, [BLUE_D, YELLOW_D, PURPLE]):
            dist = MathTex(r"P^e(X,Y)", font_size=34, color=col).next_to(env, DOWN, buff=0.42)
            mini = VGroup(*[Dot(color=col, radius=0.055).shift(RIGHT * (i % 5) * 0.18 + UP * (i // 5) * 0.16) for i in range(15)]).next_to(dist, DOWN, buff=0.2)
            dists.add(VGroup(dist, mini))
        for dist in dists:
            self.play(Write(dist[0]), FadeIn(dist[1], scale=0.85), run_time=0.75)
        arrows = VGroup(*[Arrow(env.get_bottom(), dist[0].get_top(), buff=0.1, color=env[0].get_color()) for env, dist in zip(envs, dists)])
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.15), run_time=0.9)
        shared = Text("same task, different data-generating contexts", font_size=27, color=GRAY_B).to_edge(DOWN, buff=0.45)
        self.play(FadeIn(shared, shift=UP * 0.1), run_time=0.8)
        for dist in dists:
            self.play(Indicate(dist, color=GOLD), run_time=0.45)
        self.wait(14.1)


class DistributionSet(OODScene):
    def construct(self):
        self.title("Distribution Set", "OOD means robustness over a family")
        formula = MathTex(r"\mathcal{P}=\{p_1,p_2,p_3,\ldots\}", font_size=58, color=GOLD).shift(UP * 2.15)
        self.play(Write(formula), run_time=1.0)
        points = [LEFT * 3.9 + DOWN * 0.25, LEFT * 1.35 + UP * 0.05, RIGHT * 1.25 + DOWN * 0.35, RIGHT * 3.85 + UP * 0.15]
        blobs = VGroup()
        for i, (p, col) in enumerate(zip(points, [BLUE_D, GREEN_D, YELLOW_D, PURPLE]), start=1):
            ellipse = Ellipse(width=1.7, height=1.0, color=col).set_fill(col, 0.14).move_to(p)
            txt = MathTex(fr"p_{i}", font_size=34, color=col).move_to(ellipse)
            dots = dot_cloud(12, p + DOWN * 0.6, spread=(0.38, 0.18), color=col, seed=40 + i)
            blobs.add(VGroup(ellipse, txt, dots))
        self.play(LaggedStart(*[FadeIn(b, scale=0.88) for b in blobs], lag_ratio=0.16), run_time=1.5)
        hull = SurroundingRectangle(blobs, color=GOLD, buff=0.32, corner_radius=0.18)
        self.play(Create(hull), run_time=0.9)
        cursor = Dot(blobs[0][0].get_center(), color=WHITE, radius=0.08)
        path = VMobject().set_points_smoothly([b[0].get_center() for b in blobs])
        self.play(FadeIn(cursor), run_time=0.2)
        self.play(MoveAlongPath(cursor, path), run_time=2.2)
        note = Text("train on a few, deploy on another", font_size=30, color=RED, weight=BOLD).to_edge(DOWN, buff=0.42)
        test = labeled_box("unseen p_test", 2.2, 0.64, RED, 18).move_to(RIGHT * 4.7 + DOWN * 1.75)
        self.play(FadeIn(test, shift=LEFT * 0.1), GrowArrow(Arrow(hull.get_right(), test.get_left(), color=RED, buff=0.08)), run_time=1.0)
        self.play(FadeIn(note, shift=UP * 0.1), Flash(test, color=RED), run_time=0.9)
        self.wait(13.3)


class RiskAggregation(OODScene):
    def construct(self):
        self.title("Risk Aggregation", "ERM, DRO, and CVaR differ here")
        expected = MathTex(r"R(h)=\mathbb{E}[\ell(h(X),Y)]", font_size=46, color=WHITE).shift(UP * 2.0)
        avg = MathTex(r"\frac{1}{n}\sum_i \ell_i", font_size=42, color=BLUE_D).shift(LEFT * 4.1 + UP * 0.65)
        worst = MathTex(r"\max_e R^e(h)", font_size=42, color=RED).shift(ORIGIN + UP * 0.65)
        cvar = MathTex(r"\mathrm{CVaR}_\alpha", font_size=42, color=ORANGE).shift(RIGHT * 4.1 + UP * 0.65)
        self.play(Write(expected), run_time=0.9)
        self.play(LaggedStart(Write(avg), Write(worst), Write(cvar), lag_ratio=0.25), run_time=1.5)

        losses = [0.08, 0.14, 0.22, 0.31, 0.44, 0.58, 0.74, 0.91]
        cells = VGroup()
        for i, v in enumerate(losses):
            col = interpolate_color(GREEN_D, RED, v)
            sq = Square(side_length=0.46, color=col, stroke_width=2).set_fill(col, 0.72)
            txt = Text(f"{v:.2f}", font_size=14, color=WHITE).move_to(sq)
            cells.add(VGroup(sq, txt))
        cells.arrange(RIGHT, buff=0.08).shift(DOWN * 0.45)
        self.play(LaggedStart(*[FadeIn(c, scale=0.75) for c in cells], lag_ratio=0.08), run_time=1.2)
        mean_box = SurroundingRectangle(cells, color=BLUE_D, buff=0.12)
        max_box = SurroundingRectangle(cells[-1], color=RED, buff=0.08)
        tail_box = SurroundingRectangle(VGroup(cells[-3], cells[-2], cells[-1]), color=ORANGE, buff=0.1)
        labels = VGroup(
            Text("Mean: all losses", font_size=23, color=BLUE_D).next_to(avg, DOWN, buff=1.15),
            Text("Max: worst environment", font_size=23, color=RED).next_to(worst, DOWN, buff=1.15),
            Text("CVaR: average tail", font_size=23, color=ORANGE).next_to(cvar, DOWN, buff=1.15),
        )
        self.play(Create(mean_box), FadeIn(labels[0]), run_time=0.8)
        self.play(Transform(mean_box, max_box), FadeIn(labels[1]), Flash(cells[-1], color=RED), run_time=0.9)
        self.play(Transform(mean_box, tail_box), FadeIn(labels[2]), run_time=0.9)

        family = VGroup(
            labeled_box("ERM\nmean", 1.55, 0.7, BLUE_D, 17),
            labeled_box("Group DRO\nmax", 1.85, 0.7, RED, 17),
            labeled_box("CVaR-DRO\ntail", 1.85, 0.7, ORANGE, 17),
        ).arrange(RIGHT, buff=0.55).to_edge(DOWN, buff=0.35)
        self.play(LaggedStart(*[FadeIn(f, shift=UP * 0.1) for f in family], lag_ratio=0.18), run_time=1.1)
        for f in family:
            self.play(Indicate(f, color=GOLD), run_time=0.45)
        self.play(Circumscribe(VGroup(cells, family), color=GOLD), run_time=0.9)
        self.wait(9.64)


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
        self.wait(13.9)


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
        self.wait(13.27)


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
        self.wait(12.0)
