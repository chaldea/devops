FROM python:3.6-alpine

ENV SSR_VERSION 3.2.2
RUN runDeps="\
		tar \
		wget \
		libsodium-dev \
		openssl \
	"; \
	set -ex \
	&& apk add --no-cache --virtual .build-deps ${runDeps} \
	&& wget -O /tmp/shadowsocksr.tar.gz https://github.com/shadowsocksrr/shadowsocksr/archive/${SSR_VERSION}.tar.gz \
	&& tar zxf /tmp/shadowsocksr.tar.gz -C /tmp \
	&& mv /tmp/shadowsocksr/shadowsocks /usr/local/ \
	&& rm -fr /tmp/shadowsocksr \
	&& rm -f /tmp/shadowsocksr.tar.gz

COPY ./config.json /etc/shadowsocksr/config.json
VOLUME /etc/shadowsocksr

USER nobody

CMD [ "/usr/local/shadowsocks/server.py", "-c", "/etc/shadowsocksr/config.json" ]