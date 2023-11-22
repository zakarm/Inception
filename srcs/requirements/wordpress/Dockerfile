FROM debian:bullseye

RUN apt update -y && apt upgrade -y && apt-get -y install wordpress curl sendmail python3 \
                    php php-fpm  php-mysql mariadb-client

RUN  chown -R www-data:www-data /var/www/html/

RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar && \ 
                chmod +x wp-cli.phar && \
                mv wp-cli.phar /usr/local/bin/wp

RUN wp core download --path=/var/www/html/ --allow-root

COPY ./conf/wp-config.php /var/www/html/

COPY ./tools/script.py /

CMD ["python3", "script.py"]