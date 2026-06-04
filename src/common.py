from __future__ import annotations

import math
import random
from textwrap import wrap

from manim import *


CAUSAL_COLOR = BLUE_D
SPURIOUS_COLOR = RED
ENV_COLORS = [GREEN_D, YELLOW_D, PURPLE]
MATH_HL = GOLD
ALERT_COLOR = ORANGE
TEXT_COLOR = WHITE


class OODScene(MovingCameraScene):
    def setup(self):
        super().setup()
        self.camera.background_color = BLACK

    def title(self, text: str, subtitle: str | None = None):
        head = Text(text, font_size=42, color=WHITE, weight=BOLD)
        head.to_edge(UP, buff=0.35)
        if subtitle:
            sub = Text(subtitle, font_size=24, color=GRAY_B).next_to(head, DOWN, buff=0.15)
            group = VGroup(head, sub)
            self.play(FadeIn(group, shift=DOWN * 0.2))
            return group
        self.play(FadeIn(head, shift=DOWN * 0.2))
        return head

    def question(self, text: str, font_size: int = 42):
        q = paragraph(text, font_size=font_size, color=GOLD, width=30)
        self.play(Write(q), run_time=1.2)
        self.wait(0.5)
        self.play(q.animate.to_edge(UP, buff=0.4).scale(0.72))
        return q

    def clear_scene(self):
        if self.mobjects:
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.6)
        self.camera.frame.move_to(ORIGIN).set(width=config.frame_width)


def paragraph(text: str, font_size: int = 30, color=WHITE, width: int = 36, line_spacing: float = 0.7):
    lines: list[str] = []
    for raw in text.split("\n"):
        if not raw.strip():
            lines.append("")
            continue
        lines.extend(wrap(raw.strip(), width=width, break_long_words=False, break_on_hyphens=False))
    return Text("\n".join(lines), font_size=font_size, color=color, line_spacing=line_spacing)


def card(text: str, width: float = 5.2, height: float = 2.1, color=WHITE, fill=BLACK, font_size: int = 24):
    box = RoundedRectangle(width=width, height=height, corner_radius=0.12, color=color, stroke_width=2)
    box.set_fill(fill, opacity=0.18)
    body = paragraph(text, font_size=font_size, width=max(18, int(width * 8)))
    body.move_to(box.get_center())
    return VGroup(box, body)


def labeled_box(label: str, width: float = 3.2, height: float = 1.1, color=WHITE, font_size: int = 26):
    rect = RoundedRectangle(width=width, height=height, corner_radius=0.1, color=color, stroke_width=2)
    rect.set_fill(color, opacity=0.12)
    txt = paragraph(label, font_size=font_size, width=max(10, int(width * 7))).move_to(rect)
    return VGroup(rect, txt)


def bar(label: str, value: float, color=GREEN, width: float = 4.6):
    label_m = Text(label, font_size=22, color=WHITE)
    bg = Rectangle(width=width, height=0.22, color=GRAY_D, stroke_width=0).set_fill(GRAY_D, 0.65)
    fg = Rectangle(width=width * value, height=0.22, color=color, stroke_width=0).set_fill(color, 0.95)
    fg.move_to(bg).align_to(bg, LEFT)
    bar_stack = VGroup(bg, fg)
    pct = Text(f"{int(value * 100)}%", font_size=22, color=color)
    group = VGroup(label_m, bar_stack, pct).arrange(RIGHT, buff=0.2)
    return group


def dot_cloud(count: int, center, spread=(0.8, 0.45), color=BLUE, seed=0):
    random.seed(seed)
    dots = VGroup()
    for _ in range(count):
        x = random.uniform(-spread[0], spread[0])
        y = random.uniform(-spread[1], spread[1])
        dots.add(Dot(point=np.array(center) + RIGHT * x + UP * y, radius=0.06, color=color))
    return dots


def simple_penguin(color=BLUE_D):
    body = Ellipse(width=0.38, height=0.62, color=color).set_fill(color, 0.75)
    belly = Ellipse(width=0.22, height=0.38, color=WHITE).set_fill(WHITE, 0.9).move_to(body)
    head = Circle(radius=0.16, color=color).set_fill(color, 0.8).next_to(body, UP, buff=-0.08)
    return VGroup(body, belly, head).scale(0.7)


def simple_camel(color=YELLOW_D):
    body = RoundedRectangle(width=0.62, height=0.28, corner_radius=0.09, color=color).set_fill(color, 0.7)
    hump = Arc(radius=0.18, start_angle=0, angle=PI, color=color, stroke_width=6).move_to(body.get_top() + UP * 0.04)
    neck = Line(body.get_right() + UP * 0.08, body.get_right() + RIGHT * 0.25 + UP * 0.34, color=color, stroke_width=5)
    head = Circle(radius=0.09, color=color).set_fill(color, 0.75).move_to(neck.get_end() + RIGHT * 0.07)
    legs = VGroup(*[Line(body.get_bottom() + RIGHT * x, body.get_bottom() + RIGHT * x + DOWN * 0.25, color=color, stroke_width=4) for x in [-0.22, 0.2]])
    return VGroup(body, hump, neck, head, legs).scale(0.75)


def causal_node(label: str, pos, color=BLUE_D):
    c = Circle(radius=0.5, color=color).set_fill(color, 0.15)
    t = Text(label, font_size=26, color=WHITE).move_to(c)
    return VGroup(c, t).move_to(pos)


def make_axes_plane(x_label="spurious", y_label="core"):
    axes = Axes(
        x_range=[0, 10, 2],
        y_range=[0, 10, 2],
        x_length=8,
        y_length=4.8,
        axis_config={"color": GRAY_B, "include_ticks": False},
    )
    xl = Text(x_label, font_size=24, color=GRAY_B).next_to(axes.x_axis, DOWN)
    yl = Text(y_label, font_size=24, color=GRAY_B).rotate(PI / 2).next_to(axes.y_axis, LEFT)
    return VGroup(axes, xl, yl), axes

