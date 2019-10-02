# pwd-demo
This repository contains links and commands for getting started with Docker.

## Play With Docker
[Play With Docker](https://training.play-with-docker.com/about/) is an instructional website affiliated with [Docker](https://www.docker.com/). It provides an interactive and online terminal for getting started with Docker. 

## Step-by-Step Instructions
### Prerequisites
1. Create an account at [Docker Hub](https://hub.docker.com)
    * Do not use a password that has used elsewhere, it will be used on a public server during the demo.
2. Create a new repository called `public-repo` at [Docker Hub](https://cloud.docker.com/repository/create)
3. Login to [Play With Docker](https://training.play-with-docker.com/ops-s1-hello/)
    * The terminal should appear within 10 seconds of logging in. If it doesn't, refresh the page until a prompt appears. 
4. In the PWD terminal, install `w3m` for terminal based web browsing
    * `apk update && apk add w3m`

### How to Copy and Paste in PWD Terminal
Copying and pasting works natively on MacOS using Command-C, `⌘ + c` and Command-V, `⌘ + v`. On Windows, use Control-Insert, `CTRL + Insert` instead of Control-C, `CTRL + c` and use Shift-Insert `Shift + Insert` instead of Control-V, `CTRL + v`.

### Making Sure Docker is Installed
1. `docker version`

### Running Containers
1. `docker run hello-world`
2. `docker pull grycap/cowsay`
3. `docker run --name cowsay grycap/cowsay "/usr/games/cowsay" "Hello World"`
4. `docker run -d -p 80:80 --name hello-world tutum/hello-world`
    * `curl localhost`
    * `w3m localhost`
        * `w3m` can be closed by hitting `q` key

### Show Containers
1. `docker ps -a`

### Show Images
1. `docker images`

### Stopping and Starting Containers
1. `docker stop hello-world`
    * `curl localhost` should now fail
2. `docker start hello-world`

### Removing Containers and Images
1. `docker rm -f hello-world`
    * `docker rm -f $(docker ps -a -q)` can be used to force remove all conainters
2. `docker rmi tutum/hello-world:latest`
    * `docker rmi -f $(docker images -a -q)` can be used to force remove all images

### Building and Tagging Images
1. `git clone https://github.com/HammerMeetNail/pwd-demo.git`
2. `cd pwd-demo`
3. `cat Dockerfile`
4. `cat app.py`
5. `docker build -t add:v1.0.0 .`
6. `docker run --rm add:v1.0.0 1 2`

### Entering Containers
1. `docker run -it alpine:3.9 sh`
    * Leave the container by typing `exit` to end the shell session
2. `docker run -it --entrypoint sh add:v1.0.0`
    * Browse around the container using common commands like `cd`, `ls`, `cat`
    * We can see the contents of our python app by running `cat /app/app.py`
    * Leave the container by typing `exit` to end the shell session

### Using Python in a Container
1. `docker run -it python:alpine sh`
2. `pip3 install requests`
    * The container has a full installation of `python3` and `pip3`
    * Install python packages uses `pip3`, ex. `pip3 install requests`
3. Start the interpreter using `python`
    * View the Zen of Python with `import this`
    * Import requests using `import requests`
4. Quit the interpreter using `quit()`
5. `exit`

### Storing Images
1. `docker login`
2. Make not of your [full repository name](https://cloud.docker.com/repository/list), ex. `doconno2/public-repo`
3. `docker tag add:v1.0.0 {full repository name}:v1.0.0`
    * Replace `{full repository name}` with the full name of your repository
    * Example: `docker tag add:v1.0.0 doconno2/public-repo:v1.0.0`
4. `docker push {full repository name}:v1.0.0`

### Persisting Data
1. `docker volume create temp`
2. `docker volume ls`
3. `docker run --rm -it -v temp:/temp alpine:3.9 sh -c 'echo "hello world" >> /temp/hello.txt'`
4. `docker rm -f $(docker ps -a -q)`
5. `docker ps -a`
6. `docker run --rm -it -v temp:/temp alpine:3.9 sh -c 'cat /temp/hello.txt'`
7. `docker volume rm temp`
8. `docker run --rm -it -v temp:/temp alpine:3.9 sh -c 'cat /temp/hello.txt'`

### Clean Up
1. `docker system prune`

### Docker-Compose
1. `docker-compose version`
2. `curl https://raw.githubusercontent.com/HammerMeetNail/pwd-demo/master/docker-compose.yml -O`
3. `cat docker-compose.yml`
4. `docker-compose up -d`
5. `curl localhost`
    * `w3m localhost`
        * `w3m` can be closed by hitting `q` key
6. `docker-compose logs cowsay-hello-world`
7. `docker-compose down`

### Kubernetes via K3s and Docker-Compose
1. `cd /tmp && curl https://raw.githubusercontent.com/HammerMeetNail/pwd-demo/master/docker-compose-k3s.yml -O`
2. `docker-compose -f docker-compose-k3s.yml up -d`
3. `curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl`
4. `chmod +x kubectl && mv kubectl /usr/local/bin`
5. `kubectl --kubeconfig /tmp/kubeconfig.yaml get nodes`
6. `kubectl --kubeconfig /tmp/kubeconfig.yaml create deployment hello-node --image=gcr.io/hello-minikube-zero-install/hello-node`
7. `kubectl --kubeconfig /tmp/kubeconfig.yaml get po`
8. `kubectl --kubeconfig kubeconfig.yaml expose deployment hello-node --type=LoadBalancer --port=8080`
9. `kubectl --kubeconfig /tmp/kubeconfig.yaml get services`
    * Note the `External-IP` for the `hello-node` LoadBalancer
10. `curl {external ip address}:8080`
    * Replace `{external ip address}` with `External-IP` for `hello-node`, ex. `172.20.0.2`

## Install Docker
Everything above should be runnable in Play-With-Docker, but if Play-With-Docker is unavailable Docker can be [installed manually](https://hub.docker.com/?overlay=onboarding). 

## Resources
[Play With Docker](https://training.play-with-docker.com)
[Play With Kubernetes](https://training.play-with-kubernetes.com/)
[K3s](https://github.com/rancher/k3s)
[Katacoda](https://www.katacoda.com/)
