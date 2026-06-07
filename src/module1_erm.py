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
        # Fix labels: bg_label anchored to bottom-right of axes area, shape_label to corner to avoid overlap
        bg_label = Text("background shortcut", font_size=18, color=RED).to_corner(UR, buff=0.55).shift(DOWN * 0.8)
        shape_label = Text("animal shape (causal)", font_size=18, color=BLUE_D).to_corner(UL, buff=0.55).shift(DOWN * 0.8)
        self.play(FadeIn(bg_label, shift=LEFT * 0.1), FadeIn(shape_label, shift=DOWN * 0.1), run_time=0.8)
        self.play(Indicate(bg_label, color=RED), background_rule.animate.set_stroke(width=11), run_time=0.9)
        self.play(Indicate(shape_label, color=BLUE_D), shape_rule.animate.set_opacity(0.25), run_time=0.9)
        self.play(Flash(cross, color=RED), run_time=0.7)
        # Motion fillers: cycle through key objects so audio stays in sync
        for _ in range(3):
            self.play(Indicate(bg_label, color=RED, scale_factor=1.08), run_time=0.6)
            self.play(Indicate(verdict, color=GOLD, scale_factor=1.06), run_time=0.6)
            self.play(Circumscribe(background_rule, color=RED), run_time=0.5)
            self.play(Indicate(shape_label, color=BLUE_D, scale_factor=1.08), run_time=0.5)
        self.wait(3.39)


class ERMAnatomy(OODScene):
    def construct(self):
        title = Text("ERM follows the easiest loss drop", font_size=36, color=WHITE, weight=BOLD).to_edge(UP, buff=0.35)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.8)

        formula = MathTex(r"\min_\theta\ \mathbb{E}_{P_{train}}\,[\ell]", font_size=48).next_to(title, DOWN, buff=0.35)
        train_box = SurroundingRectangle(formula, color=ORANGE, buff=0.15)
        self.play(Write(formula), Create(train_box), run_time=1.2)
        self.wait(2.4)
        self.play(FadeOut(formula), FadeOut(train_box), run_time=0.6)

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
        # Motion fillers: keep visual alive while audio explains gradient descent dynamics
        for _ in range(3):
            self.play(Indicate(red_curve, color=RED, scale_factor=1.05), run_time=0.6)
            self.play(Indicate(blue_curve, color=BLUE_D, scale_factor=1.05), run_time=0.5)
            self.play(Indicate(shortcut, color=RED), run_time=0.5)
        self.wait(4.4)


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
        self.wait(2.2)

        model = labeled_box("AI", 1.15, 0.75, WHITE, 30).shift(DOWN * 1.9)
        # Replaced DashedLine with CurvedArrow pointing from Snow to Y
        backward = CurvedArrow(snow.get_bottom() + DOWN * 0.15, y.get_bottom() + DOWN * 0.15, angle=-TAU / 5, color=RED, stroke_width=6)
        shortcut_label = Text("model reads arrow backward", font_size=22, color=RED).next_to(model, DOWN, buff=0.18)
        
        self.play(FadeIn(model), Create(backward), FadeIn(shortcut_label), true_1.animate.set_opacity(0.3), true_2.animate.set_opacity(0.3), run_time=1.2)
        self.play(Indicate(backward, color=RED), run_time=1.0)
        self.wait(2.0)

        # Environment shift animation (Arctic -> Desert)
        desert = VGroup(
            Triangle(color=YELLOW_E).set_fill(YELLOW_E, 0.45),
            Line(LEFT * 0.55, RIGHT * 0.55, color=YELLOW_D, stroke_width=4),
        ).arrange(DOWN, buff=-0.2).move_to(arctic)
        sand = VGroup(*[
            Dot(radius=0.045, color=YELLOW_D).shift(RIGHT * (i * 0.22 - 0.44) + UP * ((i % 2) * 0.12))
            for i in range(5)
        ]).move_to(snowflake)
        
        self.play(ReplacementTransform(arctic, desert), ReplacementTransform(snowflake, sand), snow.animate.set_color(YELLOW_D), run_time=1.2)
        
        # Break the shortcut arrow into pieces
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
            FadeOut(pieces),
            FadeOut(shortcut_label, shift=DOWN * 0.2),
            Flash(snow, color=ORANGE),
            run_time=1.1
        )
        self.wait(1.5)

        stable = Text("causal: stable", font_size=34, color=BLUE_D, weight=BOLD).shift(LEFT * 2.6 + DOWN * 2.65)
        brittle = Text("spurious: brittle", font_size=34, color=RED, weight=BOLD).shift(RIGHT * 2.6 + DOWN * 2.65)
        
        self.play(
            true_1.animate.set_opacity(1).set_stroke(width=8), 
            true_2.animate.set_opacity(1).set_stroke(width=8), 
            FadeIn(stable), 
            FadeIn(brittle), 
            run_time=1.2
        )
        self.play(Circumscribe(brittle, color=RED), run_time=1.0)
        self.wait(1.5)
        
        # Active environment shift sequences (Beach -> Desert -> Snow)
        for label, col in [("Beach", TEAL), ("Desert", YELLOW_D), ("Snow", BLUE_E)]:
            env_label = Text(label, font_size=24, color=col).move_to(env[1])
            crack = VGroup(*[
                Line(ORIGIN, RIGHT * 0.28, color=RED, stroke_width=4).rotate(a).move_to(snow) 
                for a in [0, PI / 4, -PI / 4]
            ])
            self.play(Transform(env[1], env_label), Create(crack), run_time=0.6)
            self.play(FadeOut(crack), Flash(snow, color=RED), run_time=0.4)
            self.wait(0.5)
            
        self.play(Indicate(stable, color=BLUE_D), true_1.animate.set_stroke(width=9), true_2.animate.set_stroke(width=9), run_time=0.9)
        self.wait(12.02)


class FormalizingXYE(OODScene):
    def construct(self):
        title = Text("Variables: X, Y, E", font_size=36, color=WHITE, weight=BOLD).to_edge(UP, buff=0.35)
        self.play(FadeIn(title, shift=DOWN*0.2), run_time=0.6)
        
        # Beat 1: X xuất hiện
        box_x = labeled_box("X: Input", 2.5, 0.75, BLUE_D, 22).shift(LEFT*3.5 + UP*0.5)
        icon_x = Text("🏥 clinical note / image", font_size=16, color=GRAY_B).next_to(box_x, DOWN, buff=0.12)
        self.play(FadeIn(box_x, shift=RIGHT*0.2), FadeIn(icon_x), run_time=0.8)
        self.wait(1.5)
        
        # Beat 2: Y xuất hiện  
        box_y = labeled_box("Y: Label", 2.5, 0.75, GREEN_D, 22).shift(RIGHT*3.5 + UP*0.5)
        icon_y = Text("✓ Diabetes / Arthritis", font_size=16, color=GRAY_B).next_to(box_y, DOWN, buff=0.12)
        self.play(FadeIn(box_y, shift=LEFT*0.2), FadeIn(icon_y), run_time=0.8)
        self.wait(1.5)
        
        # Beat 3: E xuất hiện (từ trên xuống, tỏa sáng)
        box_e = labeled_box("E: Environment", 3.2, 0.75, ORANGE, 22).shift(UP*2.5)
        icon_e = Text("Hospital A   |   Hospital B", font_size=16, color=GRAY_B).next_to(box_e, DOWN, buff=0.12)
        self.play(FadeIn(box_e, shift=DOWN*0.3), FadeIn(icon_e), run_time=0.8)
        self.play(Indicate(box_e, color=ORANGE, scale_factor=1.08), run_time=0.6)
        self.wait(1.5)
        
        # Beat 4: Mũi tên nối + triplet
        arr_ex = Arrow(box_e.get_bottom(), box_x.get_top(), color=ORANGE, buff=0.1, stroke_width=4)
        arr_ey = Arrow(box_e.get_bottom(), box_y.get_top(), color=ORANGE, buff=0.1, stroke_width=4)
        self.play(GrowArrow(arr_ex), GrowArrow(arr_ey), run_time=0.8)
        
        triplet = MathTex(r"D = \{(x_i, y_i, e_i)\}", font_size=52, color=GOLD).to_edge(DOWN, buff=0.45)
        self.play(Write(triplet), run_time=0.9)
        self.play(Circumscribe(triplet, color=GOLD), run_time=0.7)
        self.wait(1.0)
        
        # Motion fillers
        for _ in range(2):
            self.play(Indicate(box_x, color=BLUE_D), run_time=0.5)
            self.play(Indicate(box_y, color=GREEN_D), run_time=0.5)
            self.play(Indicate(box_e, color=ORANGE), run_time=0.5)
        self.active_wait(VGroup(box_x, box_y, box_e, triplet), 1.0, GOLD)


class OODShiftBreaks(OODScene):
    def construct(self):
        # Beat 1: Giả định cổ điển
        eq_text = MathTex(r"P_{\mathrm{train}} = P_{\mathrm{test}}", font_size=54, color=WHITE).shift(UP*1.2)
        assume_label = Text("Standard ML Assumption", font_size=22, color=GRAY_B).next_to(eq_text, DOWN, buff=0.2)
        self.play(Write(eq_text), FadeIn(assume_label), run_time=1.0)
        self.wait(1.8)
        
        # Beat 2: Đập vỡ dấu =
        neq = MathTex(r"P_{\mathrm{train}} \ne P_{\mathrm{test}}", font_size=54, color=RED).shift(UP*1.2)
        crack = Line(eq_text.get_left()+DOWN*0.5, eq_text.get_right()+UP*0.5, color=RED, stroke_width=6)
        ood_label = Text("OOD Shift", font_size=30, color=RED, weight=BOLD).next_to(eq_text, DOWN, buff=0.2)
        self.play(Create(crack), run_time=0.4)
        self.play(Transform(eq_text, neq), Transform(assume_label, ood_label), run_time=0.6)
        self.play(Flash(eq_text.get_center(), color=RED, num_lines=8), run_time=0.5)
        self.wait(1.0)
        
        # Beat 3: 2 đám mây phân phối
        ax_l = Axes(x_range=[-3,3], y_range=[0,1], x_length=3.5, y_length=1.8,
                    axis_config={"include_ticks": False, "color": GRAY_B}).shift(LEFT*3.2 + DOWN*1.0)
        ax_r = ax_l.copy().shift(RIGHT*6.4)
        curve_l = ax_l.plot(lambda x: math.exp(-x*x), color=BLUE_D, stroke_width=4)
        curve_r = ax_r.plot(lambda x: math.exp(-0.4*(x-1.5)**2)*0.7, color=GREEN_D, stroke_width=4)
        lab_l = Text("P_e1\n(Hospital A)", font_size=17, color=BLUE_D).next_to(ax_l, DOWN, buff=0.1)
        lab_r = Text("P_e2\n(Hospital B)", font_size=17, color=GREEN_D).next_to(ax_r, DOWN, buff=0.1)
        self.play(Create(ax_l), Create(ax_r), run_time=0.6)
        self.play(Create(curve_l), Create(curve_r), FadeIn(lab_l), FadeIn(lab_r), run_time=1.0)
        self.play(Indicate(curve_r, color=GREEN_D), run_time=0.7)
        
        # Motion fillers
        for _ in range(3):
            self.play(Indicate(eq_text, color=RED), run_time=0.6)
            self.play(Indicate(curve_r, color=GREEN_D), run_time=0.6)
        self.active_wait(VGroup(eq_text, curve_l, curve_r), 1.0, RED)


class DistributionSetFamily(OODScene):
    def construct(self):
        title = Text("Distribution Set", font_size=36, color=WHITE, weight=BOLD).to_edge(UP, buff=0.35)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.8)

        formula = MathTex(r"\mathcal{P}=\{p_1,p_2,p_3,\ldots\}", font_size=58, color=GOLD).shift(UP * 1.8)
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
        self.wait(1.0)
        
        note = Text("train on a few, deploy on another", font_size=30, color=RED, weight=BOLD).to_edge(DOWN, buff=0.42)
        test = labeled_box("unseen p_test", 2.2, 0.64, RED, 18).move_to(RIGHT * 4.7 + DOWN * 1.75)
        self.play(FadeIn(test, shift=LEFT * 0.1), GrowArrow(Arrow(hull.get_right(), test.get_left(), color=RED, buff=0.08)), run_time=1.0)
        self.play(FadeIn(note, shift=UP * 0.1), Flash(test, color=RED), run_time=0.9)
        
        stability = Text("STABILITY", font_size=40, color=GOLD, weight=BOLD).move_to(ORIGIN)
        cover = Rectangle(width=14, height=8, color=BLACK, stroke_width=0).set_fill(BLACK, 0.8)
        self.play(FadeIn(cover), FadeIn(stability, scale=1.5), run_time=1.0)
        self.play(Flash(stability.get_center(), color=GOLD, num_lines=12, line_length=0.4), run_time=0.8)
        
        for _ in range(3):
            self.play(Indicate(stability, color=GOLD, scale_factor=1.08), run_time=0.6)
            self.play(Flash(stability.get_center(), color=GOLD, num_lines=8, line_length=0.3), run_time=0.5)
        self.active_wait(VGroup(stability), 1.0, GOLD)


class GeometryInductiveBias(OODScene):
    def construct(self):
        title = self.title("Geometry & Inductive Bias", "SGD can prefer the shortcut margin")
        formula = MathTex(r"\mathbf{x}=y\mu^*+yz\mu_z+\xi", font_size=46).next_to(title, DOWN, buff=0.25)
        self.play(Write(formula), run_time=0.6)
        
        plane, axes = make_axes_plane(r"\mu_z\ (spurious)", r"\mu^*\ (invariant)")
        plane.scale(0.9).shift(DOWN * 0.35)
        self.play(Create(plane), run_time=0.6)
        
        majority_a = dot_cloud(22, axes.c2p(2.3, 7.2), color=BLUE_D, seed=21)
        majority_b = dot_cloud(22, axes.c2p(7.2, 2.5), color=YELLOW_D, seed=22)
        minority_a = dot_cloud(5, axes.c2p(7.0, 7.0), color=BLUE_D, seed=23)
        minority_b = dot_cloud(5, axes.c2p(2.2, 2.2), color=YELLOW_D, seed=24)
        
        self.play(FadeIn(majority_a), FadeIn(majority_b), run_time=0.6)
        self.play(FadeIn(minority_a), FadeIn(minority_b), run_time=0.5)
        
        causal_line = Line(axes.c2p(0.7, 4.9), axes.c2p(9.4, 4.9), color=BLUE_D, stroke_width=4).set_opacity(0.45)
        shortcut_line = Line(axes.c2p(5.0, 0.6), axes.c2p(5.0, 9.4), color=RED, stroke_width=7)
        self.play(Create(causal_line), run_time=0.5)
        
        pull = VGroup(
            Arrow(axes.c2p(2.7, 6.7), axes.c2p(4.7, 5.6), color=RED, stroke_width=5),
            Arrow(axes.c2p(6.8, 3.0), axes.c2p(5.2, 4.4), color=RED, stroke_width=5),
        )
        self.play(LaggedStart(*[GrowArrow(a) for a in pull], lag_ratio=0.1), run_time=0.5)
        self.play(Create(shortcut_line), Indicate(majority_a, color=RED), Indicate(majority_b, color=RED), run_time=0.7)
        
        pierced = VGroup(SurroundingRectangle(minority_a, color=RED, buff=0.08), SurroundingRectangle(minority_b, color=RED, buff=0.08))
        self.play(Create(pierced[0]), Create(pierced[1]), run_time=0.5)
        
        note = Text("max-margin follows majority geometry", font_size=26, color=GOLD).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.5)
        
        margin_band = VGroup(
            Line(axes.c2p(4.7, 0.6), axes.c2p(4.7, 9.4), color=RED, stroke_width=2),
            Line(axes.c2p(5.3, 0.6), axes.c2p(5.3, 9.4), color=RED, stroke_width=2),
        )
        self.play(Create(margin_band), run_time=0.5)
        self.play(shortcut_line.animate.rotate(-8 * DEGREES, about_point=axes.c2p(5, 5)), run_time=0.7)
        self.play(Indicate(minority_a, color=RED), Indicate(minority_b, color=RED), run_time=0.6)
        
        invariant = Text("invariant is present, but underused", font_size=23, color=BLUE_D).next_to(note, UP, buff=0.25)
        self.play(FadeIn(invariant, shift=UP * 0.1), Indicate(causal_line, color=BLUE_D), run_time=0.6)
        self.play(Circumscribe(formula, color=GOLD), run_time=0.5)
        
        parts = VGroup(
            Text("invariant signal", font_size=22, color=BLUE_D),
            Text("nuisance pull", font_size=22, color=RED),
            Text("noise", font_size=22, color=GRAY_B),
        ).arrange(RIGHT, buff=0.45).next_to(formula, DOWN, buff=0.18)
        
        self.play(LaggedStart(*[FadeIn(p, shift=UP * 0.08) for p in parts], lag_ratio=0.1), run_time=0.6)
        self.play(Indicate(parts[1], color=RED), shortcut_line.animate.set_stroke(width=9), run_time=0.6)
        self.play(Indicate(parts[0], color=BLUE_D), causal_line.animate.set_stroke(width=7).set_opacity(0.75), run_time=0.6)
        
        bad_margin = Text("minority groups lose margin", font_size=22, color=RED).next_to(pierced, RIGHT, buff=0.25)
        self.play(FadeIn(bad_margin, shift=LEFT * 0.1), run_time=0.5)
        self.play(Flash(pierced[0], color=RED), Flash(pierced[1], color=RED), run_time=0.6)
        self.play(Circumscribe(note, color=GOLD), run_time=0.5)
        self.wait(0.5)
        
        # ── Scene 2 Transition: Fade out Scene 1 Clutter
        self.play(
            FadeOut(VGroup(title, formula, note, plane, axes, majority_a, majority_b, minority_a, minority_b, causal_line, shortcut_line, pull, pierced, margin_band, bad_margin, invariant, parts)),
            run_time=0.6
        )
        
        # Average Loss Objective Breakdown
        eq_title = Text("ERM Objective: Average Loss", font_size=24, color=WHITE).shift(UP * 2.1)
        eq = MathTex(
            r"L_{avg} = 0.95 \cdot L_{majority} + 0.05 \cdot L_{minority}",
            font_size=34,
            color=WHITE
        ).next_to(eq_title, DOWN, buff=0.25)
        
        self.play(FadeIn(eq_title), Write(eq), run_time=0.6)
        self.wait(0.5)
        
        # Draw the cards for losses shifted down
        maj_card = VGroup(
            Text("Majority Loss (95% data)", font_size=18, color=GRAY_B),
            MathTex(r"L_{majority} = 0.01", font_size=22, color=GREEN_D),
            bar("L_maj", 0.05, GREEN_D, width=2.2).scale(0.7)
        ).arrange(DOWN, buff=0.12).shift(LEFT * 3.3 + DOWN * 0.9)
        
        min_card = VGroup(
            Text("Minority Loss (5% data)", font_size=18, color=GRAY_B),
            MathTex(r"L_{minority} = 0.80", font_size=22, color=RED),
            bar("L_min", 0.80, RED, width=2.2).scale(0.7)
        ).arrange(DOWN, buff=0.12).shift(RIGHT * 3.3 + DOWN * 0.9)
        
        self.play(FadeIn(maj_card), run_time=0.5)
        self.play(Flash(maj_card[1], color=GREEN_D), run_time=0.4)
        self.play(FadeIn(min_card), run_time=0.5)
        self.play(Flash(min_card[1], color=RED), run_time=0.4)
        self.wait(0.5)
        
        # Calculation and result
        eq_calc = MathTex(
            r"L_{avg} = 0.95 \cdot (0.01) + 0.05 \cdot (0.80) = 0.0495",
            font_size=34,
            color=GOLD
        ).move_to(eq.get_center())
        
        self.play(Transform(eq, eq_calc), run_time=0.8)
        self.play(Indicate(eq, color=GOLD), run_time=0.5)
        
        illusion_lbl = Text("Average loss is low, hiding minority failure!", font_size=22, color=GOLD).to_edge(DOWN, buff=0.4)
        self.play(FadeIn(illusion_lbl, shift=DOWN * 0.1), run_time=0.5)
        self.wait(0.5)
        
        # ── Scene 3 Transition: Decision Boundary & Simplicity Bias
        self.play(FadeOut(VGroup(eq_title, eq, maj_card, min_card, illusion_lbl)), run_time=0.6)
        
        margin_title = Text("Simplicity Bias & Insufficient Margin", font_size=24, color=WHITE).shift(UP * 2.1)
        self.play(FadeIn(margin_title), run_time=0.5)
        
        # Line, decision boundary and sample points shifted down to DOWN * 1.2
        line_f = Line(LEFT * 4.5 + DOWN * 1.2, RIGHT * 4.5 + DOWN * 1.2, color=GRAY_B, stroke_width=3)
        boundary_f = Line(DOWN * 2.0, UP * 0.0, color=GOLD, stroke_width=6).move_to(DOWN * 1.2)
        boundary_lbl = Text("Decision Boundary", font_size=18, color=GOLD).next_to(boundary_f, UP, buff=0.15)
        
        self.play(Create(line_f), Create(boundary_f), FadeIn(boundary_lbl), run_time=0.6)
        
        dot_maj = Dot(RIGHT * 2.8 + DOWN * 1.2, color=GREEN_D, radius=0.12)
        maj_lbl = Text("Majority (Easy feature)", font_size=16, color=GREEN_D).next_to(dot_maj, DOWN, buff=0.15)
        
        dot_min = Dot(LEFT * 1.8 + DOWN * 1.2, color=RED, radius=0.12)
        min_lbl = Text("Minority (Conflict)", font_size=16, color=RED).next_to(dot_min, DOWN, buff=0.15)
        
        self.play(FadeIn(dot_maj), FadeIn(maj_lbl), run_time=0.5)
        self.play(Flash(dot_maj, color=GREEN_D), run_time=0.4)
        self.play(FadeIn(dot_min), FadeIn(min_lbl), run_time=0.5)
        self.play(Flash(dot_min, color=RED), run_time=0.4)
        self.wait(0.5)
        
        # Insufficient Margin double arrow
        margin_arrow = DoubleArrow(boundary_f.get_center(), dot_min.get_center(), buff=0.05, color=RED, stroke_width=3)
        margin_arrow_lbl = Text("insufficient margin", font_size=16, color=RED).next_to(margin_arrow, UP, buff=0.1)
        self.play(GrowArrow(margin_arrow), FadeIn(margin_arrow_lbl), run_time=0.5)
        self.wait(0.5)
        
        # Conclusion
        conclusion_f = Text("Intervene in objective function", font_size=24, color=GOLD, weight=BOLD).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(conclusion_f, shift=UP * 0.1), run_time=0.5)
        self.play(Circumscribe(conclusion_f, color=GOLD), run_time=0.5)
        # Motion fillers: keep visual alive while audio explains geometric skew
        for _ in range(4):
            self.play(Indicate(dot_maj, color=GREEN_D, scale_factor=1.2), run_time=0.5)
            self.play(Indicate(dot_min, color=RED, scale_factor=1.2), run_time=0.5)
            self.play(Indicate(boundary_f, color=GOLD), run_time=0.4)
            self.play(Indicate(conclusion_f, color=GOLD), run_time=0.4)
        self.wait(5.18)


class GeometricSkewMaxMargin(OODScene):
    def construct(self):
        title = Text("Geometric Skew & Max-Margin", font_size=36, color=WHITE, weight=BOLD).to_edge(UP, buff=0.35)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.8)
        
        # 2D plane
        plane, axes = make_axes_plane(r"\phi^*\ (invariant)", r"\psi^*\ (spurious)")
        plane.scale(0.8).shift(DOWN * 0.3)
        self.play(Create(plane), run_time=1.0)
        
        # Cụm điểm majority (lớn, góc 45 độ)
        majority = dot_cloud(30, axes.c2p(5.0, 5.0), spread=(1.5, 1.5), color=GREEN_D, seed=1)
        maj_lbl = Text("Majority", font_size=20, color=GREEN_D, weight=BOLD).next_to(majority, UP)
        
        # Cụm điểm minority (nhỏ)
        minority = dot_cloud(5, axes.c2p(2.0, -2.0), spread=(0.5, 0.5), color=ORANGE, seed=2)
        min_lbl = Text("Minority", font_size=20, color=ORANGE, weight=BOLD).next_to(minority, DOWN)
        
        self.play(FadeIn(majority), FadeIn(maj_lbl), run_time=0.8)
        self.play(FadeIn(minority), FadeIn(min_lbl), run_time=0.8)
        self.wait(1.5)
        
        # Ranh giới ban đầu
        boundary = Line(axes.c2p(-3, 6), axes.c2p(6, -3), color=GRAY_B, stroke_width=4)
        boundary_lbl = Text("Ideal Boundary", font_size=18, color=GRAY_B).next_to(boundary.get_end(), RIGHT)
        self.play(Create(boundary), FadeIn(boundary_lbl), run_time=0.8)
        self.wait(1.0)
        
        # Ranh giới bị hút về majority
        skewed_boundary = Line(axes.c2p(-2, 7), axes.c2p(7, 2), color=RED, stroke_width=6)
        skewed_lbl = Text("Skewed by SGD", font_size=18, color=RED, weight=BOLD).next_to(skewed_boundary.get_end(), RIGHT)
        
        self.play(
            Transform(boundary, skewed_boundary),
            Transform(boundary_lbl, skewed_lbl),
            run_time=1.2
        )
        self.play(Flash(boundary, color=RED), run_time=0.6)
        
        # Các điểm minority bị đâm xuyên đổi màu đỏ
        cross_anim = []
        for dot in minority:
            cross_anim.append(dot.animate.set_color(RED))
        self.play(*cross_anim, run_time=0.8)
        
        # Kết luận
        conclusion = Text("Max-margin bias hurts minority groups!", font_size=26, color=GOLD, weight=BOLD).to_edge(DOWN, buff=0.3)
        self.play(FadeIn(conclusion, shift=UP * 0.1), run_time=0.8)
        
        # Motion fillers
        for _ in range(3):
            self.play(Indicate(boundary, color=RED), run_time=0.6)
            self.play(Circumscribe(minority, color=RED), run_time=0.6)
            self.play(Indicate(conclusion, color=GOLD), run_time=0.5)
        
        self.active_wait(VGroup(boundary, minority, conclusion), 1.0, GOLD)
