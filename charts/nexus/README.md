Nexus
=====

## Create
```bash
# create kubernetes deployment file
helm template nexus nexus --values nexus/values.yaml > deployment.yaml
# create helm package
helm package nexus --version 3.22.0 --app-version 3.22.0
```

## Push
```bash
helm plugin install https://github.com/chartmuseum/helm-push.git
helmpush nexus-3.22.0.tgz https://chart.chaldea.cn
# force push 
helmpush --force nexus-3.22.0.tgz https://chart.chaldea.cn
```

## Installation
```bash
# install by kubectl
kubectl apply -f deployment.yaml -n nexus
# install by helm
helm install nexus nexus
```