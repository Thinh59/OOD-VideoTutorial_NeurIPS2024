from manim import *
from common import *


class ERMAccuracyIllusion(OODScene):
    def construct(self):
        title = Text("High accuracy can hide a shortcut", font_size=36, color=WHITE, weight=BOLD).to_edge(UP, buff=0.35)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.8)

        plane, axes = make_axes_plane("background", "animal shape")
        plane.shift(DOWN * 0.25)
        snow = Rectangle(width=3.7, height=4.8, color=BLUE_E, stroke_width=0).set_fill(BLUE_E, 0.28).move_to(axes.c2p(2.0, 5.0))
        sand = Rectangle(width=3.7, height=4.8, color=YELLOW_E, stroke_width=0).set_fill(YELLOW_E, 0.24).move_to(axes.c2p(8.0, 5.0))
        self.play(FadeIn(snow), FadeIn(sand), Create(plane), run_time=1.2)
        self.wait(1.4)

        penguins = VGroup(*[
            simple_penguin().move_to(axes.c2p(1.45 + (i % 5) * 0.35, 6.6 + (i // 5) * 0.42))
            for i in range(10)
        ])
        camels = VGroup(*[
            simple_camel().move_to(axes.c2p(7.05 + (i % 5) * 0.36, 2.0 + (i // 5) * 0.42))
            for i in range(10)
        ])
        self.play(LaggedStart(*[FadeIn(p, scale=0.8) for p in penguins], lag_ratio=0.05), run_time=1.2)
        self.play(LaggedStart(*[FadeIn(c, scale=0.8) for c in camels], lag_ratio=0.05), run_time=1.2)
        self.wait(2.4)

        background_rule = Line(axes.c2p(5, 0.7), axes.c2p(5, 9.3), color=RED, stroke_width=7)
        shape_rule = Line(axes.c2p(0.8, 4.6), axes.c2p(9.4, 4.6), color=BLUE_D, stroke_width=4).set_opacity(0.4)
        meter = bar("Train", 0.98, GREEN_D).scale(0.9).to_corner(UR).shift(DOWN * 0.55)
        self.play(Create(shape_rule), run_time=0.7)
        
        # Scan background animation
        scan_line = Line(axes.c2p(0.2, 0.7), axes.c2p(0.2, 9.3), color=RED, stroke_width=4).set_opacity(0.7)
        self.play(FadeIn(scan_line), run_time=0.3)
        self.play(scan_line.animate.move_to(axes.c2p(9.8, 5.0)), run_time=1.0)
        self.play(FadeOut(scan_line), run_time=0.3)
        
        self.play(Create(background_rule), FadeIn(meter), run_time=1.0)
        self.play(Indicate(background_rule, color=RED), run_time=1.0)
        self.wait(3.0)

        desert_penguin = simple_penguin().move_to(axes.c2p(7.6, 7.0))
        ghost = desert_penguin.copy().set_opacity(0.25).move_to(axes.c2p(2.0, 7.0))
        self.play(FadeIn(ghost), run_time=0.5)
        self.play(Transform(ghost, desert_penguin), Flash(desert_penguin, color=GOLD), run_time=1.3)
        wrong_arrow = Arrow(desert_penguin.get_center() + RIGHT * 0.2, axes.c2p(7.7, 2.8), color=RED, stroke_width=7)
        camel_badge = simple_camel().move_to(axes.c2p(7.7, 2.1)).scale(1.15)
        cross = VGroup(
            Line(LEFT * 0.22 + DOWN * 0.22, RIGHT * 0.22 + UP * 0.22, color=RED, stroke_width=7),
            Line(LEFT * 0.22 + UP * 0.22, RIGHT * 0.22 + DOWN * 0.22, color=RED, stroke_width=7),
        ).move_to(camel_badge)
        self.play(GrowArrow(wrong_arrow), FadeIn(camel_badge, scale=0.8), FadeIn(cross), background_rule.animate.set_stroke(width=10), run_time=1.2)
        self.wait(3.6)

        verdict = Text("wrong feature", font_size=34, color=GOLD, weight=BOLD).to_corner(DL, buff=0.35)
        self.play(FadeIn(verdict, shift=UP), Circumscribe(background_rule, color=RED), run_time=1.2)
        bg_label = Text("background", font_size=24, color=RED).next_to(background_rule, RIGHT, buff=0.18)
        shape_label = Text("animal shape", font_size=24, color=BLUE_D).next_to(shape_rule, UP, buff=0.16)
        self.play(FadeIn(bg_label, shift=LEFT * 0.1), FadeIn(shape_label, shift=DOWN * 0.1), run_time=0.8)
        self.play(Indicate(bg_label, color=RED), background_rule.animate.set_stroke(width=11), run_time=0.9)
        self.play(Indicate(shape_label, color=BLUE_D), shape_rule.animate.set_opacity(0.25), run_time=0.9)
        self.play(Flash(cross, color=RED), run_time=0.7)
        self.wait(0.5)


class ERMAnatomy(OODScene):
    def construct(self):
        title = Text("ERM follows the easiest loss drop", font_size=36, color=WHITE, weight=BOLD).to_edge(UP, buff=0.35)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.8)

        formula = MathTex(r"\min_\theta\ \mathbb{E}_{P_{train}}\,[\ell]", font_size=48).next_to(title, DOWN, buff=0.35)
        train_box = SurroundingRectangle(formula, color=ORANGE, buff=0.15)
        self.play(Write(formula), Create(train_box), run_time=1.2)
        self.wait(2.4)

        inp = labeled_box("x", 1.0, 0.7, WHITE, 30).shift(LEFT * 5 + DOWN * 0.55)
        out = labeled_box("y", 1.0, 0.7, WHITE, 30).shift(RIGHT * 5 + DOWN * 0.55)
        core = CubicBezier(inp.get_right(), LEFT * 2.4 + UP * 1.1, RIGHT * 2.4 + UP * 1.1, out.get_left()).set_color(BLUE_D).set_stroke(width=6)
        spur = CubicBezier(inp.get_right(), LEFT * 1.3 + DOWN * 2.1, RIGHT * 1.3 + DOWN * 2.1, out.get_left()).set_color(RED).set_stroke(width=8)
        core_icon = VGroup(simple_penguin(), simple_camel()).arrange(RIGHT, buff=0.2).scale(0.75).next_to(core, UP, buff=0.25)
        spur_icon = VGroup(
            Square(0.32, color=BLUE_E).set_fill(BLUE_E, 0.8),
            Square(0.32, color=YELLOW_E).set_fill(YELLOW_E, 0.8),
        ).arrange(RIGHT, buff=0.18).next_to(spur, DOWN, buff=0.25)
        self.play(FadeIn(inp), FadeIn(out), Create(core), Create(spur), FadeIn(core_icon), FadeIn(spur_icon), run_time=1.5)
        self.wait(2.8)

        ball = Dot(inp.get_right(), color=WHITE, radius=0.1)
        self.play(FadeIn(ball), run_time=0.4)
        self.play(MoveAlongPath(ball, spur), spur.animate.set_stroke(width=11), core.animate.set_opacity(0.28), core_icon.animate.set_opacity(0.28), run_time=2.2)
        self.wait(2.8)

        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            x_length=4.4,
            y_length=3.0,
            axis_config={"color": GRAY_B, "include_ticks": False},
        ).shift(DOWN * 1.0)
        red_curve = axes.plot(lambda x: 4.2 * np.exp(-1.3 * x) + 0.35, x_range=[0, 4.5], color=RED)
        blue_curve = axes.plot(lambda x: 3.7 * np.exp(-0.42 * x) + 0.75, x_range=[0, 4.5], color=BLUE_D)
        red_dot = Dot(axes.c2p(0, 4.55), color=RED)
        blue_dot = Dot(axes.c2p(0, 4.45), color=BLUE_D)
        self.play(FadeOut(VGroup(inp, out, core, spur, core_icon, spur_icon, ball)), FadeIn(axes), Create(blue_curve), Create(red_curve), run_time=1.2)
        self.play(MoveAlongPath(red_dot, red_curve), FadeIn(red_dot), run_time=1.4)
        self.play(MoveAlongPath(blue_dot, blue_curve), FadeIn(blue_dot), run_time=2.4)
        self.wait(2.8)

        shortcut = Text("shortcut wins first", font_size=40, color=RED, weight=BOLD).to_edge(DOWN, buff=0.45)
        self.play(FadeIn(shortcut, shift=UP), Indicate(red_curve, color=RED), run_time=1.2)
        ticks = VGroup(*[
            Dot(axes.c2p(x, 4.2 * np.exp(-1.3 * x) + 0.35), color=RED, radius=0.045)
            for x in [0.8, 1.6, 2.4, 3.2, 4.0]
        ])
        slow_ticks = VGroup(*[
            Dot(axes.c2p(x, 3.7 * np.exp(-0.42 * x) + 0.75), color=BLUE_D, radius=0.045)
            for x in [0.8, 1.6, 2.4, 3.2, 4.0]
        ])
        self.play(LaggedStart(*[GrowFromCenter(t) for t in ticks], lag_ratio=0.12), run_time=0.9)
        self.play(LaggedStart(*[GrowFromCenter(t) for t in slow_ticks], lag_ratio=0.12), run_time=0.9)
        shortcut_box = SurroundingRectangle(shortcut, color=RED, buff=0.12)
        self.play(Create(shortcut_box), run_time=0.6)
        self.play(FadeOut(shortcut_box), red_curve.animate.set_stroke(width=7), run_time=0.7)
        self.wait(0.5)


class SpuriousDefinition(OODScene):
    def construct(self):
        title = Text("Spurious means unstable correlation", font_size=36, color=WHITE, weight=BOLD).to_edge(UP, buff=0.35)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.8)

        y = causal_node("Y", LEFT * 3.5 + UP * 0.9, BLUE_D)
        env = causal_node("Env", ORIGIN + UP * 0.9, GREEN_D)
        snow = causal_node("Snow", RIGHT * 3.5 + UP * 0.9, RED)
        penguin = simple_penguin().next_to(y, DOWN, buff=0.35)
        arctic = VGroup(
            Triangle(color=BLUE_E).set_fill(BLUE_E, 0.35),
            Line(LEFT * 0.5, RIGHT * 0.5, color=WHITE, stroke_width=4),
        ).arrange(DOWN, buff=-0.2).next_to(env, DOWN, buff=0.35)
        snowflake = VGroup(*[
            Line(LEFT * 0.28, RIGHT * 0.28, color=WHITE, stroke_width=3).rotate(a)
            for a in [0, PI / 3, 2 * PI / 3]
        ]).next_to(snow, DOWN, buff=0.48)
        self.play(FadeIn(y), FadeIn(env), FadeIn(snow), FadeIn(penguin), FadeIn(arctic), FadeIn(snowflake), run_time=1.2)
        true_1 = Arrow(y.get_right(), env.get_left(), color=BLUE_D, buff=0.1, stroke_width=5)
        true_2 = Arrow(env.get_right(), snow.get_left(), color=BLUE_D, buff=0.1, stroke_width=5)
        self.play(GrowArrow(true_1), GrowArrow(true_2), run_time=1.1)
        self.wait(3.2)

        model = labeled_box("AI", 1.1, 0.75, WHITE, 30).shift(DOWN * 1.9)
        backward = DashedLine(snow.get_bottom(), y.get_bottom(), color=RED, stroke_width=6).add_tip()
        self.play(FadeIn(model), Create(backward), true_1.animate.set_opacity(0.3), true_2.animate.set_opacity(0.3), run_time=1.2)
        self.play(Indicate(backward, color=RED), run_time=1.0)
        self.wait(3.4)

        desert = VGroup(
            Triangle(color=YELLOW_E).set_fill(YELLOW_E, 0.45),
            Line(LEFT * 0.55, RIGHT * 0.55, color=YELLOW_D, stroke_width=4),
        ).arrange(DOWN, buff=-0.2).move_to(arctic)
        sand = VGroup(*[
            Dot(radius=0.045, color=YELLOW_D).shift(RIGHT * (i * 0.22 - 0.44) + UP * ((i % 2) * 0.12))
            for i in range(5)
        ]).move_to(snowflake)
        self.play(ReplacementTransform(arctic, desert), ReplacementTransform(snowflake, sand), snow.animate.set_color(YELLOW_D), run_time=1.2)
        # Shattering arrow animation
        pieces = VGroup(*[
            Line(
                backward.point_from_proportion(i / 5),
                backward.point_from_proportion((i + 0.95) / 5),
                color=RED,
                stroke_width=6
            )
            for i in range(5)
        ])
        self.play(FadeOut(backward), FadeIn(pieces), run_time=0.1)
        self.play(
            LaggedStart(*[
                p.animate.shift(DOWN * 1.2 + RIGHT * random.uniform(-0.6, 0.6)).rotate(random.uniform(-PI/4, PI/4))
                for p in pieces
            ], lag_ratio=0.05),
            FadeOut(pieces, opacity=0),
            Flash(snow, color=ORANGE),
            run_time=1.1
        )
        self.wait(3.2)

        stable = Text("causal: stable", font_size=34, color=BLUE_D, weight=BOLD).shift(LEFT * 2.6 + DOWN * 2.65)
        brittle = Text("spurious: brittle", font_size=34, color=RED, weight=BOLD).shift(RIGHT * 2.6 + DOWN * 2.65)
        self.play(true_1.animate.set_opacity(1).set_stroke(width=8), true_2.animate.set_opacity(1).set_stroke(width=8), FadeIn(stable), FadeIn(brittle), run_time=1.2)
        self.play(Circumscribe(brittle, color=RED), run_time=1.0)
        for label, col in [("Beach", TEAL), ("Desert", YELLOW_D), ("Snow", BLUE_E)]:
            env_label = Text(label, font_size=24, color=col).move_to(env[1])
            crack = VGroup(*[Line(ORIGIN, RIGHT * 0.28, color=RED, stroke_width=4).rotate(a).move_to(snow) for a in [0, PI / 4, -PI / 4]])
            self.play(Transform(env[1], env_label), Create(crack), run_time=0.45)
            self.play(FadeOut(crack), Flash(snow, color=RED), run_time=0.35)
        self.play(Indicate(stable, color=BLUE_D), true_1.animate.set_stroke(width=9), true_2.animate.set_stroke(width=9), run_time=0.9)
        self.wait(5.0)


class GeometryInductiveBias(OODScene):
    def construct(self):
        self.title("Geometry & Inductive Bias", "SGD can prefer the shortcut margin")
        formula = MathTex(r"\mathbf{x}=y\mu^*+yz\mu_z+\xi", font_size=46).next_to(self.mobjects[0], DOWN, buff=0.25)
        self.play(Write(formula), run_time=1.0)
        plane, axes = make_axes_plane(r"\mu_z\ (spurious)", r"\mu^*\ (invariant)")
        plane.scale(0.9).shift(DOWN * 0.35)
        self.play(Create(plane), run_time=1.0)
        majority_a = dot_cloud(22, axes.c2p(2.3, 7.2), color=BLUE_D, seed=21)
        majority_b = dot_cloud(22, axes.c2p(7.2, 2.5), color=YELLOW_D, seed=22)
        minority_a = dot_cloud(5, axes.c2p(7.0, 7.0), color=BLUE_D, seed=23)
        minority_b = dot_cloud(5, axes.c2p(2.2, 2.2), color=YELLOW_D, seed=24)
        self.play(FadeIn(majority_a), FadeIn(majority_b), run_time=1.0)
        self.play(FadeIn(minority_a), FadeIn(minority_b), run_time=0.8)
        causal_line = Line(axes.c2p(0.7, 4.9), axes.c2p(9.4, 4.9), color=BLUE_D, stroke_width=4).set_opacity(0.45)
        shortcut_line = Line(axes.c2p(5.0, 0.6), axes.c2p(5.0, 9.4), color=RED, stroke_width=7)
        self.play(Create(causal_line), run_time=0.8)
        pull = VGroup(
            Arrow(axes.c2p(2.7, 6.7), axes.c2p(4.7, 5.6), color=RED, stroke_width=5),
            Arrow(axes.c2p(6.8, 3.0), axes.c2p(5.2, 4.4), color=RED, stroke_width=5),
        )
        self.play(LaggedStart(*[GrowArrow(a) for a in pull], lag_ratio=0.2), run_time=0.8)
        self.play(Create(shortcut_line), Indicate(majority_a, color=RED), Indicate(majority_b, color=RED), run_time=1.1)
        pierced = VGroup(SurroundingRectangle(minority_a, color=RED, buff=0.08), SurroundingRectangle(minority_b, color=RED, buff=0.08))
        self.play(Create(pierced[0]), Create(pierced[1]), run_time=0.8)
        note = Text("max-margin follows the majority geometry", font_size=28, color=GOLD).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.8)
        margin_band = VGroup(
            Line(axes.c2p(4.7, 0.6), axes.c2p(4.7, 9.4), color=RED, stroke_width=2),
            Line(axes.c2p(5.3, 0.6), axes.c2p(5.3, 9.4), color=RED, stroke_width=2),
        )
        self.play(Create(margin_band), run_time=0.8)
        self.play(shortcut_line.animate.rotate(-8 * DEGREES, about_point=axes.c2p(5, 5)), run_time=1.1)
        self.play(Indicate(minority_a, color=RED), Indicate(minority_b, color=RED), run_time=1.0)
        invariant = Text("invariant feature is present, but underused", font_size=25, color=BLUE_D).next_to(note, UP, buff=0.25)
        self.play(FadeIn(invariant, shift=UP * 0.1), Indicate(causal_line, color=BLUE_D), run_time=1.0)
        self.play(Circumscribe(formula, color=GOLD), run_time=0.8)
        parts = VGroup(
            Text("invariant signal", font_size=22, color=BLUE_D),
            Text("nuisance pull", font_size=22, color=RED),
            Text("noise", font_size=22, color=GRAY_B),
        ).arrange(RIGHT, buff=0.45).next_to(formula, DOWN, buff=0.18)
        self.play(LaggedStart(*[FadeIn(p, shift=UP * 0.08) for p in parts], lag_ratio=0.15), run_time=1.0)
        self.play(Indicate(parts[1], color=RED), shortcut_line.animate.set_stroke(width=9), run_time=1.0)
        self.play(Indicate(parts[0], color=BLUE_D), causal_line.animate.set_stroke(width=7).set_opacity(0.75), run_time=1.0)
        bad_margin = Text("minority groups lose margin", font_size=24, color=RED).next_to(pierced, RIGHT, buff=0.25)
        self.play(FadeIn(bad_margin, shift=LEFT * 0.1), run_time=0.8)
        self.play(Flash(pierced[0], color=RED), Flash(pierced[1], color=RED), run_time=0.9)
        self.play(Circumscribe(note, color=GOLD), run_time=0.8)
        self.wait(5.3)
