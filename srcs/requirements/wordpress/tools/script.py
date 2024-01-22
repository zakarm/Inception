from time import sleep
from os import environ, system
from re import sub
import subprocess

sleep (10)
system("service	php7.4-fpm start")
file = "/etc/php/7.4/fpm/pool.d/www.conf"
with open(file, "r") as f: 
    data = f.read()
data = sub(r'listen = /run/php/php7.4-fpm.sock', "listen = 9000", data)
with open(file, "w") as f: 
    f.write(data)
file = "/var/www/html/wp-config.php"
with open(file, "r") as f: 
    data = f.read()
data = sub(r'database_name_here', environ['MYSQL_DATABASE_NAME'], data)
data = sub(r'username_here', environ['MYSQL_USER'], data)
data = sub(r'password_here', environ['MYSQL_PASSWORD'], data)

with open(file, "w") as f: 
    f.write(data)

shell_script = f"""
    wp core install --url={environ['WP_URL']} --title={environ['WP_TITLE']} --admin_user={environ['WP_ADMIN_USER']} --admin_password={environ['WP_ADMIN_PASSWORD']} --admin_email={environ['WP_ADMIN_EMAIL']} --path=/var/www/html --allow-root
    wp plugin install redis-cache --activate --path=/var/www/html --allow-root
    wp plugin update --all --path=/var/www/html --allow-root
    wp redis enable --path=/var/www/html  --allow-root
    service php7.4-fpm stop
    /usr/sbin/php-fpm7.4 -F
"""
subprocess.run(shell_script, shell=True, check=True)