from manim import *
from common import *


class ImportanceWeightingInterpolation(OODScene):
    def construct(self):
        self.title("Importance Weighting", "Useful until interpolation takes over")
        formula = MathTex(r"w=\frac{p_{\mathrm{train}}(Y)}{p_{\mathrm{train}}(Y\mid Z)}", font_size=42).shift(UP * 2.0 + LEFT * 2.5)
        penalty = MathTex(r"\lambda\cdot \mathrm{penalty}", font_size=32, color=ORANGE).next_to(formula, RIGHT, buff=0.4)
        self.play(Write(formula), run_time=0.45)

        majority = VGroup(*[Dot(color=BLUE_D, radius=0.05).shift(LEFT * 4.8 + UP * 1.5 + RIGHT * (i % 6) * 0.22 + DOWN * (i // 6) * 0.18) for i in range(24)])
        minority = VGroup(*[Dot(color=RED, radius=0.06).shift(RIGHT * 3.0 + UP * 1.5 + RIGHT * (i % 3) * 0.25 + DOWN * (i // 3) * 0.2) for i in range(6)])
        maj_lab = Text("majority (w = 1)", font_size=18, color=BLUE_D).next_to(majority, DOWN, buff=0.12)
        min_lab = Text("minority (w >> 1)", font_size=18, color=RED).next_to(minority, DOWN, buff=0.12)

        self.play(FadeIn(majority), FadeIn(minority), FadeIn(maj_lab), FadeIn(min_lab), run_time=0.6)
        self.play(minority.animate.scale(1.5), Flash(minority, color=RED), run_time=0.6)
        self.wait(1.8) # beat pause

        # "But there's a problem..."
        self.play(Circumscribe(formula, color=RED), run_time=0.6)
        self.wait(1.2) # beat pause

        # "Modern networks easily interpolate..."
        net = VGroup(*[Circle(radius=0.14, color=GRAY_B).set_fill(GRAY_D, 0.35) for _ in range(12)]).arrange_in_grid(3, 4, buff=0.22).shift(LEFT * 3.8 + DOWN * 1.8)
        net_lab = Text("over-parameterized network", font_size=16, color=GRAY_B).next_to(net, DOWN, buff=0.12)
        self.play(FadeIn(net, shift=UP * 0.1), FadeIn(net_lab), run_time=0.5)

        memorized = VGroup(majority.copy(), minority.copy())
        memorized.generate_target()
        memorized.target.scale(0.18).move_to(net.get_center())
        self.play(MoveToTarget(memorized), Flash(net, color=GOLD), run_time=0.6)

        axes = Axes(x_range=[0, 4, 1], y_range=[0, 4, 1], x_length=3.0, y_length=1.4, axis_config={"color": GRAY_B, "include_ticks": False}).shift(RIGHT * 3.5 + DOWN * 1.8)
        axes_lab = Text("loss curve (interpolation)", font_size=16, color=GRAY_B).next_to(axes, DOWN, buff=0.12)
        curve = axes.plot(lambda x: 3.2 * np.exp(-1.5 * x), x_range=[0, 3.6], color=GOLD, stroke_width=4)
        zero_lbl = Text("loss = 0", font_size=16, color=GOLD).next_to(axes.c2p(3.2, 0), UP, buff=0.08)

        self.play(Create(axes), FadeIn(axes_lab), run_time=0.4)
        self.play(Create(curve), FadeIn(zero_lbl), run_time=0.5)
        self.wait(2.0)

        # "When loss is zero..."
        warning = Text("weighting is bypassed via memorization", font_size=20, color=RED, weight=BOLD).shift(DOWN * 0.1)
        memorization = Text("zero loss = zero gradient", font_size=20, color=GOLD).next_to(warning, DOWN, buff=0.12)
        self.play(FadeIn(warning, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(memorization, shift=UP * 0.1), run_time=0.5)
        self.play(LaggedStart(*[Flash(n, color=GOLD, line_length=0.15, num_lines=5) for n in net[:6]], lag_ratio=0.08), run_time=0.5)
        self.wait(2.2)

        # "The model simply memorizes..."
        bypass = VGroup(
            Arrow(majority.get_bottom(), net.get_top(), color=BLUE_D, buff=0.1, stroke_width=3),
            CurvedArrow(minority.get_bottom() + DOWN * 0.1, net.get_top() + RIGHT * 0.1, angle=-PI/4, color=RED, stroke_width=3),
        )
        self.play(GrowArrow(bypass[0]), Create(bypass[1]), run_time=0.5)
        self.play(Write(penalty), run_time=0.4)
        self.play(penalty.animate.shift(DOWN * 0.5).set_opacity(0.5), run_time=0.4)
        self.wait(1.0)
        self.active_wait(VGroup(formula, net, warning), 1.0, GOLD)
        self.wait(9.64)

class IRMInvariantIdea(OODScene):
    def construct(self):
        title = Text("One rule across environments", font_size=36, color=WHITE, weight=BOLD).to_edge(UP, buff=0.35)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.8)
        
        axes = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 10, 2],
            x_length=8,
            y_length=4.8,
            axis_config={"color": GRAY_B, "include_ticks": False},
        ).shift(DOWN * 0.2)
        self.play(Create(axes), run_time=1.0)

        clouds = VGroup(
            dot_cloud(18, axes.c2p(2.2, 7.2), color=GREEN_D, seed=10),
            dot_cloud(18, axes.c2p(5.2, 6.4), color=YELLOW_D, seed=11),
            dot_cloud(18, axes.c2p(8.0, 7.8), color=PURPLE, seed=12),
        )
        self.play(LaggedStart(*[FadeIn(c) for c in clouds], lag_ratio=0.15), run_time=1.0)
        self.wait(0.5)

        bad_lines = VGroup(
            Line(axes.c2p(3.1, 0.8), axes.c2p(3.1, 9.2), color=RED, stroke_width=5),
            Line(axes.c2p(5.1, 0.8), axes.c2p(5.1, 9.2), color=RED, stroke_width=5),
            Line(axes.c2p(7.0, 0.8), axes.c2p(7.0, 9.2), color=RED, stroke_width=5),
        )
        self.play(LaggedStart(*[Create(l) for l in bad_lines], lag_ratio=0.15), run_time=0.8)
        self.wait(14.4)
        good = Line(axes.c2p(0.6, 5.4), axes.c2p(9.5, 5.4), color=BLUE_D, stroke_width=7)
        self.play(ReplacementTransform(bad_lines, good), run_time=1.0)
        self.play(Circumscribe(good, color=BLUE_D), run_time=1.0)
        
        rep_space_text = Text("representation space", font_size=20, color=GRAY_B).move_to(LEFT * 4.6 + UP * 2.0)
        x_arrow = Arrow(axes.c2p(0.0, 0.0), axes.c2p(9.5, 0.0), color=RED, stroke_width=5, buff=0)
        y_arrow = Arrow(axes.c2p(0.0, 0.0), axes.c2p(0.0, 9.5), color=BLUE_D, stroke_width=5, buff=0)
        shortcut_lab = Text("shortcut direction", font_size=20, color=RED).next_to(x_arrow, DOWN, buff=0.15)
        invariant_lab = Text("invariant direction", font_size=20, color=BLUE_D).rotate(PI / 2).next_to(y_arrow, LEFT, buff=0.15)

        self.play(FadeIn(rep_space_text, shift=DOWN * 0.1), GrowArrow(x_arrow), GrowArrow(y_arrow), run_time=1.1)
        self.play(FadeIn(shortcut_lab), FadeIn(invariant_lab), run_time=0.8)
        
        proj_short = VGroup(*[
            DashedLine(dot.get_center(), axes.c2p(axes.p2c(dot.get_center())[0], 0.0), color=RED, stroke_width=2)
            for cloud in clouds for dot in cloud[:4]
        ])
        proj_inv = VGroup(*[
            DashedLine(dot.get_center(), axes.c2p(0.0, axes.p2c(dot.get_center())[1]), color=BLUE_D, stroke_width=2)
            for cloud in clouds for dot in cloud[4:8]
        ])
        self.play(LaggedStart(*[Create(p) for p in proj_short], lag_ratio=0.03), run_time=1.0)
        self.play(Indicate(shortcut_lab, color=RED), good.animate.set_opacity(0.35), run_time=0.8)
        self.play(LaggedStart(*[Create(p) for p in proj_inv], lag_ratio=0.03), run_time=1.0)
        self.play(good.animate.set_opacity(1).set_stroke(width=9), Indicate(invariant_lab, color=BLUE_D), run_time=0.9)
        shared_w = labeled_box("same w\nall envs", 1.65, 0.66, GOLD, 17).to_corner(DR, buff=0.35)
        env_tokens = VGroup(*[Text(f"e{i}", font_size=23, color=col) for i, col in enumerate([GREEN_D, YELLOW_D, PURPLE], start=1)]).arrange(RIGHT, buff=0.35).next_to(shared_w, UP, buff=0.22)
        self.play(FadeIn(shared_w, shift=UP * 0.1), FadeIn(env_tokens), run_time=0.6)
        self.play(LaggedStart(*[Indicate(t, color=t.get_color()) for t in env_tokens], lag_ratio=0.1), Circumscribe(shared_w, color=GOLD), run_time=0.8)
        self.active_wait(VGroup(clouds, good, shared_w, env_tokens), 1.0, GOLD)


class IRMFormula(OODScene):
    def construct(self):
        title = Text("IRM objective", font_size=36, color=WHITE, weight=BOLD).to_edge(UP, buff=0.35)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.35)
        full = MathTex(
            r"\min_{\Phi,w}\ \sum_{e\in\mathcal{E}} R^e(w\circ\Phi)",
            font_size=43,
            color=WHITE,
        ).shift(UP * 1.35)
        constraint = MathTex(
            r"\mathrm{s.t.}\quad w\in\arg\min_{\bar w} R^e(\bar w\circ\Phi)\quad \forall e",
            font_size=38,
            color=GOLD,
        ).next_to(full, DOWN, buff=0.42)
        self.play(Write(full), run_time=0.35)
        self.play(Circumscribe(full, color=BLUE_D), run_time=0.25)
        self.play(Write(constraint), run_time=0.35)
        self.play(Circumscribe(constraint, color=GOLD), run_time=0.25)

        hard = VGroup(
            labeled_box("outer:\nlearn Phi,w", 2.15, 0.75, BLUE_D, 17),
            labeled_box("inner:\nw optimal in e", 2.35, 0.75, ORANGE, 17),
            labeled_box("for all\nenvironments", 2.15, 0.75, PURPLE, 17),
        ).arrange(RIGHT, buff=0.55).shift(DOWN * 0.75)
        self.play(LaggedStart(*[FadeIn(h, scale=0.85, shift=UP * 0.1) for h in hard], lag_ratio=0.15), run_time=0.4)
        arrows_h = VGroup(
            Arrow(hard[0].get_right(), hard[1].get_left(), buff=0.1, color=GRAY_B),
            Arrow(hard[1].get_right(), hard[2].get_left(), buff=0.1, color=GRAY_B),
        )
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows_h], lag_ratio=0.15), run_time=0.25)
        self.play(Indicate(hard[1], color=ORANGE), Flash(constraint, color=GOLD), run_time=0.3)
        difficult = Text("bi-level constraint: hard to optimize directly", font_size=25, color=RED).to_edge(DOWN, buff=0.45)
        self.play(FadeIn(difficult, shift=UP * 0.1), run_time=0.25)
        self.play(Circumscribe(VGroup(hard, arrows_h), color=RED), run_time=0.4)

        envs = VGroup(*[
            Circle(radius=0.38, color=c, stroke_width=4).set_fill(c, 0.18)
            for c in [GREEN_D, YELLOW_D, PURPLE]
        ]).arrange(RIGHT, buff=1.0).shift(DOWN * 1.25)
        w = labeled_box("w", 0.9, 0.62, BLUE_D, 28).next_to(envs, DOWN, buff=0.45)
        arrows = VGroup(*[Arrow(e.get_bottom(), w.get_top(), color=e.get_color(), buff=0.08, stroke_width=5) for e in envs])
        
        # Shake/vibrate environments to show different contexts
        self.play(
            FadeOut(hard), FadeOut(arrows_h), FadeOut(difficult),
            FadeIn(envs, scale=0.8), FadeIn(w, scale=0.8),
            LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.18),
            run_time=0.5
        )
        self.play(
            envs[0].animate.shift(LEFT * 0.15),
            envs[1].animate.shift(UP * 0.1),
            envs[2].animate.shift(RIGHT * 0.15),
            run_time=0.25
        )
        self.play(
            envs[0].animate.shift(RIGHT * 0.15),
            envs[1].animate.shift(DOWN * 0.1),
            envs[2].animate.shift(LEFT * 0.15),
            run_time=0.25
        )
        self.play(Indicate(w, color=BLUE_D), run_time=0.35)

        relax = MathTex(r"\sum_e R^e(1\cdot\Phi)+\lambda\sum_e\left\|\nabla_{w\mid w=1}R^e(w\cdot\Phi)\right\|^2", font_size=33, color=ORANGE).to_edge(DOWN, buff=0.32)
        self.play(Transform(constraint, relax), run_time=0.45)
        self.play(LaggedStart(*[Indicate(e, color=e.get_color()) for e in envs], lag_ratio=0.15), run_time=0.35)
        
        # Animate the arrows pulsing
        for scale in [1.15, 0.85, 1.0]:
            self.play(*[a.animate.scale(scale, about_point=w.get_top()) for a in arrows], run_time=0.15)
            
        self.play(Circumscribe(relax, color=ORANGE), run_time=0.35)
        steps = VGroup(
            Text("constraint", font_size=22, color=GOLD),
            Text("hard", font_size=22, color=RED),
            Text("relax", font_size=22, color=ORANGE),
            Text("IRMv1", font_size=22, color=GREEN_D),
        ).arrange(RIGHT, buff=0.5).next_to(title, DOWN, buff=0.28)
        self.play(FadeIn(steps[0]), run_time=0.15)
        for s, target in [(steps[1], constraint), (steps[2], relax), (steps[3], w)]:
            self.play(FadeIn(s, shift=DOWN * 0.08), Indicate(target, color=s.get_color()), run_time=0.2)
            self.wait(0.2)
        self.active_wait(VGroup(full, relax, envs, w), 1.0, ORANGE)
        self.wait(13.66)


class IRMGradientVectors(OODScene):
    def construct(self):
        title = Text("Gradients should agree", font_size=36, color=WHITE, weight=BOLD).to_edge(UP, buff=0.35)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.8)
        
        center = LEFT * 3.0 + DOWN * 0.5
        base = Dot(center, color=WHITE, radius=0.08)
        arrows = VGroup(
            Arrow(center, center + LEFT * 1.8 + UP * 0.8, color=GREEN_D, stroke_width=6),
            Arrow(center, center + RIGHT * 1.6 + UP * 0.6, color=YELLOW_D, stroke_width=6),
            Arrow(center, center + UP * 1.8, color=PURPLE, stroke_width=6),
        )
        self.play(FadeIn(base), LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.2), run_time=1.2)
        
        # Dynamic rotation/wiggle of vectors to show disagreement
        self.play(
            arrows[0].animate.rotate(0.18, about_point=center),
            arrows[1].animate.rotate(-0.14, about_point=center),
            arrows[2].animate.rotate(0.08, about_point=center),
            run_time=1.0
        )
        self.play(
            arrows[0].animate.rotate(-0.22, about_point=center),
            arrows[1].animate.rotate(0.18, about_point=center),
            arrows[2].animate.rotate(-0.12, about_point=center),
            run_time=1.0
        )
        self.play(
            arrows[0].animate.rotate(0.04, about_point=center),
            arrows[1].animate.rotate(-0.04, about_point=center),
            arrows[2].animate.rotate(0.04, about_point=center),
            run_time=1.0
        )
        
        target = Arrow(center, center + UP * 2.0, color=BLUE_D, stroke_width=8)
        penalty = Text("gradient penalty", font_size=26, color=ORANGE).shift(RIGHT * 3.2 + UP * 1.2)
        self.play(FadeIn(penalty, shift=UP * 0.1), run_time=0.5)
        
        for scale in [0.8, 0.55, 0.28]:
            self.play(*[a.animate.become(Arrow(center, center + UP * 2.0 * scale, color=a.get_color(), stroke_width=6)) for a in arrows], run_time=0.65)
        self.play(*[a.animate.become(target.copy().set_color(a.get_color())) for a in arrows], run_time=0.9)
        self.play(Flash(target.get_end(), color=GOLD), Indicate(penalty, color=ORANGE), run_time=0.8)
        
        lambda_bar = NumberLine(x_range=[0, 10, 2], length=3.5, color=GRAY_B).shift(RIGHT * 3.2 + DOWN * 1.0)
        dot = Dot(lambda_bar.n2p(0), color=ORANGE)
        lam_lab = Text("lambda weighting", font_size=20, color=ORANGE).next_to(lambda_bar, UP, buff=0.15)
        
        self.play(FadeIn(lambda_bar), FadeIn(dot), FadeIn(lam_lab), run_time=0.7)
        self.play(dot.animate.move_to(lambda_bar.n2p(10)), *[a.animate.scale(0.35, about_point=center) for a in arrows], run_time=2.1)
        self.play(Flash(center + UP * 0.25, color=GOLD), run_time=0.5)
        
        self.active_wait(VGroup(arrows, penalty, lambda_bar, dot), 1.0, ORANGE)
        self.wait(0.2)

class IRMLimitations(OODScene):
    def construct(self):
        title = Text("IRM is not a silver bullet", font_size=36, color=WHITE, weight=BOLD).to_edge(UP, buff=0.35)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.8)
        
        gear = VGroup(
            Circle(radius=0.42, color=RED, stroke_width=4).set_fill(RED, 0.08),
            *[Line(ORIGIN, UP * 0.42, color=RED, stroke_width=3).rotate(i * PI / 4) for i in range(8)],
        )
        icons = VGroup(
            VGroup(Circle(radius=0.42, color=ORANGE).set_fill(ORANGE, 0.15), Text("E", font_size=30, color=ORANGE, weight=BOLD)),
            VGroup(gear, Text("opt", font_size=22, color=RED, weight=BOLD)),
            VGroup(Triangle(color=PURPLE).set_fill(PURPLE, 0.14).scale(0.55), Text("?", font_size=34, color=PURPLE, weight=BOLD)),
        ).arrange(RIGHT, buff=1.35).shift(UP * 0.5)
        
        for g in icons:
            g[1].move_to(g[0])
            
        labels = VGroup(
            Text("diverse envs", font_size=24, color=ORANGE),
            Text("sensitive", font_size=24, color=RED),
            Text("counterexamples", font_size=24, color=PURPLE),
        )
        for lab, icon in zip(labels, icons):
            lab.next_to(icon, DOWN, buff=0.35)
            
        self.play(LaggedStart(*[FadeIn(VGroup(i, l), scale=0.85) for i, l in zip(icons, labels)], lag_ratio=0.15), run_time=0.8)
        self.wait(0.5)
        self.play(Indicate(VGroup(icons[0], labels[0]), color=GOLD), run_time=0.9)
        self.play(Indicate(VGroup(icons[1], labels[1]), color=RED), run_time=0.9)
        self.play(Indicate(VGroup(icons[2], labels[2]), color=PURPLE), run_time=0.9)
        
        # Clear top icons to prevent overlapping with environments below
        self.play(FadeOut(VGroup(icons, labels)), run_time=0.5)
        
        same_envs = VGroup(
            labeled_box("env 1\nsame shortcut", 2.35, 0.82, ORANGE, 15),
            labeled_box("env 2\nsame shortcut", 2.35, 0.82, ORANGE, 15),
        ).arrange(RIGHT, buff=0.8).shift(UP * 0.2)
        
        self.play(FadeIn(same_envs[0], shift=UP * 0.1), FadeIn(same_envs[1], shift=UP * 0.1), run_time=0.8)
        
        arr1 = Arrow(same_envs[0].get_top(), same_envs[0].get_top() + UP * 0.75 + RIGHT * 0.4, color=RED, stroke_width=4)
        arr2 = Arrow(same_envs[1].get_top(), same_envs[1].get_top() + UP * 0.75 + RIGHT * 0.4, color=RED, stroke_width=4)
        self.play(GrowArrow(arr1), GrowArrow(arr2), run_time=0.8)
        self.play(Indicate(VGroup(arr1, arr2), color=RED), run_time=0.8)
        
        hidden = Text("no disagreement -> IRM cannot detect it", font_size=25, color=RED).next_to(same_envs, DOWN, buff=0.4)
        self.play(FadeIn(hidden, shift=UP * 0.1), run_time=0.8)
        self.play(Circumscribe(same_envs, color=RED), run_time=0.8)
        
        # Clear screen for final summary boxes
        self.play(FadeOut(VGroup(same_envs, hidden, arr1, arr2)), run_time=0.5)
        
        # Bring back icons and labels to show the complete picture
        self.play(FadeIn(icons), FadeIn(labels), run_time=0.5)
        
        failure_steps = VGroup(
            labeled_box("needs diverse E", 2.2, 0.65, ORANGE, 15),
            labeled_box("sensitive lambda", 2.2, 0.65, RED, 15),
            labeled_box("ERM can compete", 2.2, 0.65, PURPLE, 15),
        )
        for f, icon in zip(failure_steps, icons):
            f.next_to(icon, DOWN, buff=1.1)
            
        self.play(LaggedStart(*[FadeIn(f, shift=UP * 0.08) for f in failure_steps], lag_ratio=0.1), run_time=0.6)
        self.active_wait(VGroup(failure_steps, icons), 1.0, RED)
        self.wait(10.2)


class NuRD(OODScene):
    def construct(self):
        self.title("NuRD", "Nuisance-Randomized Distillation")
        
        # Composite input X showing a penguin and a red background patch (spurious attribute Z)
        x_box = RoundedRectangle(width=1.8, height=1.3, corner_radius=0.1, color=WHITE, stroke_width=2).set_fill(WHITE, opacity=0.05).shift(LEFT * 5.0 + UP * 0.3)
        x_label = Text("X (input image)", font_size=18, color=WHITE).next_to(x_box, UP, buff=0.1)
        penguin = simple_penguin().scale(0.55).move_to(x_box.get_center() + LEFT * 0.3)
        bg_patch = Rectangle(width=0.45, height=0.45, color=RED).set_fill(RED, 0.5).move_to(x_box.get_center() + RIGHT * 0.3)
        bg_label = Text("Z spurious", font_size=14, color=RED).next_to(bg_patch, UP, buff=0.05)
        x = VGroup(x_box, x_label, penguin, bg_patch, bg_label)
        
        phi = labeled_box("phi(X)\nfilter", 1.8, 0.9, BLUE_D, 20).shift(LEFT * 1.8 + UP * 0.3)
        clean = labeled_box("clean\nrepresentation", 2.2, 0.9, GREEN_D, 16).shift(RIGHT * 1.2 + UP * 0.3)
        w = labeled_box("w", 0.9, 0.72, GOLD, 24).shift(RIGHT * 3.7 + UP * 0.3)
        y = labeled_box("Y", 0.9, 0.72, GREEN_D, 24).shift(RIGHT * 5.2 + UP * 0.3)
        z = labeled_box("Z nuisance", 1.8, 0.65, RED, 16).shift(LEFT * 1.8 + DOWN * 1.7)
        
        arrows = VGroup(
            Arrow(x_box.get_right(), phi.get_left(), buff=0.1, color=GRAY_B),
            Arrow(phi.get_right(), clean.get_left(), buff=0.1, color=BLUE_D),
            Arrow(clean.get_right(), w.get_left(), buff=0.1, color=GREEN_D),
            Arrow(w.get_right(), y.get_left(), buff=0.1, color=GOLD),
            Arrow(phi.get_bottom(), z.get_top(), buff=0.08, color=RED),
        )
        
        self.play(FadeIn(x), FadeIn(phi), GrowArrow(arrows[0]), run_time=0.25)
        self.play(GrowArrow(arrows[4]), FadeIn(z, shift=DOWN * 0.1), run_time=0.25)
        
        z_cross = VGroup(
            Line(z.get_corner(UL), z.get_corner(DR), color=RED, stroke_width=5),
            Line(z.get_corner(DL), z.get_corner(UR), color=RED, stroke_width=5),
        )
        discard_label = Text("discarded", font_size=18, color=RED).next_to(z, DOWN, buff=0.12)
        
        self.play(Flash(z, color=RED), z.animate.set_opacity(0.3),
                  Create(z_cross), FadeIn(discard_label, shift=UP * 0.1), run_time=0.25)
        self.play(FadeIn(clean), GrowArrow(arrows[1]), run_time=0.25)
        self.play(FadeIn(w), GrowArrow(arrows[2]), FadeIn(y), GrowArrow(arrows[3]), run_time=0.3)
        
        condition = MathTex(r"Y\perp Z\mid \phi(X)", font_size=48, color=GOLD).shift(DOWN * 2.6)
        self.play(Write(condition), run_time=0.3)
        self.play(Circumscribe(condition, color=GOLD), run_time=0.3)
        
        # Sync with narration
        self.wait(1.8)
        
        random_z = VGroup(*[Text("Z", font_size=24, color=RED).move_to(phi).shift(UP * np.random.uniform(-0.3, 0.3) + RIGHT * np.random.uniform(-0.3, 0.3)) for _ in range(5)])
        self.play(LaggedStart(*[FadeIn(rz) for rz in random_z], lag_ratio=0.1), run_time=0.25)
        self.play(LaggedStart(*[rz.animate.move_to(phi.get_bottom() + DOWN * 0.3) for rz in random_z], lag_ratio=0.06), run_time=0.3)
        self.play(FadeOut(random_z, shift=DOWN * 0.2), Flash(phi, color=BLUE_D), run_time=0.25)
        self.play(Indicate(clean, color=GREEN_D), Indicate(y, color=GREEN_D), run_time=0.3)
        
        probe = labeled_box("probe for Z", 1.8, 0.65, RED, 16).next_to(clean, DOWN, buff=0.45)
        probe_arrow = Arrow(clean.get_bottom(), probe.get_top(), buff=0.08, color=RED)
        fail = Text("fails", font_size=24, color=RED, weight=BOLD).next_to(probe, RIGHT, buff=0.18)
        
        self.play(GrowArrow(probe_arrow), FadeIn(probe, shift=UP * 0.1), run_time=0.25)
        self.play(FadeIn(fail, scale=1.1), Flash(probe, color=RED), run_time=0.25)
        self.play(Indicate(condition, color=GOLD), run_time=0.3)
        
        clean_path = VGroup(arrows[1], arrows[2], arrows[3])
        self.play(clean_path.animate.set_stroke(width=7), run_time=0.25)
        self.play(Circumscribe(clean, color=GREEN_D), run_time=0.25)
        
        # FADE OUT the entire flow diagram and probes to clear the screen
        self.play(
            FadeOut(VGroup(x, phi, clean, w, y, z, arrows, z_cross, discard_label, condition, probe, probe_arrow, fail)),
            run_time=0.6
        )
        
        # Display the N1-N5 stages cleanly at the top half
        stages = VGroup(
            labeled_box("N1: Core\nIdea", 1.6, 0.85, BLUE_D, 14),
            labeled_box("N2: Semantic\nCorruption", 2.2, 0.85, ORANGE, 14),
            labeled_box("N3: Vision\nMasking", 1.9, 0.85, PURPLE, 14),
            labeled_box("N4: Nuisance\nDistill", 1.9, 0.85, GREEN_D, 14),
            labeled_box("N5: Mutual\nInfo", 1.9, 0.85, GOLD, 14),
        ).arrange(RIGHT, buff=0.2).shift(UP * 1.5)
        
        self.play(LaggedStart(*[FadeIn(s, shift=DOWN * 0.1) for s in stages], lag_ratio=0.12), run_time=0.5)
        
        # Create elements for details below the stages
        # N3 Details: Vision Masking (re-create x and slide a purple mask onto bg_patch)
        det_x_box = RoundedRectangle(width=1.6, height=1.1, corner_radius=0.08, color=WHITE, stroke_width=2).set_fill(WHITE, opacity=0.05).shift(LEFT * 4.0 + DOWN * 1.0)
        det_penguin = simple_penguin().scale(0.45).move_to(det_x_box.get_center() + LEFT * 0.25)
        det_bg = Rectangle(width=0.4, height=0.4, color=RED).set_fill(RED, 0.5).move_to(det_x_box.get_center() + RIGHT * 0.25)
        det_x = VGroup(det_x_box, det_penguin, det_bg)
        
        mask = VGroup(
            Rectangle(width=0.42, height=0.42, color=PURPLE).set_fill(PURPLE, 0.7),
            Text("mask", font_size=10, color=WHITE)
        ).move_to(det_x_box.get_center() + UP * 1.2 + LEFT * 0.2)
        
        # N4 Details: Distillation (teacher and student)
        teacher = labeled_box("teacher", 1.4, 0.55, GREEN_D, 15).shift(LEFT * 0.2 + DOWN * 1.0)
        student = labeled_box("student phi", 1.6, 0.55, BLUE_D, 15).next_to(teacher, RIGHT, buff=0.4)
        distill_arrow = Arrow(teacher.get_right(), student.get_left(), color=GREEN_D, buff=0.08)
        
        # N5 Details: Mutual Info
        mi = MathTex(r"\min I(\phi(X);Z)\quad \mathrm{keep}\quad I(\phi(X);Y)", font_size=30, color=GOLD).shift(RIGHT * 3.8 + DOWN * 1.0)
        
        self.play(Indicate(stages[1], color=ORANGE), run_time=0.4)
        
        # Show N3 Masking details
        self.play(FadeIn(det_x), FadeIn(mask), Indicate(stages[2], color=PURPLE), run_time=0.4)
        self.play(mask.animate.move_to(det_bg.get_center()), Flash(det_x_box, color=PURPLE), run_time=0.5)
        
        # Show N4 Distillation details
        self.play(FadeIn(teacher, shift=UP * 0.1), FadeIn(student, shift=UP * 0.1), GrowArrow(distill_arrow), Indicate(stages[3], color=GREEN_D), run_time=0.5)
        
        # Show N5 Mutual Info details
        self.play(Write(mi), Indicate(stages[4], color=GOLD), run_time=0.4)
        self.play(Circumscribe(mi, color=GOLD), run_time=0.3)
        
        self.active_wait(VGroup(stages, mask, teacher, student, mi), 1.0, GOLD)
        self.wait(1.0)
