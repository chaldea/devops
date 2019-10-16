FROM alpine:3.8

ENV NPS_VERSION 0.23.2
RUN set -x && \
	wget --no-check-certificate https://github.com/cnlh/nps/releases/download/v${NPS_VERSION}/linux_amd64_server.tar.gz && \ 
    mkdir /nps && \
	tar xzf linux_amd64_server.tar.gz -C /nps && \
	rm -rf linux_amd64_server.tar.gz && \
    chmod +x /nps/nps

VOLUME /nps/conf

CMD ["/nps/nps"]