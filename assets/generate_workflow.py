from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
ASSETS_DIR.mkdir(exist_ok=True)

output_path = ASSETS_DIR / "workflow.png"

W, H = 1800, 1050
img = Image.new("RGB", (W, H), "#F7F3EA")
draw = ImageDraw.Draw(img)

try:
    title_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 64)
    subtitle_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 32)
    box_title_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 34)
    box_text_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 25)
    small_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 22)
except:
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()
    box_title_font = ImageFont.load_default()
    box_text_font = ImageFont.load_default()
    small_font = ImageFont.load_default()

# Colors
navy = "#1D2A35"
blue = "#4C7A89"
teal = "#6FA89A"
sand = "#E6D5B8"
cream = "#FFFDF7"
brown = "#9A6B4F"
gray = "#5C6670"
line = "#B8A88A"

# Header
draw.text((90, 70), "HCI Paper Reading Assistant", fill=navy, font=title_font)
draw.text(
    (95, 150),
    "An API-based workflow for transforming HCI papers into structured research notes",
    fill=gray,
    font=subtitle_font
)

# Helper functions
def rounded_box(x, y, w, h, title, body, fill, outline="#D8C8A8"):
    draw.rounded_rectangle((x, y, x + w, y + h), radius=28, fill=fill, outline=outline, width=3)
    draw.text((x + 34, y + 28), title, fill=navy, font=box_title_font)

    body_lines = body.split("\n")
    yy = y + 82
    for line_text in body_lines:
        draw.text((x + 34, yy), line_text, fill=gray, font=box_text_font)
        yy += 36

def arrow(x1, y1, x2, y2):
    draw.line((x1, y1, x2, y2), fill=brown, width=5)
    # arrow head
    if x2 > x1:
        draw.polygon([(x2, y2), (x2 - 18, y2 - 11), (x2 - 18, y2 + 11)], fill=brown)
    elif y2 > y1:
        draw.polygon([(x2, y2), (x2 - 11, y2 - 18), (x2 + 11, y2 - 18)], fill=brown)

# Layout
box_w = 420
box_h = 180
gap_x = 110

x1, y1 = 110, 300
x2, y2 = x1 + box_w + gap_x, 300
x3, y3 = x2 + box_w + gap_x, 300

x4, y4 = 110, 650
x5, y5 = x4 + box_w + gap_x, 650
x6, y6 = x5 + box_w + gap_x, 650

rounded_box(
    x1, y1, box_w, box_h,
    "1. PDF Papers",
    "Input academic papers\nfrom HCI / HAI research",
    cream
)

rounded_box(
    x2, y2, box_w, box_h,
    "2. Text Extraction",
    "Use PyMuPDF to extract\npaper text from PDFs",
    "#F3E9D6"
)

rounded_box(
    x3, y3, box_w, box_h,
    "3. HCI Prompt",
    "Apply a reading framework:\nproblem, method, findings",
    "#E8F0EC"
)

rounded_box(
    x4, y4, box_w, box_h,
    "4. API Analysis",
    "Call OpenAI-compatible API\nfor structured interpretation",
    "#E9EEF2"
)

rounded_box(
    x5, y5, box_w, box_h,
    "5. Reading Report",
    "Generate Markdown notes\nfor human reading",
    "#F4E6DC"
)

rounded_box(
    x6, y6, box_w, box_h,
    "6. Research Reuse",
    "Support literature review,\npaper discussion, project ideas",
    "#E6EFEA"
)

# Arrows
arrow(x1 + box_w, y1 + box_h / 2, x2, y2 + box_h / 2)
arrow(x2 + box_w, y2 + box_h / 2, x3, y3 + box_h / 2)
arrow(x3 + box_w / 2, y3 + box_h, x3 + box_w / 2, y5)
arrow(x3, y5 + box_h / 2, x5 + box_w, y5 + box_h / 2)
arrow(x5 + box_w, y5 + box_h / 2, x6, y6 + box_h / 2)

# Connection label
draw.text((700, 555), "LLM-supported academic sensemaking", fill=brown, font=small_font)

# Bottom note
draw.rounded_rectangle((90, 925, 1710, 990), radius=22, fill="#EFE4D0", outline="#D8C8A8", width=2)
draw.text(
    (125, 945),
    "Positioning: Human-AI Collaboration for Academic Sensemaking · HCI Research Training Tool · API-based AI Workflow",
    fill=navy,
    font=small_font
)

img.save(output_path)
print(f"Workflow image saved to: {output_path}")