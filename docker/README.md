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