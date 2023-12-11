import os
nginx_conf = """
server 
{
    listen 3000;

    location / {
        root /var/www/html;
        index index.html index.htm;
    }
}
"""
with open("/etc/nginx/sites-enabled/default", 'w') as f:
    f.write(nginx_conf)
print(f"Nginx configuration written to /etc/nginx/sites-enabled/default.")