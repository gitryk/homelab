# Overview

My Target is ...

Infra Diagram

&nbsp;

## Network

**IP Table**

|Range|Host|Domain|Note|
|:---:|---|---|---|
|001|TryK-Router|router|Redmi AX6000(OpenWRT)|
|002|iVentoy||Proxmox LXC(PXE Server)|
|003|ca-root|-|Proxmox LXC(Devian 13)|
|004|ca-server|ca|Proxmox LXC(Devian 13)|
|005|truenas|nas|Lenovo M720q|
|006|pbs|pbs|TrueNAS VM|
|010|pve|pve|Lenovo M70q, Proxmox Master|
|020|k8s-master|k8s|Lenovo M75q Gen2(Talos Linux)|
|021|k8s-worker-01||Lenovo M720q(Talos Linux)|
|022|k8s-worker-02||Lenovo M720q(Talos Linux)|
|023|k8s-worker-03||Lenovo M720q(Talos Linux)|
|025-039|MetalLB IP Range|||
|040-099|Proxmox VM/LXC Range|||
|040|DevOps-Rocky|devops|Proxmox VM(Rocky Linux)|
|050|TryK-Bastion||Proxmox VM(Windows 10 LTSC)|
|100-249|DHCP Range|||
|250|wireguard||Proxmox LXC(VPN Tunnel)|

Etc...

&nbsp;

## Software

Code-Server

Gitea

ArgoCD

S3 API Compatible Storage

MetalLB

Traefik

Immich

Supports the S3 API File Browser

Step-CA

iVentoy

&nbsp;
