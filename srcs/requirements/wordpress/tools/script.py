import os, sys, time, subprocess
try:
    time.sleep(5)
    subprocess.run(f"wp config create --dbname={os.environ['MYSQL_DATABASE_NAME']} --dbuser={os.environ['MYSQL_USER']} --dbpass={os.environ['MYSQL_ROOT_PASSWORD']} --dbhost=mariadb:3306 --path=/var/www/wordpress --allow-root", shell=True, check=True)
    subprocess.run(f"wp core install --url={os.environ['WP_URL']} --title={os.environ['WP_TITLE']} --admin_user={os.environ['WP_ADMIN_USER']} --admin-pass={os.environ['WP_ADMIN_PASSWORD']} --path=/var/www/wordpress --allow-root", shell=True, check=True)
    subprocess.run(f"/usr/sbin/php-fpm7.4 -F", shell=True, check=True)
except KeyboardInterrupt:
    sys.exit(0)