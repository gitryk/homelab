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

## If Need Reset yubikey

```
ykman piv reset
```

&nbsp;

## yubikey initialize

```
ykman piv access change-management-key -a AES256 -g
```
```
Enter the current management key [blank to use default key]: (Press Enter)
Generated management key: ***************************************
```

> Setting up management key

&nbsp;

```
ykman piv access change-pin --pin 123456
```
```
Enter the new PIN:
Repeat for confirmation:
New PIN set.
```

> Setting up PIN

&nbsp;

```
ykman piv access change-puk --puk 12345678
```
```
Enter the new PUK:
Repeat for confirmation:
New PUK set.
```

> Setting up PUK

&nbsp;

## Create Root CA Key

```
ykman piv keys generate -a ECCP384 9a root.pem
ykman piv certificates generate -s 'C=KR,ST=Incheon,L=Incheon,O=TryK-Lab,OU=TryK-Lab Certification,CN=TryK-Lab Root CA' -d 7305 -a SHA512 9a root.pem
ykman piv certificates export 9a root-signed.pem
openssl x509 -in root-signed.pem -text -noout
```
> root.pem : public key

> slot 9a : private key ()

> root-signed.pem : self-signed certificate


&nbsp;

## Verify Certificate

```
pkcs11-tool --module "/usr/lib/x86_64-linux-gnu/pkcs11/opensc-pkcs11.so" --list-objects --login
```

&nbsp;


## Create ca.conf

```
cat <<EOF > root_ca.conf
[req]
x509_extensions=root_ca
distinguished_name=req_distinguished_name
prompt=no

[req_distinguished_name]
C=KR
ST=Incheon
L=Bupyeong-gu
O=TryK-Lab
CN=TryK-Lab Root CA
OU=TryK-Lab Certification

[root_ca]
subjectKeyIdentifier=hash
basicConstraints=critical,CA:true,pathlen:1
keyUsage=critical,keyCertSign,cRLSign
nameConstraints=critical,@name_constraints

[name_constraints]
permitted;DNS.0=lab.tryk.app
EOF
```

&nbsp;

## Create inter ca key and signing

```
openssl req -new -key test.key -out test.csr -sha512
openssl x509 -engine pkcs11 -CAkeyform engine -CAkey id_1 -sha512 -CA root-signed.pem -CAcreateserial -req -days 3650 -extfile ca.conf -extensions inter_ca -in test.csr -out inter-signed.pem
openssl x509 -in inter-signed.pem -text -noout
```

&nbsp;
&nbsp;
## Reference document
[yubikey-ca](https://github.com/samngms/yubikey-ca)
