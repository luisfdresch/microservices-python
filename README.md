## Microservice Architecture and System Design with Python & Kubernetes

This repository refers to the [freeCodeCamp.org](https://www.freecodecamp.org/) hands-on tutorial about microservices architecture and distributed systems using Python, Kubernetes, RabbitMQ, MongoDB, and MySQL.

Watch the [YouTube video](https://www.youtube.com/watch?v=hmkF77F9TLw) for more information.


### Install docker and kubernetes using ansible

`setup.yaml`
```yaml
---
- hosts: all
  roles:
    - role: geerlingguy.docker
      become: yes
    
    - role: geerlingguy.kubernetes
      become: yes
```

```bash
ansible-galaxy role install geerlingguy.docker
ansible-galaxy role install geerlingguy.kubernetes
ansible-playbook setup.yaml --connection=local --inventory 127.0.0.1, -K
```


### Install minikube, k9s, and MySQL


### Create local registry
```bash
minikube addons enable registry
```

Pull Python docker image and store it locally
```bash
docker run -d -p 5000:5000 --name registry registry:2
docker pull python:3.10-slim-bullseye 
docker image tag python:3.10-slim-bullseye localhost:5000/python:3.10-slim-bullseye
docker push localhost:5000/python:3.10-slim-bullseye
docker rmi python:3.10-slim-bullseye
```

edit /etc/docker/daemon.json
```
{ "insecure-registries":["192.168.49.2:5000"] } 
```

Build image using local python image, create tag, push it into minikube repository
```bash
docker build --build-arg BASE_IMAGE=localhost:5000/python:3.10-slim-bullseye -t $(minikube ip):5000/auth:latest . 
docker push $(minikube ip):5000/auth:latest
```

### Ensure minikube and kubectl are compatible
Kubectl and kubernetes must be within a certaing version range, it is possible to specify the kubernetes version by
```bash
minikube start --kubernetes-version v1.27 --insecure-registry "192.168.49.0/24"
```

