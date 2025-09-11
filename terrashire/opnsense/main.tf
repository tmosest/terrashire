# https://registry.terraform.io/providers/browningluke/opnsense/latest/docs
# https://github.com/dalet-oss/terraform-provider-opnsense
terraform {
  required_providers {
    opnsense = {
      source = "gxben/opnsense"
      version = "0.3.0"
    }
  }
}

provider "opnsense" {
  uri = var.opnsense_ip
  user = var.opnsense_user
  password = var.opnsense_password
}

/*
resource "opnsense_dhcp_static_map" "dhcp1" {
  interface = "opt3"
  mac       = "00:11:22:33:44:55"
  ipaddr    = "192.168.0.100"
  hostname  = "my_hostname"
}

resource "opnsense_dns_host_override" "dns1" {
  type   = "A"
  host   = "www"
  domain = "acme.local"
  ip     = "192.168.0.1"
}
*/
