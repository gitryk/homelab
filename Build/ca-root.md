# CA-Server-Root
## If Need Initalize
[Initailize Debian](https://github.com/gitryk/homelab/blob/main/Build/Initialize/Debian.md)

## Init Setting

```
apt-add-repository ppa:yubico/stable
apt update
apt install yubikey-manager opensc libengine-pkcs11-openssl
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
openssl req -x509 -new -newkey ed25519 -sha512 \
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

```
yubico-piv-tool -a import-key -s 9a -i root_ca.key
yubico-piv-tool -a import-certificate -s 9a -i root_ca.crt
rm -rf root_ca.key
```

&nbsp;

## Create Intermediate CA Key and Signing

```
openssl req -new -newkey ed25519 -sha512 \
  -keyout intermediate_key -config ca-inter.conf -out intermediate.csr
```
|Enter PEM pass phrase: (pass phrase you want)<br>Verifying - Enter PEM pass phrase:(1 more)|
|:---|
> Create Intermediate CA Key

&nbsp;

```
openssl x509 -sha512 -engine pkcs11 -CAkeyform engine \
  -CAkey id_1 -CA root_ca.crt -CAcreateserial \
  -extfile ca-inter.conf -in intermediate.csr -out intermediate_ca.crt \
  -req -days 3650
```
> Sign CSR with Root CA Key inside Yubikey

&nbsp;

```
openssl x509 -in intermediate_ca.crt -text -noout
```
> Check Intermediate CA if you want

&nbsp;

Copy 3 File(**intermediate_ca.crt, intermediate_key, root_ca.crt**) to ca-server

&nbsp;
## Reference document
[yubikey-ca](https://github.com/samngms/yubikey-ca)
