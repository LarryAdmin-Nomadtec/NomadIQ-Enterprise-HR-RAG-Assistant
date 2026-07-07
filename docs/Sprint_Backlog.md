# Agile Sprint Backlog

# Enterprise HR Knowledge Assistant with RAG

---

## Project Goal

Deliver an enterprise Retrieval-Augmented Generation (RAG) application that enables employees to ask natural-language HR policy questions and receive accurate, grounded responses using Amazon Bedrock.

---

# Epic 1 — Document Ingestion

## Sprint 1

### User Story

As an AI system, I need to ingest HR policy documents so they can be searched and queried.

### Tasks

- Load HR Leave Policy PDF
- Validate document ingestion
- Handle metadata
- Verify page loading

### Acceptance Criteria

- PDF loads successfully
- All pages are accessible

---

# Epic 2 — Document Processing

## Sprint 2

### User Story

As a retrieval system, I need to split documents into meaningful chunks for semantic search.

### Tasks

- Configure RecursiveCharacterTextSplitter
- Tune chunk size
- Configure overlap
- Validate chunk quality

### Acceptance Criteria

- Documents are chunked correctly
- Context continuity is maintained

---

# Epic 3 — Embeddings & Vector Store

## Sprint 3

### User Story

As a semantic search engine, I need to convert document chunks into vector embeddings.

### Tasks

- Configure Amazon Titan Embeddings V2
- Generate embeddings
- Create FAISS vector store
- Validate similarity search

### Acceptance Criteria

- Embeddings generated successfully
- Relevant chunks retrieved accurately

---

# Epic 4 — Large Language Model

## Sprint 4

### User Story

As an employee, I want accurate answers generated from HR policy documents.

### Tasks

- Configure Amazon Bedrock
- Connect Claude Sonnet
- Build retrieval pipeline
- Engineer grounded prompts

### Acceptance Criteria

- Accurate grounded responses
- Minimal hallucinations

---

# Epic 5 — Frontend Experience

## Sprint 5

### User Story

As an employee, I want a simple interface where I can ask HR questions.

### Tasks

- Build Streamlit UI
- Add branding
- Display responses
- Improve usability
- Add example questions

### Acceptance Criteria

- User can submit questions
- Responses display clearly
- Interface is intuitive

---

# Epic 6 — Documentation & Delivery

## Sprint 6

### User Story

As an AI Product Manager, I need complete project documentation so stakeholders understand the business value and technical implementation.

### Tasks

- Create README
- Document architecture
- Write Product Requirements Document
- Build Sprint Backlog
- Capture screenshots
- Prepare GitHub repository

### Acceptance Criteria

- Repository is production-quality
- Documentation is complete
- Ready for stakeholder review

---

# Success Metrics

- Accurate semantic retrieval
- Grounded AI responses
- Fast response times
- Positive user experience
- Professional documentation
- Production-ready repository