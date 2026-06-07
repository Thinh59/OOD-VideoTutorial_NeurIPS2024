from manim import *
from common import *


class ScaleDoesNotSolve(OODScene):
    def construct(self):
        self.question("Do larger models automatically avoid shortcuts?")
        
        # --- STEP 1: Axes & Robustness Gap (Shifted left to avoid right-heavy look) ---
        axes = Axes(x_range=[0, 4, 1], y_range=[40, 90, 10], x_length=6.0, y_length=3.2, axis_config={"color": GRAY_B}).shift(LEFT * 1.8 + DOWN * 0.15)
        x_labs = VGroup(*[Text(t, font_size=16) for t in ["10M", "1B", "10B", "100B"]])
        for i, lab in enumerate(x_labs):
            lab.next_to(axes.c2p(i + 0.4, 40), DOWN, buff=0.1)
            
        erm_pts = [axes.c2p(0.4, 48), axes.c2p(1.4, 55), axes.c2p(2.4, 57), axes.c2p(3.4, 58)]
        dro_pts = [axes.c2p(0.4, 52), axes.c2p(1.4, 64), axes.c2p(2.4, 72), axes.c2p(3.4, 76)]
        erm_line = VMobject(color=RED, stroke_width=4).set_points_as_corners(erm_pts)
        dro_line = VMobject(color=BLUE_D, stroke_width=4).set_points_as_corners(dro_pts)
        
        legend = VGroup(
            Text("ERM", font_size=18, color=RED), 
            Text("robust objective", font_size=18, color=BLUE_D)
        ).arrange(DOWN, aligned_edge=LEFT).shift(RIGHT * 3.8 + UP * 1.2)
        
        self.play(Create(axes), FadeIn(x_labs), run_time=0.6)
        self.play(Create(erm_line), FadeIn(legend[0]), run_time=0.6)
        self.play(Create(dro_line), FadeIn(legend[1]), run_time=0.6)
        
        gap = DoubleArrow(erm_pts[-1], dro_pts[-1], buff=0.08, color=GOLD, stroke_width=3)
        gap_label = Text("robustness gap", font_size=18, color=GOLD).next_to(gap, RIGHT, buff=0.1)
        self.play(GrowArrow(gap), FadeIn(gap_label, shift=LEFT * 0.1), run_time=0.5)
        self.wait(1.5)
        
        # Display 3 model size boxes on the right side
        boxes = VGroup(*[Square(side_length=s, color=GRAY_B).set_fill(GRAY_D, 0.15) for s in [0.55, 0.8, 1.05]]).arrange(RIGHT, buff=0.25).shift(RIGHT * 3.8 + DOWN * 0.8)
        self.play(LaggedStart(*[FadeIn(b, scale=0.85) for b in boxes], lag_ratio=0.15), run_time=0.5)
        
        note = Text("Bigger != more robust", font_size=28, color=GOLD, weight=BOLD).to_edge(DOWN, buff=0.3)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.5)
        self.play(Circumscribe(note, color=GOLD), run_time=0.5)
        self.wait(2.0)
        
        # --- STEP 2: Transition to Capacity (Clear screen, show centered boxes) ---
        self.play(
            FadeOut(VGroup(axes, erm_line, dro_line, legend, gap, gap_label, x_labs, note)),
            boxes.animate.arrange(RIGHT, buff=0.8).shift(UP * 0.5 + LEFT * 3.8),
            run_time=0.6
        )
        
        capacity_title = Text("Bigger Models = More Complex Shortcuts", font_size=26, color=GOLD).shift(UP * 2.2)
        self.play(FadeIn(capacity_title, shift=DOWN * 0.1), run_time=0.5)
        
        cap_labels = VGroup(
            Text("Small (10M)\nSimple shortcut", font_size=14, color=GREEN_D),
            Text("Medium (1B)\nTextual shortcut", font_size=14, color=ORANGE),
            Text("Large (100B)\nHigh-dimensional noise", font_size=14, color=PURPLE)
        )
        for i, b in enumerate(boxes):
            cap_labels[i].next_to(b, DOWN, buff=0.2)
            
        self.play(LaggedStart(*[FadeIn(l, shift=UP * 0.1) for l in cap_labels], lag_ratio=0.15), run_time=0.6)
        
        short1 = Text("Color", font_size=13, color=GREEN_D).move_to(boxes[0].get_center())
        short2 = Text("N-Grams", font_size=13, color=ORANGE).move_to(boxes[1].get_center())
        short3 = Text("Texture\nNoise", font_size=11, color=PURPLE).move_to(boxes[2].get_center())
        
        self.play(FadeIn(short1), FadeIn(short2), FadeIn(short3), run_time=0.4)
        self.play(Flash(boxes[2], color=PURPLE), run_time=0.4)
        
        cap_explain = Text("Larger models possess the capacity to memorize complex, subtle shortcuts.", font_size=18, color=GOLD).shift(DOWN * 2.0)
        self.play(FadeIn(cap_explain, shift=UP * 0.1), run_time=0.5)
        self.wait(2.2)
        
        # --- STEP 3: Transition to Accuracy on the Line Paradox ---
        self.play(FadeOut(VGroup(boxes, cap_labels, short1, short2, short3, cap_explain, capacity_title)), run_time=0.5)
        
        line_title = Text("Accuracy on the Line Paradox", font_size=26, color=WHITE).shift(UP * 2.2)
        self.play(FadeIn(line_title), run_time=0.5)
        
        plot_axes = Axes(x_range=[0, 100, 20], y_range=[0, 100, 20], x_length=5.0, y_length=3.2, axis_config={"color": GRAY_B}).shift(LEFT * 1.5 + DOWN * 0.3)
        plot_labels = VGroup(
            Text("ID Accuracy", font_size=14).next_to(plot_axes.x_axis, RIGHT, buff=0.1),
            Text("OOD Accuracy", font_size=14).next_to(plot_axes.y_axis, UP, buff=0.1)
        )
        self.play(Create(plot_axes), FadeIn(plot_labels), run_time=0.6)
        
        ideal_line = plot_axes.plot(lambda x: x, color=BLUE_D, stroke_width=4)
        ideal_lbl = Text("Accuracy on the Line\n(Simple Shifts)", font_size=13, color=BLUE_D).next_to(plot_axes.c2p(70, 70), UL, buff=0.1)
        self.play(Create(ideal_line), FadeIn(ideal_lbl), run_time=0.5)
        self.wait(1.2)
        
        spur_dots = VGroup(*[Dot(plot_axes.c2p(x, y), color=RED, radius=0.08) for x, y in [(40, 20), (60, 22), (80, 25), (95, 26)]])
        spur_curve = plot_axes.plot(lambda x: 10 + 0.15 * x, color=RED, stroke_width=4)
        spur_lbl = Text("Spurious Shift Collapse\n(Scale alone fails!)", font_size=13, color=RED).next_to(plot_axes.c2p(80, 25), UR, buff=0.1)
        
        self.play(FadeIn(spur_dots), Create(spur_curve), FadeIn(spur_lbl), run_time=0.6)
        self.play(Flash(plot_axes.c2p(95, 26), color=RED), run_time=0.4)
        self.wait(2.5)
        
        # Final summary beats
        transition_lbl = Text("Scale alone is not enough.", font_size=24, color=GOLD, weight=BOLD).shift(RIGHT * 3.8 + UP * 1.2)
        self.play(FadeIn(transition_lbl, shift=LEFT * 0.1), run_time=0.5)
        self.play(Circumscribe(transition_lbl, color=GOLD), run_time=0.5)
        
        final_beats = VGroup(
            labeled_box("average improves", 2.2, 0.55, GREEN_D, 14),
            labeled_box("worst group stalls", 2.2, 0.55, RED, 14),
            labeled_box("scale is not enough", 2.2, 0.55, GOLD, 14),
        ).arrange(DOWN, buff=0.2).shift(RIGHT * 3.8 + DOWN * 0.8)
        
        self.play(LaggedStart(*[FadeIn(b, shift=LEFT * 0.1) for b in final_beats], lag_ratio=0.15), run_time=0.6)
        self.active_wait(VGroup(final_beats, transition_lbl), 1.0, GOLD)
        self.wait(1.0)


class CLIPSpuriousWeb(OODScene):
    def construct(self):
        self.title("CLIP and Web Correlations")
        
        # --- STEP 1: Pretraining Pipeline ---
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
        
        self.play(LaggedStart(*[FadeIn(x, shift=RIGHT * 0.1) for x in image_stream], lag_ratio=0.1), run_time=0.4)
        self.play(Circumscribe(image_stream, color=BLUE_D), run_time=0.4)
        
        prompt = labeled_box("text prompts\nfrom the web", 2.25, 0.72, PURPLE, 17).next_to(txt_enc, DOWN, buff=0.3)
        prompt_arrow = Arrow(prompt.get_top(), txt_enc.get_bottom(), buff=0.08, color=PURPLE, stroke_width=3)
        self.play(FadeIn(prompt, shift=UP * 0.1), GrowArrow(prompt_arrow), run_time=0.4)
        
        self.play(FadeIn(img_enc), GrowArrow(arrows[0]), FadeIn(txt_enc), GrowArrow(arrows[1]), run_time=0.5)
        self.play(FadeIn(score), LaggedStart(*[GrowArrow(a) for a in arrows[2:4]], lag_ratio=0.1), run_time=0.5)
        self.play(Flash(score.get_center(), color=GOLD), run_time=0.4)
        
        self.play(FadeIn(out), GrowArrow(arrows[4]), run_time=0.4)
        self.play(Indicate(out, color=RED), run_time=0.5)
        
        bars = VGroup(
            bar("doctor + male", 0.86, GREEN_D, width=2.8).scale(0.7),
            bar("doctor + female", 0.48, RED, width=2.8).scale(0.7),
        ).arrange(DOWN, buff=0.15).to_edge(DOWN, buff=0.4)
        
        self.play(FadeIn(bars[0], shift=UP * 0.1), run_time=0.35)
        self.play(FadeIn(bars[1], shift=UP * 0.1), run_time=0.35)
        self.play(Circumscribe(bars[1], color=RED), run_time=0.4)
        
        hidden = Text("pretraining data can become the shortcut", font_size=24, color=GOLD, weight=BOLD).next_to(bars, UP, buff=0.2)
        self.play(FadeIn(hidden, shift=UP * 0.1), run_time=0.4)
        self.wait(3.5)
        
        # --- STEP 2: Transition to Diversity Comparison ---
        self.play(
            FadeOut(VGroup(image_stream, img_enc, txt_enc, score, out, arrows, prompt, prompt_arrow, bars, hidden)),
            run_time=0.5
        )
        
        comp_title = Text("Waterbirds Zero-Shot Robustness", font_size=26, color=WHITE).shift(UP * 2.2)
        self.play(FadeIn(comp_title), run_time=0.5)
        
        clip_bar = bar("CLIP Zero-Shot", 0.75, GREEN_D, width=4.0).scale(0.85).shift(UP * 0.4)
        erm_bar = bar("ERM Baseline", 0.32, RED, width=4.0).scale(0.85).next_to(clip_bar, DOWN, buff=0.25)
        
        self.play(FadeIn(erm_bar, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(clip_bar, shift=UP * 0.1), run_time=0.5)
        self.play(Circumscribe(clip_bar, color=GREEN_D), run_time=0.5)
        self.wait(1.5)
        
        # Draw penguin contexts breaking spurious correlations
        p_beach = VGroup(simple_penguin(), Square(1.0, color=YELLOW_E).set_fill(YELLOW_E, 0.25)).arrange(IN).shift(LEFT * 3.3 + DOWN * 1.5)
        p_grass = VGroup(simple_penguin(), Square(1.0, color=GREEN_E).set_fill(GREEN_E, 0.25)).arrange(IN).shift(ORIGIN + DOWN * 1.5)
        p_snow = VGroup(simple_penguin(), Square(1.0, color=BLUE_E).set_fill(BLUE_E, 0.25)).arrange(IN).shift(RIGHT * 3.3 + DOWN * 1.5)
        
        text_vec = Text('"penguin"', font_size=22, color=GOLD).shift(DOWN * 0.2)
        a_beach = Arrow(p_beach.get_top(), text_vec.get_bottom() + LEFT * 0.5, color=GOLD, stroke_width=3)
        a_grass = Arrow(p_grass.get_top(), text_vec.get_bottom(), color=GOLD, stroke_width=3)
        a_snow = Arrow(p_snow.get_top(), text_vec.get_bottom() + RIGHT * 0.5, color=GOLD, stroke_width=3)
        
        self.play(
            FadeOut(VGroup(erm_bar, clip_bar, comp_title)),
            FadeIn(text_vec),
            run_time=0.5
        )
        self.play(
            FadeIn(p_beach), GrowArrow(a_beach),
            FadeIn(p_grass), GrowArrow(a_grass),
            FadeIn(p_snow), GrowArrow(a_snow),
            run_time=0.6
        )
        
        break_lbl = Text("Diverse web backgrounds break the penguin-snow shortcut!", font_size=18, color=GREEN_D).next_to(text_vec, UP, buff=0.25)
        self.play(FadeIn(break_lbl, shift=UP * 0.1), run_time=0.4)
        self.wait(3.0)
        
        # --- STEP 3: Transition to Web Bias Failure ---
        self.play(FadeOut(VGroup(text_vec, p_beach, p_grass, p_snow, a_beach, a_grass, a_snow, break_lbl)), run_time=0.5)
        
        bias_title = Text("But CLIP Inherits Web Biases", font_size=26, color=WHITE).shift(UP * 2.2)
        self.play(FadeIn(bias_title), run_time=0.5)
        
        doc_lbl = Text('"doctor"', font_size=26, color=GOLD).shift(LEFT * 2.8 + UP * 0.6)
        assoc_box = VGroup(
            Text("Web Co-occurrences:", font_size=16, color=GRAY_B),
            Text("Male faces: 80%", font_size=18, color=RED),
            Text("Female faces: 20%", font_size=18, color=GRAY_B)
        ).arrange(DOWN, buff=0.1).shift(RIGHT * 2.2 + UP * 0.6)
        
        self.play(FadeIn(doc_lbl), FadeIn(assoc_box), run_time=0.5)
        self.play(Flash(assoc_box, color=RED), run_time=0.4)
        self.wait(1.5)
        
        test_doc_f = Text("Test Time Prediction:", font_size=18, color=GRAY_B).shift(DOWN * 0.4)
        test_card = VGroup(
            Text("Female Doctor Image", font_size=18, color=WHITE),
            Arrow(LEFT * 0.8, RIGHT * 0.8, color=RED, stroke_width=4),
            Text('"nurse"', font_size=22, color=RED, weight=BOLD)
        ).arrange(RIGHT, buff=0.35).next_to(test_doc_f, DOWN, buff=0.15)
        
        self.play(FadeIn(test_doc_f), FadeIn(test_card), run_time=0.5)
        self.play(Flash(test_card[2], color=RED), run_time=0.4)
        self.wait(3.0)
        
        # Final tag & loop summaries (NO empty screen during final wait!)
        final_tag = Text("Scaling web data scales up web biases!", font_size=22, color=RED, weight=BOLD).to_edge(DOWN, buff=0.3)
        self.play(
            FadeOut(VGroup(bias_title, doc_lbl, assoc_box, test_doc_f, test_card)),
            FadeIn(final_tag, shift=UP * 0.1),
            run_time=0.5
        )
        self.play(Circumscribe(final_tag, color=RED), run_time=0.5)
        
        bias_loop = VGroup(
            labeled_box("400M web pairs", 2.1, 0.58, PURPLE, 15),
            labeled_box("correlation", 1.65, 0.58, ORANGE, 15),
            labeled_box("feature", 1.4, 0.58, RED, 15),
        ).arrange(RIGHT, buff=0.35).next_to(final_tag, UP, buff=0.55)
        
        loop_arrows = VGroup(
            Arrow(bias_loop[0].get_right(), bias_loop[1].get_left(), buff=0.08, color=GRAY_B),
            Arrow(bias_loop[1].get_right(), bias_loop[2].get_left(), buff=0.08, color=GRAY_B),
        )
        
        self.play(FadeIn(bias_loop[0], shift=UP * 0.1), run_time=0.3)
        self.play(GrowArrow(loop_arrows[0]), FadeIn(bias_loop[1], shift=UP * 0.1), run_time=0.3)
        self.play(GrowArrow(loop_arrows[1]), FadeIn(bias_loop[2], shift=UP * 0.1), run_time=0.3)
        # Motion fillers: cycle through bias loop boxes
        for _ in range(3):
            self.play(Indicate(bias_loop[0], color=PURPLE, scale_factor=1.08), run_time=0.5)
            self.play(Indicate(bias_loop[1], color=ORANGE, scale_factor=1.08), run_time=0.4)
            self.play(Indicate(bias_loop[2], color=RED, scale_factor=1.08), run_time=0.4)
            self.play(Indicate(final_tag, color=RED), run_time=0.4)
        self.active_wait(VGroup(bias_loop, final_tag), 1.0, RED)
        self.wait(1.0)


class ICLShortcuts(OODScene):
    def construct(self):
        self.question("Can the prompt create its own shortcut?")
        
        examples = VGroup(
            labeled_box('"The movie was great" -> Positive', 5.7, 0.55, WHITE, 17),
            labeled_box('"Best movie this year" -> Positive', 5.7, 0.55, WHITE, 17),
            labeled_box('"I loved this movie" -> Positive', 5.7, 0.55, WHITE, 17),
        ).arrange(DOWN, buff=0.15).shift(UP * 0.85)
        
        self.play(LaggedStart(*[FadeIn(e, shift=UP * 0.08) for e in examples], lag_ratio=0.16), run_time=0.7)
        self.wait(1.5)
        
        highlights = VGroup(*[SurroundingRectangle(e, color=RED, buff=0.05) for e in examples])
        for h in highlights:
            self.play(Create(h), run_time=0.2)
            
        rule = Text('"movie" -> Positive', font_size=40, color=RED, weight=BOLD).next_to(examples, DOWN, buff=0.38)
        self.play(FadeIn(rule, scale=1.08), run_time=0.5)
        self.wait(1.5)
        
        test = labeled_box('"The food was terrible" -> ???', 4.8, 0.68, ORANGE, 18).to_edge(DOWN, buff=0.85)
        pred = Text("Positive", font_size=30, color=RED, weight=BOLD).next_to(test, RIGHT, buff=0.35)
        cross = VGroup(
            Line(LEFT * 0.18 + DOWN * 0.18, RIGHT * 0.18 + UP * 0.18, color=RED, stroke_width=6), 
            Line(LEFT * 0.18 + UP * 0.18, RIGHT * 0.18 + DOWN * 0.18, color=RED, stroke_width=6)
        ).next_to(pred, RIGHT, buff=0.18)
        
        self.play(FadeIn(test, shift=UP * 0.1), run_time=0.4)
        self.play(TransformFromCopy(rule, pred), FadeIn(cross), run_time=0.5)
        self.play(Flash(rule, color=RED), Indicate(pred, color=RED), run_time=0.5)
        self.wait(2.0)
        
        fix_prompt = labeled_box("balanced prompt:\nmovie can be negative too", 4.0, 0.72, GREEN_D, 17).next_to(rule, DOWN, buff=0.28)
        self.play(FadeIn(fix_prompt, shift=UP * 0.1), run_time=0.4)
        self.play(FadeOut(highlights), Indicate(fix_prompt, color=GREEN_D), run_time=0.5)
        self.play(Circumscribe(rule, color=RED), run_time=0.4)
        self.wait(1.5)
        
        timeline = VGroup(
            labeled_box("prompt examples", 2.1, 0.56, WHITE, 15),
            labeled_box("shortcut rule", 1.9, 0.56, RED, 15),
            labeled_box("OOD query", 1.65, 0.56, ORANGE, 15),
            labeled_box("balanced prompt", 2.1, 0.56, GREEN_D, 15),
        ).arrange(RIGHT, buff=0.25).to_edge(DOWN, buff=0.28)
        
        self.play(LaggedStart(*[FadeIn(t, shift=UP * 0.08) for t in timeline], lag_ratio=0.1), run_time=0.4)
        self.active_wait(VGroup(examples, rule, test, fix_prompt, timeline), 1.0, GOLD)
        self.wait(9.76)


class ReverseScaling(OODScene):
    def construct(self):
        self.title("Reverse Scaling", "Larger models can be more sensitive to ICL shortcuts")
        
        # Shift axes LEFT to prevent overlaps with right-side model boxes
        axes = Axes(x_range=[0, 3, 1], y_range=[0, 100, 20], x_length=5.2, y_length=3.2, axis_config={"color": GRAY_B}).shift(LEFT * 1.8 + DOWN * 0.25)
        y_axis_lbl = Text("OOD Accuracy (%)", font_size=15).next_to(axes.y_axis, UP, buff=0.12)
        labs = VGroup(Text("2.7B", font_size=20), Text("7B", font_size=20), Text("13B", font_size=20))
        for i, l in enumerate(labs):
            l.next_to(axes.c2p(i + 0.5, 0), DOWN, buff=0.1)
            
        # OOD Accuracy decreases as scale increases (Reverse Scaling!)
        pts = [axes.c2p(0.5, 75), axes.c2p(1.5, 48), axes.c2p(2.5, 22)]
        line = VMobject(color=RED, stroke_width=5).set_points_as_corners(pts)
        dots = VGroup(*[Dot(p, color=RED) for p in pts])
        nums = VGroup(*[Text(v, font_size=20, color=RED).next_to(Dot(p), UP, buff=0.08) for v, p in zip(["75%", "48%", "22%"], pts)])
        
        # Position boxes on the right to resolve the ox axis labels collision
        boxes = VGroup(*[labeled_box(t, 1.2 + 0.15 * i, 0.5 + 0.1 * i, GRAY_B, 15) for i, t in enumerate(["2.7B", "7B", "13B"])]).arrange(RIGHT, buff=0.25).shift(RIGHT * 3.8 + DOWN * 1.6)
        
        self.play(Create(axes), FadeIn(y_axis_lbl), FadeIn(labs), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(b, scale=0.85) for b in boxes], lag_ratio=0.15), run_time=0.5)
        self.wait(1.5)
        
        self.play(Create(line), LaggedStart(*[FadeIn(d) for d in dots], lag_ratio=0.1), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(n, shift=UP * 0.1) for n in nums], lag_ratio=0.1), run_time=0.4)
        self.play(Indicate(line, color=GOLD), boxes[-1].animate.set_color(RED), run_time=0.5)
        self.wait(1.5)
        
        note = Text("bigger models read prompt shortcuts better", font_size=20, color=GOLD).shift(RIGHT * 3.8 + UP * 1.2)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.4)
        
        red_rules = VGroup(*[Text("shortcut", font_size=15, color=RED).next_to(b, UP, buff=0.12) for b in boxes])
        self.play(LaggedStart(*[FadeIn(r, shift=UP * 0.08) for r in red_rules], lag_ratio=0.15), run_time=0.5)
        self.play(boxes[-1].animate.scale(1.1), Flash(nums[-1], color=RED), run_time=0.5)
        self.play(Circumscribe(note, color=GOLD), run_time=0.4)
        self.wait(1.5)
        
        stages = VGroup(
            labeled_box("capacity", 1.45, 0.52, PURPLE, 15),
            labeled_box("pattern pickup", 1.9, 0.52, ORANGE, 15),
            labeled_box("reverse scaling", 2.0, 0.52, RED, 15),
        ).arrange(DOWN, buff=0.18).shift(RIGHT * 3.8 + UP * 0.5)
        
        self.play(FadeOut(red_rules), FadeOut(note))
        self.play(LaggedStart(*[FadeIn(s, shift=LEFT * 0.1) for s in stages], lag_ratio=0.15), run_time=0.5)
        
        self.active_wait(VGroup(line, dots, nums, boxes, stages), 1.0, RED)
        self.wait(8.17)


class PromptingForRobustness(OODScene):
    def construct(self):
        self.title("PfR: Prompting for Robustness")
        
        # ── Step 1: Image Grid centered ──
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
        self.play(LaggedStart(*[FadeIn(c, scale=0.85) for c in grid], lag_ratio=0.06), run_time=0.5)
        self.wait(1.0)

        # ── Step 2: VLM Scans Grid ──
        vlm = labeled_box("VLM  GPT-4V", 2.8, 0.7, PURPLE).move_to(DOWN * 1.3)
        arr_down = Arrow(grid.get_bottom(), vlm.get_top(), buff=0.1, color=PURPLE, stroke_width=4)
        self.play(GrowArrow(arr_down), FadeIn(vlm, shift=UP * 0.2), run_time=0.4)

        highlight = SurroundingRectangle(grid[0], color=PURPLE, buff=0.04, stroke_width=3)
        self.play(Create(highlight), run_time=0.15)
        for i in range(1, 6):
            self.play(highlight.animate.move_to(grid[i]), run_time=0.12)
        self.play(FadeOut(highlight), run_time=0.1)

        cap_data = [("water", BLUE_D), ("water", BLUE_D), ("land", YELLOW_D),
                    ("water", BLUE_D), ("land", YELLOW_D), ("water", BLUE_D)]
        caps = VGroup()
        for i, (txt, col) in enumerate(cap_data):
            lab = Text(txt, font_size=14, color=col, weight=BOLD).next_to(grid[i], DOWN, buff=0.06)
            caps.add(lab)
        self.play(LaggedStart(*[FadeIn(c, shift=DOWN * 0.06) for c in caps], lag_ratio=0.06), run_time=0.45)
        self.wait(2.0)

        # ── Step 3: Transition to Horizontal Pipeline ──
        self.play(*[FadeOut(m) for m in [grid, arr_down, vlm, caps]], run_time=0.3)

        img_box = labeled_box("Waterbird\nimages", 1.8, 0.78, BLUE_D, 19).move_to(LEFT * 4.45 + UP * 1.12)
        vlm2 = labeled_box("VLM\nGPT-4V", 1.65, 0.78, PURPLE, 19).move_to(LEFT * 1.5 + UP * 1.12)
        lab_box = labeled_box("Auto labels\nwater / land", 2.05, 0.78, GOLD, 18).move_to(RIGHT * 1.5 + UP * 1.12)
        dro = labeled_box("Group\nDRO", 1.65, 0.78, GREEN_D, 19).move_to(RIGHT * 4.45 + UP * 1.12)

        a1 = Arrow(img_box.get_right(), vlm2.get_left(), buff=0.1, color=PURPLE, stroke_width=4)
        a2 = Arrow(vlm2.get_right(), lab_box.get_left(), buff=0.1, color=GOLD, stroke_width=4)
        a3 = Arrow(lab_box.get_right(), dro.get_left(), buff=0.1, color=GREEN_D, stroke_width=4)

        self.play(FadeIn(img_box, shift=RIGHT * 0.15), run_time=0.3)
        self.play(GrowArrow(a1), FadeIn(vlm2, shift=RIGHT * 0.15), run_time=0.35)
        self.play(GrowArrow(a2), FadeIn(lab_box, shift=RIGHT * 0.15), run_time=0.35)
        self.play(Indicate(lab_box, color=GOLD), run_time=0.35)
        self.wait(1.5)

        # ── Step 4: Group DRO ──
        self.play(GrowArrow(a3), FadeIn(dro, shift=RIGHT * 0.15), run_time=0.35)
        self.play(Flash(dro.get_center(), color=GREEN_D), run_time=0.35)
        self.wait(1.5)

        # ── Step 5: Accuracy Bar ──
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

        self.play(FadeIn(wga_label), FadeIn(bar_bg), FadeIn(bar_fill), FadeIn(pct), run_time=0.4)
        self.wait(1.0)

        bar_end = progress_fill(0.91, GREEN_D)
        pct_end = Text("91%", font_size=22, color=WHITE, weight=BOLD).move_to(
            bar_end.get_right() + LEFT * 0.34
        ).set_z_index(3)

        self.play(Transform(bar_fill, bar_end), Transform(pct, pct_end), run_time=1.0)
        self.play(
            Flash(pct.get_center(), color=GREEN),
            Indicate(dro, color=GREEN_D),
            run_time=0.5,
        )
        
        conclusion = Text("No manual annotation needed", font_size=26, color=GOLD, weight=BOLD).to_edge(DOWN, buff=0.18)
        self.play(FadeIn(conclusion, shift=UP * 0.12), run_time=0.35)
        self.play(Circumscribe(conclusion, color=GOLD), run_time=0.4)
        self.wait(2.2)
        
        # ── Step 6: Results Comparison (No empty screen) ──
        self.play(
            FadeOut(VGroup(img_box, vlm2, lab_box, dro, a1, a2, a3, wga_label, bar_bg, bar_fill, pct, conclusion)),
            run_time=0.5
        )
        
        results_title = Text("Worst-Group Accuracy Comparison", font_size=24, color=WHITE).shift(UP * 1.5)
        self.play(FadeIn(results_title), run_time=0.4)
        
        erm_bar = bar("ERM Baseline", 0.32, RED, width=4.5).scale(0.85).shift(UP * 0.4)
        manual_bar = bar("Group DRO (Manual)", 0.914, BLUE_D, width=4.5).scale(0.85).next_to(erm_bar, DOWN, buff=0.2)
        pfr_bar = bar("PfR (VLM Auto Labels)", 0.9105, GREEN_D, width=4.5).scale(0.85).next_to(manual_bar, DOWN, buff=0.2)
        
        self.play(FadeIn(erm_bar), run_time=0.4)
        self.play(FadeIn(manual_bar), run_time=0.4)
        self.play(FadeIn(pfr_bar), run_time=0.4)
        self.play(Circumscribe(pfr_bar, color=GREEN_D), run_time=0.5)
        self.wait(2.0)
        
        # ── Step 7: Cost and AI Fixing AI paradigm ──
        self.play(FadeOut(VGroup(results_title, erm_bar, manual_bar, pfr_bar)), run_time=0.5)
        
        cost_title = Text("Efficiency Comparison", font_size=24, color=WHITE).shift(UP * 1.5)
        self.play(FadeIn(cost_title), run_time=0.4)
        
        manual_cost = VGroup(
            Text("Manual Annotation", font_size=20, color=RED, weight=BOLD),
            Text("• Cost: ~$1,000+", font_size=16),
            Text("• Time: Days / Weeks", font_size=16)
        ).arrange(DOWN, aligned_edge=LEFT).shift(LEFT * 3.0 + UP * 0.2)
        
        pfr_cost = VGroup(
            Text("PfR (AI labeling)", font_size=20, color=GREEN_D, weight=BOLD),
            Text("• Cost: ~$5 API fee", font_size=16),
            Text("• Time: Minutes", font_size=16)
        ).arrange(DOWN, aligned_edge=LEFT).shift(RIGHT * 3.0 + UP * 0.2)
        
        self.play(FadeIn(manual_cost), FadeIn(pfr_cost), run_time=0.6)
        self.play(Flash(pfr_cost[0], color=GREEN_D), run_time=0.4)
        self.wait(2.2)
        
        self.play(FadeOut(VGroup(cost_title, manual_cost, pfr_cost)), run_time=0.45)
        
        loop_title = Text("AI Fixing AI Paradigm", font_size=26, color=GOLD, weight=BOLD).shift(UP * 1.5)
        self.play(FadeIn(loop_title), run_time=0.4)
        
        step_vlm = labeled_box("Large VLM\n(CLIP/GPT-4)", 2.4, 0.78, PURPLE).shift(LEFT * 3.0)
        step_dro = labeled_box("Robust Model\n(Group DRO)", 2.4, 0.78, GREEN_D).shift(RIGHT * 3.0)
        
        a_vlm_dro = Arrow(step_vlm.get_right(), step_dro.get_left(), color=GOLD, stroke_width=4)
        arrow_lbl = Text("automates labels", font_size=14, color=GOLD).next_to(a_vlm_dro, UP, buff=0.1)
        
        self.play(FadeIn(step_vlm), FadeIn(step_dro), GrowArrow(a_vlm_dro), FadeIn(arrow_lbl), run_time=0.6)
        self.play(Flash(step_dro, color=GREEN_D), run_time=0.25)
        
        final_concl = Text("We leverage AI strengths to fix AI weaknesses.", font_size=24, color=GOLD, weight=BOLD).to_edge(DOWN, buff=0.25)
        self.play(FadeIn(final_concl, shift=UP * 0.1), run_time=0.4)
        self.play(Circumscribe(final_concl, color=GOLD), run_time=0.4)
        
        loop = VGroup(step_vlm, step_dro, a_vlm_dro, arrow_lbl, final_concl)
        self.active_wait(loop, 1.0, GOLD)
        self.wait(1.0)


class CATO(OODScene):
    def construct(self):
        self.title("CATO: Counterfactual Data with LLMs")
        
        # --- STEP 1: Core stages and Synthesis (Shifted bird down to avoid overlapping the prompt box!) ---
        steps = VGroup(
            labeled_box("1. find\nspurious Z", 2.7, 0.78, ORANGE, 17),
            labeled_box("2. generate\ncounterfactual", 2.7, 0.78, PURPLE, 17),
            labeled_box("3. retrain on\nbalanced data", 2.7, 0.78, GREEN_D, 17),
        ).arrange(DOWN, buff=0.35).shift(LEFT * 4.2 + DOWN * 0.05)
        
        # Shifted birds down to UP * 0.2
        bird_water = VGroup(simple_penguin(), Square(1.15, color=BLUE_E).set_fill(BLUE_E, 0.2)).arrange(IN, buff=0).shift(LEFT * 0.8 + UP * 0.2)
        bird_land = VGroup(simple_penguin(), Square(1.15, color=YELLOW_E).set_fill(YELLOW_E, 0.22)).arrange(IN, buff=0).shift(RIGHT * 1.25 + UP * 0.2)
        arrow = Arrow(bird_water.get_right(), bird_land.get_left(), color=PURPLE, stroke_width=5)
        
        # Prompt box shifted down slightly to buff=0.6 above the arrow to avoid overlaps
        prompt = labeled_box("LLM prompt:\nchange background, keep bird", 3.4, 0.78, GOLD, 16).next_to(arrow, UP, buff=0.6)
        
        pie1 = Circle(radius=0.75, color=RED).set_fill(RED, 0.25).shift(RIGHT * 3.9 + UP * 0.8)
        pie2 = Circle(radius=0.75, color=GREEN_D).set_fill(GREEN_D, 0.25).shift(RIGHT * 3.9 + DOWN * 1.25)
        t1 = Text("minority\n5%", font_size=20).move_to(pie1)
        t2 = Text("balanced", font_size=20).move_to(pie2)
        
        self.play(FadeIn(steps[0], shift=RIGHT * 0.1), FadeIn(bird_water, scale=0.9), run_time=0.5)
        self.wait(2.0)
        self.play(FadeIn(steps[1], shift=RIGHT * 0.1), GrowArrow(arrow), TransformFromCopy(bird_water, bird_land), run_time=0.6)
        self.play(FadeIn(prompt, shift=DOWN * 0.1), run_time=0.4)
        self.wait(2.0)
        
        self.play(FadeIn(VGroup(pie1, t1), scale=0.9), run_time=0.4)
        self.wait(1.5)
        self.play(FadeIn(steps[2], shift=RIGHT * 0.1), Transform(VGroup(pie1, t1), VGroup(pie2, t2)), run_time=0.6)
        self.play(Flash(pie2, color=GREEN_D), Indicate(steps[2], color=GREEN_D), run_time=0.5)
        self.wait(2.0)
        
        samples = VGroup(*[bird_land.copy().move_to(ORIGIN).scale(0.45) for _ in range(6)]).arrange_in_grid(2, 3, buff=0.12).next_to(bird_land, DOWN, buff=0.3)
        self.play(LaggedStart(*[FadeIn(s, scale=0.8) for s in samples], lag_ratio=0.08), run_time=0.5)
        
        aug = Text("counterfactual minority samples", font_size=20, color=PURPLE).next_to(samples, DOWN, buff=0.15)
        self.play(FadeIn(aug, shift=UP * 0.1), run_time=0.4)
        self.play(Circumscribe(samples, color=PURPLE), run_time=0.5)
        self.wait(2.5)
        
        final = Text("causal augmentation balances the rare groups", font_size=22, color=GREEN_D).to_edge(DOWN, buff=0.2)
        self.play(FadeIn(final, shift=UP * 0.1), run_time=0.4)
        self.play(Circumscribe(final, color=GREEN_D), run_time=0.4)
        self.wait(2.5)
        
        # --- STEP 2: Scarcity Problem ---
        self.play(
            FadeOut(VGroup(steps, bird_water, bird_land, arrow, prompt, pie1, pie2, t1, t2, samples, aug, final)),
            run_time=0.5
        )
        
        scarcity_title = Text("The Minority Data Scarcity Problem", font_size=26, color=WHITE).shift(UP * 2.2)
        self.play(FadeIn(scarcity_title), run_time=0.5)
        
        maj_samples = bar("Majority Group", 0.95, BLUE_D, width=5.0).scale(0.85).shift(UP * 0.3)
        min_samples = bar("Minority Group", 0.05, RED, width=5.0).scale(0.85).next_to(maj_samples, DOWN, buff=0.25)
        
        self.play(FadeIn(maj_samples), run_time=0.5)
        self.wait(1.5)
        self.play(FadeIn(min_samples), run_time=0.5)
        self.play(Circumscribe(min_samples, color=RED), run_time=0.5)
        self.wait(3.0)
        
        # --- STEP 3: Causal Graph Intervention (Spread nodes by 3.0 units to prevent overlaps!) ---
        self.play(FadeOut(VGroup(scarcity_title, maj_samples, min_samples)), run_time=0.5)
        
        scm_title = Text("SCM Intervention: Break the shortcut", font_size=26, color=WHITE).shift(UP * 2.2)
        self.play(FadeIn(scm_title), run_time=0.5)
        
        # Spread out nodes horizontally: -4.5, -1.5, 1.5, 4.5
        y_node = causal_node("Y (Label)", LEFT * 4.5 + UP * 0.2, BLUE_D)
        core_node = causal_node("Core (Shape)", LEFT * 1.5 + UP * 0.2, BLUE_D)
        spur_node = causal_node("Spurious (BG)", RIGHT * 1.5 + UP * 0.2, RED)
        env_node = causal_node("Env", RIGHT * 4.5 + UP * 0.2, GREEN_D)
        
        a1_node = Arrow(y_node.get_right(), core_node.get_left(), color=BLUE_D)
        a2_node = Arrow(env_node.get_left(), spur_node.get_right(), color=GREEN_D)
        a3_node = CurvedArrow(y_node.get_bottom() + DOWN * 0.1, env_node.get_bottom() + DOWN * 0.1, angle=-PI / 3.5, color=RED)
        
        self.play(
            FadeIn(VGroup(y_node, core_node, env_node, spur_node, a1_node, a2_node, a3_node)),
            run_time=0.8
        )
        self.wait(2.5)
        
        scissors = Text("✂", font_size=36, color=RED).move_to(a3_node.get_center())
        self.play(FadeIn(scissors, scale=1.2), run_time=0.3)
        self.play(FadeOut(a3_node), FadeOut(scissors), Flash(a3_node.get_center(), color=RED), run_time=0.5)
        self.wait(3.0)
        
        # --- STEP 4: Generative Counterfactual Synthesis (Prevent prompt overflow!) ---
        self.play(FadeOut(VGroup(scm_title, y_node, core_node, env_node, spur_node, a1_node, a2_node)), run_time=0.5)
        
        gen_title = Text("Generative Counterfactual Synthesis", font_size=26, color=WHITE).shift(UP * 2.2)
        self.play(FadeIn(gen_title), run_time=0.5)
        
        # Make the box wider (7.5) and text slightly smaller (16) to completely prevent layout overflow!
        prompt_input = labeled_box('VLM Prompt: "Place a penguin on a sandy beach"', 7.5, 0.68, GOLD, 16).shift(UP * 0.6)
        synth_grid = VGroup(*[
            VGroup(simple_penguin(), Square(0.9, color=YELLOW_E).set_fill(YELLOW_E, 0.25)).arrange(IN).scale(0.7)
            for _ in range(5)
        ]).arrange(RIGHT, buff=0.25).shift(DOWN * 0.8)
        
        self.play(FadeIn(prompt_input, shift=DOWN * 0.1), run_time=0.5)
        self.wait(1.5)
        self.play(LaggedStart(*[FadeIn(s, scale=0.8) for s in synth_grid], lag_ratio=0.15), run_time=0.8)
        self.play(Flash(synth_grid, color=YELLOW_D), run_time=0.5)
        self.wait(3.0)
        
        # --- STEP 5: Final Narrative Arc summary (NO empty screen during final wait!) ---
        self.play(FadeOut(VGroup(gen_title, prompt_input, synth_grid)), run_time=0.5)
        
        arc_title = Text("The OOD Generalization Narrative Arc", font_size=26, color=GOLD, weight=BOLD).shift(UP * 2.2)
        self.play(FadeIn(arc_title), run_time=0.5)
        
        steps_flow = VGroup(
            Text("1. Model Scale", font_size=20, color=RED),
            Text("2. Fails OOD", font_size=20, color=RED),
            Text("3. AI Labels", font_size=20, color=GREEN_D),
            Text("4. AI Synthesizes", font_size=20, color=GREEN_D),
            Text("5. Robustness!", font_size=22, color=GOLD, weight=BOLD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).shift(LEFT * 1.5 + DOWN * 0.2)
        
        for i, st in enumerate(steps_flow):
            self.play(FadeIn(st, shift=RIGHT * 0.1), run_time=0.5)
            if i == 4:
                self.play(Circumscribe(st, color=GOLD), run_time=0.4)
            self.wait(1.0)
        
        self.active_wait(VGroup(steps_flow, arc_title), 1.0, GOLD)
