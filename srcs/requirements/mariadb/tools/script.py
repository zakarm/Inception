from time import sleep
from os import system, environ, remove
import subprocess

system("service mariadb start")
sleep(5)
shell_script = f"""
mysql_secure_installation << EOF > /dev/null 2>&1
n
{environ["MYSQL_ROOT_PASSWORD"]}
{environ["MYSQL_ROOT_PASSWORD"]}
y
n
n
n
n
EOF
"""
subprocess.run(shell_script, shell=True, check=False)
sql_script = f"""
    CREATE DATABASE IF NOT EXISTS {environ["MYSQL_DATABASE_NAME"]};
    CREATE USER IF NOT EXISTS '{environ["MYSQL_USER"]}'@'%' IDENTIFIED BY '{environ["MYSQL_PASSWORD"]}';
    GRANT ALL PRIVILEGES ON {environ["MYSQL_DATABASE_NAME"]}.* TO '{environ["MYSQL_USER"]}'@'%';
    FLUSH PRIVILEGES;
"""
with open("db1.sql", "w") as f: 
    f.write(sql_script)
system(f"mariadb -u root -p{environ['MYSQL_ROOT_PASSWORD']} < db1.sql")
remove("db1.sql")
system(f"mysqladmin -u root -p{environ['MYSQL_ROOT_PASSWORD']} shutdown")
system("mariadbd")