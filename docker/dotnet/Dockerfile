FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
RUN sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list && \
    sed -i 's/security.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list && \
    apt-get update -y && apt-get upgrade -y && apt-get install -y zip unzip
RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm config set registry https://registry.npmmirror.com
RUN npm i -g yarn && yarn config set registry https://registry.npmmirror.com
