# HCI Paper Reading Assistant

An API-based workflow that helps early-stage HCI researchers transform academic papers into structured reading notes.

This project extracts text from HCI paper PDFs and uses an OpenAI-compatible API to generate structured research notes, including research problems, research questions, methods, findings, contributions, limitations, and possible replication ideas.

## 1. Project Motivation

Reading HCI papers can be difficult for beginners because papers often contain dense theoretical background, complex methodology, and implicit research contributions.

This project explores how large language models can support academic sensemaking by turning unstructured paper text into structured reading reports. Instead of producing a generic summary, the assistant is designed around HCI-specific reading needs, such as identifying research questions, study methods, design implications, and opportunities for replication or extension.

## 2. What This Project Does

The assistant takes one or more PDF papers as input and generates:

- A Markdown reading report
- A JSON structured note file
- HCI-specific analysis sections
- Replication or extension ideas for future projects

The current version supports batch processing of multiple PDF files.

## 3. Workflow

```text
PDF Papers
   ↓
Text Extraction with PyMuPDF
   ↓
HCI-specific Prompt Template
   ↓
OpenAI-compatible API Call
   ↓
Structured Markdown Reading Report
   ↓
Reusable Literature Review Notes