### Install Docker
```
yum install -y yum-utils
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
yum install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### Docker Register Service
```
systemctl enable docker.service
systemctl start docker.service
# add promission (need relogin)
sudo usermod -a -G docker $USER
```

### Use Aliyun Docker Mirror
```
mkdir -p /etc/docker
tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://up673l1h.mirror.aliyuncs.com"]
}
EOF
systemctl daemon-reload
systemctl restart docker
```