import os
nginx_conf = """
server 
{
    listen 80;

    location / {
        root /var/www/html;
        index index.html index.htm;
    }
}
"""
with open("/etc/nginx/sites-enabled/default", 'w') as f:
    f.write(nginx_conf)