# InsightFlow: Enterprise-Grade RAG Architecture

[![Status: Private Preview](https://img.shields.io/badge/Status-Private_Preview-blue.svg)]()
[![Azure: Deployed](https://img.shields.io/badge/Azure-Deployed-0078D4.svg)]()
[![Python: 3.13](https://img.shields.io/badge/Python-3.13-3776AB.svg)]()

## 1. Project Overview
InsightFlow is a "Private Brain" Retrieval-Augmented Generation (RAG) system engineered for the FinTech and GovTech sectors. It solves the critical "Hallucination" and "Data Sovereignty" trade-offs inherent in standard LLM deployments.

## 2. Core Architectural Principles
* **Zero-Trust Verifiability:** Every generated claim is strictly anchored to PDF coordinates via a custom `Citation Mapper` algorithm. (The "Glass Box" approach).
* **Data Sovereignty:** Full deployment within Azure Virtual Networks (VNet). No data leakage to public OpenAI endpoints.
* **Multi-Tenant Security:** Role-Based Access Control (RBAC) enforced at the Azure AI Search vector index level.

## 3. System Architecture
*(System architecture diagram illustrating the split-screen verification UI and the backend orchestration layer.)*

![System Architecture](./docs/architecture/architecture-diagram.png)

## 4. Technology Stack
* **Cloud Infrastructure:** Microsoft Azure (Azure OpenAI GPT-4, Azure AI Search, Blob Storage)
* **Orchestration Layer:** Python 3.11, FastAPI, LangChain
* **Client UI:** Flutter / Next.js (Split-screen document verification)
* **Infrastructure as Code (IaC):** Azure Bicep

## 5. Directory Structure (Preview)
```text
├── docs/                  # Architecture diagrams and whitepapers
├── infra/                 # Azure Bicep templates for resource provisioning
├── src/
│   ├── api/               # FastAPI routing and endpoints
│   ├── core/              # RBAC security and configurations
│   └── services/          # Core RAG engine & Citation Mapping logic
│   └── engines/          # Core RAG engine & Citation Mapping logic
└── tests/                 # RAGAS evaluation metrics (Faithfulness & Relevance)

Development Roadmap

[] Phase 0	Mock/Dify UI	UX Validation & Citation Flow	Completed

[] Phase 1	Headless Dify API	Decoupling Frontend from Orchestration	In Progress

[] Phase 2	Azure Native RAG	Enterprise Compliance & Security (VNet)	Spring 2026

© 2026 Shengwei Liu. Architected for Trust.