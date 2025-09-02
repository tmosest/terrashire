# https://registry.terraform.io/providers/Sander0542/nginxproxymanager/latest/docs

terraform {
    required_providers {
        nginxproxymanager = {
          source  = "Sander0542/nginxproxymanager"
          version = "1.2.1" # Use the latest stable version
        }
    }
}

provider "nginxproxymanager" {
    url      = var.npm_url
    username = var.npm_username
    password = var.npm_password
}

/*
  Un comment below to generate an SSL cert

  duckdns.org is helpful
*/
/*
resource "nginxproxymanager_certificate_letsencrypt" "moseslab" {
  domain_names = [var.npm_domain_name, "*.${var.npm_domain_name}"]

  letsencrypt_email = var.npm_letsencrypt_email
  letsencrypt_agree = true

  dns_challenge            = true
  dns_provider             = "duckdns"
  dns_provider_credentials = "dns_duckdns_token=${var.npm_letsencrypt_secret}"
}
*/

/*
  Un comment below to add a proxy host for nginx.
*/
/*
resource "nginxproxymanager_proxy_host" "nginx" {
  domain_names = ["ngnix.${var.npm_domain_name}"]

  forward_scheme = "http"
  forward_host   = var.npm_nginx_ip
  forward_port   = 81

  caching_enabled         = false
  allow_websocket_upgrade = false
  block_exploits          = false

  # access_list_id = 2

  locations = [
  ]

  certificate_id  = nginxproxymanager_certificate_letsencrypt.moseslab.id
  ssl_forced      = true
  http2_support   = true
  hsts_enabled    = false
  hsts_subdomains = false
}
*/
