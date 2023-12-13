#!/bin/sh

# Replace the placeholder with the actual machine name
sed -i "s/__MACHINE_NAME__/$MACHINE_NAME/g" /usr/share/nginx/html/index.html

# Start Nginx
nginx -g 'daemon off;'