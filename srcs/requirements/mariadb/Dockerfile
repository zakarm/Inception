FROM debian:bullseye

RUN apt-get update -y && apt-get install -y mariadb-server python3

COPY conf/50-server.cnf /etc/mysql/mariadb.conf.d/

COPY ./tools/script.py /

CMD ["python3", "script.py"]