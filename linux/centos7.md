查看系统版本
cat /etc/centos-release
cat /etc/os-release
uname -r

ssh远程登录
ssh -l root -p 1234 192.168.50.51

修改ssh端口
vi /etc/ssh/sshd_config
#Port 22
systemctl restart sshd

修改防火墙规则
systemctl start firewalld
systemctl status firewalld
systemctl stop firewalld
firewall-cmd --zone=public --list-ports
firewall-cmd --zone=public --add-port=28721/tcp --permanent
firewall-cmd --zone= public --remove-port=80/tcp --permanent
firewall-cmd --reload

tar.gz
tar -xvzf xxx.tar.gz
tar -xvzf xxx.tar.gz -C /opt/xxx
tar -cvzf xxx.tar.gz /opt/xxx

文件传输
scp -P 1234 root@192.168.50.51:/home
scp -r dir root@192.168.1.101:/data/storage/anime

修改yum源
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
mv /etc/yum.repos.d/epel.repo /etc/yum.repos.d/epel.repo.backup
curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
curl -o /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo
yum clean all
yum makecache

修改HostName
hostnamectl set-hostname xxx
hostnamectl set-hostname ""

修改网络参数
uuidgen #注意：复制的虚拟机的网卡的UUID是重复的
vi /etc/sysconfig/network-scripts/ifcfg-eth0
service network restart

CentOS企业版替换免费的yum
确保已经安装wget类工具
# 查看yum包
rpm -qa |grep yum
# 卸载yum
rpm -qa|grep yum|xargs rpm -e --nodeps
# 从第三方源下载刚刚卸载的yum包
curl -o yum-3.4.3-161.el7.centos.noarch.rpm https://mirrors.aliyun.com/centos/7.6.1810/os/x86_64/Packages/yum-3.4.3-161.el7.centos.noarch.rpm
curl -o yum-plugin-fastestmirror-1.1.31-50.el7.noarch.rpm https://mirrors.aliyun.com/centos/7.6.1810/os/x86_64/Packages/yum-plugin-fastestmirror-1.1.31-50.el7.noarch.rpm
curl -o yum-utils-1.1.31-50.el7.noarch.rpm https://mirrors.aliyun.com/centos/7.6.1810/os/x86_64/Packages/yum-utils-1.1.31-50.el7.noarch.rpm
curl -o yum-plugin-versionlock-1.1.31-50.el7.noarch.rpm https://mirrors.aliyun.com/centos/7.6.1810/os/x86_64/Packages/yum-plugin-versionlock-1.1.31-50.el7.noarch.rpm
curl -o yum-metadata-parser-1.1.4-10.el7.x86_64.rpm https://mirrors.aliyun.com/centos/7.6.1810/os/x86_64/Packages/yum-metadata-parser-1.1.4-10.el7.x86_64.rpm
# 安装yum包
rpm -ivh yum-*

NTP时间同步
vi /etc/ntp.conf
server 0.cn.pool.ntp.org iburst
server 1.cn.pool.ntp.org iburst
server 2.cn.pool.ntp.org iburst
server 3.cn.pool.ntp.org iburst
systemctl start ntpd
ntpstat

磁盘管理
lsblk
parted 
fdisk

ACL权限控制
查看是否开启ACL控制
dumpe2fs -h /dev/sdb1 | grep options

