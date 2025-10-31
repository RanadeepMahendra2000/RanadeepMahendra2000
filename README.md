# 👋 Hi, I'm Ranadeep Mahendra!

Full-Stack SWE (4+ yrs) building **Java/Spring Boot + React/Next.js** platforms on **AWS** with **Kafka, PostgreSQL, Docker/K8s, Terraform**, and production **RAG/LLM** features. I optimize for **p95 < 200ms**, **zero-downtime** releases, and clear **SLOs**.

[![Portfolio](https://img.shields.io/badge/Portfolio-ranadeepdev.online-4F46E5?logo=vercel&logoColor=white)](https://ranadeepdev.online)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-ranadeep--mahendra-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ranadeep-mahendra-6534b41b7/)
[![GitHub](https://img.shields.io/badge/GitHub-RanadeepMahendra2000-181717?logo=github)](https://github.com/RanadeepMahendra2000)
[![Email](https://img.shields.io/badge/Email-workwithranadeep%40gmail.com-EA4335?logo=gmail&logoColor=white)](mailto:workwithranadeep@gmail.com)

---
## 🏆 My LeetCode Progress

![Solved](https://img.shields.io/badge/Solved-73/3647-blue?cache=1754876697) ![Easy](https://img.shields.io/badge/Easy-41/890-brightgreen?cache=1754876697) ![Medium](https://img.shields.io/badge/Medium-31/1897-orange?cache=1754876697) ![Hard](https://img.shields.io/badge/Hard-1/860-red?cache=1754876697) 

### 📊 LeetCode Activity Graph

![Heatmap](https://leetcard.jacoblin.cool/ranadeep_mahendra2426?theme=dark&font=Karma&ext=heatmap&cache=1754876697)

---

## 🧰 Tech Stack
![Java](https://img.shields.io/badge/Java-17+-blue)
![Spring_Boot](https://img.shields.io/badge/Spring%20Boot-3.x-6DB33F)
![React](https://img.shields.io/badge/React-18-61DAFB)
![Next.js](https://img.shields.io/badge/Next.js-14-black)
![TypeScript](https://img.shields.io/badge/TypeScript-5-3178C6)
![Node.js](https://img.shields.io/badge/Node.js-20-339933)
![NestJS](https://img.shields.io/badge/NestJS-9-E0234E)
![FastAPI](https://img.shields.io/badge/FastAPI-0.1-009688)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-47A248)
![Redis](https://img.shields.io/badge/Redis-Cache-D82C20)
![Kafka](https://img.shields.io/badge/Kafka-Streams-231F20)
![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED)
![Kubernetes](https://img.shields.io/badge/Kubernetes-EKS-326CE5)
![Terraform](https://img.shields.io/badge/Terraform-IaC-7B42BC)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF)
![Grafana](https://img.shields.io/badge/Grafana-Observability-F46800)
![Prometheus](https://img.shields.io/badge/Prometheus-Metrics-E6522C)
![Elastic](https://img.shields.io/badge/Elastic-Search%2FLogs-005571)

---

## 🌟 Featured Projects
| Project | What it is | Impact | Stack |
|---|---|---|---|
| **Trade Settlement Platform** | High-throughput microservices for settlements | **1M+ tx/day**, **p95 < 200ms**, zero-downtime | Spring Boot • Kafka Streams • EKS • Redis • PostgreSQL |
| **Portfolio & Analytics APIs** | Portfolio/analytics surfaces for global managers | **1.5M+ logs/day**, reports **3h → <40m** | Spring Boot • GraphQL/REST • Redis • Elastic • Lambda |
| **GenAI Trade Insights Assistant** | RAG assistant over trades/positions | **6+ analyst-hours/day saved** | FastAPI • LangChain • OpenAI • pgvector/FAISS • S3 • Elastic |
| **Gmail Job Tracker** | Auto-tag & triage job emails | **~70% faster triage** | React • TypeScript • Supabase (RLS/Edge) • OAuth • CI/CD |

> More write-ups & live demos → **https://ranadeepdev.online**

---



**Architecture snapshot (Mermaid flow):**
```mermaid
flowchart TB
  subgraph Client
    UI[React/Next.js]
  end
  UI --> GW[API Gateway]
  subgraph AWS EKS
    SVC1[Spring Boot • Trades]
    SVC2[Spring Boot • Reconciliation]
  end
  GW --> SVC1
  GW --> SVC2
  SVC1 -- events --> KAFKA[(Kafka Streams)]
  SVC2 -- events --> KAFKA
  SVC1 --> PG[(PostgreSQL)]
  SVC2 --> PG
  KAFKA --> ES[(Elasticsearch/Kibana)]
```

**Analytics/Compliance query lifecycle (Mermaid sequence):**
```mermaid
sequenceDiagram
  autonumber
  participant UI as React Dashboards
  participant API as GraphQL/REST API
  participant Cache as Redis
  participant DB as PostgreSQL
  participant ES as Elastic
  UI->>API: Query positions/holdings
  API->>Cache: Check cached aggregates
  alt Cache Hit
    Cache-->>API: Aggregates
  else Cache Miss
    API->>DB: Param SQL + window functions
    API->>ES: Pull audit snippets
    DB-->>API: Rows + metrics
    ES-->>API: Logs/notes
    API->>Cache: Set short TTL
  end
  API-->>UI: JSON + facets
```

## 🧠 RAG / GenAI pipeline (fixed Mermaid)

```mermaid
flowchart LR
  Q["Analyst Question"] --> E["Embed Query"]
  E --> V["Vector DB (pgvector/FAISS)"]
  V --> C["Context Builder + Policies"]
  C --> L["LLM (LangChain/OpenAI)"]
  L --> A["Answer + Citations"]
  A --> Audit["Elastic Audit Log"]
```
**Zero-downtime release (Mermaid Gantt):**
```mermaid
gantt
  dateFormat  YYYY-MM-DD
  title Progressive Delivery
  section Build
  Compile & Unit Tests     :a1, 2025-01-01, 1d
  Dockerize & SBOM         :a2, after a1, 1d
  section Verify
  Contract/Smoke Tests     :b1, after a2, 1d
  Load Tests (k6)          :b2, 1d
  section Deploy
  Blue/Green to Staging    :c1, after b2, 1d
  Canary 10%→50%→100%      :c2, 1d
  Post-deploy SLO Watch    :c3, 1d
```

**Operating KPIs (snapshot):**
```
Latency p95 (ms): 230 → 190 → 170 → 155
Error rate (%):   1.1 → 0.7 → 0.4 → 0.3
MTTD (mins):      7   →  5  →  4  →  3
```


**Pin-worthy repos (rename to your actual repo names/links):**  
- 🚀 settlement-platform — Spring Boot + Kafka Streams on EKS (blue/green + canary)  
- 📈 portfolio-analytics-api — GraphQL/REST analytics with Redis caching  
- 🧠 genai-trade-assistant — FastAPI + LangChain RAG with pgvector/FAISS  
- ✉️ gmail-job-tracker — Supabase + OAuth, embeddings auto-tagging  
- 🧰 devops-iac-blueprints — Terraform modules, GitHub Actions, ArgoCD patterns  

**Contact:** workwithranadeep@gmail.com • +1-716-533-5625 • Florida, USA (open to relocate) • LinkedIn: linkedin.com/in/ranadeep-mahendra-6534b41b7 • Portfolio: ranadeepdev.online
