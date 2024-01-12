FROM debian:bullseye

RUN apt-get update -y && apt-get install -y \
    --no-install-recommends wget=1.21-1+deb11u1 tar ca-certificates \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/portainer/portainer/releases/download/2.19.0/portainer-2.19.0-linux-amd64.tar.gz \
    && tar xvzf /portainer-2.19.0-linux-amd64.tar.gz \
    && rm -rf portainer-2.19.0-linux-amd64.tar.gz

EXPOSE 9000

CMD ["/portainer/portainer"]