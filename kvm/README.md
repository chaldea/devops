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
