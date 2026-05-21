# DevOps and Cloud Infrastructure Portfolio

This repository contains selected academic projects from my MSc in Cloud-based Services and Operations at OsloMet. The projects document hands-on work with DevOps practices, cloud infrastructure, automation, containerization, Kubernetes, distributed storage, observability, and CI/CD prototypes.

## Projects

### 1. Canario DevOps Prototype

The Canario project demonstrates a DevOps transition prototype for a web application. It includes a FastAPI application, Docker containerization, and a GitLab CI/CD pipeline prototype with build and test stages.

Main topics:

- FastAPI web application
- Docker containerization
- GitLab CI/CD prototype
- Environment-variable-based feature control
- DevOps transition planning

Folder: [`project-1-Canario-devops/`](project-1-Canario-devops/)

### 2. Kubernetes Rook-Ceph Storage and Observability Project

This project was completed as part of the ACIT 4430 Infrastructure Services and Operations course at OsloMet. The goal was to design and test a Kubernetes-based storage solution using Rook-Ceph on OpenStack.

Main topics:

- Terraform for OpenStack provisioning
- Ansible for configuration automation
- Kubernetes cluster deployment using Kubespray
- Rook-Ceph storage setup
- Observability setup using Prometheus, Grafana, and Loki
- Backup integration attempt using Kasten K10 and MinIO
- Troubleshooting of Ceph OSD, PVC, pod scheduling, taints, and resource-pressure issues

Folder: [`project-2-kubernetes-rook-ceph/`](project-2-kubernetes-rook-ceph/)

## Repository Structure

```text
.
|-- project-1-Canario-devops/
|   |-- app/
|   |-- docs/
|   |-- Dockerfile
|   `-- gitlab-ci.yml
`-- project-2-kubernetes-rook-ceph/
    |-- ansible/
    |-- docs/
    |-- kubernetes/
    |-- observability/
    `-- terraform/
```

## Notes

These projects are academic portfolio examples. They are intended to show implementation work, learning outcomes, and troubleshooting processes rather than production-ready infrastructure. Sensitive information are hidden in the project
