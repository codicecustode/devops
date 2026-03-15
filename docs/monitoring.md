## Monitoring and Infrastructure Strategy

### Logging

- Application logs are collected via `docker logs`
- Nginx access logs help identify traffic patterns
- Azure Monitor / ELK stack can be integrated for centralized logging

### Downtime Handling

- Docker container restart policies improve resilience
- Healthcheck endpoint ensures service availability
- Load balancer can be added for redundancy

### Scaling Strategy

- Horizontal scaling using multiple containers
- VM Scale Sets or Kubernetes for auto-scaling
- Stateless architecture to allow scaling

### API Credit Monitoring

- Middleware can track API usage
- Threshold alerts can notify via email or Slack

### Cost Optimization

- Use smaller VM size for staging
- Schedule non-production shutdown during low usage
- Use autoscaling to match demand

### Secrets Management

- GitHub Secrets
- Azure Key Vault
- Avoid storing secrets in codebase