FROM debian:bullseye

RUN apt update -y && apt upgrade -y

RUN mkdir -p /var/www/html

COPY ./conf/index.html /var/www/html/

RUN chmod 755 /var/www/html

RUN chown -R www-data:www-data /var/www/html/

CMD ["tail", "-f", "/dev/null"]