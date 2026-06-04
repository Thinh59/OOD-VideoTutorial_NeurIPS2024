from manim import *
from common import *


class ScaleDoesNotSolve(OODScene):
    def construct(self):
        self.question("Do larger models automatically avoid shortcuts?")
        axes = Axes(x_range=[0, 4, 1], y_range=[40, 90, 10], x_length=6.3, y_length=3.4, axis_config={"color": GRAY_B}).shift(LEFT * 1.1 + DOWN * 0.15)
        x_labs = VGroup(*[Text(t, font_size=18) for t in ["10M", "1B", "10B", "100B"]])
        for i, lab in enumerate(x_labs):
            lab.next_to(axes.c2p(i + 0.4, 40), DOWN, buff=0.12)
        erm_pts = [axes.c2p(0.4, 48), axes.c2p(1.4, 55), axes.c2p(2.4, 57), axes.c2p(3.4, 58)]
        dro_pts = [axes.c2p(0.4, 52), axes.c2p(1.4, 64), axes.c2p(2.4, 72), axes.c2p(3.4, 76)]
        erm_line = VMobject(color=RED, stroke_width=5).set_points_as_corners(erm_pts)
        dro_line = VMobject(color=BLUE_D, stroke_width=5).set_points_as_corners(dro_pts)
        legend = VGroup(Text("ERM", font_size=20, color=RED), Text("robust objective", font_size=20, color=BLUE_D)).arrange(DOWN, aligned_edge=LEFT).to_corner(UR).shift(DOWN * 0.6)
        self.play(Create(axes), FadeIn(x_labs), run_time=1.0)
        self.play(Create(erm_line), FadeIn(legend[0]), run_time=1.0)
        self.play(Indicate(erm_line, color=RED), run_time=0.9)
        self.play(Create(dro_line), FadeIn(legend[1]), run_time=1.0)
        self.play(Indicate(dro_line, color=BLUE_D), run_time=0.9)
        gap = DoubleArrow(erm_pts[-1], dro_pts[-1], buff=0.08, color=GOLD, stroke_width=4)
        gap_label = Text("robustness gap", font_size=22, color=GOLD).next_to(gap, RIGHT, buff=0.15)
        self.play(GrowArrow(gap), FadeIn(gap_label, shift=LEFT * 0.1), run_time=0.9)
        self.play(Flash(gap.get_center(), color=GOLD, line_length=0.35, num_lines=8), run_time=0.8)
        self.wait(0.2)
        boxes = VGroup(*[Square(side_length=s, color=GRAY_B).set_fill(GRAY_D, 0.15) for s in [0.55, 0.8, 1.05]]).arrange(RIGHT, buff=0.35).next_to(legend, DOWN, buff=0.45)
        red_edges = VGroup()
        for b in boxes:
            for k in range(3):
                red_edges.add(Line(b.get_center(), b.get_center() + RIGHT * (0.25 + 0.15 * k) + UP * (0.12 * (k - 1)), color=RED, stroke_width=3))
        self.play(LaggedStart(*[FadeIn(b, scale=0.85) for b in boxes], lag_ratio=0.15), run_time=0.8)
        self.play(LaggedStart(*[Create(e) for e in red_edges], lag_ratio=0.04), run_time=1.2)
        self.play(Indicate(boxes[-1], color=RED), run_time=0.8)
        self.wait(0.2)
        note = Text("Bigger != more robust", font_size=34, color=GOLD, weight=BOLD).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(note, shift=UP * 0.1), Indicate(erm_line, color=RED), run_time=1.0)
        self.play(Circumscribe(note, color=GOLD), run_time=0.9)
        self.wait(0.5)


class CLIPSpuriousWeb(OODScene):
    def construct(self):
        self.title("CLIP and Web Correlations")
        image_stream = VGroup(*[labeled_box(t, 1.7, 0.55, BLUE_D, 14) for t in ["doctor", "doctor", "nurse", "waterbird"]]).arrange(DOWN, buff=0.12).shift(LEFT * 4.5 + UP * 0.3)
        img_enc = labeled_box("Image\nencoder", 2.0, 0.8, BLUE_D, 18).shift(LEFT * 1.65 + UP * 1.0)
        txt_enc = labeled_box("Text\nencoder", 2.0, 0.8, PURPLE, 18).shift(LEFT * 1.65 + DOWN * 0.55)
        score = labeled_box("cosine\nscore", 1.8, 0.78, GOLD, 18).shift(RIGHT * 1.2 + UP * 0.25)
        out = labeled_box("web bias\nbecomes feature", 2.6, 0.85, RED, 18).shift(RIGHT * 4.0 + UP * 0.25)
        arrows = VGroup(
            Arrow(image_stream.get_right(), img_enc.get_left(), buff=0.1, color=BLUE_D),
            Arrow(image_stream.get_right(), txt_enc.get_left(), buff=0.1, color=PURPLE),
            Arrow(img_enc.get_right(), score.get_left(), buff=0.1, color=BLUE_D),
            Arrow(txt_enc.get_right(), score.get_left(), buff=0.1, color=PURPLE),
            Arrow(score.get_right(), out.get_left(), buff=0.1, color=RED),
        )
        self.play(LaggedStart(*[FadeIn(x, shift=RIGHT * 0.1) for x in image_stream], lag_ratio=0.12), run_time=1.2)
        self.play(Circumscribe(image_stream, color=BLUE_D), run_time=1.0)
        self.wait(0.2)
        self.play(FadeIn(img_enc), GrowArrow(arrows[0]), run_time=0.9)
        self.play(Indicate(img_enc, color=BLUE_D), run_time=0.8)
        self.wait(0.2)
        prompt = labeled_box("text prompts\nfrom the web", 2.25, 0.72, PURPLE, 17).next_to(txt_enc, DOWN, buff=0.35)
        prompt_arrow = Arrow(prompt.get_top(), txt_enc.get_bottom(), buff=0.08, color=PURPLE, stroke_width=4)
        self.play(FadeIn(prompt, shift=UP * 0.1), GrowArrow(prompt_arrow), run_time=0.9)
        self.play(FadeIn(txt_enc), GrowArrow(arrows[1]), run_time=0.9)
        self.play(Indicate(txt_enc, color=PURPLE), run_time=0.8)
        self.wait(0.2)
        self.play(FadeIn(score), LaggedStart(*[GrowArrow(a) for a in arrows[2:4]], lag_ratio=0.12), run_time=1.0)
        self.play(Flash(score.get_center(), color=GOLD, line_length=0.3, num_lines=8), run_time=0.8)
        self.wait(0.2)
        self.play(FadeIn(out), GrowArrow(arrows[4]), run_time=0.9)
        self.play(Indicate(out, color=RED), run_time=0.9)
        self.wait(0.2)
        bars = VGroup(
            bar("doctor + male", 0.86, GREEN_D, width=3.0).scale(0.72),
            bar("doctor + female", 0.48, RED, width=3.0).scale(0.72),
        ).arrange(DOWN, buff=0.2).to_edge(DOWN, buff=0.45)
        self.play(FadeIn(bars[0], shift=UP * 0.1), run_time=0.8)
        self.play(Indicate(bars[0], color=GREEN_D), run_time=0.8)
        self.wait(0.2)
        self.play(FadeIn(bars[1], shift=UP * 0.1), Indicate(out, color=RED), run_time=0.9)
        self.play(Circumscribe(bars[1], color=RED), run_time=1.0)
        self.wait(0.2)
        hidden = Text("pretraining data can become the shortcut", font_size=27, color=GOLD, weight=BOLD).next_to(bars, UP, buff=0.28)
        self.play(FadeIn(hidden, shift=UP * 0.1), run_time=0.8)
        self.play(Flash(out.get_center(), color=RED, line_length=0.35, num_lines=8), Circumscribe(hidden, color=GOLD), run_time=1.2)
        self.wait(1.5)


class ICLShortcuts(OODScene):
    def construct(self):
        self.question("Can the prompt create its own shortcut?")
        examples = VGroup(
            labeled_box('"The movie was great" -> Positive', 5.7, 0.55, WHITE, 17),
            labeled_box('"Best movie this year" -> Positive', 5.7, 0.55, WHITE, 17),
            labeled_box('"I loved this movie" -> Positive', 5.7, 0.55, WHITE, 17),
        ).arrange(DOWN, buff=0.15).shift(UP * 0.85)
        self.play(LaggedStart(*[FadeIn(e, shift=UP * 0.08) for e in examples], lag_ratio=0.16), run_time=1.4)
        highlights = VGroup(*[SurroundingRectangle(e, color=RED, buff=0.05) for e in examples])
        for h in highlights:
            self.play(Create(h), run_time=0.35)
        rule = Text('"movie" -> Positive', font_size=40, color=RED, weight=BOLD).next_to(examples, DOWN, buff=0.38)
        self.play(FadeIn(rule, scale=1.08), run_time=0.8)
        test = labeled_box('"The food was terrible" -> ???', 4.8, 0.68, ORANGE, 18).to_edge(DOWN, buff=0.85)
        pred = Text("Positive", font_size=30, color=RED, weight=BOLD).next_to(test, RIGHT, buff=0.35)
        cross = VGroup(Line(LEFT * 0.18 + DOWN * 0.18, RIGHT * 0.18 + UP * 0.18, color=RED, stroke_width=6), Line(LEFT * 0.18 + UP * 0.18, RIGHT * 0.18 + DOWN * 0.18, color=RED, stroke_width=6)).next_to(pred, RIGHT, buff=0.18)
        self.play(FadeIn(test, shift=UP * 0.1), run_time=0.7)
        self.play(TransformFromCopy(rule, pred), FadeIn(cross), run_time=0.9)
        self.play(Flash(rule, color=RED), Indicate(pred, color=RED), run_time=1.0)
        fix_prompt = labeled_box("balanced prompt:\nmovie can be negative too", 4.0, 0.72, GREEN_D, 17).next_to(rule, DOWN, buff=0.28)
        self.play(FadeIn(fix_prompt, shift=UP * 0.1), run_time=0.8)
        self.play(FadeOut(highlights), Indicate(fix_prompt, color=GREEN_D), run_time=0.9)
        self.play(Circumscribe(rule, color=RED), run_time=0.7)
        self.wait(5.8)


class ReverseScaling(OODScene):
    def construct(self):
        self.title("Reverse Scaling", "Larger models can be more sensitive to ICL shortcuts")
        axes = Axes(x_range=[0, 3, 1], y_range=[0, 80, 20], x_length=7, y_length=4.2, axis_config={"color": GRAY_B})
        labs = VGroup(Text("2.7B", font_size=22), Text("7B", font_size=22), Text("13B", font_size=22))
        for i, l in enumerate(labs):
            l.next_to(axes.c2p(i + 0.5, 0), DOWN)
        pts = [axes.c2p(0.5, 30), axes.c2p(1.5, 52), axes.c2p(2.5, 71)]
        line = VMobject(color=RED, stroke_width=6).set_points_as_corners(pts)
        dots = VGroup(*[Dot(p, color=RED) for p in pts])
        nums = VGroup(*[Text(v, font_size=24, color=RED).next_to(Dot(p), UP) for v, p in zip(["30%", "52%", "71%"], pts)])
        boxes = VGroup(*[labeled_box(t, 1.25 + 0.18 * i, 0.55 + 0.12 * i, GRAY_B, 16) for i, t in enumerate(["2.7B", "7B", "13B"])]).arrange(RIGHT, buff=0.35).to_edge(DOWN, buff=0.35)
        self.play(Create(axes), FadeIn(labs), run_time=0.9)
        self.play(LaggedStart(*[FadeIn(b, scale=0.85) for b in boxes], lag_ratio=0.16), run_time=0.9)
        self.play(Create(line), LaggedStart(*[FadeIn(d) for d in dots], lag_ratio=0.12), run_time=1.1)
        self.play(LaggedStart(*[FadeIn(n, shift=UP * 0.1) for n in nums], lag_ratio=0.12), run_time=0.8)
        self.play(Indicate(line, color=GOLD), boxes[-1].animate.set_color(RED), run_time=1.0)
        note = Text("bigger models read prompt shortcuts better", font_size=26, color=GOLD).next_to(boxes, UP, buff=0.25)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.8)
        red_rules = VGroup(*[Text("shortcut", font_size=17, color=RED).next_to(b, UP, buff=0.12) for b in boxes])
        self.play(LaggedStart(*[FadeIn(r, shift=UP * 0.08) for r in red_rules], lag_ratio=0.18), run_time=0.9)
        self.play(boxes[-1].animate.scale(1.12), Flash(nums[-1], color=RED), run_time=0.9)
        self.play(Circumscribe(note, color=GOLD), run_time=0.8)
        self.wait(5.0)


class PromptingForRobustness(OODScene):
    def construct(self):
        # ── Beat 0: title  (~0–1.2s)
        self.title("PfR: Prompting for Robustness")

        # ── Beat 1: image grid centered  (~1.2–3.0s)
        # "uses a large vision language model to label spurious attributes"
        def bird_card(bg_color, bird_color):
            bg = RoundedRectangle(width=1.1, height=0.9, corner_radius=0.08,
                                  color=bg_color, stroke_width=2).set_fill(bg_color, 0.28)
            bird = simple_penguin(bird_color).scale(0.55).move_to(bg)
            return VGroup(bg, bird)

        grid = VGroup(
            bird_card(BLUE_E, BLUE_D),
            bird_card(BLUE_E, BLUE_D),
            bird_card(YELLOW_E, BLUE_D),
            bird_card(BLUE_E, BLUE_D),
            bird_card(YELLOW_E, BLUE_D),
            bird_card(BLUE_E, BLUE_D),
        ).arrange_in_grid(2, 3, buff=0.15).scale(0.8).move_to(UP * 0.3)
        self.play(LaggedStart(*[FadeIn(c, scale=0.85) for c in grid], lag_ratio=0.06), run_time=1.0)

        # ── Beat 2: VLM scans grid  (~3.0–5.5s)
        # "For Waterbirds, a VLM can describe whether the background is water or land"
        vlm = labeled_box("VLM  GPT-4V", 2.8, 0.7, PURPLE).move_to(DOWN * 1.3)
        arr_down = Arrow(grid.get_bottom(), vlm.get_top(), buff=0.1, color=PURPLE, stroke_width=4)
        self.play(GrowArrow(arr_down), FadeIn(vlm, shift=UP * 0.2), run_time=0.8)

        highlight = SurroundingRectangle(grid[0], color=PURPLE, buff=0.04, stroke_width=3)
        self.play(Create(highlight), run_time=0.3)
        for i in range(1, 6):
            self.play(highlight.animate.move_to(grid[i]), run_time=0.22)
        self.play(FadeOut(highlight), run_time=0.2)

        # captions below each card
        cap_data = [("water", BLUE_D), ("water", BLUE_D), ("land", YELLOW_D),
                    ("water", BLUE_D), ("land", YELLOW_D), ("water", BLUE_D)]
        caps = VGroup()
        for i, (txt, col) in enumerate(cap_data):
            lab = Text(txt, font_size=14, color=col, weight=BOLD).next_to(grid[i], DOWN, buff=0.06)
            caps.add(lab)
        self.play(LaggedStart(*[FadeIn(c, shift=DOWN * 0.06) for c in caps], lag_ratio=0.06), run_time=0.9)
        self.wait(0.4)

        # ── Beat 3: fade out phase 1, build pipeline  (~5.5–7.0s)
        # "Those labels can then feed Group DRO"
        self.play(*[FadeOut(m) for m in [grid, arr_down, vlm, caps]], run_time=0.6)

        # horizontal pipeline layout
        img_box = labeled_box("Waterbird\nimages", 1.8, 0.78, BLUE_D, 19).move_to(LEFT * 4.45 + UP * 1.12)
        vlm2 = labeled_box("VLM\nGPT-4V", 1.65, 0.78, PURPLE, 19).move_to(LEFT * 1.5 + UP * 1.12)
        lab_box = labeled_box("Auto labels\nwater / land", 2.05, 0.78, GOLD, 18).move_to(RIGHT * 1.5 + UP * 1.12)
        dro = labeled_box("Group\nDRO", 1.65, 0.78, GREEN_D, 19).move_to(RIGHT * 4.45 + UP * 1.12)

        a1 = Arrow(img_box.get_right(), vlm2.get_left(), buff=0.1, color=PURPLE, stroke_width=4)
        a2 = Arrow(vlm2.get_right(), lab_box.get_left(), buff=0.1, color=GOLD, stroke_width=4)
        a3 = Arrow(lab_box.get_right(), dro.get_left(), buff=0.1, color=GREEN_D, stroke_width=4)

        self.play(FadeIn(img_box, shift=RIGHT * 0.15), run_time=0.5)
        self.play(GrowArrow(a1), FadeIn(vlm2, shift=RIGHT * 0.15), run_time=0.7)

        # ── Beat 4: labels appear  (~7.0–9.0s)
        self.play(GrowArrow(a2), FadeIn(lab_box, shift=RIGHT * 0.15), run_time=0.7)
        self.play(Indicate(lab_box, color=GOLD), run_time=0.7)
        self.wait(0.3)

        # ── Beat 5: Group DRO  (~9.0–11.0s)
        self.play(GrowArrow(a3), FadeIn(dro, shift=RIGHT * 0.15), run_time=0.7)
        self.play(Flash(dro.get_center(), color=GREEN_D, line_length=0.3, num_lines=8), run_time=0.7)
        self.wait(0.3)

        # ── Beat 6: WGA bar 71% → 91%  (~11.0–15.5s)
        # "improving worst-group performance"
        wga_label = Text("Worst-Group Accuracy", font_size=24, color=WHITE).move_to(DOWN * 1.05)
        bar_w = 5.8
        bar_bg = RoundedRectangle(width=bar_w, height=0.32, corner_radius=0.14,
                                  color=GRAY_D, stroke_width=0).set_fill(GRAY_D, 0.5)
        bar_bg.next_to(wga_label, DOWN, buff=0.15)

        def progress_fill(value, color):
            fill = RoundedRectangle(width=bar_w * value, height=0.32, corner_radius=0.14,
                                    color=color, stroke_width=0).set_fill(color, 0.92)
            fill.move_to(bar_bg.get_left() + RIGHT * (fill.width / 2))
            fill.set_y(bar_bg.get_y()).set_z_index(2)
            return fill

        bar_fill = progress_fill(0.71, RED)
        pct = Text("71%", font_size=22, color=WHITE, weight=BOLD).move_to(
            bar_fill.get_right() + LEFT * 0.34
        ).set_z_index(3)

        self.play(FadeIn(wga_label), FadeIn(bar_bg), FadeIn(bar_fill), FadeIn(pct), run_time=0.8)
        self.wait(0.5)

        bar_end = progress_fill(0.91, GREEN_D)
        pct_end = Text("91%", font_size=22, color=WHITE, weight=BOLD).move_to(
            bar_end.get_right() + LEFT * 0.34
        ).set_z_index(3)

        self.play(Transform(bar_fill, bar_end), Transform(pct, pct_end), run_time=2.0)
        self.play(
            Flash(pct.get_center(), color=GREEN, line_length=0.35, num_lines=10),
            Indicate(dro, color=GREEN_D),
            run_time=1.0,
        )

        # ── Beat 7: conclusion  (~15.5–17.7s)
        conclusion = Text("No manual annotation needed", font_size=26, color=GOLD, weight=BOLD).to_edge(DOWN, buff=0.18)
        self.play(FadeIn(conclusion, shift=UP * 0.12), run_time=0.7)
        self.play(Circumscribe(conclusion, color=GOLD), run_time=0.8)
        self.wait(2.9)


class CATO(OODScene):
    def construct(self):
        self.title("CATO: Counterfactual Data with LLMs")
        steps = VGroup(
            labeled_box("1. find\nspurious Z", 2.7, 0.78, ORANGE, 17),
            labeled_box("2. generate\ncounterfactual", 2.7, 0.78, PURPLE, 17),
            labeled_box("3. retrain on\nbalanced data", 2.7, 0.78, GREEN_D, 17),
        ).arrange(DOWN, buff=0.35).shift(LEFT * 4.2 + DOWN * 0.05)
        bird_water = VGroup(simple_penguin(), Square(1.15, color=BLUE_E).set_fill(BLUE_E, 0.2)).arrange(IN, buff=0).shift(LEFT * 0.8 + UP * 1.2)
        bird_land = VGroup(simple_penguin(), Square(1.15, color=YELLOW_E).set_fill(YELLOW_E, 0.22)).arrange(IN, buff=0).shift(RIGHT * 1.25 + UP * 1.2)
        arrow = Arrow(bird_water.get_right(), bird_land.get_left(), color=PURPLE, stroke_width=5)
        # LLM prompt above the arrow to avoid overlapping with samples below
        prompt = labeled_box("LLM prompt:\nchange background, keep bird", 3.3, 0.78, GOLD, 16).next_to(arrow, UP, buff=0.25)
        pie1 = Circle(radius=0.75, color=RED).set_fill(RED, 0.25).shift(RIGHT * 3.9 + UP * 0.8)
        pie2 = Circle(radius=0.75, color=GREEN_D).set_fill(GREEN_D, 0.25).shift(RIGHT * 3.9 + DOWN * 1.25)
        t1 = Text("minority\n5%", font_size=20).move_to(pie1)
        t2 = Text("balanced", font_size=20).move_to(pie2)
        self.play(FadeIn(steps[0], shift=RIGHT * 0.1), FadeIn(bird_water, scale=0.9), run_time=0.8)
        self.play(FadeIn(steps[1], shift=RIGHT * 0.1), GrowArrow(arrow), TransformFromCopy(bird_water, bird_land), run_time=1.2)
        self.play(FadeIn(prompt, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(VGroup(pie1, t1), scale=0.9), run_time=0.6)
        self.play(FadeIn(steps[2], shift=RIGHT * 0.1), Transform(VGroup(pie1, t1), VGroup(pie2, t2)), run_time=1.1)
        self.play(Flash(pie2, color=GREEN_D), Indicate(steps[2], color=GREEN_D), run_time=0.9)
        samples = VGroup(*[bird_land.copy().scale(0.45) for _ in range(6)]).arrange_in_grid(2, 3, buff=0.12).next_to(bird_land, DOWN, buff=0.35)
        self.play(LaggedStart(*[FadeIn(s, scale=0.8) for s in samples], lag_ratio=0.08), run_time=0.9)
        aug = Text("counterfactual minority samples", font_size=22, color=PURPLE).next_to(samples, DOWN, buff=0.18)
        self.play(FadeIn(aug, shift=UP * 0.1), run_time=0.7)
        self.play(Circumscribe(samples, color=PURPLE), run_time=0.8)
        for s in samples:
            self.play(s.animate.shift(UP * 0.08), run_time=0.12)
            self.play(s.animate.shift(DOWN * 0.08), run_time=0.12)
        final = Text("causal augmentation balances the rare groups", font_size=24, color=GREEN_D).to_edge(DOWN, buff=0.25)
        self.play(FadeIn(final, shift=UP * 0.1), run_time=0.8)
        self.play(Circumscribe(final, color=GREEN_D), run_time=0.8)
        self.wait(3.6)
