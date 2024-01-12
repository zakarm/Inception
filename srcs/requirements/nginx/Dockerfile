FROM debian:bullseye

RUN apt-get update -y && apt-get install -y \
    --no-install-recommends \
    nginx=1.18.0-6.1+deb11u3 openssl=1.1.1w-0+deb11u1 \
    curl=7.74.0-1.3+deb11u11 python3=3.9.2-3  \
    && apt-get clean && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /etc/nginx/ssl \
    && openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/nginx/ssl/inception.key \
    -out /etc/nginx/ssl/inception.crt \
    -subj "/C=MA/ST=Khouribga/L=Khouribga/O=1337/CN=inception" \
    && mkdir -p /var/run/nginx

COPY ./conf/default /etc/nginx/sites-enabled/
 
COPY ./tools/script.py /

RUN chmod 755 /var/www/html && chown -R www-data:www-data /var/www/html

EXPOSE 443

CMD ["sh", "-c", "python3 /script.py & nginx -g 'daemon off;'"]