# PXE-iVentoy-LXC

## LXC Build

Run "**Proxmox VE Shell**"

```sh
bash -c "$(curl -fsSL https://raw.githubusercontent.com/community-scripts/ProxmoxVE/main/ct/iventoy.sh)"
```
> It need priviliged Install

&nbsp;

## Mount Proxmox ISO Folder
```sh
pct set [LXC ID] -mp0 /var/lib/vz/template/iso,mp=/opt/iventoy/iso
```
&nbsp;

## iVentoy Setting
DHCP Server Mode : External

EFI Boot File : snp.efi

&nbsp;

## Modify OpenWrt dnsmasq config
```sh
dhcp-match=set:bios,option:client-arch,0      # x86 BIOS
dhcp-match=set:efi,option:client-arch,7       # x64 UEFI
dhcp-match=set:efi,option:client-arch,9       # x64 UEFI (Alternative)

dhcp-boot=tag:bios,iventoy_loader_16000,,192.168.xx.x
dhcp-boot=tag:efi,iventoy_loader_16000_uefi,,192.168.xx.x
```
> Modify IP your iVentoy IP, and Add line at /etc/dnsmasq.conf

> Then, restart dnsmasq

&nbsp;

## Reference document
[Net Boot ISOs with iPXE boot using iVentoy!](https://youtu.be/2cajcKWlYyk)

[Proxmox VE Helper-Scripts iVentoy](https://community-scripts.github.io/ProxmoxVE/scripts?id=iventoy)

[Mount host directory into LXC container](https://forum.proxmox.com/threads/mount-host-directory-into-lxc-container.66555/)
