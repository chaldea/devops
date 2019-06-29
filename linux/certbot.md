certbot --nginx certonly --nginx-server-root /usr/local/nginx/conf

certbot register --update-registration --email <email>

certbot --standalone --server https://acme-v02.api.letsencrypt.org/directory -d *.chaldea.cn --manual --preferred-challenges dns-01 certonly

certbot certonly --standalone -d example.com -d www.example.com