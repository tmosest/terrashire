# OPNSense 

Open Source routing software.

This folder contains your terraform code and env variables to edit your router.

```
terraform init
terraform plan -out plan
terraform apply "plan"
```

That should edit your server. Assuming your `./terraform.tfvars` are correctly set.

## Sources

- [Terraform](https://registry.terraform.io/providers/browningluke/opnsense/latest/docs)
