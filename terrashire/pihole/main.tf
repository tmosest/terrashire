# https://registry.terraform.io/providers/ryanwholey/pihole/latest/docs
terraform {
  required_providers {
    pihole = {
      source = "ryanwholey/pihole"
    }
  }
}

provider "pihole" {
    url      = var.pihole_url              # PIHOLE_URL
    password = var.pihole_password         # PIHOLE_PASSWORD
}
