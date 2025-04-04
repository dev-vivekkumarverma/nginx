FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y nginx && apt clean

# Ensure default config is removed
RUN rm -f /etc/nginx/conf.d/default.conf

EXPOSE 80
# Set up working directories
WORKDIR /app

# Ensure required directories exist
RUN mkdir -p /logs /applogs /template \
    && touch /logs/error.log /logs/access.log \
    && touch /applogs/access.log /applogs/error.log

# Ensure directories exist before copying
RUN mkdir -p /template
COPY ./template/index.html /template/index.html
COPY ./test/nginx/nginx.conf /etc/nginx/nginx.conf

# Start nginx and keep container running
CMD nginx -t && nginx -g 'daemon off;' && tail -f /dev/null
