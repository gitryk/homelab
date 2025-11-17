# Proxmox Initailize
**Disk Area Integration**

```shell
lvremove /dev/pve/data
lvresize -l +100%FREE /dev/pve/root
resize2fs -p /dev/pve/root
```
> Datacenter > Storage > "local-lvm" Delete > Add role "local" Storage

&nbsp;
