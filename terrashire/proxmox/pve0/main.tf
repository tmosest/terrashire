# https://registry.terraform.io/providers/Terraform-for-Proxmox/proxmox/latest/docs
terraform {
  required_providers {
    proxmox = {
      source = "telmate/proxmox"
      #latest version as of Nov 30 2022
      version = "3.0.2-rc04"
    }
  }
}

provider "proxmox" {
  # References our vars.tf file to plug in the api_url 
  pm_api_url = var.api_url
  # References our secrets.tfvars file to plug in our token_id
  pm_api_token_id = var.token_id
  # References our secrets.tfvars to plug in our token_secret 
  pm_api_token_secret = var.token_secret
  # Default to `true` unless you have TLS working within your pve setup 
  pm_tls_insecure = true

  pm_log_enable = true
  pm_log_file   = "terraform-promox-plugin-${var.app_name}.log"
  pm_debug      = true
  pm_log_levels = {
    _default    = "debug"
    _capturelog = ""
  }
}

/*
  Un Comment below to generate a node on the host machine from a clone
*/
/*
resource "proxmox_vm_qemu" var.app_name {
    name            = var.app_name
    target_node     = var.proxmox_host
    clone           = var.clone
    bios            = "seabios"
    onboot          = true
    ipconfig0       = "ip=dhcp" 
    agent           = 1
    # iso           = "local:iso/ubuntu-25.04-live-server-amd64.iso" # "/var/lib/vz/template/iso/ubuntu-25.04-live-server-amd64.iso" # "local:iso/ubuntu-25.04-live-server-amd64.iso"
    # template      = "ubuntu-25.04"
    cpu {
      cores         = 1
      sockets       = 1
      type          = "host"
    }
    # cpu_type      = "host"
    # cpu_type      = "qemu64" 
    
    memory          = 2048
    boot            = "order=scsi0;net0"
    kvm             = true

    skip_ipv6       = true

    disk {
      slot = "scsi0"
      # set disk size here. leave it small for testing because expanding the disk takes time.
      size = 32
      type = "disk"
      storage = "local-lvm"
      # iothread = true
     }

    network {
        id        = 0
        bridge    = "vmbr0"
        model     = "virtio"
    }

    provisioner "local-exec" {
        when    = create
        command = "sleep 15"
    }
}

output "vm_ip_address" {
  # TOOD figure out dynamic version of this
  value = proxmox_vm_qemu.app-name.default_ipv4_address
}
*/
