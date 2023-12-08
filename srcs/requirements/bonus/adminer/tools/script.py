import sys, subprocess

try:
    subprocess.run("cd /var/www/html && rm -rf index.html && php -S 0.0.0.0:80", shell=True, check = True)
except Exception as e :
    print(e)