# CA-Server-ACME
## If Need Initalize
[Initailize Debian](https://github.com/gitryk/homelab/blob/main/Build/Initialize/Debian.md)

If you can't Login LXC Container, connect to console, and **adduser**

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

## Step CA initialize
```sh
step ca init
```
> Enter any information, which does not apply because it is the task of creating the structure of the data.

&nbsp;

```
rm -rf /root/.step/certs/* /root/.step/secrets/*
mv intermediate_ca.crt /root/.step/certs/intermediate_ca.crt
mv intermediate_ca_key /root/.step/secrets/intermediate_ca_key
mv root_ca.crt /root/.step/certs/root_ca.crt
mv password /root/.step/config/password
```
> Delete the temporarily created structure and move the file.

&nbsp;

```
step certificate install /root/.step/certs/root_ca.crt
step certificate fingerprint /root/.step/certs/root_ca.crt
```
> install Root CA Cert

&nbsp;

```
step ca provisioner add acme --type ACME
```
> Set Provisioner

&nbsp;

```
vi /root/.step/config/ca.json
```

```
...
        "authority": {
                "claims": {
                        "disableRenewal": false,
                        "allowRenewalAfterExpiry": false,
                        "maxTLSCertDuration": "360h",
                        "defaultTLSCertDuration": "168h"
                },
                "provisioners": [
...
```

> Sample ca.json part
> Max 15d, default 7d

&nbsp;

```
vi /etc/systemd/system/step-ca.service
```
> create systemctl service

&nbsp;

```
[Unit]
Description=Step Certificates
Documentation=https://smallstep.com/docs/step-ca/
After=network.target

[Service]
ExecStart=/usr/bin/step-ca /root/.step/config/ca.json --password-file /root/.step/config/password
WorkingDirectory=/root/.step
User=root
Group=root
LimitNOFILE=65536
Restart=on-failure
RestartSec=5s

[Install]
WantedBy=multi-user.target
```

```
systemctl enable step-ca
systemctl start step-ca
```
> Service Create And Execute

# ACME For Proxmox

**Variable declaration**

```shell
DOMAIN="domain.com"
```

&nbsp;

**Install Root CA**

```
wget --no-check-certificate https://ca.$DOMAIN/roots.pem
mv roots.pem /usr/local/share/ca-certificates/root_ca.crt
update-ca-certificates
```
> install Root CA Cert

&nbsp;

Create ACME default Account, Address is **https://ca.$domain/acme/acme/directory**, Type is **standalone**

&nbsp;

# ACME For TrueNAS

**Token Create at CA-Server**

```shell
DOMAIN="domain.com"
step ca token nas --san nas.domain.com --not-after 1h
```

&nbsp;

**Setup to TrueNAS(Need Allow SSH for Root)**

```shell
DOMAIN="domain.com"
wget https://dl.smallstep.com/cli/docs-ca-install/latest/step_linux_amd64.tar.gz
tar -xf step_linux_amd64.tar.gz
mv step_linux_amd64/bin/step /root
chown root:root step
rm -rf step_*
mkdir /root/cert
wget --no-check-certificate https://ca.$DOMAIN/roots.pem
wget https://raw.githubusercontent.com/danb35/deploy-freenas/refs/heads/master/deploy_truenas.py
chmod 700 deploy_truenas.py
```
> Basic Environment Setup

&nbsp;

**Issue Cert for NAS**

```shell
TOKEN="(Paste Before Step Token)"
/root/step ca certificate --token $TOKEN --not-after 168h nas /root/cert/nas.crt /root/cert/nas.key
```
> 

&nbsp;

**Create Script Setting**

```shell
vi deploy_config
```
```
[deploy]
api_key = (Create API Key at TrueNAS WebUI, Set User "Root")

privkey_path = /root/cert/nas.key
fullchain_path = /root/cert/nas.crt

delete_old_certs = true

verify_ssl = false
```

&nbsp;

**Run Python Script**

```
python3 /root/deploy_truenas.py
```

&nbsp;

**Add Cron(Recommanded before the expiration interval)**
```
/root/step ca renew --ca-url https://ca.(your domain)/acme/acme/directory --force --root /root/roots.pem /root/cert/nas.crt /root/cert/nas.key && /usr/bin/python3 /root/deploy_truenas.py
```

&nbsp;

# ACME For OpenWRT(not Working mbedtls)

**Variable declaration**

```shell
DOMAIN="domain.com"
ACME_VER="3.1.1"
ACME_EMAIL="yourmail@domain.com"
WRT_IP="192.168.1.1"
```

**Suppose work in home directory**

```
wget --no-check-certificate https://ca.$DOMAIN/roots.pem
mv roots.pem /etc/ssl/certs/root_ca.crt
HASH="$(openssl x509 -hash -noout -in /etc/ssl/certs/root_ca.crt).0" 
echo "$HASH"
ln -s "/etc/ssl/certs/root_ca.crt" "/etc/ssl/certs/$HASH"
```
> install Root CA Cert

&nbsp;

[acmesh-official/acme.sh](https://github.com/acmesh-official/acme.sh) you can download latest acme.sh

```
opkg update
opkg install unzip
wget https://github.com/acmesh-official/acme.sh/archive/refs/tags/$ACME_VER.zip
unzip $ACME_VER.zip
mv /usr/lib/acme /usr/lib/acme.origin
mv acme.sh-$ACME_VER /usr/lib/acme.install
mkdir -p /etc/ssl/acme
mkdir -p /etc/acme/config
/usr/lib/acme.install/acme.sh --install --home /usr/lib/acme --cert-home /etc/ssl/acme --config-home /etc/acme/config \
    --accountkey /etc/acme/account --useragent "" --log /var/log/acme.log \
    --accountemail $ACME_EMAIL
rm -rf $ACME_VER.zip /usr/lib/acme.install
```
> Change Email Address

&nbsp;

```
/usr/lib/acme/acme.sh --issue --webroot /var/run/acme/challenge/ --cert-home /etc/ssl/acme \
    --server https://ca.$DOMAIN/acme/acme/directory \
    -d router.$DOMAIN -d $WRT_IP
```
> Your cert is in: /root/.acme.sh/router.domain.com_ecc/router.domain.com.cer
> 
> Your cert key is in: **/root/.acme.sh/router.domain.com_ecc/router.domain.com.key**
> 
> The intermediate CA cert is in: /root/.acme.sh/router.domain.com_ecc/ca.cer
> 
> And the full-chain cert is in: **/root/.acme.sh/router.domain.com_ecc/fullchain.cer**

&nbsp;

```
vi /etc/config/uhttpd
```
> change option cert(full-chain cert absolute path), option key(key absolute path)

After restart uhttpd

&nbsp;

```
/usr/lib/acme/acme.sh --cron --home "/usr/lib/acme" --accountconf "/etc/acme/config/account.conf" --config-home "/etc/acme/config" --cert-home "/etc/ssl/acme"
/usr/lib/acme/acme.sh --cron
```
> Register Cron

&nbsp;

```
/usr/lib/acme/acme.sh --list
```
> Check your acme list if you want

&nbsp;

## Reference document
[Install Step-CA](https://smallstep.com/docs/step-ca/installation/#debianubuntu)

[Build a Tiny Certificate Authority For Your Homelab](https://smallstep.com/blog/build-a-tiny-ca-with-raspberry-pi-yubikey/)

[Building Your Own PKI with Step-CA](https://gyptazy.com/building-your-own-pki-with-step-ca-from-root-ca-to-proxmox-integration-with-acme/)

[LetsEncrypt with ACME on OpenWRT](https://wiki.terrabase.info/wiki/LetsEncrypt_with_ACME_on_OpenWRT)

[Trouble with Certificates: Automating my SSH CA and the many many exceptions required](https://i.am.eddmil.es/posts/ssh-certificates/)
