import subprocess

subprocess.run("service mariadb start", shell=True, check=True)

db1_name = "your_db_name"
db1_user = "your_db_user"
db1_pwd = "your_db_password"
sql_script = f"""
CREATE DATABASE IF NOT EXISTS {db1_name};
CREATE USER IF NOT EXISTS '{db1_user}'@'%' IDENTIFIED BY '{db1_pwd}';
GRANT ALL PRIVILEGES ON {db1_name}.* TO '{db1_user}'@'%';
ALTER USER 'root'@'localhost' IDENTIFIED BY 'oujda';
FLUSH PRIVILEGES;
"""

with open("db1.sql", "w") as f:
    f.write(sql_script)

subprocess.run("mysql < db1.sql", shell=True, check=True)
subprocess.run("kill $(cat /var/run/mysqld/mysqld.pid)", shell=True, check=True)
subprocess.run("mysqld", shell=True, check=True)