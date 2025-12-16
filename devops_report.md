
# DevOps Project Report – LabDevops

## Technologies Used
- **AWS**: Cloud infrastructure
- **Terraform**: Infrastructure as Code
- **Ansible**: Configuration management
- **Docker & Docker Compose**: Containerization
- **Kubernetes (Minikube)**: Container orchestration
- **PostgreSQL & Redis**: Persistence & caching
- **Git & GitHub**: Version control

---

## Pipeline & Infrastructure Diagram (Conceptual)
```
Developer → GitHub → Docker Build → Kubernetes Deployment
                     |
                  Terraform (AWS Infra)
                     |
                  Ansible (Config)
```

---

## Secret Management Strategy
- Kubernetes **Secrets** used for DB credentials
- Sensitive values not committed to Git
- Environment variables injected via ConfigMaps & Secrets

---

## Monitoring Strategy
(Current – Basic)
- `kubectl get pods`, `kubectl logs`
- Application health endpoint `/health/`

(Future Enhancements)
- Prometheus & Grafana
- AWS CloudWatch
- Alertmanager

---

## Lessons Learned
- Importance of Infrastructure as Code for repeatability
- Kubernetes service discovery via service names
- Managing secrets securely is critical
- Debugging containerized apps requires logs & pod inspection
- Collaboration is easier with proper branching strategy

---

## Conclusion
This project successfully demonstrates a complete DevOps lifecycle from infrastructure provisioning to Kubernetes deployment, fulfilling all academic requirements.
