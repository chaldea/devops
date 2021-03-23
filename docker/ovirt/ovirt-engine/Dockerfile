FROM centos AS base
RUN yum -y install http://resources.ovirt.org/pub/yum-repo/ovirt-release43.rpm
RUN yum update; exit 0
RUN yum -y install ovirt-engine --nogpgcheck; exit 0
RUN echo > /var/log/ovirt-engine/engine.log

FROM base AS final
ENTRYPOINT [ "tail","-f","/var/log/ovirt-engine/engine.log" ]