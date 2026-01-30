# CA-Server-Root
## If Need Initalize
[Initailize Debian](https://github.com/gitryk/homelab/blob/main/Build/Initialize/Debian.md)

&nbsp;

## If use Proxmox LXC
```
lsusb
```
|Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub<br>Bus 001 Device 002: ID 1050:0407 Yubico.com Yubikey 4/5 OTP+U2F+CCID<br>Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub|
|:---|
> ADD > Device Passthrough > "/dev/bus/usb/001/002"
> 
> Modify it to suit your environment. 

&nbsp;

## Yubikey Install Dependencies
```
apt-add-repository ppa:yubico/stable
apt update
apt install yubikey-manager yubico-piv-tool opensc libengine-pkcs11-openssl
```
> if not have yubikey, skip this step

&nbsp;

## Download Pre-Config File

**Variable declaration**

```shell
GIT_URL="https://raw.githubusercontent.com/gitryk/homelab/refs/heads/main"
```
&nbsp;

```
wget $GIT_URL/Build/acme/ca-inter.conf
wget $GIT_URL/Build/acme/ca-root.conf
```

> modify conf if your want

**Before next step, recommend that you proceed offline.**

&nbsp;

## Yubikey initialize

```
ykman piv reset
```
> If Need Reset yubikey

&nbsp;

```
ykman piv access change-management-key -a AES256 -g
```
|Enter the current management key [blank to use default key]: (Press Enter)<br> Generated management key: ***************************************|
|:---|

> Setting up management key

&nbsp;

```
ykman piv access change-pin --pin 123456
```
|Enter the new PIN: (pin you want)<br>Repeat for confirmation: (1 more)<br>New PIN set.|
|:---|

> Setting up PIN

&nbsp;

```
ykman piv access change-puk --puk 12345678
```
|Enter the new PUK: (puk you want)<br>Repeat for confirmation: (1 more)<br>New PUK set.|
|:---|

> Setting up PUK

&nbsp;

## Create Root CA Key

```
openssl req -x509 -new -newkey ec -pkeyopt ec_paramgen_curve:prime256v1 -sha256 \
  -config ca-root.conf -keyout root_ca.key -out root_ca.crt \
  -days 7300
```
|Enter PEM pass phrase: (pass phrase you want)<br>Verifying - Enter PEM pass phrase:(1 more)|
|:---|

> Create Self Signed Root CA

&nbsp;

```
openssl x509 -in root_ca.crt -text -noout
```
> Check Root CA if you want

&nbsp;

## Insert Root CA to Yubikey 5

Import your key:

```
ykman piv keys import 9a root_ca.key
```
|Enter password to decrypt key: (decrypt key)<br>Enter a management key [blank to use default key]: (Generated key at before step)|
|:---|

&nbsp;

Import your cert:

```
ykman piv certificates import 9a root_ca.crt
```
|Enter a management key [blank to use default key]: (Generated key at before step)|
|:---|

&nbsp;

Check your yubikey slot:

```
yubico-piv-tool -a status -s 9a
```

```
Version:        5.7.4
Serial Number:  ****
CHUID:  ***************************************
CCC:    No data available
Slot 9a:
        Algorithm:      RSA2048
        Subject DN:     C=KR, ST=Incheon, L=Bupyeong-gu, O=TryK-Lab, CN=TryK-Lab Root CA, OU=TryK-Lab Certification
        Issuer DN:      C=KR, ST=Incheon, L=Bupyeong-gu, O=TryK-Lab, CN=TryK-Lab Root CA, OU=TryK-Lab Certification
        Fingerprint:    *********************************
        Not Before:     Aug 11 02:23:01 2025 GMT
        Not After:      Aug  6 02:23:01 2045 GMT
```

```
rm -rf root_ca.key
```

Step Ended, Delete your key (Only Yubikey you have)

&nbsp;

## Create Intermediate CA Key and Signing

```
openssl req -new -newkey ec -pkeyopt ec_paramgen_curve:prime256v1 -sha256 \
  -keyout intermediate_ca_key -config ca-inter.conf -out intermediate.csr
```
|Enter PEM pass phrase: (pass phrase you want)<br>Verifying - Enter PEM pass phrase:(1 more)|
|:---|
> Create Intermediate CA Key

&nbsp;

```
openssl x509 -sha256 -engine pkcs11 -CAkeyform engine \
  -CAkey id_1 -CA root_ca.crt -CAcreateserial \
  -extfile ca-inter.conf -in intermediate.csr -out intermediate_ca.crt \
  -req -days 3650
```
> Sign CSR with Root CA Key inside Yubikey

&nbsp;

```
openssl x509 -sha256 -CAkey root_ca.key -CA root_ca.crt \
  -extfile ca-inter.conf -in intermediate.csr -out intermediate_ca.crt \
  -req -days 3650
```
> if don't have Yubikey


&nbsp;

```
openssl x509 -in intermediate_ca.crt -text -noout
```
> Check Intermediate CA if you want

&nbsp;

Copy 3 File(**intermediate_ca.crt, intermediate_ca_key, root_ca.crt**) to ca-server

&nbsp;
## Reference document
[yubikey-ca](https://github.com/samngms/yubikey-ca)
