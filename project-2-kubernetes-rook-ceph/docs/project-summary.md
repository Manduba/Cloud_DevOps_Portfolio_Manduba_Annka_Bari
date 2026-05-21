# Project Summary

This project was created for the ACIT 4430 Infrastructure Services and Operations course at OsloMet.

The goal was to design and test a Kubernetes-based storage solution for persistent data using Rook-Ceph. The infrastructure was deployed on OpenStack, with Terraform and Ansible used for automation.

The project included:

- Provisioning OpenStack virtual machines
- Generating Ansible inventory from Terraform output
- Deploying Kubernetes using Kubespray
- Installing Rook-Ceph for distributed storage
- Creating a CephBlockPool and StorageClass
- Testing PersistentVolumeClaims with WordPress and MySQL
- Deploying observability components with Prometheus, Grafana, and Loki
- Attempting backup integration with Kasten K10 and MinIO
- Troubleshooting Ceph OSD crashes, pending PVCs, pod scheduling issues, taints, and memory pressure

The project was partially successful. The Kubernetes cluster and several automation steps worked, but the Rook-Ceph storage deployment had OSD and scheduling issues. These limitations are included because troubleshooting was an important part of the learning outcome.