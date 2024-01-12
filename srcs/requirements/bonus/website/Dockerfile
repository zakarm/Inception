FROM debian:bullseye

RUN apt-get update -y && apt-get install -y \
    --no-install-recommends \
    nginx=1.18.0-6.1+deb11u3 && mkdir -p /var/www/html \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY ./conf/index.html /var/www/html/

COPY ./conf/styles.css /var/www/html/

RUN chmod 755 /var/www/html && chown -R www-data:www-data /var/www/html/

COPY ./conf/default /etc/nginx/sites-enabled/

CMD ["sh", "-c", "nginx -g 'daemon off;'"]