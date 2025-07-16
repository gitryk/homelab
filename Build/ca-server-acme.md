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

## Install Step-CA
```sh
sudo apt update && sudo apt install -y --no-install-recommends curl vim gpg ca-certificates
sudo curl -fsSL https://packages.smallstep.com/keys/apt/repo-signing-key.gpg -o /etc/apt/trusted.gpg.d/smallstep.asc && \
    echo 'deb [signed-by=/etc/apt/trusted.gpg.d/smallstep.asc] https://packages.smallstep.com/stable/debian debs main' \
    | sudo tee /etc/apt/sources.list.d/smallstep.list
sudo apt update && sudo apt install -y step-cli step-ca
```
&nbsp;

Can check the result by **step version**, **step-cli version**

```
tryk@step-ca-acme:~$ step version
Smallstep CLI/0.28.7 (linux/amd64)
Release Date: 2025-07-14T04:10:42Z

tryk@step-ca-acme:~$ step-cli version
Smallstep CLI/0.28.7 (linux/amd64)
Release Date: 2025-07-14T04:10:42Z
```


&nbsp;
&nbsp;
## Reference document
[Install Step-CA](https://smallstep.com/docs/step-ca/installation/#debianubuntu)

[Build a Tiny Certificate Authority For Your Homelab](https://smallstep.com/blog/build-a-tiny-ca-with-raspberry-pi-yubikey/)

[Building Your Own PKI with Step-CA](https://gyptazy.com/building-your-own-pki-with-step-ca-from-root-ca-to-proxmox-integration-with-acme/)
