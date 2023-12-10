FROM debian:bullseye

RUN apt update -y && apt upgrade -y && apt-get install -y nginx openssl vim curl python3

RUN mkdir -p /etc/nginx/ssl

RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/nginx/ssl/inception.key \
    -out /etc/nginx/ssl/inception.crt \
    -subj "/C=MA/ST=Khouribga/L=Khouribga/O=1337/CN=inception"

RUN mkdir -p /var/run/nginx

COPY ./conf/default /etc/nginx/sites-enabled/
 
COPY ./tools/script.py /

RUN chmod 755 /var/www/html

RUN chown -R www-data:www-data /var/www/html

EXPOSE 443

CMD ["python3 script.py"]