FROM debian:bullseye

RUN apt update -y && apt upgrade -y && apt-get install nginx -y

RUN mkdir -p /var/www/html

COPY ./conf/index.html /var/www/html/

RUN chmod 755 /var/www/html

RUN chown -R www-data:www-data /var/www/html/

COPY ./conf/default /etc/nginx/sites-enabled/

CMD ["sh", "-c", "nginx -g 'daemon off;'"]