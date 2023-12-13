# Use the latest version of Alpine Linux as the base image
FROM alpine:latest

# Install Nginx and create necessary directories and files
RUN apk add --no-cache nginx && \
    touch /var/run/nginx.pid && \
    mkdir -p /run/nginx && \
    mkdir -p /etc/ssl/certs/ && \
    mkdir -p /etc/ssl/private/ && \
    mkdir -p /usr/share/nginx/html /var/cache/nginx /etc/nginx/conf.d 

# Copy the build files to the Nginx document root
COPY build /usr/share/nginx/html/

# Copy the Nginx configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Set the permissions of the files in the Nginx document root to be readable by everyone
# If the Nginx process needs to execute any of these files, you might need to add execute permissions as well
RUN chmod -R 744 /usr/share/nginx/html/*

# Change the ownership of the necessary directories and files to the 'nginx' user
# This allows the Nginx process to read, write, and execute the files
RUN chown -R nginx:nginx /var/run/nginx.pid /usr/share/nginx/html/* /var/cache/nginx /var/log/nginx /etc/nginx/conf.d /etc/ssl/private/ /etc/ssl/certs/

# Run the container as the 'nginx' user
USER nginx

# Expose port 443 for HTTPS

EXPOSE 80
# Start Nginx in the foreground so that the Docker container doesn't exit
CMD ["nginx", "-g", "daemon off;"]