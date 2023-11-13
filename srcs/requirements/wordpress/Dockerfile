FROM debian:bullseye

RUN apt update -y && apt upgrade -y && apt-get install wordpress curl sendmail python3 -y

RUN apt-get install -y php php-fpm  php-mysql mariadb-client 

RUN mkdir -p /run/php

RUN chown -R root:root /var/www/html

RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar

RUN chmod +x wp-cli.phar

RUN mv wp-cli.phar /usr/local/bin/wp

RUN wp core download --path=/var/www/html/ --allow-root

COPY ./conf/wp-config.php /var/www/html/

COPY ./tools/script.py /

CMD ["python3", "script.py"]
