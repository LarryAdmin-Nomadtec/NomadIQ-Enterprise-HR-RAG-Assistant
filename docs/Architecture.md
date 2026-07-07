# System Architecture

# Enterprise HR Knowledge Assistant with Retrieval-Augmented Generation (RAG)

---

## Overview

The Enterprise HR Knowledge Assistant uses Retrieval-Augmented Generation (RAG) to answer employee questions using trusted HR policy documents rather than relying solely on an LLM's pre-trained knowledge.

This architecture minimizes hallucinations while improving response accuracy.

---

# High-Level Architecture

Employee
    │
    ▼
Streamlit Web Application
    │
    ▼
Python Backend (LangChain)
    │
    ├──────────────► Amazon Titan Embeddings
    │
    ▼
FAISS Vector Store
    │
    ▼
Similarity Search
    │
    ▼
Relevant Document Chunks
    │
    ▼
Amazon Bedrock
(Claude Sonnet)
    │
    ▼
Grounded Response
    │
    ▼
Employee

---

# Data Flow

## Step 1

Load the HR Leave Policy PDF.

---

## Step 2

Split the document into overlapping chunks using LangChain.

---

## Step 3

Generate semantic embeddings using Amazon Titan Embeddings V2.

---

## Step 4

Store embeddings inside a FAISS vector database.

---

## Step 5

User submits a natural language question.

---

## Step 6

FAISS performs semantic similarity search.

---

## Step 7

The most relevant document chunks are retrieved.

---

## Step 8

The retrieved context is combined with the user's question.

---

## Step 9

Amazon Bedrock invokes Claude Sonnet to generate a grounded response.

---

## Step 10

The response is returned to the Streamlit application.

---

# AWS Services

- Amazon Bedrock
- Amazon Titan Embeddings V2
- Anthropic Claude Sonnet
- AWS IAM Credentials

---

# Open Source Components

- LangChain
- FAISS
- Streamlit

---

# Security Considerations

- AWS credentials managed using local AWS profiles
- No HR documents sent outside Amazon Bedrock
- Semantic search limits unnecessary LLM context
- Grounded responses reduce hallucinations

---

# Scalability

Future enhancements may include:

- Amazon OpenSearch Serverless
- Amazon Bedrock Knowledge Bases
- Amazon S3 document storage
- Multiple HR policy documents
- Enterprise authentication (SSO)

---

# Cost Optimization

- Titan Embeddings generated once during indexing
- FAISS performs inexpensive local vector search
- Only relevant document chunks are sent to Bedrock
- Smaller prompts reduce token consumption and inference cost