# Production RAG Platform

A scalable, containerized **Retrieval-Augmented Generation** backend. This isn't a basic wrapper script—it’s a modular system designed for production-grade AI infrastructure using FastAPI, Qdrant, and K8s.

## 🚀 The Stack
* **API:** FastAPI (Asynchronous, streaming responses)
* **Vector DB:** Qdrant (Hybrid search ready)
* **Embeddings:** Sentence-Transformers (Local/HuggingFace)
* **Infrastructure:** Docker + Kubernetes
* **Observability:** Prometheus metrics & Structured logging

## 🏗️ System Architecture
The platform follows a decoupled service pattern to ensure horizontal scalability:

1. **Ingestion Pipeline:** Raw Docs → Intelligent Chunking → Embedding Model → Qdrant Index.
2. **Query Lifecycle:** User Question → Semantic Search → Context Injection → LLM (Streaming) → Response.

Project Highlights
Streaming Support: Reduced perceived latency via token-by-token generation.

Production Guardrails: Built-in API key auth and rate limiting to prevent cost/resource spikes.

K8s Ready: Includes deployment manifests (k8s/) for scaling the retriever and API independently.

Observability: Built-in /metrics endpoint for Prometheus/Grafana monitoring.
