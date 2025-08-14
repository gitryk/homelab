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

```
step-ca
```

# ACME For Proxmox
```
wget --no-check-certificate https://acme.lab.tryk.app:443/roots.pem
mv roots.pem /usr/local/share/ca-certificates/root_ca.crt
update-ca-certificates
```
> install Root CA Cert

&nbsp;

Create ACME default Account, Address is **https://acme.domain.com/acme/acme/directory** Set, Type is **standalone** Set

# ACME For OpenWRT

**Suppose work in home directory**

```
wget --no-check-certificate https://acme.lab.tryk.app:443/roots.pem
mv roots.pem /etc/ssl/certs/root_ca.crt
HASH="$(openssl x509 -hash -noout -in /etc/ssl/certs/root_ca.crt).0" 
echo "$HASH"
ln -s "/etc/ssl/certs/root_ca.crt" "/etc/ssl/certs/$HASH"
```
> install Root CA Cert

&nbsp;

```
opkg update
opkg install acme acme-dnsapi luci-app-acme unzip
```
> It's OK to install from Luci

> I don't think luci-app-acme is necessary..?

&nbsp;

[acmesh-official/acme.sh](https://github.com/acmesh-official/acme.sh) you can download latest acme.sh

```
wget https://github.com/acmesh-official/acme.sh/archive/refs/tags/3.1.1.zip
unzip 3.1.1.zip
mv /usr/lib/acme /usr/lib/acme.origin
mv acme.sh-3.1.1 /usr/lib/acme.install
mkdir -p /etc/ssl/acme
mkdir -p /etc/acme/config
./acme.sh --install --home /usr/lib/acme --cert-home /etc/ssl/acme --config-home /etc/acme/config \
    --accountkey /etc/acme/account --useragent "" --log /var/log/acme.log \
    --accountemail YourEmail@YourProvider.com
```
> Change Email Address

&nbsp;

```
/usr/lib/acme/acme.sh --issue -d router.domain.com --webroot /var/run/acme/challenge/ --server https://acme.domain.com/acme/acme/directory
```
> Your cert is in: /root/.acme.sh/router.domain.com_ecc/router.lab.tryk.app.cer
> 
> Your cert key is in: **/root/.acme.sh/router.domain.com_ecc/router.lab.tryk.app.key**
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
/usr/lib/acme/acme.sh --cron --home "/usr/lib/acme" --accountconf "/etc/acme/config/account.conf" --config-home "/etc/acme/config" --cert-home "/etc/acme/config/certs"
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
