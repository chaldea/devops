安装
yum install http://resources.ovirt.org/pub/yum-repo/ovirt-release43.rpm
yum update
yum install cockpit-ovirt-dashboard
systemctl enable cockpit.socket
systemctl start cockpit.socket
配置防火墙规则
443 9090

挂在数据中心
文件夹权限
chmod 775 /vm/data
chown qemu:kvm /vm/data
