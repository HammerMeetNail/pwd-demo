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
Copying and pasting works natively on MacOS using Command-V, `⌘ + v`. On Windows, use Shift-Insert `Shift + Insert` instead of Control-V, `CTRL + v`.

### Making Sure Docker is Installed
1. `docker version`

### Running Containers
1. `docker run hello-world`
2. `docker run -d -p 80:80 --name hello-world tutum/hello-world`
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
1. `curl https://raw.githubusercontent.com/HammerMeetNail/pwd-demo/master/Dockerfile -O`
2. `docker build -t my-app:v1.0.0 .`
3. `docker run --rm my-app:v1.0.0`

### Storing Images
1. `docker login`
2. Make not of your [full repository name[(https://cloud.docker.com/repository/list)], ex. `doconno2/public-repo`
3. `docker tag my-app:v1.0.0 {full repository name}:v1.0.0`
    * Replace `{full repository name}` with the full name of your repository
4. `docker push {full repository name}:v1.0.0`

### Persisting Data
1. `docker volume create temp`
2. `docker volume ls`
3. `docker run --rm -it -v temp:/temp alpine:3.9 sh -c 'echo "hello world" >> /temp/hello.txt'`
4. `docker run --rm -it -v temp:/temp alpine:3.9 sh -c 'cat /temp/hello.txt'`
5. `docker volume rm temp`
6. `docker run --rm -it -v temp:/temp alpine:3.9 sh -c 'cat /temp/hello.txt'`

### Clean Up
1. `docker system prune`

### Docker-Compose

### Kubernetes

- Basics
    - Core Commands
        - Build
            - Tag
        - Run
            - Exec
        - Push
            - Login
    - Persisting Data
        - Volume
        - Prune/RM/RMI
    - Hello World
        - https://hub.docker.com/r/tutum/hello-world/
        - docker run -d -p 80:80 tutum/hello-world
- Docker-compose
    - docker-compose.yml
    - Create and run yml
- Sharing Images
- Kubernetes
    - k3s
    - alias kubectl="docker run --rm -it --network host -v /tmp/k3s:/tmp/k3s -v $(pwd):/mnt --workdir /mnt bitnami/kubectl:latest"

