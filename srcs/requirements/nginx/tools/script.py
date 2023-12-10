import os, re
file = "/etc/nginx/sites-enabled/default"
with open(file, "r") as f:
    data = f.read()
data = re.sub(r'/etc/nginx/ssl/',  os.environ["CERTS_"], data)
with open(file, "w") as f:
    f.write(data)
file = "/etc/nginx/sites-enabled/default"
with open(file, "r") as f:
    data = f.read()
data = re.sub(r'localhost',  os.environ["DOMAIN_NAME"], data)
with open(file, "w") as f:
    f.write(data)