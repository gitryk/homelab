# CA-Server-Root
## If Need Initalize
[Initailize Debian](https://github.com/gitryk/homelab/blob/main/Build/Initialize/Debian.md)

## Init Setting

```
apt-add-repository ppa:yubico/stable
apt update
apt install yubikey-manager yubico-piv-tool opensc libengine-pkcs11-openssl
```

&nbsp;

## Download Pre-Config File
```
wget https://raw.githubusercontent.com/gitryk/homelab/refs/heads/main/Build/acme/ca-inter.conf
wget https://raw.githubusercontent.com/gitryk/homelab/refs/heads/main/Build/acme/ca-root.conf
```

> Change information if your want

**From the next step, recommend that you proceed offline.**

&nbsp;

## Create Root CA Key

```
openssl req -x509 -new -newkey rsa:2048 -sha512 \
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

## If Need Reset yubikey

```
ykman piv reset
```

&nbsp;

## yubikey initialize

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


## Insert Private Key to Yubikey 5

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

Step Ended, Delete your key

&nbsp;

## Create Intermediate CA Key and Signing

```
openssl req -new -newkey rsa:2048 -sha512 \
  -keyout intermediate_ca_key -config ca-inter.conf -out intermediate.csr
```
|Enter PEM pass phrase: (pass phrase you want)<br>Verifying - Enter PEM pass phrase:(1 more)|
|:---|
> Create Intermediate CA Key

&nbsp;

```
openssl x509 -sha512 -engine pkcs11 -CAkeyform engine \
  -CAkey id_1 -CA root_ca.crt -CAcreateserial \
  -extfile ca-inter.conf -extensions inter_ca \
  -in intermediate.csr -out intermediate_ca.crt \
  -req -days 3650
```
> Sign CSR with Root CA Key inside Yubikey

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
