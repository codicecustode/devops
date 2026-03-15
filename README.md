# DevOps Technical Assignment

This project demonstrates practical DevOps implementation including structured Git workflow, CI/CD automation, Docker-based deployment, environment separation, monitoring strategy and production debugging approach.

---

## 🔧 Tech Stack

- FastAPI (Python)
- Docker (Containerization)
- GitHub Actions (CI/CD)
- Azure Virtual Machine (Cloud Deployment)
- Nginx (Reverse Proxy)
- Git Branching Strategy (Feature → Develop → Main)

---

## 🌿 Branching Strategy

This repository follows a structured Git branching model:

- `main` → Production environment
- `develop` → Staging / integration environment
- `feature/*` → Feature development branches

### Workflow

1. Feature branch is created from `develop`
2. Pull Request is raised to `develop`
3. CI pipeline validates build & container health
4. Feature is merged into `develop` (staging deploy triggered)
5. Release PR is created from `develop` to `main`
6. Merge to `main` triggers production deployment

Branch protection practices:

- No direct push to `main`
- CI must pass before merge
- PR review required

---

## ⚙️ CI/CD Pipeline

CI/CD is implemented using GitHub Actions.

### CI Stage

- Dependency installation
- Syntax validation
- Docker image build verification
- Container health endpoint validation

### CD Stage

- `develop` branch → Deploys staging container
- `main` branch → Deploys production container
- Deployment happens via secure SSH automation into Azure VM
- Containers are rebuilt and restarted on each deployment

---

## 🚀 Deployment Architecture

Application is deployed on a single Azure VM using Docker containers.

### Runtime Architecture

- Production container runs on port **8000**
- Staging container runs on port **8001**
- Nginx reverse proxy routes external traffic
- CI pipeline performs automated remote deployment

### Live URLs

- Staging → `http://20.244.44.228/staging/health`
- Production → `http://20.244.44.228/prod/health`

---

## 🔐 Environment & Secrets Management

- SSH credentials stored in GitHub Secrets
- Environment variables passed during container runtime
- Azure Key Vault recommended for production scale deployments

---

## 🔁 Rollback Strategy

- Revert to previous Git commit
- Redeploy previous Docker image tag
- Restart container with last stable version
- Re-run CI/CD workflow

---

## 📊 Monitoring & Infrastructure Strategy

- Container logs monitored using `docker logs`
- Nginx access logs help identify traffic patterns
- Azure Monitor can track CPU / memory utilization
- Health endpoint alerts can detect service failure
- Horizontal container scaling can be implemented for load handling

---

## 🛠 Production Debugging Approach

If production deployment fails:

1. Identify blast radius (staging vs production impact)
2. Check GitHub Actions logs
3. SSH into Azure VM
4. Validate container status and logs
5. Verify environment configuration
6. Rollback to last stable release
7. Redeploy and monitor

---

## 🌟 Bonus Implementation

### Dockerization

The application is fully containerized using Docker with a production-ready image design:

- Dockerized application deployment
- Environment separation using container ports
- Reverse proxy routing via Nginx
- Cloud VM deployment on Azure
- CI validated container health checks
- Uses slim Python base image for reduced size
- Runs as non-root user for better security
- Includes container healthcheck endpoint
- Supports environment-based deployments
- Enables reproducible builds across environments

### Kubernetes Deployment Approach (High Level)

For large-scale production deployment, this architecture can be migrated to Kubernetes:

- Docker image can be deployed using Kubernetes Deployment resource
- Service object can expose application internally
- Ingress controller can replace Nginx reverse proxy
- Horizontal Pod Autoscaler can scale pods based on CPU / memory usage
- ConfigMaps and Secrets can manage runtime configuration
- Rolling updates can ensure zero downtime deployments

### AWS Exposure

Although this implementation uses Azure VM for deployment, similar architecture can be implemented on AWS using:

- EC2 instances for container hosting
- Application Load Balancer for routing
- CloudWatch for logs and metrics
- Auto Scaling Groups for infrastructure scaling
- ECS or EKS for container orchestration

---