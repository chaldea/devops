ssh远程登录
ssh -l root -p 1234 192.168.50.51

修改ssh端口
nano /etc/ssh/sshd_config
#Port 22
service sshd restart

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
