# LabDevops – DevOps Final Project

## Overview
This project demonstrates an end-to-end DevOps workflow including:
- Infrastructure provisioning with Terraform (AWS)
- Configuration management with Ansible
- Containerization with Docker & Docker Compose
- Kubernetes deployment using Minikube
- CI-ready structure for team collaboration

---

## Prerequisites
- Git
- Docker & Docker Compose
- Minikube
- kubectl
- Terraform
- Ansible
- AWS Account (for Terraform step)

---

## Run Locally (Without Docker)
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Access: http://127.0.0.1:8000

---

## Run with Docker Compose
```bash
docker-compose up --build
```
Services:
- Django App: http://localhost:8000
- PostgreSQL
- Redis

---

## Run on Kubernetes (Minikube)
```bash
minikube start
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/
minikube service webapp -n dev
```

Check status:
```bash
kubectl get pods -n dev
kubectl get svc -n dev
```

---

## Infrastructure Setup (Terraform)
```bash
cd infra
terraform init
terraform apply
```

### Destroy Infrastructure
```bash
terraform destroy
```

---

## Ansible Configuration
```bash
cd ansible
ansible-playbook -i host.ini playbook.yaml
```

---

## Repository Structure
```
LabDevops/
├── infra/        # Terraform IaC
├── ansible/      # Configuration management
├── k8s/          # Kubernetes manifests
├── docker-compose.yml
├── Dockerfile
├── README.md
└── devops_report.md
```

---

## Contributors
- Minal (Infrastructure, Ansible, Kubernetes)
- Team Member 2 (CI/CD, Monitoring, Enhancements)
