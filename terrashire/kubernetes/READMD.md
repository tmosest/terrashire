```
apt install -y sudo
sudo apt update
sudo apt install -y ca-certificates curl apt-transport-https
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.29/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.29/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo apt update
sudo apt install -y kubectl
kubectl version --client
```

You would usually copy this file from your Kubernetes master node to the Proxmox host (e.g., to ~/.kube/config).


https://kubernetes.io/docs/tutorials/hello-minikube/