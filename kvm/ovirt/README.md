# Introduction
>oVirt is an open source server and desktop virtualization platform built on operating systems like CentOS and Red Hat Enterprise Linux. This guide covers:

1. The installation and configuration of an oVirt Engine.
2. The installation and configuration of hosts.
3. Attach existing FCP storage to your oVirt environment.

## Install oVirt-Engine
### Installing Packages
```bash
yum install http://resources.ovirt.org/pub/yum-repo/ovirt-release43.rpm
yum update
yum install ovirt-engine
```

### Configuring
```bash
engine-setup
```
Detail steps see [Installing](https://ovirt.org/documentation/install-guide/chap-Installing_oVirt.html)

## Install oVirt-Node
### RPM
```bash
yum install http://resources.ovirt.org/pub/yum-repo/ovirt-release43.rpm
yum update
yum install cockpit-ovirt-dashboard
systemctl enable cockpit.socket
systemctl start cockpit.socket
```

## Update Firewall Rules
### firewalld
```bash
firewall-cmd --zone=public --add-port=443/tcp --permanent
firewall-cmd --zone=public --add-port=9090/tcp --permanent
firewall-cmd --reload
```

## Create Local Storage
Create local storage for vm data, iso images and export data. eg:
```bash
mkdir /vm/data /vm/iso /vm/export
chmod -R 775 /vm
chown -R qemu:kvm /vm
```
Then you can add `data, iso, export` domains on the ovirt-engine `Storage Domains` page.

## Upload Image To Local Storage
When use a local storage, you don't need `ovirt-iso-uploader` command to upload a image, just copy the image file to `iso` folder.
