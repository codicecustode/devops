## Production Deployment Failure Debugging Approach

If production deployment fails after merge:

1. Check GitHub Actions logs to identify failing stage
2. SSH into Azure VM
3. Verify Docker container status using `docker ps`
4. Check container logs using `docker logs`
5. Validate environment variables and port bindings
6. Test application health endpoint locally inside VM
7. Rollback to last working commit using `git revert`
8. Rebuild Docker image and restart container
9. Monitor logs after redeployment

This structured approach minimizes downtime and ensures faster recovery.