# Kubernetes Rook-Ceph Storage and Observability Project

This project was completed as part of the ACIT 4430 Infrastructure Services and Operations course at OsloMet.

The goal was to design and test a Kubernetes-based storage solution using Rook-Ceph on OpenStack. The project also included automation with Terraform and Ansible, Kubernetes deployment using Kubespray, observability components, and backup integration attempts.

## What this project demonstrates

- OpenStack VM provisioning with Terraform
- Automation with Ansible
- Kubernetes cluster deployment using Kubespray
- Rook-Ceph storage setup
- CephBlockPool and StorageClass configuration
- PersistentVolumeClaim testing with WordPress and MySQL
- Observability setup using Prometheus, Grafana, and Loki
- Backup integration attempt using Kasten K10 and MinIO
- Troubleshooting of Ceph OSD, PVC, pod scheduling, taints, and resource-pressure issues

## Tools Used

- OpenStack
- Terraform
- Ansible
- Kubernetes
- Kubespray
- Rook-Ceph
- Prometheus
- Grafana
- Loki
- Kasten K10
- MinIO
- WordPress
- MySQL

## Project Status

This was an academic infrastructure project. The Kubernetes cluster deployment and several automation steps were completed. The Rook-Ceph storage deployment faced OSD and scheduling issues, which are documented as part of the troubleshooting work.

This repository includes selected configuration files and documentation from the project.