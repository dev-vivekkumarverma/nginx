FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y nginx && apt clean

RUN rm -f /etc/nginx/conf.d/default.conf

EXPOSE 80

RUN mkdir -p certificates

COPY nginx.conf /etc/nginx/nginx.conf
COPY certificates /certificates/ 
RUN mkdir -p /logs && touch /logs/error.log

CMD nginx -t && nginx -g "daemon off;" && tail -f /logs/error.log