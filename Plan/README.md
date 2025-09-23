# Overview

My Target is ...

Infra Diagram

&nbsp;

## Network

**IP Table**

|Range|Host|Domain|Note|
|:---:|---|---|---|
|001|OpenWrt|router+dns|Redmi AX6000|
|002||||
|003|ca-root|-|Proxmox VM|
|004|ca-server|ca|Proxmox LXC|
|005|Proxmox VE|pve|Lenovo M70q|
|006|Proxmox BS|pbs|Preserved|
|007|NAS|nas|Lenovo M720q|
|008||||
|009|iVentoy|-|LXC|
|010|Control-Plane VIP|k8s||
|011|Control-Plane-001||Radxa X4|
|012|Control-Plane-002||Radxa X4|
|013|Control-Plane-003||Radxa X4|
|020||||
|021|Worker-Node-001||Lenovo M720q|
|022|Worker-Node-002||Lenovo M720q|
|023|Worker-Node-003||Lenovo M720q|
|030|MetalLB IP Range|*(wildcard)|for traefik-ingress|
|031-039|MetalLB IP Range||for service|
|040-099|Proxmox VM Range|||
|100-149|DHCP Range|||

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
