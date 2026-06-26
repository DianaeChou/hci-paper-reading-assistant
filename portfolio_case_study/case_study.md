# HCI Paper Reading Assistant  
## AI-assisted Academic Sensemaking Workflow

## 1. Project Overview

HCI Paper Reading Assistant is a Python-based research workflow that helps early-stage HCI learners transform academic papers into structured reading notes.

The system takes HCI paper PDFs as input, extracts text from the documents, and uses an OpenAI-compatible API to generate structured reading reports. Each report includes the paper’s research problem, research questions, methodology, findings, contributions, limitations, relevance to Human-AI Interaction, and possible replication or extension ideas.

This project was designed as a small Human-AI Collaboration tool for academic sensemaking. Instead of replacing human reading, it scaffolds the reading process by making the structure of HCI papers easier to understand.

## 2. Problem Context

Reading HCI papers can be difficult for beginners because academic papers often combine theoretical framing, empirical methods, design implications, and implicit research contributions.

For early-stage learners, the challenge is not only to understand what a paper is about, but also to identify:

- What research problem the paper addresses
- Why the problem matters in HCI
- What research questions guide the study
- What methods are used
- What the main findings are
- What contribution the paper makes
- How the paper connects to Human-AI Interaction
- What can be replicated or extended in a small project

A generic summary is usually not enough for research training. Beginners need a structured reading framework that helps them move from passive reading to research-oriented interpretation.

## 3. Design Goal

The goal of this project is to build an AI-assisted workflow for structured HCI paper reading.

The assistant is designed to help users generate reusable research notes from academic PDFs. The output is organized around HCI-specific reading dimensions rather than generic summarization.

The main design goals are:

- Support beginners in understanding the structure of HCI papers
- Extract research-oriented information from dense academic text
- Make paper reading outputs reusable for literature review and project ideation
- Connect paper analysis with Human-AI Interaction research interests
- Generate replication and extension ideas for future small projects

## 4. System Workflow

The workflow consists of six steps:

```text
Input HCI Paper PDFs
        ↓
PDF Text Extraction with PyMuPDF
        ↓
HCI-specific Reading Prompt
        ↓
OpenAI-compatible API Call
        ↓
Markdown and JSON Output
        ↓
Reusable Research Notes
```

The system currently supports batch processing. When multiple PDF papers are placed in the `papers/` folder, the program automatically analyzes each paper and saves the generated reports in the `outputs/` folder.

## 5. Implementation

The project was implemented in Python.

Main technical components include:

- `PyMuPDF` for extracting text from PDF papers
- `python-dotenv` for managing local API configuration
- `OpenAI-compatible API` for language model analysis
- `Markdown` for readable research reports
- `JSON` for structured note export

The project uses a prompt template specifically designed for HCI paper reading. The prompt asks the model to analyze each paper through research-oriented sections, including problem framing, methodology, findings, contributions, limitations, and possible future extensions.

## 6. Input and Output

### Input

The input is one or more academic PDF papers placed in the `papers/` folder.

Example:

```text
papers/
├── Relational_Dissonance_in_Human-AI_Interactions_The_Case_of_Knowledge_Work.pdf
└── Are_We_Automating_the_Joy_Out_of_Work_Designing_AI_to_Augment_Work_Not_Meaning.pdf
```

### Output

For each paper, the system generates two files:

```text
outputs/
├── paper_name_reading_report.md
└── paper_name_structured_notes.json
```

The Markdown report is designed for human reading. The JSON file can be reused for later processing, such as literature review synthesis, paper comparison, or research topic clustering.

## 7. Output Structure

Each generated reading report includes the following sections:

1. Basic information  
2. One-sentence summary  
3. Research problem  
4. Research questions  
5. Theoretical background and key concepts  
6. Methodology  
7. Main findings  
8. Contributions  
9. Limitations  
10. Relevance to Human-AI Interaction  
11. Ideas for replication or extension  
12. Sentences useful for literature review  
13. Personal reflection questions  

This structure turns a paper from an unstructured academic PDF into a reusable research note.

## 8. Example Use Case

In the prototype, the assistant was tested on papers related to Human-AI Interaction and AI-supported knowledge work.

The generated reports helped organize each paper around:

- The central HCI problem
- The role of AI in knowledge work
- The relationship between automation and human meaning
- The methodological choices of the study
- The paper’s contribution to Human-AI Interaction research
- Possible small projects inspired by the paper

This makes the tool useful for HCI learners who want to build a literature review, prepare for research discussions, or identify possible project directions.

## 9. Project Value

This project demonstrates how LLM APIs can support academic sensemaking.

Its value is not only in summarizing papers, but in transforming academic reading into a structured research workflow. The assistant helps users understand papers in terms of research problems, methods, contributions, and future opportunities.

For HCI and Human-AI Interaction, the project also serves as a small example of AI-assisted knowledge work. The AI assistant does not replace the researcher’s judgment. Instead, it provides a scaffold that helps the researcher read, compare, and reflect more efficiently.

## 10. Current Limitations

The current version is a working prototype and has several limitations:

- It uses simple text extraction from PDFs, so output quality depends on PDF formatting.
- It uses simple truncation for long papers.
- It does not yet support citation-level extraction.
- It does not yet compare multiple papers across themes.
- The generated analysis still requires human checking and interpretation.
- It does not yet provide a graphical user interface.

## 11. Future Improvements

Future versions could include:

- Multi-paper comparison
- Literature review synthesis
- Research gap detection
- Paper clustering by topic
- Better long-document chunking
- Citation-aware extraction
- A simple Streamlit interface
- Export to Notion, Markdown knowledge base, or Zotero notes

## 12. Reflection

This project helped me understand how LLM APIs can be used to support research workflows beyond simple summarization.

The most important design decision was to make the assistant HCI-specific. A general paper summary is useful, but it does not fully support research training. For HCI learners, the reading process needs to highlight research problems, methodology, findings, contributions, limitations, and design implications.

This project also helped me connect technical implementation with Human-AI Interaction research. It shows how an AI system can support academic knowledge work by scaffolding the user’s sensemaking process rather than simply providing final answers.

## 13. Portfolio Positioning

This project can be positioned as:

**AI-assisted Research Workflow / Human-AI Collaboration for Academic Sensemaking / HCI Paper Reading Tool**

It is suitable for demonstrating skills in:

- Python workflow development
- API-based AI application prototyping
- Prompt design for research tasks
- HCI-oriented problem framing
- Academic sensemaking tool design
- Human-AI Interaction project development