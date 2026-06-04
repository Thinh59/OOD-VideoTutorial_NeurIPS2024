from manim import *
from common import *


class ImportanceWeightingInterpolation(OODScene):
    def construct(self):
        self.title("Importance Weighting", "Useful until interpolation takes over")
        formula = MathTex(r"w=\frac{p_{train}(Y)}{p_{train}(Y\mid Z)}", font_size=58).shift(UP * 1.55)
        self.play(Write(formula), run_time=1.0)
        majority = VGroup(*[Dot(color=BLUE_D, radius=0.06).shift(LEFT * 3.2 + RIGHT * (i % 6) * 0.28 + DOWN * (i // 6) * 0.22) for i in range(24)])
        minority = VGroup(*[Dot(color=RED, radius=0.08).shift(RIGHT * 1.7 + RIGHT * (i % 3) * 0.32 + DOWN * (i // 3) * 0.25) for i in range(6)])
        maj_lab = Text("majority", font_size=22, color=BLUE_D).next_to(majority, DOWN)
        min_lab = Text("minority gets larger weight", font_size=22, color=RED).next_to(minority, DOWN)
        self.play(FadeIn(majority), FadeIn(minority), FadeIn(maj_lab), run_time=1.0)
        weight_tags = VGroup(
            Text("w = 1", font_size=22, color=BLUE_D).next_to(majority, UP, buff=0.18),
            Text("w >> 1", font_size=26, color=RED, weight=BOLD).next_to(minority, UP, buff=0.18),
        )
        self.play(FadeIn(weight_tags[0], shift=DOWN * 0.1), run_time=0.6)
        self.play(minority.animate.scale(1.7), FadeIn(min_lab), FadeIn(weight_tags[1], scale=1.1), run_time=1.0)
        self.play(Flash(minority, color=RED), run_time=0.8)
        net = VGroup(*[Circle(radius=0.18, color=GRAY_B).set_fill(GRAY_D, 0.35) for _ in range(18)]).arrange_in_grid(3, 6, buff=0.28).to_edge(DOWN, buff=0.55)
        self.play(FadeIn(net, shift=UP * 0.1), run_time=0.8)
        memorized = VGroup(majority.copy(), minority.copy())
        memorized.generate_target()
        memorized.target.scale(0.2).move_to(net.get_center())
        self.play(MoveToTarget(memorized), Flash(net, color=GOLD), run_time=1.2)
        loss = Text("over-parameterized net: train loss = 0", font_size=30, color=GOLD, weight=BOLD).next_to(net, UP, buff=0.25)
        self.play(FadeIn(loss, shift=UP * 0.1), run_time=0.8)
        axes = Axes(x_range=[0, 4, 1], y_range=[0, 4, 1], x_length=3.3, y_length=1.7, axis_config={"color": GRAY_B, "include_ticks": False}).shift(RIGHT * 3.6 + DOWN * 0.35)
        curve = axes.plot(lambda x: 3.5 * np.exp(-1.25 * x), x_range=[0, 3.6], color=GOLD, stroke_width=5)
        zero = Text("0", font_size=22, color=GOLD).next_to(axes.c2p(3.6, 0), RIGHT, buff=0.12)
        self.play(Create(axes), run_time=0.7)
        self.play(Create(curve), FadeIn(zero), run_time=1.2)
        bypass = VGroup(
            Arrow(minority.get_bottom(), net.get_top(), color=RED, buff=0.12, stroke_width=5),
            Arrow(majority.get_bottom(), net.get_top(), color=BLUE_D, buff=0.12, stroke_width=4),
        )
        self.play(LaggedStart(*[GrowArrow(a) for a in bypass], lag_ratio=0.15), run_time=1.0)
        warning = Text("weighting and penalties can be bypassed", font_size=28, color=RED).to_edge(DOWN, buff=0.2)
        self.play(FadeIn(warning, shift=UP * 0.1), Circumscribe(formula, color=RED), run_time=1.0)
        self.play(Indicate(loss, color=GOLD), run_time=0.8)
        penalty = MathTex(r"\lambda\cdot penalty", font_size=36, color=ORANGE).next_to(formula, DOWN, buff=0.28)
        self.play(Write(penalty), run_time=0.8)
        self.play(penalty.animate.shift(DOWN * 1.2).set_opacity(0.45), loss.animate.set_color(RED), run_time=1.0)
        memorization = Text("memorization satisfies every weighted example", font_size=24, color=GOLD).next_to(net, DOWN, buff=0.18)
        self.play(FadeIn(memorization, shift=UP * 0.1), run_time=0.8)
        self.play(LaggedStart(*[Flash(n, color=GOLD, line_length=0.15, num_lines=5) for n in net[:6]], lag_ratio=0.08), run_time=1.2)
        self.play(Circumscribe(warning, color=RED), run_time=0.9)
        side_note = VGroup(
            Text("weighted loss", font_size=22, color=ORANGE),
            Text("penalty loss", font_size=22, color=RED),
            Text("both become zero on train", font_size=22, color=GOLD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).to_corner(DR, buff=0.35)
        self.play(FadeIn(side_note[0], shift=LEFT * 0.1), run_time=0.7)
        self.play(FadeIn(side_note[1], shift=LEFT * 0.1), run_time=0.7)
        self.play(FadeIn(side_note[2], shift=LEFT * 0.1), Flash(curve, color=GOLD), run_time=0.9)
        self.play(LaggedStart(*[Indicate(s, color=GOLD) for s in side_note], lag_ratio=0.15), run_time=1.4)
        self.play(Circumscribe(net, color=GOLD), run_time=0.9)
        self.wait(5.0)


class IRMInvariantIdea(OODScene):
    def construct(self):
        title = Text("One rule across environments", font_size=36, color=WHITE, weight=BOLD).to_edge(UP, buff=0.35)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.8)
        plane, axes = make_axes_plane("shortcut", "causal")
        plane.shift(DOWN * 0.2)
        self.play(Create(plane), run_time=1.0)
        clouds = VGroup(
            dot_cloud(18, axes.c2p(2.2, 7.2), color=GREEN_D, seed=10),
            dot_cloud(18, axes.c2p(5.2, 6.4), color=YELLOW_D, seed=11),
            dot_cloud(18, axes.c2p(8.0, 7.8), color=PURPLE, seed=12),
        )
        self.play(LaggedStart(*[FadeIn(c) for c in clouds], lag_ratio=0.18), run_time=1.4)
        self.wait(2.6)

        bad_lines = VGroup(
            Line(axes.c2p(3.1, 0.8), axes.c2p(3.1, 9.2), color=RED, stroke_width=5),
            Line(axes.c2p(5.1, 0.8), axes.c2p(5.1, 9.2), color=RED, stroke_width=5),
            Line(axes.c2p(7.0, 0.8), axes.c2p(7.0, 9.2), color=RED, stroke_width=5),
        )
        self.play(LaggedStart(*[Create(l) for l in bad_lines], lag_ratio=0.18), run_time=1.2)
        self.wait(2.6)
        good = Line(axes.c2p(0.6, 5.4), axes.c2p(9.5, 5.4), color=BLUE_D, stroke_width=7)
        self.play(ReplacementTransform(bad_lines, good), run_time=1.0)
        self.play(Circumscribe(good, color=BLUE_D), run_time=1.0)
        self.wait(9.0)


class IRMFormula(OODScene):
    def construct(self):
        title = Text("Risk + invariance penalty", font_size=36, color=WHITE, weight=BOLD).to_edge(UP, buff=0.35)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.8)
        risk = MathTex(r"\sum_e R^e", font_size=58, color=WHITE).shift(LEFT * 2.2 + UP * 0.4)
        penalty = MathTex(r"\lambda\sum_e\|\nabla_w R^e\|^2", font_size=50, color=ORANGE).shift(RIGHT * 2.4 + UP * 0.4)
        plus = Text("+", font_size=56, color=GOLD).move_to(UP * 0.4)
        self.play(Write(risk), run_time=1.0)
        self.wait(2.4)
        self.play(FadeIn(plus), Write(penalty), run_time=1.2)
        self.wait(2.8)

        envs = VGroup(*[
            Circle(radius=0.38, color=c, stroke_width=4).set_fill(c, 0.18)
            for c in [GREEN_D, YELLOW_D, PURPLE]
        ]).arrange(RIGHT, buff=1.0).shift(DOWN * 1.4)
        w = labeled_box("w", 0.9, 0.62, BLUE_D, 28).next_to(envs, DOWN, buff=0.45)
        arrows = VGroup(*[Arrow(e.get_bottom(), w.get_top(), color=e.get_color(), buff=0.08, stroke_width=5) for e in envs])
        self.play(FadeIn(envs), FadeIn(w), LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.18), run_time=1.3)
        self.play(Indicate(w, color=BLUE_D), run_time=1.0)
        self.wait(8.5)


class IRMGradientVectors(OODScene):
    def construct(self):
        title = Text("Gradients should agree", font_size=36, color=WHITE, weight=BOLD).to_edge(UP, buff=0.35)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.8)
        center = ORIGIN + DOWN * 0.35
        base = Dot(center, color=WHITE, radius=0.08)
        arrows = VGroup(
            Arrow(center, center + LEFT * 2.0 + UP * 1.0, color=GREEN_D, stroke_width=6),
            Arrow(center, center + RIGHT * 1.8 + UP * 0.75, color=YELLOW_D, stroke_width=6),
            Arrow(center, center + UP * 2.0, color=PURPLE, stroke_width=6),
        )
        self.play(FadeIn(base), LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.2), run_time=1.2)
        # Dynamic rotation/wiggle of vectors to show disagreement during wait
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
        target = Arrow(center, center + UP * 2.2, color=BLUE_D, stroke_width=8)
        penalty = Text("gradient penalty", font_size=28, color=ORANGE).to_edge(DOWN, buff=0.45)
        self.play(FadeIn(penalty, shift=UP * 0.1), run_time=0.5)
        for scale in [0.8, 0.55, 0.28]:
            self.play(*[a.animate.become(Arrow(center, center + UP * 2.2 * scale, color=a.get_color(), stroke_width=6)) for a in arrows], run_time=0.65)
        self.play(*[a.animate.become(target.copy().set_color(a.get_color())) for a in arrows], run_time=0.9)
        self.play(Flash(target.get_end(), color=GOLD), Indicate(penalty, color=ORANGE), run_time=0.8)
        lambda_bar = NumberLine(x_range=[0, 10, 2], length=4, color=GRAY_B).to_edge(DOWN, buff=0.28)
        dot = Dot(lambda_bar.n2p(0), color=ORANGE)
        lam_lab = Text("lambda", font_size=22, color=ORANGE).next_to(lambda_bar, UP, buff=0.12)
        self.play(FadeIn(lambda_bar), FadeIn(dot), FadeIn(lam_lab), run_time=0.7)
        self.play(dot.animate.move_to(lambda_bar.n2p(10)), *[a.animate.scale(0.35, about_point=center) for a in arrows], run_time=2.1)
        self.play(Flash(center + UP * 0.25, color=GOLD), run_time=0.7)
        self.wait(3.7)


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
        ).arrange(RIGHT, buff=1.35)
        for g in icons:
            g[1].move_to(g[0])
        labels = VGroup(
            Text("diverse envs", font_size=24, color=ORANGE),
            Text("sensitive", font_size=24, color=RED),
            Text("counterexamples", font_size=24, color=PURPLE),
        )
        for lab, icon in zip(labels, icons):
            lab.next_to(icon, DOWN, buff=0.35)
        self.play(LaggedStart(*[FadeIn(VGroup(i, l), scale=0.85) for i, l in zip(icons, labels)], lag_ratio=0.2), run_time=1.3)
        self.wait(3.2)
        self.play(Indicate(VGroup(icons[0], labels[0]), color=GOLD), run_time=0.9)
        self.play(Indicate(VGroup(icons[1], labels[1]), color=RED), run_time=0.9)
        self.play(Indicate(VGroup(icons[2], labels[2]), color=PURPLE), run_time=0.9)
        same_envs = VGroup(
            labeled_box("env 1\nsame shortcut", 2.2, 0.72, ORANGE, 16),
            labeled_box("env 2\nsame shortcut", 2.2, 0.72, ORANGE, 16),
        ).arrange(RIGHT, buff=0.5).to_edge(DOWN, buff=0.3)
        hidden = Text("no disagreement -> IRM cannot detect it", font_size=25, color=RED).next_to(same_envs, UP, buff=0.22)
        self.play(FadeIn(same_envs[0], shift=UP * 0.1), FadeIn(same_envs[1], shift=UP * 0.1), run_time=0.8)
        
        arr1 = Arrow(same_envs[0].get_top(), same_envs[0].get_top() + UP * 0.75 + RIGHT * 0.4, color=RED, stroke_width=4)
        arr2 = Arrow(same_envs[1].get_top(), same_envs[1].get_top() + UP * 0.75 + RIGHT * 0.4, color=RED, stroke_width=4)
        self.play(GrowArrow(arr1), GrowArrow(arr2), run_time=0.8)
        self.play(Indicate(VGroup(arr1, arr2), color=RED), run_time=0.8)

        self.play(FadeIn(hidden, shift=UP * 0.1), Indicate(VGroup(icons[0], labels[0]), color=ORANGE), run_time=1.0)
        self.wait(2.2)


class NuRD(OODScene):
    def construct(self):
        self.title("NuRD", "Nuisance-Randomized Distillation")
        x = labeled_box("X", 1.1, 0.72, WHITE, 24).shift(LEFT * 5 + UP * 0.3)
        phi = labeled_box("phi(X)\nfilter", 2.0, 0.9, BLUE_D, 20).shift(LEFT * 2 + UP * 0.3)
        clean = labeled_box("clean\nrepresentation", 2.4, 0.9, GREEN_D, 18).shift(RIGHT * 1.1 + UP * 0.3)
        w = labeled_box("w", 1.1, 0.72, GOLD, 24).shift(RIGHT * 3.7 + UP * 0.3)
        y = labeled_box("Y", 1.1, 0.72, GREEN_D, 24).shift(RIGHT * 5.2 + UP * 0.3)
        z = labeled_box("Z nuisance", 2.0, 0.65, RED, 18).shift(LEFT * 2 + DOWN * 1.7)
        arrows = VGroup(
            Arrow(x.get_right(), phi.get_left(), buff=0.1, color=GRAY_B),
            Arrow(phi.get_right(), clean.get_left(), buff=0.1, color=BLUE_D),
            Arrow(clean.get_right(), w.get_left(), buff=0.1, color=GREEN_D),
            Arrow(w.get_right(), y.get_left(), buff=0.1, color=GOLD),
            Arrow(phi.get_bottom(), z.get_top(), buff=0.08, color=RED),
        )
        self.play(FadeIn(x), FadeIn(phi), GrowArrow(arrows[0]), run_time=0.8)
        self.play(GrowArrow(arrows[4]), FadeIn(z, shift=DOWN * 0.1), run_time=0.8)
        # Keep Z visible but dimmed, add cross to show it's discarded
        z_cross = VGroup(
            Line(z.get_corner(UL), z.get_corner(DR), color=RED, stroke_width=5),
            Line(z.get_corner(DL), z.get_corner(UR), color=RED, stroke_width=5),
        )
        discard_label = Text("discarded", font_size=18, color=RED).next_to(z, DOWN, buff=0.12)
        self.play(Flash(z, color=RED), z.animate.set_opacity(0.3),
                  Create(z_cross), FadeIn(discard_label, shift=UP * 0.1), run_time=0.8)
        self.play(FadeIn(clean), GrowArrow(arrows[1]), run_time=0.8)
        self.play(FadeIn(w), GrowArrow(arrows[2]), FadeIn(y), GrowArrow(arrows[3]), run_time=1.0)
        # Move condition formula higher to avoid overlap with final_note
        condition = MathTex(r"Y\perp Z\mid \phi(X)", font_size=48, color=GOLD).shift(DOWN * 2.6)
        self.play(Write(condition), run_time=1.0)
        self.play(Circumscribe(condition, color=GOLD), run_time=0.9)
        self.wait(0.8)
        random_z = VGroup(*[Text("Z", font_size=24, color=RED).move_to(phi).shift(UP * np.random.uniform(-0.5, 0.5) + RIGHT * np.random.uniform(-0.5, 0.5)) for _ in range(5)])
        self.play(LaggedStart(*[FadeIn(rz) for rz in random_z], lag_ratio=0.1), run_time=0.8)
        self.play(LaggedStart(*[rz.animate.move_to(phi.get_bottom() + DOWN * 0.3) for rz in random_z], lag_ratio=0.06), run_time=0.9)
        self.play(FadeOut(random_z, shift=DOWN * 0.2), Flash(phi, color=BLUE_D), run_time=0.8)
        self.play(Indicate(clean, color=GREEN_D), Indicate(y, color=GREEN_D), run_time=0.9)
        probe = labeled_box("probe for Z", 1.8, 0.65, RED, 17).next_to(clean, DOWN, buff=0.45)
        probe_arrow = Arrow(clean.get_bottom(), probe.get_top(), buff=0.08, color=RED)
        fail = Text("fails", font_size=24, color=RED, weight=BOLD).next_to(probe, RIGHT, buff=0.18)
        self.play(GrowArrow(probe_arrow), FadeIn(probe, shift=UP * 0.1), run_time=0.8)
        self.play(FadeIn(fail, scale=1.1), Flash(probe, color=RED), run_time=0.8)
        self.play(Indicate(condition, color=GOLD), run_time=0.9)
        clean_path = VGroup(arrows[1], arrows[2], arrows[3])
        self.play(clean_path.animate.set_stroke(width=7), run_time=0.8)
        self.play(Circumscribe(clean, color=GREEN_D), run_time=0.8)
        # Fade out condition, then show final_note at bottom without overlap
        self.play(FadeOut(condition, shift=DOWN * 0.15), run_time=0.5)
        final_note = Text("prediction keeps Y, not the nuisance Z", font_size=25, color=GOLD).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(final_note, shift=UP * 0.1), run_time=0.8)
        self.play(Flash(y, color=GREEN_D), Flash(probe, color=RED), run_time=0.9)
        self.play(Circumscribe(final_note, color=GOLD), run_time=0.8)
        self.wait(1.5)
