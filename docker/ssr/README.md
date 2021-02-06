# SSR
shadowsocksrr python server.   
See project [SSR](https://github.com/shadowsocksrr/shadowsocksr).

## Usage
* run ssr server
```bash
docker-compose up -d
```
* stop ssr server
```
docker-compose down
```

## Docker-compose
```yaml
version: '3.5'
services:
  ssr:
    container_name: ssr
    image: chaldea/ssr
    restart: always
    network_mode: host
    environment:
      SSR_SERVER_PORT: 8388
      SSR_PASSWORD: UrmjvSmqTxTUjAeh72SGJX6aBJH7Kd
      SSR_METHOD: none
      SSR_PROTOCOL: auth_chain_d
      SSR_OBFS: tls1.2_ticket_auth
```

## Environments
| Name                    | Default Value  |
| :---------------------- | :------------- |
| SSR_SERVER              | 0.0.0.0 |
| SSR_SERVER_PORT         | 8388 |
| SSR_PASSWORD            | UrmjvSmqTxTUjAeh72SGJX6aBJH7Kd |
| SSR_METHOD              | none (more options, [Encryption](#Encryption-Method)) |
| SSR_PROTOCOL            | auth_chain_d (more options, [Protocol](#Protocol)) |
| SSR_PROTOCOL_PARAM      |  |
| SSR_OBFS                | tls1.2_ticket_auth (more options, [Obfs](#Obfs)) |
| SSR_OBFS_PARAM          |  |

## Encryption Method
| Method          | 
| :-------------- | 
| none            | 
| aes-128-ctr     | 
| aes-192-ctr     | 
| aes-256-ctr     | 
| aes-128-cfb     | 
| aes-192-cfb     | 
| aes-256-cfb     | 
| rc4             | 
| rc4-md5         | 
| rc4-md5-6       | 
| aes-128-cfb8    | 
| aes-192-cfb8    | 
| aes-256-cfb8    | 
| salsa20         | 
| chacha20        | 
| xsalsa20        | 
| xchacha20       | 
| chacha20-ietf   |  

## Protocol
| Protocol           |  
| :----------------- | 
| origin             |  
| verify_deflate     |  
| auth_sha1_v4       |  
| auth_aes128_md5    |  
| auth_aes128_sha1   |  
| auth_chain_a       |  
| auth_chain_b       |  
| auth_chain_c       |  
| auth_chain_d       |  
| auth_chain_e       |  
| auth_chain_f       |  
| auth_akarin_rand   |  
| auth_akarin_spec_a |  

## Obfs
| Obfs                   | 
| :--------------------- | 
| plain                  | 
| http_simple            | 
| http_post              | 
| random_head            | 
| tls1.2_ticket_auth     | 
| tls1.2_ticket_fastauth | 