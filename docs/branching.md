## Branching Strategy

This project follows a structured Git branching model:

- `main` → Production environment
- `develop` → Staging / integration environment
- `feature/*` → Feature development branches

### Workflow

1. Developer creates a feature branch from `develop`
2. Feature is implemented and pushed
3. Pull Request is created to `develop`
4. CI pipeline validates build and container health
5. After approval, feature is merged into `develop`
6. Release Pull Request is created from `develop` to `main`
7. On merge to `main`, production deployment is triggered

### Conflict Resolution Approach

Before merging, the feature branch is rebased or merged with latest `develop` branch.
Conflicts are resolved locally, tested again, and then pushed.

### Branch Protection Strategy

Even though GitHub free plan does not enforce strict protection:

- Direct push to `main` is avoided
- Pull Request approval is required
- CI pipeline must pass before merge
- Feature branches are short-lived