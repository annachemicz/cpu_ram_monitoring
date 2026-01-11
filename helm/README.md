# My Backend Helm Chart

This Helm chart deploys a simple Node.js backend on Kubernetes.

## Requirements

- Kubernetes cluster (e.g., k3s, minikube)
- Helm 3
- Local Docker image: `node-backend:latest`

## Install

1. Build and import Docker image:

```bash
docker build -t node-backend:latest ./backend
sudo k3s ctr images import ./node-backend.tar

    Install chart:

helm install backend ./my-backend -f values.yaml

    Update /etc/hosts:

127.0.0.1 backend.local

    Access in browser:

http://backend.local
