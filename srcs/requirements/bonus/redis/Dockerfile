FROM debian:bullseye

RUN apt update -y && apt upgrade -y && apt-get install redis-server -y

COPY ./conf/redis.conf /etc/redis/

CMD ["redis-server", "--protected-mode", "no"]