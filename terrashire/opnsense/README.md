# OPNSense 

Open Source routing software.

This folder contains your terraform code and env variables to edit your router.

```
Creating an OPNsense API Key:
Access User Management:
.
Navigate to System > Access > Users within the OPNsense web GUI.
Select or Create User:
.
Choose an existing user or create a new user account that will be used for API access. It is recommended to create a dedicated user for API interactions for better security and access control.
Generate API Key:
.
Edit the selected user. Under the "API keys" section, locate and click the "Add" (or "+") button to generate a new key/secret pair. 
Download Key/Secret:
.
A text file containing the generated API key and secret will be downloaded. This file is crucial as the secret is only generated once and is not stored on OPNsense.
Securely Store Credentials:
.
Store the downloaded key and secret in a secure location, as they are required for authenticating API calls.
```

```
terraform init
terraform plan -out plan
terraform apply "plan"
```

That should edit your server. Assuming your `./terraform.tfvars` are correctly set.

## Sources

- [Terraform](https://registry.terraform.io/providers/browningluke/opnsense/latest/docs)
- https://github.com/dalet-oss/terraform-provider-opnsense
