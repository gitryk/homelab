# tailscale-LXC

## After LXC(Debian) Create

Modify **/etc/pve/lxc/(tailscale CT ID).conf**

```sh
lxc.cgroup2.devices.allow: c 10:200 rwm
lxc.mount.entry: /dev/net/tun dev/net/tun none bind,create=file
```
> Add This Code at Last

&nbsp;

## Init Setting
```sh
apt update && apt upgrade -y && apt install curl vim sudo
```
Next,

```
echo 'net.ipv4.ip_forward = 1' | sudo tee -a /etc/sysctl.d/99-tailscale.conf
echo 'net.ipv6.conf.all.forwarding = 1' | sudo tee -a /etc/sysctl.d/99-tailscale.conf
sudo sysctl -p /etc/sysctl.d/99-tailscale.conf
```

&nbsp;

## Install Tailscale
```sh
curl -fsSL https://tailscale.com/install.sh | sh
```

&nbsp;

## Tailscale Up
```sh
tailscale up --accept-routes --hostname=*** --auth-key=tskey-auth-*** --advertise-routes=192.168.*.*/24
```

&nbsp;

## Reference document
[Enable IP forwarding](https://tailscale.com/kb/1019/subnets?tab=linux#enable-ip-forwarding)

[Proxmox VE Helper-Scripts iVentoy](https://community-scripts.github.io/ProxmoxVE/scripts?id=iventoy)
