# Terra Shire CLI

Terrashire CLI is a convient and easy way to manage your network as infrastructure using the command line.

![The Shire](imgs/the_shire.webp)

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

#### Unit Tests

```
source ~/.venv/bin/activate
pytest
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

### Tech stack

<table>
    <tr>
        <th>Logo</th>
        <th>Name</th>
        <th>Description</th>
    </tr>
    <tr>
        <td><img width="32" src="https://simpleicons.org/icons/ansible.svg"></td>
        <td><a href="https://www.ansible.com">Ansible</a></td>
        <td>Automate bare metal provisioning and configuration</td>
    </tr>
    <tr>
        <td><img width="32" src="https://avatars.githubusercontent.com/u/30269780"></td>
        <td><a href="https://argoproj.github.io/cd">ArgoCD</a></td>
        <td>GitOps tool built to deploy applications to Kubernetes</td>
    </tr>
    <tr>
        <td><img width="32" src="https://github.com/jetstack/cert-manager/raw/master/logo/logo.png"></td>
        <td><a href="https://cert-manager.io">cert-manager</a></td>
        <td>Cloud native certificate management</td>
    </tr>
    <tr>
        <td><img width="32" src="https://avatars.githubusercontent.com/u/21054566?s=200&v=4"></td>
        <td><a href="https://cilium.io">Cilium</a></td>
        <td>eBPF-based Networking, Observability and Security (CNI, LB, Network Policy, etc.)</td>
    </tr>
    <tr>
        <td><img width="32" src="https://avatars.githubusercontent.com/u/314135?s=200&v=4"></td>
        <td><a href="https://www.cloudflare.com">Cloudflare</a></td>
        <td>DNS and Tunnel</td>
    </tr>
    <tr>
        <td><img width="32" src="https://www.docker.com/wp-content/uploads/2022/03/Moby-logo.png"></td>
        <td><a href="https://www.docker.com">Docker</a></td>
        <td>Ephemeral PXE server</td>
    </tr>
    <tr>
        <td><img width="32" src="https://github.com/kubernetes-sigs/external-dns/raw/master/docs/img/external-dns.png"></td>
        <td><a href="https://github.com/kubernetes-sigs/external-dns">ExternalDNS</a></td>
        <td>Synchronizes exposed Kubernetes Services and Ingresses with DNS providers</td>
    </tr>
    <tr>
        <td><img width="32" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Fedora_logo.svg/267px-Fedora_logo.svg.png"></td>
        <td><a href="https://getfedora.org/en/server">Fedora Server</a></td>
        <td>Base OS for Kubernetes nodes</td>
    </tr>
    <tr>
        <td><img width="32" src="https://upload.wikimedia.org/wikipedia/commons/b/bb/Gitea_Logo.svg"></td>
        <td><a href="https://gitea.com">Gitea</a></td>
        <td>Self-hosted Git service</td>
    </tr>
    <tr>
        <td><img width="32" src="https://grafana.com/static/img/menu/grafana2.svg"></td>
        <td><a href="https://grafana.com">Grafana</a></td>
        <td>Observability platform</td>
    </tr>
    <tr>
        <td><img width="32" src="https://helm.sh/img/helm.svg"></td>
        <td><a href="https://helm.sh">Helm</a></td>
        <td>The package manager for Kubernetes</td>
    </tr>
    <tr>
        <td><img width="32" src="https://avatars.githubusercontent.com/u/49319725"></td>
        <td><a href="https://k3s.io">K3s</a></td>
        <td>Lightweight distribution of Kubernetes</td>
    </tr>
    <tr>
        <td><img width="32" src="https://kanidm.com/images/logo.svg"></td>
        <td><a href="https://kanidm.com">Kanidm</a></td>
        <td>Modern and simple identity management platform</td>
    </tr>
    <tr>
        <td><img width="32" src="https://avatars.githubusercontent.com/u/13629408"></td>
        <td><a href="https://kubernetes.io">Kubernetes</a></td>
        <td>Container-orchestration system, the backbone of this project</td>
    </tr>
    <tr>
        <td><img width="32" src="https://github.com/grafana/loki/blob/main/docs/sources/logo.png?raw=true"></td>
        <td><a href="https://grafana.com/oss/loki">Loki</a></td>
        <td>Log aggregation system</td>
    </tr>
    <tr>
        <td><img width="32" src="https://avatars.githubusercontent.com/u/1412239?s=200&v=4"></td>
        <td><a href="https://www.nginx.com">NGINX</a></td>
        <td>Kubernetes Ingress Controller</td>
    </tr>
    <tr>
        <td><img width="32" src="https://raw.githubusercontent.com/NixOS/nixos-artwork/refs/heads/master/logo/nix-snowflake-colours.svg"></td>
        <td><a href="https://nixos.org">Nix</a></td>
        <td>Convenient development shell</td>
    </tr>
    <tr>
        <td><img width="32" src="https://ntfy.sh/_next/static/media/logo.077f6a13.svg"></td>
        <td><a href="https://ntfy.sh">ntfy</a></td>
        <td>Notification service to send notifications to your phone or desktop</td>
    </tr>
    <tr>
        <td><img width="32" src="https://avatars.githubusercontent.com/u/3380462"></td>
        <td><a href="https://prometheus.io">Prometheus</a></td>
        <td>Systems monitoring and alerting toolkit</td>
    </tr>
    <tr>
        <td><img width="32" src="https://docs.renovatebot.com/assets/images/logo.png"></td>
        <td><a href="https://www.whitesourcesoftware.com/free-developer-tools/renovate">Renovate</a></td>
        <td>Automatically update dependencies</td>
    </tr>
    <tr>
        <td><img width="32" src="https://raw.githubusercontent.com/rook/artwork/master/logo/blue.svg"></td>
        <td><a href="https://rook.io">Rook Ceph</a></td>
        <td>Cloud-Native Storage for Kubernetes</td>
    </tr>
    <tr>
        <td><img width="32" src="https://avatars.githubusercontent.com/u/48932923?s=200&v=4"></td>
        <td><a href="https://tailscale.com">Tailscale</a></td>
        <td>VPN without port forwarding</td>
    </tr>
    <tr>
        <td><img width="32" src="https://avatars.githubusercontent.com/u/13991055?s=200&v=4"></td>
        <td><a href="https://www.wireguard.com">Wireguard</a></td>
        <td>Fast, modern, secure VPN tunnel</td>
    </tr>
    <tr>
        <td><img width="32" src="https://avatars.githubusercontent.com/u/84780935?s=200&v=4"></td>
        <td><a href="https://woodpecker-ci.org">Woodpecker CI</a></td>
        <td>Simple yet powerful CI/CD engine with great extensibility</td>
    </tr>
    <tr>
        <td><img width="32" src="https://zotregistry.dev/v2.0.2/assets/images/logo.svg"></td>
        <td><a href="https://zotregistry.dev">Zot Registry</a></td>
        <td>Private container registry</td>
    </tr>
</table>

# Sources

- [Python Command Line Tool](https://packaging.python.org/en/latest/guides/creating-command-line-tools/)
- [Terraform code](https://developer.hashicorp.com/terraform)
- [khuedoan/homelab](https://github.com/khuedoan/homelab)
- [Ephemeral PXE server inspired by Minimal First Machine in the DC](https://speakerdeck.com/amcguign/minimal-first-machine-in-the-dc)
- [ArgoCD usage and monitoring configuration in locmai/humble](https://github.com/locmai/humble)
- [README template](https://github.com/othneildrew/Best-README-Template)
- [Run the same Cloudflare Tunnel across many `cloudflared` processes](https://developers.cloudflare.com/cloudflare-one/tutorials/many-cfd-one-tunnel)
- [MAC address environment variable in GRUB config](https://askubuntu.com/questions/1272400/how-do-i-automate-network-installation-of-many-ubuntu-18-04-systems-with-efi-and)
- [Official k3s systemd service file](https://github.com/k3s-io/k3s/blob/master/k3s.service)
- [Official Cloudflare Tunnel examples](https://github.com/cloudflare/argo-tunnel-examples)
- [Initialize GitOps repository on Gitea and integrate with Tekton by RedHat](https://github.com/redhat-scholars/tekton-tutorial/tree/master/triggers)
- [SSO configuration from xUnholy/k8s-gitops](https://github.com/xUnholy/k8s-gitops)
- [Pre-commit config from k8s-at-home/flux-cluster-template](https://github.com/k8s-at-home/flux-cluster-template)
- [Diátaxis technical documentation framework](https://diataxis.fr)
- [Official Terratest examples](https://github.com/gruntwork-io/terratest/tree/master/test)
- [Self-host an automated Jellyfin media streaming stack](https://zerodya.net/self-host-jellyfin-media-streaming-stack)
- [App Template Helm chart by bjw-s](https://bjw-s-labs.github.io/helm-charts/docs/app-template)
- [Various application configurations in onedr0p/home-ops](https://github.com/onedr0p/home-ops)
- [Docker Options](https://woodpecker-ci.org/docs/administration/configuration/backends/docker)
- [Local Development Guide](https://woodpecker-ci.org/docs/development/getting-started)
- [Local Woodpecker Config Explained](https://wilw.dev/notes/woodpecker)
- [Cool Guy](https://jan.wildeboer.net/2024/12/Woodpecker-Shenanigans/)
- [NGINX Proxy Setup](https://anthonyconstant.co.uk/blog/f/local-ssl-certificate-using-nginx-proxy-manager-dockerportainer)
- [What Is PXE Boot and How Does It Work?](https://heimdalsecurity.com/blog/what-is-pxe-boot/)
- [Set up a Kubernetes cluster in under 5 minutes with Proxmox and k3s](https://dev.to/mihailtd/set-up-a-kubernetes-cluster-in-under-5-minutes-with-proxmox-and-k3s-2987)
- [khanh-ph/proxmox-kubernetes](https://github.com/khanh-ph/proxmox-kubernetes)
- [Ghost Kub](https://github.com/sredevopsorg/ghost-on-kubernetes)
- [terraform-provider-matchbox](https://github.com/poseidon/terraform-provider-matchbox)
- [Dynamic DNS Using AWS Route 53](https://avishayil.medium.com/dynamic-dns-using-aws-route-53-60a2331a58a4)
- [Setting Up the AWS CLI & IAM User API Keys](https://medium.com/@terminalsandcoffee/setting-up-the-aws-cli-iam-user-api-keys-b83554e314e4)
- [Set up nginx-proxy-manager with LetsEncrypt SSL certificates](https://unixorn.github.io/post/hass/2023-07-09-set-up-nginx-proxy-manager/)
- [ARGO CD](https://argoproj.github.io/cd/)
- [Next Cloud Drive](https://github.com/nextcloud/all-in-one#nextcloud-all-in-one)
- [Borg Backup](https://github.com/borgbackup/borg#what-is-borgbackup)
- [PiHole](https://pi-hole.net/)
- [Wordpress Docker Compose](https://github.com/nezhar/wordpress-docker-compose)
- [Kubernetes on Proxmox: A Practical Guide for DevOps](https://www.plural.sh/blog/kubernetes-on-proxmox-guide/)
- [https://kustomize.io/](https://kustomize.io/)
- [https://helm.sh/](https://helm.sh/)
- [Deploy Docker/Compose using Woodpecker CI](https://hinty.io/vverenko/deploy-docker-compose-using-woodpecker-ci/)
- [Ghost on Docker with Traefik](https://faun.pub/ghost-on-docker-with-traefik-50358b59dfd3)

## Useful Homelab Tools

- [OPNSense / PFSense : Router Software]()
    - [Terraform and OPNSense](https://registry.terraform.io/providers/browningluke/opnsense/latest/docs)
- [Argo CD](https://argoproj.github.io/cd/)
- [Borg Backup](https://github.com/borgbackup/borg#what-is-borgbackup)
- [PiHole : DNS Sink](https://pi-hole.net/)
    - [PiHole Setup Guide](https://www.raspberrypi.com/tutorials/running-pi-hole-on-a-raspberry-pi/)
- [Gitea : Git Hosting]()
- [NextCloud : Files](https://github.com/nextcloud/all-in-one#nextcloud-all-in-one)
- [WoodPecker : CI / CD Tech](https://woodpecker-ci.org/docs/intro)
    - [Docker Compose WoodPecker](https://codeberg.org/alexruf/docker-compose-woodpecker-ci)
- [khuedoan : Great setup and easy config on a cluster](https://github.com/khuedoan/homelab)
- [Local Docker Registry: I like her site I should copy this basically](https://www.allisonthackston.com/articles/local-docker-registry.html)

## Useful Hardware

- [OPNSense Router 4 Ports](https://a.co/d/13mnVcU)
- [NAS 2 Bay](https://a.co/d/fwVYIlW)
- [Mini Server $150](https://a.co/d/gJYIDzQ)
- [Mini PC or OPNSense](https://a.co/d/98bnOv4)
- [8 Port Switch](https://a.co/d/1AAodm2)

Note: This repo is combination of Terra for Earth / Home / Terraform and The Shire, the home of the hobbits, from Lord of The Rings. 

Moses was here.
