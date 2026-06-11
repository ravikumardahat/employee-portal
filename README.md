# Employee Management Portal on Kubernetes

## Project Overview

Employee Management Portal is a cloud-native web application built using Flask and MySQL, containerized with Docker, and deployed on Kubernetes.

The project demonstrates modern DevOps and Kubernetes practices including CI/CD, container orchestration, persistent storage, secrets management, health checks, and application self-healing.

---

## Architecture

```text
GitHub
   |
GitHub Actions
   |
Docker Hub
   |
Kubernetes Cluster
   |
Ingress
   |
Service
   |
Flask Application
   |
MySQL StatefulSet
   |
Persistent Volume
```

---

## Features

### Application Features

* Add Employee
* View Employees
* Update Employee Details
* Delete Employees
* Bootstrap-based Web UI
* MySQL Backend Database

### Kubernetes Features

* Deployment with Multiple Replicas
* StatefulSet for MySQL
* Persistent Volume Claims (PVC)
* Headless Service
* NGINX Ingress Controller
* ConfigMap for Application Configuration
* Secret for Database Credentials
* Resource Requests and Limits
* Readiness Probe
* Liveness Probe
* Init Container
* Self-Healing Capability
* Rolling Updates

### CI/CD Features

* Source Code Management with GitHub
* Branching Strategy (main / dev)
* Automated Docker Image Build
* Automated Push to Docker Hub using GitHub Actions

---

## Repository Structure

```text
employee-portal/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   └── edit.html
│
├── k8s/
│   ├── emp-configmap.yaml
│   ├── emp-deployment.yaml
│   ├── emp-ingress.yaml
│   ├── emp-service.yaml
│   ├── mysql-headless-service.yaml
│   ├── mysql-secret.yaml
│   └── mysql-statefulset.yaml
│
└── .github/
    └── workflows/
        └── docker-build.yml
```

---

## Technology Stack

| Component          | Technology               |
| ------------------ | ------------------------ |
| Frontend           | HTML, Bootstrap          |
| Backend            | Flask (Python)           |
| Database           | MySQL                    |
| Container Runtime  | Docker                   |
| CI/CD              | GitHub Actions           |
| Container Registry | Docker Hub               |
| Orchestration      | Kubernetes               |
| Ingress            | NGINX Ingress Controller |

---

## Kubernetes Concepts Implemented

* Deployment
* Service
* Ingress
* ConfigMap
* Secret
* StatefulSet
* Persistent Volume Claim (PVC)
* Resource Requests & Limits
* Init Containers
* Readiness Probes
* Liveness Probes
* Rolling Updates
* Self-Healing

---

## Deployment Steps

### Clone Repository

```bash
git clone <repository-url>
cd employee-portal
```

### Apply Kubernetes Resources

```bash
kubectl apply -f k8s/
```

### Verify Resources

```bash
kubectl get pods
kubectl get svc
kubectl get ingress
kubectl get pvc
```

---

## Health Monitoring

The application uses:

### Readiness Probe

Ensures the pod receives traffic only when it is ready.

### Liveness Probe

Automatically restarts unhealthy containers.

### Init Container

Waits for MySQL availability before starting the Flask application.

---

## Security

Database credentials are stored using Kubernetes Secrets.

Application configuration is managed through Kubernetes ConfigMaps.

No sensitive credentials are hardcoded in the application source code.

---

## Future Enhancements

* Horizontal Pod Autoscaler (HPA)
* Pod Disruption Budget (PDB)
* Trivy Image Scanning
* Helm Charts
* ArgoCD GitOps Deployment
* Monitoring with Prometheus and Grafana

---

## Architecture Diagram

```text
                           +------------------+
                           |      GitHub      |
                           | Source Code Repo |
                           +---------+--------+
                                     |
                                     v
                         +----------------------+
                         |   GitHub Actions     |
                         |  CI/CD Pipeline      |
                         +----------+-----------+
                                    |
                                    v
                         +----------------------+
                         |     Docker Hub       |
                         | Container Registry   |
                         +----------+-----------+
                                    |
                                    v
+------------------------------------------------------------------+
|                      Kubernetes Cluster                          |
|                                                                  |
|  +-------------------+                                           |
|  | NGINX Ingress     |                                           |
|  | Controller        |                                           |
|  +---------+---------+                                           |
|            |                                                     |
|            v                                                     |
|  +-------------------+                                           |
|  |   emp-service     |                                           |
|  |   ClusterIP       |                                           |
|  +---------+---------+                                           |
|            |                                                     |
|    +-------+--------+                                            |
|    |                |                                            |
|    v                v                                            |
| +--------+      +--------+                                       |
| | Flask  |      | Flask  |                                       |
| | Pod-1  |      | Pod-2  |                                       |
| +---+----+      +---+----+                                       |
|     |               |                                            |
|     +-------+-------+                                            |
|             |                                                    |
|             v                                                    |
|      +-------------+                                             |
|      | ConfigMap   |                                             |
|      | App Config  |                                             |
|      +-------------+                                             |
|                                                                   |
|      +-------------+                                             |
|      | Secret      |                                             |
|      | DB Password |                                             |
|      +-------------+                                             |
|                                                                   |
|             |                                                    |
|             v                                                    |
|      +-------------+                                             |
|      | mysql       |                                             |
|      | HeadlessSvc |                                             |
|      +------+------+                                             |
|             |                                                    |
|             v                                                    |
|      +-------------+                                             |
|      | MySQL       |                                             |
|      | StatefulSet |                                             |
|      +------+------+                                             |
|             |                                                    |
|             v                                                    |
|      +-------------+                                             |
|      | PVC         |                                             |
|      | Persistent  |                                             |
|      | Storage     |                                             |
|      +-------------+                                             |
|                                                                  |
+------------------------------------------------------------------+
```


## Author

Ravi Kumar

DevOps | Linux | Kubernetes | Cloud Infrastructure
