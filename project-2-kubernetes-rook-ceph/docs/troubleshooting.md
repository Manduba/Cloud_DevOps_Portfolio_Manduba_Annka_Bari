# Troubleshooting Summary

This document summarizes the main troubleshooting issues found during Project 2.

The project aimed to deploy a Kubernetes-based storage solution using Rook-Ceph on OpenStack. The Kubernetes cluster and several automation steps worked, but the storage solution faced issues during the Rook-Ceph and workload validation stages.

## Main Issues Found

### 1. Ceph OSD pods crashing

The most serious issue was that Ceph OSD pods repeatedly crashed. OSDs are responsible for managing the disks used by Ceph. When the OSDs were not running correctly, the storage system could not provide stable persistent volumes.

Possible causes included:

- disks not being fully wiped before use
- leftover disk metadata from previous attempts
- incorrect or incomplete disk preparation
- Ceph not being able to use the attached OpenStack volumes correctly

### 2. PVCs stayed in Pending state

PersistentVolumeClaims for workloads such as WordPress and MySQL did not bind correctly. This happened because the Ceph storage backend was not healthy enough to provide volumes.

### 3. Pod scheduling issues

Some pods could not be scheduled because of Kubernetes taints and resource constraints.

Issues included:

- control-plane taint preventing workload scheduling on the master node
- memory pressure on worker nodes
- missing tolerations in some pod definitions
- limited resources available for storage, backup, and observability components

### 4. Observability and backup components affected

Grafana, Loki, Prometheus, Kasten K10, and MinIO were affected by the storage and scheduling issues. Some pods stayed Pending, Evicted, or failed to start correctly.

## What Was Tried

The following troubleshooting actions were attempted during the project:

- checking Rook-Ceph pod status
- entering the Rook-Ceph toolbox
- checking Ceph health using `ceph status`
- checking OSD state using `ceph osd tree`
- manually wiping disks
- deleting and recreating OSD pods
- editing the Rook-Ceph cluster configuration
- checking Kubernetes taints and pod events
- checking memory pressure and scheduling errors

## Learning Outcome

Although the full storage solution did not become fully stable, the project gave practical experience with:

- Kubernetes cluster deployment
- Terraform and Ansible automation
- Rook-Ceph installation
- Ceph OSD troubleshooting
- PVC and StorageClass configuration
- observability deployment
- backup integration attempts
- Kubernetes scheduling and resource-pressure issues

## Sensitive Information

Real IP addresses, SSH keys, kubeconfig files, OpenStack credentials, and private environment details are not included in this public repository.
