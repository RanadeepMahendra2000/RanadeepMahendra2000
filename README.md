# 👋 Hi, I'm Ranadeep Mahendra!

## 🏆 My LeetCode Progress

![Solved](https://img.shields.io/badge/Solved-73/3647-blue?cache=1754876697) ![Easy](https://img.shields.io/badge/Easy-41/890-brightgreen?cache=1754876697) ![Medium](https://img.shields.io/badge/Medium-31/1897-orange?cache=1754876697) ![Hard](https://img.shields.io/badge/Hard-1/860-red?cache=1754876697) 

### 📊 LeetCode Activity Graph

![Heatmap](https://leetcard.jacoblin.cool/ranadeep_mahendra2426?theme=dark&font=Karma&ext=heatmap&cache=1754876697)
sequenceDiagram
  autonumber
  participant Dev as Developer
  participant CI as GitHub Actions
  participant REG as Container Registry
  participant CD as ArgoCD
  participant K8s as EKS
  Dev->>CI: Push/PR
  CI->>CI: Build • Unit/Contract/Static Scans
  CI->>REG: Push Image + SBOM
  CI->>CD: Update Helm/Manifests
  CD->>K8s: Progressive rollout (blue/green/canary)
  K8s-->>CD: Health & SLO checks
  CD-->>Dev: Status + metrics
