# Raspberry Pi GitOps Cluster (k3s + ArgoCD + GitHub Actions)

This project demonstrates a professional **GitOps workflow** running on a **Raspberry Pi cluster** using **k3s**. It automates the entire lifecycle of microservices from code commit and multi-arch Docker builds to automated deployment via ArgoCD.

---

## 🚀 Project Overview

The goal of this project is to implement a modern, automated "Home Lab" infrastructure that follows industry-standard DevOps practices:
- **CI/CD Pipeline**: GitHub Actions builds Docker images for **ARM64** architecture and pushes them to GitHub Container Registry (GHCR).
- **GitOps Deployment**: **ArgoCD** monitors the repository and synchronizes the state of the cluster with the defined Kubernetes manifests.
- **Microservices Stack**: 
  - **System Monitor**: Real-time CPU temperature and usage monitoring.
  - **Redis Counter**: A stateful application demonstrating inter-pod communication with a Redis database.
  - **Weather Station**: Integration with external APIs to merge local hardware data with cloud data.
- **Traffic Management**: **Traefik** acts as the Ingress Controller, managing routing and providing a centralized dashboard.

---

## 🧩 Architecture

```text
  ┌────────────────┐       ┌──────────────────────────┐       ┌──────────────────────┐
  │  Developer PC  │       │      GitHub Cloud        │       │     Raspberry Pi     │
  │  (git push)    │──────▶│  Actions + Container Reg │──────▶│   k3s + ArgoCD       │
  └────────────────┘       └─────────────┬────────────┘       └──────────┬───────────┘
                                         │                               │
                                         ▼                               ▼
                           ┌──────────────────────────┐       ┌──────────────────────┐
                           │ Multi-Arch Docker Build  │       │  [Target Microapps]  │
                           │ (Linux/ARM64 via QEMU)   │       │ - System Monitor     │
                           └──────────────────────────┘       │ - Redis Counter      │
                                                              │ - Weather Station    │
                                                              └──────────────────────┘
```

---

## 🛠️ Tech Stack
| Tool | Purpose |
| ------------------------- | --------------------------------------------------- |
| **k3s** | Lightweight Kubernetes distribution for Edge/ARM |
| **ArgoCD** | GitOps tool for automated Kubernetes deployments |
| **GitHub Actions** | CI/CD platform for automated building and testing |
| **Docker + QEMU** | Multi-platform builds (x86_64 to ARM64) |
| **Traefik** | Ingress Controller and Edge Router |
| **Redis** | In-memory data structure store used as a database |
| **Python (Flask)** | Language used for microservices development |

---

## ⚙️ Project Structure

```text
raspberry-pi-gitops/
├── .github/workflows/         # CI/CD Pipeline definitions
│   ├── build-monitor.yaml     # Build/Push System Monitor image
│   ├── build-counter.yaml     # Build/Push Redis Counter image
│   └── build-weather.yaml     # Build/Push Weather Station image
├── apps/                      # Microservices source code & manifests
│   ├── system-monitor/        # App 1: Hardware metrics
│   ├── redis-counter/         # App 2: Python + Redis integration
│   └── weather-station/       # App 3: Cloud API + Local Hardware data
│       ├── k8s/               # Kubernetes Manifests (Deploy, Service, Ingress)
│       ├── app.py             # Application Logic
│       └── Dockerfile         # Container Recipe
├── infrastructure/            # Cluster-wide configurations
│   └── traefik-config/        # Traefik Dashboard & Middlewares
└── README.md
```

---

## 🧠 Key Features
- ✅ **Infrastructure as Code (IaC)**: Entire cluster state is defined in YAML manifests for full reproducibility.
- ✅ **Multi-Arch CI/CD**: Automatic Docker image builds for **ARM64** architecture using GitHub Actions and QEMU.
- ✅ **Service Discovery**: Internal Kubernetes DNS allows seamless communication between microservices (e.g., Python app to Redis).
- ✅ **Edge Routing**: Centralized traffic management using Traefik with advanced PathPrefix routing and Middlewares.
- ✅ **Hardware Integration**: Secure access to Raspberry Pi thermal sensors via Kubernetes `hostPath` volume mounts.
- ✅ **GitOps Principles**: ArgoCD ensures that the live cluster state always matches the configuration stored in the Git repository.

---

## 📸 Example Dashboard
Once the ArgoCD sync is complete, the following endpoints will be accessible via your cluster's Ingress (Traefik):

| Service | Path      | Description |
| ------- |-----------| ----------- |
| **System Monitor** | `/monitor` | Real-time CPU temperature and load metrics. |
| **Redis Counter** | `/counter` | Visit counter stored in a stateful Redis database. |
| **Weather Station** | `/weather` | Dashboard merging local thermal data with Open-Meteo API. |
| **Traefik UI** | `/dashboard/` | Infrastructure overview and routing status. |
| **ArgoCD UI** | `/argocd` | GitOps lifecycle and deployment synchronization status. |

---

## 📚 Future Improvements
- [ ] **Persistent Storage**: Implement **Longhorn** or **Local Path Provisioner** to ensure Redis data persists across pod restarts.
- [ ] **Automated SSL/TLS**: Configure **Cert-Manager** with Let's Encrypt to enable HTTPS for all public-facing services.
- [ ] **Monitoring & Observability**: Deploy a **Prometheus** and **Grafana** stack to visualize historical hardware and cluster metrics.
- [ ] **Secrets Management**: Integrate **Bitnami Sealed Secrets** to securely store sensitive data (like API keys) within the Git repository.
- [ ] **Node Scalability**: Expand the cluster with additional Raspberry Pi nodes to demonstrate high availability (HA).

---

## 🧑‍💻 Author
- Jakub Jasiński
- Cloud & DevOps Engineer
- 🌐 github.com/KoJotPG