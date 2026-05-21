# Kubernetes Cluster Preparation

This document summarizes the Kubernetes cluster preparation workflow used in Project 2.

The original workflow was documented in Trello and later used in the technical report. Real IP addresses, SSH keys, and environment-specific access details are not included in this public repository.

## Phase 1: VM Launch

The worker virtual machines were launched using the project deployment script.

```bash
chmod +x deploy_all.sh
./deploy.sh