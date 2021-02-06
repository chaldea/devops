## 部署集群
```bash
# 1.安装ansible
yum install git python-pip -y
pip install pip --upgrade -i https://mirrors.aliyun.com/pypi/simple/
pip install ansible==2.6.18 netaddr==0.7.19 -i https://mirrors.aliyun.com/pypi/simple/
# 2.设置证书登录(所有机器包括管理节点)
ssh-keygen -t rsa -b 2048 -N '' -f ~/.ssh/id_rsa
ssh-copy-id 192.168.1.151
# 3.下载安装脚本和程序文件
curl -C- -fLO --retry 3 https://github.com/easzlab/kubeasz/releases/download/2.2.0/easzup
chmod +x ./easzup
./easzup -D
# 4.修改配置并部署
cd /etc/ansible && cp example/hosts.multi-node hosts
ansible-playbook 90.setup.yml
```

## 获取dashboard端口和管理员账号
```bash
kubectl get svc -n kube-system
kubectl -n kube-system describe secret $(kubectl -n kube-system get secret | grep admin-user | awk '{print $1}')
```

## 创建标签
```bash
kubectl get nodes --show-labels=true
kubectl label node 192.168.1.154 storage=repository
kubectl label node 192.168.1.155 storage=database
kubectl label node 192.168.1.156 storage=nas
```

## 安装NPS反向代理
```bash
kubectl create namespace chaldea-proxy
kubectl apply -f nps/npc-deployment.yaml -n chaldea-proxy
```

## 安装rancher
```bash
kubectl create namespace cattle-system
kubectl apply -f rancher/local-path-storage.yaml
kubectl apply -f rancher/deployment.yaml -n cattle-system
```

## 安装cert-manager
```bash
# 部署cert-manager组件(https://github.com/jetstack/cert-manager/releases/download/v0.14.1/cert-manager.yaml)
kubectl apply --validate=false -f cert-manager/cert-manager.yaml
# 3.安装阿里云DNS插件
kubectl apply -f cert-manager/rbac.yaml -n kube-system
kubectl apply -f cert-manager/webhook-alidns.yaml -n cert-manager
kubectl -n cert-manager create secret generic alidns-credentials --from-literal=accessKeySecret='xxxxxxxx'
kubectl apply -f cert-manager/cluster-issuer.yaml
```

## 安装traefik
```bash
# 1.查看traefik默认是否已经安装
kubectl get all -n kube-system | grep traefik
# 2.创建默认https证书
kubectl create secret generic traefik-cert --from-file=traefik/pki/tls.crt --from-file=traefik/pki/tls.key -n kube-system
# 3.创建ConfigMap
kubectl create configmap traefik-conf --from-file=traefik/traefik.toml -n kube-system
# 4.部署组件
kubectl apply -f traefik/deployment.yaml -n kube-system
```

## 安装nexus
```bash
kubectl create namespace chaldea-repository
helm template nexus ../charts/nexus --values ../charts/nexus/values.yaml > ./nexus/deployment.yaml
kubectl apply -f nexus/deployment.yaml -n chaldea-repository
```

## 安装minio
```bash
# Use helm (minio/values.yaml)
# namespace: chaldea-repository
```

## 安装openldap
```bash
kubectl create namespace chaldea-auth
# Use helm (openldap/values.yaml)
# 登录openldap管理员
# Host: NodeIP  Port: NodePort
# Base: dc=chaldea,dc=cn
# UserName: cn=admin,dc=chaldea,dc=cn
# Password: kubectl get secret -n chaldea-auth (通过查看secret来获取密码)
# 密码有两个
# LDAP_ADMIN_PASSWORD 对应账号admin
# LDAP_CONFIG_PASSWORD 对应账号config
```

## 安装mongodb
```bash
kubectl create namespace chaldea-database
# Use helm (mongodb/values.yaml)
```

## 安装postgresql
```bash

```