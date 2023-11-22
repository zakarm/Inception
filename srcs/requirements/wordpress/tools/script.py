import os, sys, time, subprocess, re

time.sleep (5)

try:
    subprocess.run("service	php7.4-fpm start", shell = True, check = True)
    file = "/etc/php/7.4/fpm/pool.d/www.conf"
    with open(file, "r") as f: 
        data = f.read()
    data = re.sub(r'listen = /run/php/php7.4-fpm.sock', "listen = 0.0.0.0:9000", data)
    with open(file, "w") as f: 
        f.write(data)
    time.sleep(5)
    file = "/var/www/html/wp-config.php"
    with open(file, "r") as f: 
        data = f.read()
    data = re.sub(r'database_name_here', os.environ['MYSQL_DATABASE_NAME'], data)
    data = re.sub(r'username_here', os.environ['MYSQL_USER'], data)
    data = re.sub(r'password_here', os.environ['MYSQL_PASSWORD'], data)
    with open(file, "w") as f: 
        f.write(data)
    subprocess.run(f"wp core install --url={os.environ['WP_URL']} --title={os.environ['WP_TITLE']} --admin_user={os.environ['WP_ADMIN_USER']} --admin_password={os.environ['WP_ADMIN_PASSWORD']} --admin_email={os.environ['WP_ADMIN_EMAIL']} --path=/var/www/html --allow-root", shell=True, check=True)
    subprocess.run("service php7.4-fpm stop", shell=True, check=True)
    subprocess.run(f"/usr/sbin/php-fpm7.4 -F", shell=True, check=True)
except KeyboardInterrupt:
    sys.exit(0)
