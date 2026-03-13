# System Architecture

The RAG platform is composed of multiple subsystems:

User Interface
↓
FastAPI API Layer
↓
Authentication + Rate Limiting
↓
Retriever Service
↓
Vector Database (Qdrant)
↓
Prompt Builder
↓
LLM Runtime
↓
Streaming Response

Supporting pipelines:

Document Storage
↓
Ingestion Pipeline
↓
Chunking Engine
↓
Embedding Model
↓
Vector Database Indexing

Infrastructure Layer:

Docker Containers
↓
Kubernetes Deployment
↓
Prometheus Metrics
↓
Logging System

