# Overview

My Target is ...

Infra Diagram

&nbsp;

## Network

**IP Table**

|Range|Host|Domain|Note|
|:---:|---|---|---|
|001|OpenWrt|router|Redmi AX6000|
|002|ca-root|-|Proxmox VM|
|003|ca-server|ca|Proxmox LXC|
|010|pve-00|pve-00|Lenovo M70q, Proxmox Master|
|011|pve-01|pve-01|Lenovo M720q, Proxmox Node 01|
|012|pve-02|pve-02|Lenovo M720q, Proxmox Node 02|
|013|pve-03|pve-03|Lenovo M720q, Proxmox Node 03|
|020||k8s|TalOS Vip|
|021|TalOS-Master-01||TalOS Control-Plane VM|
|022|TalOS-Master-02||TalOS Control-Plane VM|
|023|TalOS-Master-03||TalOS Control-Plane VM|
|030||||
|031|TalOS-Worker-01||TalOS Worker-Node VM|
|032|TalOS-Worker-02||TalOS Worker-Node VM|
|033|TalOS-Worker-03||TalOS Worker-Node VM|
|040-099|Proxmox VM Range|||
|150-249|DHCP Range|||
|||||

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
