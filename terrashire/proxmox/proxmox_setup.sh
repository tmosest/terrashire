# TODO figure out missing roles
# These commands need to be run on the new generated PROXMOX host
pveum role add terraform-role -privs "VM.Allocate VM.Clone VM.Config.CDROM VM.Config.CPU VM.Config.Cloudinit VM.Config.Disk VM.Config.HWType VM.Config.Memory VM.Config.Network VM.Config.Options VM.Audit VM.PowerMgmt Datastore.AllocateSpace Datastore.Audit"

pveum user add terraform@pve

pveum aclmod / -user terraform@pve -role terraform-role

pveum user token add terraform@pve terraform-token --privsep=0