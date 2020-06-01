FROM python:3.6-alpine
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories

RUN runDeps="\
		tar \
		wget \
		libsodium-dev \
		openssl \
	"; \
	set -ex \
	&& apk add --no-cache --virtual .build-deps ${runDeps}

ENV SSR_VERSION 3.2.2
RUN wget -O /tmp/shadowsocksr.tar.gz https://github.com/shadowsocksrr/shadowsocksr/archive/${SSR_VERSION}.tar.gz \
	&& tar zxf /tmp/shadowsocksr.tar.gz -C /tmp \
	&& mv /tmp/shadowsocksr-${SSR_VERSION}/shadowsocks /usr/local/ \
	&& rm -fr /tmp/shadowsocksr-${SSR_VERSION} \
	&& rm -f /tmp/shadowsocksr.tar.gz

COPY ./config.json /etc/shadowsocksr/config.json
COPY ./entrypoint.py /usr/local/shadowsocks/entrypoint.py
RUN chmod 775 /usr/local/shadowsocks/entrypoint.py
VOLUME /etc/shadowsocksr
ENV SSR_SERVER 0.0.0.0
ENV SSR_SERVER_PORT 8388
ENV SSR_PASSWORD UrmjvSmqTxTUjAeh72SGJX6aBJH7Kd
ENV SSR_METHOD none
ENV SSR_PROTOCOL auth_chain_d
ENV SSR_OBFS tls1.2_ticket_auth

CMD python /usr/local/shadowsocks/entrypoint.py && /usr/local/shadowsocks/server.py -c /etc/shadowsocksr/config.json