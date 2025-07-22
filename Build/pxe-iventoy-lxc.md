# PXE-iVentoy-LXC

## LXC Build

Run "**Proxmox VE Shell**"

```sh
bash -c "$(curl -fsSL https://raw.githubusercontent.com/community-scripts/ProxmoxVE/main/ct/iventoy.sh)"
```
&nbsp;

## Mount Proxmox ISO Folder
```sh
pct set [LXC ID] -mp0 /var/lib/vz/template/iso,mp=/opt/iventoy/iso
```
&nbsp;

## Modify OpenWrt dnsmasq config
```sh
dhcp-match=set:bios,60,PXEClient:Arch:00000
dhcp-boot=tag:bios,iventoy_loader_16000,,192.168.x.x
```
> Modify IP your iVentoy IP, and Add line at /etc/dnsmasq.conf

> Then, reboot OpenWrt

&nbsp;

## Reference document
[Net Boot ISOs with iPXE boot using iVentoy!](https://youtu.be/2cajcKWlYyk)

[Proxmox VE Helper-Scripts iVentoy](https://community-scripts.github.io/ProxmoxVE/scripts?id=iventoy)

[Mount host directory into LXC container](https://forum.proxmox.com/threads/mount-host-directory-into-lxc-container.66555/)
