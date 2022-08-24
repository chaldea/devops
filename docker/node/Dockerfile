FROM node:16.16.0 as base
RUN sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list && \
    sed -i 's/security.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list && \
    apt-get update -y && apt-get install -y zip unzip
RUN wget -q https://dl.min.io/client/mc/release/linux-amd64/mc -P /usr/local/bin && \
    chmod +x /usr/local/bin/mc