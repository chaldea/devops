Install
yum install qemu-kvm qemu-img libvirt libvirt-python libguestfs-tools virt-install

创建virsh用户
saslpasswd2 -a libvirt {用户名}

UUID挂载硬盘
UUID=d1dde6a6-a082-4e10-aaac-a69172bfcf1f /data auto defaults 0 0

创建网桥
TYPE=Ethernet
PROXY_METHOD="none"
BROWSER_ONLY="no"
DEFROUTE="yes"
IPV4_FAILURE_FATAL="no"
NAME=em4
UUID=80c23439-1e13-45c3-919c-443843c8786f
DEVICE=em4
ONBOOT=yes
IPADDR="192.168.1.101"
PREFIX="24"
GATEWAY="192.168.1.1"
DNS1="114.114.114.114"
IPV6_PRIVACY="no"
BRIDGE=bridge0

STP=no
TYPE=Bridge
PROXY_METHOD=none
BROWSER_ONLY=no
BOOTPROTO=none
IPADDR=192.168.1.101
PREFIX=24
GATEWAY=192.168.1.1
DNS1=114.114.114.114
DEFROUTE=yes
IPV4_FAILURE_FATAL=no
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_FAILURE_FATAL=no
IPV6_ADDR_GEN_MODE=stable-privacy
NAME=bridge0
UUID=07ef9cf2-a6b5-4849-830c-a26ab8ae59ad
DEVICE=bridge0
ONBOOT=yes
AUTOCONNECT_SLAVES=yes

NAT网络模式
配置路径：/etc/libvirt/qemu/networks/default.xml
<network>
  <name>default</name>
  <uuid>b09d09a8-ebbd-476d-9045-e66012c9e83d</uuid>
  <forward mode='nat'/>
  <bridge name='virbr0' stp='on' delay='0'/>
  <mac address='52:54:00:9d:82:de'/>
  <ip address='192.168.122.1' netmask='255.255.255.0'>
    <dhcp>
      <range start='192.168.122.2' end='192.168.122.254'/>
    </dhcp>
  </ip>
</network>

查看网络配置
#查看当前所有网络配置
virsh net-list
#查看详细配置
virsh net-dumpxml default

创建网络配置
virsh net-define /etc/libvirt/qemu/networks/default.xml
virsh net-autostart `name`
virsh net-start `name`

删除配置
virsh net-destory default
virsh net-undefine default

查看网桥
brctl show

重启虚拟化服务
systemctl restart libvirtd

创建磁盘
qemu-img create -f qcow2 -o preallocation=metadata /data/kvm/images/centos7.qcow2 40G

查看支持的machine
/usr/libexec/qemu-kvm -machine ?

查看NVC端口号
netstat -ntlpu | grep kvm

克隆虚拟机
virt-clone -o centos7 -n new_centos7 -f /data/kvm/images/new_centos7.qcow2

hostnamectl set-hostname k8s-node
uuidgen
vi /etc/sysconfig/network-scripts/ifcfg-ens3
systemctl restart network

克隆虚拟机实例
```
# 克隆虚拟机
# o: original 模板
# n: new name 新虚拟机名称
# f: new disk file 新虚拟机磁盘(克隆时自动创建)
virt-clone -o template -n new_vm -f /data/kvm/images/new_vm.qcow2
```

```虚拟机操作
# 查看所有虚拟机
virsh list --all

# 强制关闭虚拟机
virsh destroy chaldea-dev

# 删除虚拟机
virsh undefine chaldea-dev

# 关闭虚拟机
virsh shutdown chaldea-dev

# 启动虚拟机
virsh start chaldea-dev
```
