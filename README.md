# Terra Shire CLI

Terrashire CLI is a convient and easy way to manage your network as infrastructure using the command line.

Generates Terraform Code Repos that manage network state.

The tool generates a repo with [terraform code](https://developer.hashicorp.com/terraform) patterns and then makes it easy to edit those configurations.

## Getting Started

This python project can be installed as a command line tool. 

### Setup

```
source ~/.venv/bin/activate

pip3 install -r requirements.txt

pipx install . --verbose --force

terrashire help
```

There should now be a new `terrashire` command.

### Commands

Terraform comes with helpful commands for setting up a homelab and keeping everything up-to-date / in-sync with code.

#### Init Project

To setup a new homelab we can now use the `terrashire` command line tool.

Either 

`cd /path/to/where/you/want/infrastructure/repo && terrashire init .`

OR

`terrashire init /path/to/where/you/want/infrastructure/repo`

This should create a new folder if it not there, init a git repo, and move over any folders and files to get started.

E.G. `terrashire init ~/terrashire-cli-test`

#### Init Feature

In this example we will add `opnsense` to our homelab. We can replace `opnsense` with other options like `ngm` etc to use those features.

Either 

`cd /path/to/where/you/want/infrastructure/repo && terrashire opnsense init`

This will generate an `opnsense` folder inside of your repo. 

All sensitive data such as passwords will be stored in files that are not tracked by the git repo by default.
They will need to be added as environmental variables in any build tools.

# Sources

- [Command Line Tool](https://packaging.python.org/en/latest/guides/creating-command-line-tools/)
- [Terraform code](https://developer.hashicorp.com/terraform)

Note: This repo is combination of Terra for Earth / Home / Terraform and The Shire, the home of the hobbits, from Lord of The Rings. 
