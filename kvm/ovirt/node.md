安装Node代理
Node代理用于向Engine注册主机名和IP地址
yum -y install epel-release
yum install ovirt-guest-agent-common
systemctl enable ovirt-guest-agent.service
systemctl start ovirt-guest-agent.service
systemctl status ovirt-guest-agent.service

sasl认证
saslpasswd2 -a libvirt admin

Unmanaged Interfaces
remove config from /etc/sysconfig/network-scripts/ifcfg-`interfaces`
NM_CONTROLLED=no
