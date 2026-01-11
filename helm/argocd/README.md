# Argo CD Helm Chart

This Helm chart installs Argo CD on a Kubernetes cluster.

## Requirements

- Kubernetes cluster (k3s, minikube, or any cloud cluster)
- Helm 3.x installed
- kubectl configured to access the cluster

## Install Argo CD

```bash
# Add the official Argo Helm repo
helm repo add argo https://argoproj.github.io/argo-helm
helm repo update

# Install Argo CD in namespace 'argocd'
kubectl create namespace argocd
helm install argo-cd argo/argo-cd -n argocd -f values.yaml

Verify Installation

kubectl get pods -n argocd
kubectl get svc -n argocd

All pods should be in Running state.
Access the Argo CD UI

    If using LoadBalancer, get the external IP:

kubectl get svc -n argocd argo-cd-server

    If using NodePort, forward the port:

kubectl port-forward svc/argo-cd-server -n argocd 8080:80

Then open in your browser:

http://localhost:8080

Login

# Get initial admin password
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d

    Username: admin

    Password: output from command above

Usage

Once logged in, you can create Applications in Argo CD that point to Git repositories with your Helm charts.


---

## **5️⃣ Deploy Argo CD Using Helm**

1. **Add Helm repo**  

```bash
helm repo add argo https://argoproj.github.io/argo-helm
helm repo update

    Create namespace

kubectl create namespace argocd

    Install Argo CD

helm install argo-cd argo/argo-cd -n argocd -f values.yaml

    Check pods

kubectl get pods -n argocd

    Access UI

kubectl port-forward svc/argo-cd-server -n argocd 8080:80

    Login

kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d


