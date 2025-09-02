# Proxmox

Open Source virtual machine software.

## Setup

Need to setup an API on the proxmox instance and it is good to give them static ip addresses in used blocks at least in opnsense settings.

Notes need more permissions than these. TODO update this list to include everything instead of using the roles in the admin GUI
```
pveum role add terraform-role -privs "VM.Allocate VM.Clone VM.Config.CDROM VM.Config.CPU VM.Config.Cloudinit VM.Config.Disk VM.Config.HWType VM.Config.Memory VM.Config.Network VM.Config.Options VM.Audit VM.PowerMgmt Datastore.AllocateSpace Datastore.Audit"

pveum user add terraform@pve

pveum aclmod / -user terraform@pve -role terraform-role

pveum user token add terraform@pve terraform-token --privsep=0
```

┌──────────────┬──────────────────────────────────────┐
│ key          │ value                                │
╞══════════════╪══════════════════════════════════════╡
│ full-tokenid │ terraform@pve!terraform-token        │
├──────────────┼──────────────────────────────────────┤
│ info         │ {"privsep":"0"}                      │
├──────────────┼──────────────────────────────────────┤
│ value        │ XXXXX-XXXXX-XXXXX-XXXXX-XXXXX        │
└──────────────┴──────────────────────────────────────┘

## Terraform

This folder contains your terraform code and env variables to edit your proxmox instnaces.

Each folder has terraform code for each machine you have. Then nodes can be easily generated fro each machine.

```
cd ./pve0
terraform init
terraform plan -out plan
terraform apply "plan"
```

That should edit your server. Assuming your `./terraform.tfvars` are correctly set.

## Sources

- [Terraform](https://registry.terraform.io/providers/Terraform-for-Proxmox/proxmox/latest/docs)
