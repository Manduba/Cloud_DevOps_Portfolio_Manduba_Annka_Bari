# Validation Commands

This document records the validation commands used during Project 2.

These commands are documented for portfolio and workflow reference only. They are not intended to be run directly from this repository.

## Kubernetes Cluster Validation

```bash
kubectl get nodes
kubectl get pods -o wide
kubectl get svc
curl http://<worker-ip>:30000
