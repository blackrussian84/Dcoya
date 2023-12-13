# Use Nginx alpine image
FROM alpine:latest

RUN apk add --no-cache nginx && \
    touch /var/run/nginx.pid && \
    chown -R nginx:nginx /var/run/nginx.pid && \
    mkdir -p /run/nginx && \
    mkdir -p /etc/ssl/certs/ && \
    mkdir -p /etc/ssl/private/ && \
    mkdir -p /usr/share/nginx/html /var/cache/nginx /etc/nginx/conf.d 

# Change ownership of the Nginx web directory to the nginx user
RUN chown -R nginx:nginx /usr/share/nginx/html && chmod -R 755 /usr/share/nginx/html

# Copy the index.html and start.sh files to the Docker image
COPY index.html start.sh /usr/share/nginx/html/
COPY nginx.conf /etc/nginx/
COPY default.conf /etc/nginx/conf.d/

# Make the start.sh script executable
RUN chmod +x /usr/share/nginx/html/start.sh

# Switch to the nginx user
USER nginx

# Start the container with the start.sh script
CMD ["/usr/share/nginx/html/start.sh"]
