FROM debian:bullseye

RUN apt-get update -y && apt install -y mariadb-server python3 python3-pip

RUN pip3 install mysql-connector-python

COPY conf/50-server.cnf /etc/mysql/mariadb.conf.d/

COPY /tools/script.py /

CMD ["python3", "script.py"]