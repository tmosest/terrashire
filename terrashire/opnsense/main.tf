# https://registry.terraform.io/providers/browningluke/opnsense/latest/docs
terraform {
  required_providers {
    opnsense = {
      version = "~> x.0"
      source  = "browningluke/opnsense"
    }
  }
}

provider "opnsense" {
  uri = var.opnsense_url
  api_key = var.opnsense_key
  api_secret = var.opnsense_secret
}

/*
  Create a new static mapping using opnsense_dhcp
*/
/*
resource "opnsense_dhcp_static_mapping" "example_static_mapping" {
  interface = "lan"  # Or the interface where the client is connected (e.g., "vlan10")
  mac       = "AA:BB:CC:DD:EE:FF" # MAC address of the client device
  ipaddr    = "192.168.1.100"    # Desired static IP address
  hostname  = "my-static-device" # Optional: hostname for the client
  enabled   = true
}
*/

/*
  Create a new a static IP for the LAN interface itself
*/
/*
resource "opnsense_interface_ipv4" "lan_config" {
  interface = "lan"
  type = "static"
  address = "192.168.1.1/24"
}
*/

# --- Data source for DHCPv4 static mappings ---
# Retrieve a list of all static DHCPv4 mappings for a specific interface.
# Replace "lan" with the appropriate interface ID if needed.
data "opnsense_dhcpv4_static_mappings" "lan_static_ips" {
  interface = "lan"
}

# --- Output the list of static IPs ---
output "static_ip_addresses" {
  description = "Lists all static IP addresses configured on the LAN interface."
  value = [for mapping in data.opnsense_dhcpv4_static_mappings.lan_static_ips.mappings : mapping.ip_address]
}
