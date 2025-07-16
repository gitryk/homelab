# CA-Server-ACME
## If Need Initalize
[Initailize Debian](https://github.com/gitryk/homelab/blob/main/Build/Initialize/Debian.md)

If you can't Login LXC Container, connect to console, and **adduser**

&nbsp;

## Register Root-CA
```sh
sudo cp root_ca.crt /usr/local/share/ca-certificates/tryklab_root_ca.crt
sudo update-ca-certificates
```


&nbsp;
&nbsp;
## Reference document
[Install Step-CA](https://smallstep.com/docs/step-ca/installation/#debianubuntu)

[Build a Tiny Certificate Authority For Your Homelab](https://smallstep.com/blog/build-a-tiny-ca-with-raspberry-pi-yubikey/)

[Building Your Own PKI with Step-CA](https://gyptazy.com/building-your-own-pki-with-step-ca-from-root-ca-to-proxmox-integration-with-acme/)
