# Proxmox Initailize
**Disk Area Integration**

```shell
lvremove /dev/pve/data
lvresize -l +100%FREE /dev/pve/root
resize2fs -p /dev/pve/root
```
> Datacenter > Storage > "local-lvm" Delete > Add role "local" Storage

&nbsp;

**Post Install Script**

```shell
bash -c "$(curl -fsSL https://raw.githubusercontent.com/community-scripts/ProxmoxVE/main/tools/pve/post-pve-install.sh)"
```
