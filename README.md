# pwd-demo
Links and commands to execute on https://training.play-with-docker.com/

# PWD Docker
- Access to Docker and docker-compose
    - Create account for https://hub.docker.com
    - Login to https://training.play-with-docker.com/ops-s1-hello/
    - Make sure it works
        - docker version
        - docker run hello-world
    - Create public repository
        - https://cloud.docker.com/repository/create
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

