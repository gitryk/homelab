# PXE-iVentoy-LXC

## LXC Build
```sh
sudo mkdir /ca
sudo cp * /ca
cd /ca
sudo cp root_ca.crt /usr/local/share/ca-certificates/tryklab_root_ca.crt
sudo update-ca-certificates
```
> Assume that you have the downloaded Root CA and the copied Intermediate CA file.

&nbsp;

## Mount Proxmox ISO Folder
```sh
pct set [LXC ID] -mp0 /var/lib/vz/template/iso,mp=/opt/iventoy/iso
```
&nbsp;
