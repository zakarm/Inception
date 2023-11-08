import subprocess, os, sys, time
try:
    subprocess.run("service mariadb start", shell=True, check=True)
    time.sleep(1)
    sql_script = f"""
    CREATE DATABASE IF NOT EXISTS {os.environ["MYSQL_DATABASE_NAME"]};
    CREATE USER IF NOT EXISTS '{os.environ["MYSQL_USER"]}'@'%' IDENTIFIED BY '{os.environ["MYSQL_PASSWORD"]}';
    GRANT ALL PRIVILEGES ON {os.environ["MYSQL_DATABASE_NAME"]}.* TO '{os.environ["MYSQL_USER"]}'@'%';
    ALTER USER 'root'@'localhost' IDENTIFIED BY '{os.environ["MYSQL_ROOT_PASSWORD"]}';
    FLUSH PRIVILEGES;
    """
    with open("db1.sql", "w") as f: f.write(sql_script)
    subprocess.run(f"mysql -u root -p'{os.environ['MYSQL_ROOT_PASSWORD']}' < db1.sql", shell=True, check=True)
    subprocess.run("rm -rf db1.sql", shell=True, check=True)
    subprocess.run(f"mysqladmin -u root -p{os.environ['MYSQL_ROOT_PASSWORD']} shutdown", shell=True, check=True)
    subprocess.run(f"mysqld", shell=True, check=True)
except KeyboardInterrupt:
    sys.exit(0)