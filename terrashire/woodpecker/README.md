# Woodpecker

set -a
source .my-env
docker-compose up -d

## Resources

- [Docker Options](https://woodpecker-ci.org/docs/administration/configuration/backends/docker)
- [Local Development Guide](https://woodpecker-ci.org/docs/development/getting-started)
- [Local Woodpecker Config Explained](https://wilw.dev/notes/woodpecker)
- [Cool Guy](https://jan.wildeboer.net/2024/12/Woodpecker-Shenanigans/)

https://wilw.dev/blog/2023/04/23/woodpecker-ci/


server {
    listen 443 ssl http2;
    server_name woodpecker.example.com;
    location / {
        grpc_pass grpc://127.0.0.1:3002;
    }
}

```
proxy_read_timeout 3600s;
proxy_connect_timeout 3600s;
proxy_send_timeout 3600s;

proxy_set_header X-Forwarded-For $remote_addr;
proxy_set_header X-Forwarded-Proto $scheme;

proxy_http_version 1.1;
proxy_buffering off;
chunked_transfer_encoding off;

proxy_hide_header X-XSS-Protection;
add_header X-XSS-Protection "0";
add_header X-Frame-Options "SAMEORIGIN" always;
```
