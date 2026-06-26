import os
import json
from pathlib import Path

import fitz  # PyMuPDF
from dotenv import load_dotenv
from openai import OpenAI


BASE_DIR = Path(__file__).resolve().parent
PAPERS_DIR = BASE_DIR / "papers"
PROMPT_PATH = BASE_DIR / "prompts" / "paper_reading_prompt.txt"
OUTPUTS_DIR = BASE_DIR / "outputs"

OUTPUTS_DIR.mkdir(exist_ok=True)


def load_api_client():
    load_dotenv(BASE_DIR / ".env")

    api_key = os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("OPENAI_BASE_URL")

    if not api_key:
        raise ValueError("OPENAI_API_KEY not found. Please check your .env file.")

    if not base_url:
        raise ValueError("OPENAI_BASE_URL not found. Please check your .env file.")

    print(f"Base URL loaded: {base_url}")
    return OpenAI(api_key=api_key, base_url=base_url)


def extract_text_from_pdf(pdf_path: Path) -> str:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    doc = fitz.open(pdf_path)
    text_pages = []

    for page_number, page in enumerate(doc, start=1):
        text = page.get_text("text")
        text_pages.append(f"\n\n--- Page {page_number} ---\n{text}")

    doc.close()
    return "\n".join(text_pages)


def load_prompt() -> str:
    if not PROMPT_PATH.exists():
        raise FileNotFoundError(f"Prompt file not found: {PROMPT_PATH}")

    return PROMPT_PATH.read_text(encoding="utf-8")


def truncate_text(text: str, max_chars: int = 90000) -> str:
    """
    Version 1 uses simple truncation to avoid sending overly long papers.
    Later this can be upgraded to chunking or retrieval.
    """
    if len(text) <= max_chars:
        return text

    return text[:max_chars] + "\n\n[Text truncated due to length limit.]"


def analyze_paper(client: OpenAI, paper_text: str, prompt: str, model: str) -> str:
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": f"Please analyze the following HCI paper text:\n\n{paper_text}"
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content


def save_markdown_report(report: str, output_path: Path):
    output_path.write_text(report, encoding="utf-8")


def save_json_notes(report: str, output_path: Path):
    data = {
        "report_type": "HCI Paper Reading Report",
        "content": report
    }

    output_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )


def main():
    client = load_api_client()
    model = os.getenv("OPENAI_MODEL", "gpt-5.4-mini")

    pdf_files = list(PAPERS_DIR.glob("*.pdf"))

    if not pdf_files:
        print("No PDF files found in the papers/ folder.")
        return

    prompt = load_prompt()

    for pdf_path in pdf_files:
        print(f"Analyzing: {pdf_path.name}")

        paper_text = extract_text_from_pdf(pdf_path)
        paper_text = truncate_text(paper_text)

        report = analyze_paper(
            client=client,
            paper_text=paper_text,
            prompt=prompt,
            model=model
        )

        stem = pdf_path.stem
        md_output = OUTPUTS_DIR / f"{stem}_reading_report.md"
        json_output = OUTPUTS_DIR / f"{stem}_structured_notes.json"

        save_markdown_report(report, md_output)
        save_json_notes(report, json_output)

        print(f"Saved Markdown report: {md_output}")
        print(f"Saved JSON notes: {json_output}")

    print("All done.")


if __name__ == "__main__":
    main()