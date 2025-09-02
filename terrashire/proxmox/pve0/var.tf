# Blank var for use by terraform.tfvars
variable "ssh_key" {
}

variable "token_secret" {
}

variable "token_id" {
}

variable "url" {
}

variable "proxmox_host" {
    default = "pv0"
}

variable "app_name" {
    default = "node"
}

variable "clone" {
    default = "builder"
}

# Provide the url of the host you would like the API to communicate on.
# It is safe to default to setting this as the URL for what you used
# as your `proxmox_host`, although they can be different
variable "api_url" {
    default = "${var.url}/api2/json"
}

# TODO most of this is not being used really.
# --------------------------------------------------------------

# Specify which template name you'd like to use
variable "template_name" {
    default = "ubuntu-25.04-standard"
}
# Establish which nic you would like to utilize
variable "nic_name" {
    default = "vmbr1"
}
# Establish the VLAN you'd like to use
variable "vlan_num" {
    default = "0"
}