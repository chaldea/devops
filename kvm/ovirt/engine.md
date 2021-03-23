Engine登录时提示未注册
The redirection URI for client is not registered
OR
The client is not authorized to request an authorization. It's required to access the system using FQDN.
方案一、本地Host写域名，使用域名访问
方案二、
```
vi /etc/ovirt-engine/engine.conf.d/99-sso.conf
# SSO_CALLBACK_PREFIX_CHECK=false
service ovirt-engine restart
```

Backup
```
engine-backup --mode=backup
```
Backup File Path: /var/lib/ovirt-engine-backup/xxx.backup