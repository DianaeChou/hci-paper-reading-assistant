from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


PROJECT_DIR = Path(__file__).resolve().parent.parent
OUTPUT_PATH = PROJECT_DIR / "assets" / "workflow.png"

W, H = 1900, 1250

COLORS = {
    "bg": "#F7F3EA",
    "navy": "#1E2A32",
    "text": "#3D4A53",
    "muted": "#68747D",
    "line": "#8B6F47",
    "border": "#D3C4A5",
    "shadow": "#E5DCCB",
    "cream": "#FFFDF7",
    "sand": "#EFE3CC",
    "green": "#E6EFEA",
    "blue": "#E8EEF3",
    "rose": "#F3E4DA",
    "lavender": "#ECE8F3",
    "footer": "#EFE4D0",
}


def font(size, bold=False):
    paths = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for path in paths:
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            continue
    return ImageFont.load_default()


TITLE_FONT = font(68, bold=True)
SUBTITLE_FONT = font(31)
STEP_FONT = font(22, bold=True)
BOX_TITLE_FONT = font(32, bold=True)
BOX_BODY_FONT = font(24)
SECTION_FONT = font(28, bold=True)
FOOTER_FONT = font(24)


img = Image.new("RGB", (W, H), COLORS["bg"])
draw = ImageDraw.Draw(img)


def text_width(text, used_font):
    box = draw.textbbox((0, 0), text, font=used_font)
    return box[2] - box[0]


def center_text(x, y, w, text, used_font, fill):
    tw = text_width(text, used_font)
    draw.text((x + (w - tw) / 2, y), text, font=used_font, fill=fill)


def draw_module(x, y, w, h, step, title, lines, fill):
    # shadow
    draw.rounded_rectangle(
        (x + 8, y + 10, x + w + 8, y + h + 10),
        radius=32,
        fill=COLORS["shadow"],
    )

    # box
    draw.rounded_rectangle(
        (x, y, x + w, y + h),
        radius=32,
        fill=fill,
        outline=COLORS["border"],
        width=3,
    )

    # step pill
    pill_w, pill_h = 74, 34
    draw.rounded_rectangle(
        (x + 30, y + 26, x + 30 + pill_w, y + 26 + pill_h),
        radius=17,
        fill=COLORS["navy"],
    )
    center_text(x + 30, y + 31, pill_w, step, STEP_FONT, "#FFFFFF")

    # title
    draw.text((x + 30, y + 82), title, font=BOX_TITLE_FONT, fill=COLORS["navy"])

    # body lines
    yy = y + 136
    for line in lines:
        draw.text((x + 34, yy), "• " + line, font=BOX_BODY_FONT, fill=COLORS["muted"])
        yy += 36


def arrow_right(x1, y1, x2, y2):
    draw.line((x1, y1, x2, y2), fill=COLORS["line"], width=6)
    draw.polygon([(x2, y2), (x2 - 22, y2 - 14), (x2 - 22, y2 + 14)], fill=COLORS["line"])


def arrow_left(x1, y1, x2, y2):
    draw.line((x1, y1, x2, y2), fill=COLORS["line"], width=6)
    draw.polygon([(x2, y2), (x2 + 22, y2 - 14), (x2 + 22, y2 + 14)], fill=COLORS["line"])


def arrow_down(x, y1, y2):
    draw.line((x, y1, x, y2), fill=COLORS["line"], width=6)
    draw.polygon([(x, y2), (x - 14, y2 - 22), (x + 14, y2 - 22)], fill=COLORS["line"])


def draw_footer_box(x, y, w, h, title, body):
    draw.rounded_rectangle(
        (x, y, x + w, y + h),
        radius=26,
        fill=COLORS["footer"],
        outline=COLORS["border"],
        width=2,
    )
    draw.text((x + 32, y + 24), title, font=SECTION_FONT, fill=COLORS["navy"])
    draw.text((x + 32, y + 72), body, font=FOOTER_FONT, fill=COLORS["text"])


# Header
draw.text((100, 70), "HCI Paper Reading Assistant", font=TITLE_FONT, fill=COLORS["navy"])
draw.text(
    (105, 152),
    "A structured AI workflow for transforming HCI papers into reusable research notes",
    font=SUBTITLE_FONT,
    fill=COLORS["muted"],
)

# Main workflow layout
box_w = 470
box_h = 245

x_left = 100
x_mid = 715
x_right = 1330

y_top = 275
y_bottom = 610

modules = [
    (
        x_left,
        y_top,
        "01",
        "Input Layer",
        ["HCI / HAI paper PDFs", "Multiple papers supported", "Local papers/ folder"],
        COLORS["cream"],
    ),
    (
        x_mid,
        y_top,
        "02",
        "Text Processing",
        ["Extract text with PyMuPDF", "Preserve page structure", "Prepare text for analysis"],
        COLORS["sand"],
    ),
    (
        x_right,
        y_top,
        "03",
        "HCI Reading Prompt",
        ["Research problem", "Method and findings", "Contribution and limitation"],
        COLORS["green"],
    ),
    (
        x_right,
        y_bottom,
        "04",
        "API Analysis",
        ["OpenAI-compatible API", "Structured LLM analysis", "HCI-focused interpretation"],
        COLORS["blue"],
    ),
    (
        x_mid,
        y_bottom,
        "05",
        "Output Layer",
        ["Markdown reading report", "JSON structured notes", "Reusable research materials"],
        COLORS["rose"],
    ),
    (
        x_left,
        y_bottom,
        "06",
        "Research Reuse",
        ["Literature review support", "Paper discussion preparation", "Project idea generation"],
        COLORS["lavender"],
    ),
]

for x, y, step, title, lines, fill in modules:
    draw_module(x, y, box_w, box_h, step, title, lines, fill)

# Arrows
top_mid_y = y_top + box_h // 2
bottom_mid_y = y_bottom + box_h // 2

arrow_right(x_left + box_w + 28, top_mid_y, x_mid - 28, top_mid_y)
arrow_right(x_mid + box_w + 28, top_mid_y, x_right - 28, top_mid_y)

arrow_down(x_right + box_w // 2, y_top + box_h + 30, y_bottom - 30)

arrow_left(x_right - 28, bottom_mid_y, x_mid + box_w + 28, bottom_mid_y)
arrow_left(x_mid - 28, bottom_mid_y, x_left + box_w + 28, bottom_mid_y)

# Project components section
component_x = 100
component_y = 925
component_w = 1700
component_h = 135

draw_footer_box(
    component_x,
    component_y,
    component_w,
    component_h,
    "Project Components",
    "main.py · prompts/ · papers/ · outputs/ · examples/ · assets/ · portfolio_case_study/ · README.md",
)

# Positioning section
position_y = 1085
draw_footer_box(
    component_x,
    position_y,
    component_w,
    105,
    "Portfolio Positioning",
    "AI-assisted Research Workflow · Academic Sensemaking Tool · Human-AI Collaboration for HCI Research Training",
)

img.save(OUTPUT_PATH)
print(f"Workflow image saved to: {OUTPUT_PATH}")