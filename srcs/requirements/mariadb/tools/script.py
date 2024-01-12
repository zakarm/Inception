from subprocess import run
import os, time

def run_c(cmd, res):
    if res: run(cmd, check=True, shell=True)
    else: return run(cmd, check=True, shell=True, capture_output=True, text=True)

run_c("service mariadb start", False)
while run_c(f"mysqladmin ping -u root -p{os.environ['MYSQL_ROOT_PASSWORD']}", True).stdout != "mysqld is alive\n": time.sleep(0.5)
sql_script = f"""
    CREATE DATABASE IF NOT EXISTS {os.environ["MYSQL_DATABASE_NAME"]};
    CREATE USER IF NOT EXISTS '{os.environ["MYSQL_USER"]}'@'%' IDENTIFIED BY '{os.environ["MYSQL_PASSWORD"]}';
    GRANT ALL PRIVILEGES ON {os.environ["MYSQL_DATABASE_NAME"]}.* TO '{os.environ["MYSQL_USER"]}'@'%';
    ALTER USER 'root'@'localhost' IDENTIFIED BY '{os.environ["MYSQL_ROOT_PASSWORD"]}';
    FLUSH PRIVILEGES;
"""
with open("db1.sql", "w") as f: f.write(sql_script)
run_c(f"mysql -u root -p'{os.environ['MYSQL_ROOT_PASSWORD']}' < db1.sql", False)
run_c("rm -rf db1.sql", False)
run_c(f"mysqladmin -u root -p{os.environ['MYSQL_ROOT_PASSWORD']} shutdown",False)
run_c(f"mysqld", False)