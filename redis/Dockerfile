# syntax=docker/dockerfile:1

FROM ubuntu:22.04

WORKDIR /redis

VOLUME ["/redis"]

# https://redis.io/docs/getting-started/installation/install-redis-on-linux/
RUN apt-get update && apt-get install -y lsb-release curl gpg && \
    curl -fsSL https://packages.redis.io/gpg | \
    gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | \
    tee /etc/apt/sources.list.d/redis.list && \
    apt-get update && \
    apt-get install -y redis

CMD ["redis-server", "--protected-mode", "no"]

EXPOSE 6379