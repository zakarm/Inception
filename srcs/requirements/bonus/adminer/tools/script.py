from os import system
system("cd /var/www/html && rm -rf index.html && php -S 0.0.0.0:80 -t /var/www/html /var/www/html/adminer.php")