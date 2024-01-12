FROM debian:bullseye

RUN apt-get update -y && apt-get install -y --no-install-recommends \
    curl=7.74.0-1.3+deb11u11 python3=3.9.2-3 \
    php-fpm=2:7.4+76 php-redis=5.3.2+4.3.0-2+deb11u1 \
    php-mysql=2:7.4+76 wordpress=5.7.8+dfsg1-0+deb11u2 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN chmod 777 /var/www/html \
    && chown -R www-data:www-data /var/www/html \
    && curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar && \ 
    chmod +x wp-cli.phar && \
    mv wp-cli.phar /usr/local/bin/wp \
    && wp core download --path=/var/www/html/ --allow-root

COPY ./conf/wp-config.php /var/www/html/

COPY ./tools/script.py /

CMD ["python3", "/script.py"]