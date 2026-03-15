## Deployment Architecture

Application is deployed on an Azure Virtual Machine using Docker.

Two environments are maintained on the same VM:

- Staging → Container running on port 8001 (develop branch)
- Production → Container running on port 8000 (main branch)

Nginx reverse proxy routes traffic to appropriate containers.

### Environment Variable Management

Sensitive values are not stored in the repository.

They are managed using:

- GitHub Secrets for CI/CD authentication
- Environment variables inside Docker runtime
- Azure Key Vault can be used in real production

### Rollback Strategy

If deployment fails:

- Previous commit can be reverted
- Older Docker image can be redeployed
- Container can be restarted with previous tag
- GitHub Actions workflow can be re-run