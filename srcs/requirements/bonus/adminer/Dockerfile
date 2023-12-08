FROM debian:bullseye

RUN apt update -y && apt upgrade -y && apt-get install wget python3 php php-mysql -y && \
    wget https://www.adminer.org/latest.php -O /var/www/html/adminer.php

RUN chmod 755 /var/www/html/adminer.php

RUN chown -R www-data:www-data /var/www/html/adminer.php

COPY ./tools/script.py ./

CMD ["python3", "script.py"]