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
