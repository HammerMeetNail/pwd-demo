# pwd-demo
This repository contains links and commands for getting started with Docker.

# Important Links
https://training.play-with-docker.com/

# Play With Docker
(Play With Docker)[https://training.play-with-docker.com/about/] is an instructional website affiliated with (Docker)[https://www.docker.com/]. It provides an interactive and online terminal for getting started with Docker. 

# Step-by-Step Instructions
## Prerequisites
1. Create an account at [Docker Hub](https://hub.docker.com)
2. Create a new repository called `public-repo` at [Docker Hub](https://cloud.docker.com/repository/create)
3. Login to [Play With Docker](https://training.play-with-docker.com/ops-s1-hello/)
    * The terminal should appear within 10 seconds of logging in. If it doesn't, refresh the page until a prompt appears. 

## How to Copy and Paste in PWD Terminal
Copying and pasting works natively on MacOS using Command-V, `⌘ + v`. On Windows, use Shift-Insert `Shift + Insert` instead of Control-V, `CTRL + v`.

## Making Sure Docker Works
1. `docker version`
2. `docker run hello-world`

## Running Containers
1. 

## Building Images

## Storing Images

## Clean Up

## Docker-Compose

## Kubernetes

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

