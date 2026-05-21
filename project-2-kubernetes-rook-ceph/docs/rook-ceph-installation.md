# Rook-Ceph Installation

This document summarizes the Rook-Ceph installation workflow used in Project 2.

The goal of this phase was to deploy Ceph inside Kubernetes using Rook, so that Kubernetes workloads could use distributed persistent storage.

## Phase 3: Rook-Ceph Installation

### 1. Clone the Rook repository

```bash
git clone --single-branch --branch v1.17.1 https://github.com/rook/rook.git