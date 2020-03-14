# Certbot
Certbot is EFF's tool to obtain certs from Let's Encrypt and (optionally) auto-enable HTTPS on your server. It can also act as a client for any other CA that uses the ACME protocol.

# Command
```bash
--nginx                         # nginx mode
--webroot                       # webroot mode
--standalone                    # standalone mode(need 443 port)
--manual                        # manual mode
--preferred-challenges          # dns(wildcard)
--server                        # server of acme-v02
--dry-run                       # test
```

## Usage
```bash
# nginx
certbot certonly --nginx --nginx-server-root /usr/local/nginx/conf

# webroot
certbot certonly --webroot -w /var/www/example -d example.com

# standalone
certbot certonly --standalone -d example.com

# wildcard
certbot certonly --manual --preferred-challenges dns -d "*.example.com" --server https://acme-v02.api.letsencrypt.org/directory

# renew
certbot renew --dry-run # for test
certbot renew

# update registration
certbot register --update-registration --email <email>
```

# Remark
For domain names not supported by certbot, you need to manually add DNS resolution.  
eg: Aliyun dns
* Use manual mode
* Get DNS TXT info from console. Like bekow:  
  Host record: _acme-challenge.example.com  
  Record value: xxxxxxxxxxxxxxxxxxxxxxxxxxxxx  
* Add host record & value to dns server, and contine to finish.
