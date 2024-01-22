from re import sub
from os import environ, system

file = "/etc/nginx/sites-enabled/default"
with open(file, "r") as f:
    data = f.read()
data = sub(r'/etc/nginx/ssl/',  environ["CERTS_"], data) 
with open(file, "w") as f:
    f.write(data)
data = ""
with open(file, "r") as f:
    data = f.read()
data = sub(r'localhost',  environ["DOMAIN_NAME"], data)
with open(file, "w") as f:
    f.write(data)
system("nginx -g 'daemon off;'")