# Architecture

## V0.1

```text
User
  ↓
Interface
  ↓
Business Request + Documents
  ↓
Document Processing
  ↓
LLM
  ↓
Structured Analysis
  ↓
Interface


# Main Components

Interface — allows the analyst to provide a business request and upload documents.
Document Processing — extracts and prepares information from uploaded documents.
LLM — analyzes the request and available information.
Structured Analysis — organizes the AI output into clear, unclear, missing and further exploration areas.
Interface — presents the analysis, suggested questions and concise summary to the analyst.