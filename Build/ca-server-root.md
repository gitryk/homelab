# CA-Server
## If Need Initalize
[Initailize Debian](https://github.com/gitryk/homelab/blob/main/Build/Initialize/Debian.md)

## Install Yubikey-Manager
```sh
sudo apt update
sudo apt install -y yubikey-manager
```

&nbsp;

Can check the result by **ykman info**

```
tryk@step-ca-root:~$ ykman info
Device type: YubiKey 5 Nano
Serial number: ********
Firmware version: 5.7.4
Form factor: Nano (USB-A)
Enabled USB interfaces: OTP, FIDO, CCID

Applications
...
PIV             Enabled
```

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
tryk@step-ca-root:~$ step version
Smallstep CLI/0.28.7 (linux/amd64)
Release Date: 2025-07-14T04:10:42Z

tryk@step-ca-root:~$ step-cli version
Smallstep CLI/0.28.7 (linux/amd64)
Release Date: 2025-07-14T04:10:42Z
```

## Formatting Backup USB Drive
Checking External USB Path
```
sudo fdisk -l
```
&nbsp;

**Result:**
```
tryk@step-ca-root:~$ sudo fdisk -l
...
Disk /dev/sdb: 14.65 GiB, 15728640000 bytes, 30720000 sectors
Disk model: ProductCode
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x0c546f5b
```
> It can vary depending on the environment. I used a 16GB USB memory stick.

&nbsp;

My USB Stick is **/dev/sdb**, so
```
tryk@step-ca-root:~$ sudo fdisk /dev/sdb
Command (m for help): d
Partition number (1-3, default 3): 3

...

Command (m for help): d
Selected partition 1
Partition 1 has been deleted.
```
> If there were existing partitions, they will be deleted.

&nbsp;

```
Command (m for help): n
Partition type
   p   primary (0 primary, 0 extended, 4 free)
   e   extended (container for logical partitions)
Select (default p): p
Partition number (1-4, default 1): 1
First sector (2048-30719999, default 2048):
Last sector, +/-sectors or +/-size{K,M,G,T,P} (2048-30719999, default 30719999):
...
Command (m for help): w
The partition table has been altered.
```

&nbsp;

**ext4 formating..**

```
tryk@step-ca-root:~$ sudo mkfs.ext4 /dev/sdb1 -v
...
Allocating group tables: done
Writing inode tables: done
Creating journal (16384 blocks): done
Writing superblocks and filesystem accounting information: done
```
&nbsp;

## Create Root CA
**Mounting USB**
```sh
sudo mount /dev/sda1 /mnt
sudo mkdir /mnt/ca
sudo chown tryk:tryk -R /mnt/ca
export STEPPATH=/mnt/ca
cd /mnt/ca
```
&nbsp;

**init Step-CA**
```sh
step ca init \
  --pki \
  --name="TryK-HomeLab Root CA" \
  --dns="192.168.*.*" \
  --dns="tryk.lab" \
  --deployment-type="standalone"
```
&nbsp;

**Result:**
```
Choose a password for your CA keys.
✔ [leave empty and we'll generate one]:

Generating root certificate... done!
Generating intermediate certificate... done!

✔ Root certificate: /mnt/ca/certs/root_ca.crt
✔ Root private key: /mnt/ca/secrets/root_ca_key
✔ Root fingerprint: *****************************
✔ Intermediate certificate: /mnt/ca/certs/intermediate_ca.crt
✔ Intermediate private key: /mnt/ca/secrets/intermediate_ca_key
```
&nbsp;

**If you want, available Check CA**
```sh
step certificate inspect /mnt/ca/certs/root_ca.crt
step certificate inspect /mnt/ca/certs/intermediate_ca.crt
```
&nbsp;

**Result:**
```
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: *** (***)
    Signature Algorithm: ECDSA-SHA256
        Issuer: O=TryK-HomeLab Root CA,CN=TryK-HomeLab Root CA Root CA
        Validity
            Not Before: Jul 16 05:10:55 2025 UTC
            Not After : Jul 14 05:10:55 2035 UTC
```
&nbsp;

**Save CA to Yubikey**
```
sudo systemctl enable pcscd
sudo systemctl start pcscd

ykman piv certificates import 9a /mnt/ca/certs/root_ca.crt
Enter a management key [blank to use default key]:

ykman piv keys import 9a /mnt/ca/secrets/root_ca_key
Enter password to decrypt key:
Enter a management key [blank to use default key]:
```
&nbsp;

**Register Root CA to Root-CA Server**
```sh
sudo cp /mnt/ca/certs/root_ca.crt /usr/local/share/ca-certificates/tryklab_root_ca.crt
sudo update-ca-certificates
```
&nbsp;

Then, Download /mnt/ca/certs/root_ca.crt,

Create a copy /mnt/ca/secrets/intermediate_ca_key, /mnt/ca/certs/intermediate_ca.crt to ACME Step-CA Server

And Root-CA Server Go to Offline

&nbsp;
&nbsp;
## Reference document
[Install Step-CA](https://smallstep.com/docs/step-ca/installation/#debianubuntu)

[Build a Tiny Certificate Authority For Your Homelab](https://smallstep.com/blog/build-a-tiny-ca-with-raspberry-pi-yubikey/)

[Building Your Own PKI with Step-CA](https://gyptazy.com/building-your-own-pki-with-step-ca-from-root-ca-to-proxmox-integration-with-acme/)
