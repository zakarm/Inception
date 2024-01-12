FROM debian:bullseye

RUN apt-get update -y && apt-get install -y \
    --no-install-recommends \
    mariadb-server=1:10.5.21-0+deb11u1 python3=3.9.2-3 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY conf/50-server.cnf /etc/mysql/mariadb.conf.d/

COPY ./tools/script.py /

CMD ["python3", "/script.py"]