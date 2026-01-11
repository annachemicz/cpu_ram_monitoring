Node.js + PostgreSQL + Ingress on k3s

This guide walks you through setting up a Node.js backend with a PostgreSQL database on k3s, including PersistentVolume, PersistentVolumeClaim, ClusterIP Services, and Ingress Nginx for local access.

1️⃣ Build the Local Node.js Image

Navigate to your backend directory:

cd ./backend


Build the Docker image:

sudo docker build -t node-backend:latest .


If your user is in the Docker group, sudo can be omitted.

Save the image to a tar file:

docker save -o node-backend.tar node-backend:latest

2️⃣ Load the Image into k3s

Import the image into k3s (containerd):

sudo k3s ctr images import ./node-backend.tar


Make sure your backend.yaml Deployment specifies:

image: node-backend:latest
imagePullPolicy: Never


This ensures k3s uses the local image instead of pulling from DockerHub.

3️⃣ Install Ingress Nginx in k3s
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.1/deploy/static/provider/k3s/deploy.yaml
kubectl get pods -n ingress-nginx


All pods in the ingress-nginx namespace should be Running.

4️⃣ Deploy Kubernetes Resources

Create PersistentVolume and PersistentVolumeClaim for PostgreSQL:

kubectl apply -f postgres-pv-pvc.yaml


Deploy PostgreSQL:

kubectl apply -f postgres.yaml


Deploy the backend:

kubectl apply -f backend.yaml


Deploy the Ingress:

kubectl apply -f ingress.yaml

5️⃣ Update /etc/hosts

Add this line so your browser can resolve the local domain:

127.0.0.1 backend.local

6️⃣ Test the Deployment

Check all pods:

kubectl get pods


All pods should be Running.

Check Services and Endpoints:

kubectl get svc
kubectl get endpoints


Test from a temporary pod:

kubectl run tmp-shell --rm -i --tty --image=alpine -- sh
apk add --no-cache curl
curl http://backend-service:80


You should see:

Node.js application is running 🚀


Open in your browser:

http://backend.local
