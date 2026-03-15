## Production Deployment Failure Debugging Approach

If production deployment fails after merge:
1. Identify blast radius — confirm whether issue affects staging or production only.
2. Check GitHub Actions logs to identify failing stage
3. SSH into Azure VM
4. Verify Docker container status using `docker ps`
5. Check container logs using `docker logs`
6. Validate environment variables and port bindings
7. Test application health endpoint locally inside VM
8. Rollback to last working commit using `git revert`
9. Rebuild Docker image and restart container
10. Monitor logs after redeployment

This structured approach minimizes downtime and ensures faster recovery.