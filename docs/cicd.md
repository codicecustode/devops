## CI/CD Pipeline Flow

CI/CD is implemented using GitHub Actions.

### CI Flow

- Pipeline triggers on Pull Requests to `develop` and `main`
- Dependencies are installed
- Syntax validation is performed
- Docker image build is tested
- Container health endpoint is validated

If any step fails, the PR cannot be safely merged.

### CD Flow

- Push to `develop` triggers staging deployment
- Push to `main` triggers production deployment
- Deployment happens via SSH into Azure VM
- Docker container is rebuilt and restarted

This ensures continuous delivery with minimal manual intervention.


### Deployment Safety Controls

- Docker image is built and container health endpoint is validated during CI stage.
- SSH based deployment ensures immutable infrastructure pattern where container is recreated on each release.