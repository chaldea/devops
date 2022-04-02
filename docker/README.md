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

### Enable 2375 Port
```bash
mkdir -p /etc/systemd/system/docker.service.d
vi /etc/systemd/system/docker.service.d/docker.conf
[Service]
ExecStart=
ExecStart=/usr/bin/dockerd -H tcp://0.0.0.0:2375 -H unix://var/run/docker.sock

systemctl daemon-reload
systemctl restart docker
```