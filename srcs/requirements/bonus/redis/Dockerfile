FROM debian:bullseye

RUN apt update -y && apt upgrade -y && apt install -y redis-server

COPY ./conf/redis.conf /etc/redis/

CMD ["redis-server", "--protected-mode", "no"]