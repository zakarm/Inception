FROM debian:bullseye

RUN apt-get update -y && apt-get install -y \
    wget=1.21-1+deb11u1 python3=3.9.2-3 php=2:7.4+76 php-mysql=2:7.4+76 \
    && apt-get clean && rm -rf /var/lib/apt/lists/* \
    && wget https://www.adminer.org/latest.php -O /var/www/html/adminer.php

RUN chmod 755 /var/www/html/adminer.php && chown -R www-data:www-data /var/www/html/adminer.php

COPY ./tools/script.py /

CMD ["python3", "/script.py"]