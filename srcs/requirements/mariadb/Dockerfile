FROM debian:bullseye

RUN apt update && apt upgrade && apt install -y mariadb-server vim curl

COPY conf/50-server.cnf /etc/mysql/mariadb.conf.d/50-server.cnf

