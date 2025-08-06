# CA-Server-Root
## If Need Initalize
[Initailize Debian](https://github.com/gitryk/homelab/blob/main/Build/Initialize/Debian.md)

## TEST

```
apt-add-repository ppa:yubico/stable
apt update
apt install yubikey-manager opensc libengine-pkcs11-openssl
```

ykman piv reset

```
ykman piv access change-management-key -a AES256 -g
Enter the current management key [blank to use default key]: (Press Enter)
Generated management key: ***************************************
```

```
ykman piv access change-pin --pin 123456
Enter the new PIN:
Repeat for confirmation:
New PIN set.
```

```
ykman piv access change-puk --puk 12345678
Enter the new PUK:
Repeat for confirmation:
New PUK set.
```

```
ykman piv keys generate -a ECCP384 9a root.pem
ykman piv certificates generate -s 'C=KR,ST=Incheon,L=Incheon,O=TryK-Lab,OU=TryK-Lab Certification,CN=TryK-Lab Root CA' -d 7305 -a SHA512 9a root.pem
ykman piv certificates export 9a root-signed.pem
openssl x509 -in root-signed.pem -text -noout
```

```
pkcs11-tool --module "/usr/lib/x86_64-linux-gnu/pkcs11/opensc-pkcs11.so" --list-objects --login
```

```
openssl req -new -key test.key -out test.csr -sha512
openssl x509 -engine pkcs11 -CAkeyform engine -CAkey id_1 -sha512 -CA root-signed.pem -CAcreateserial -req -days 3650 -extfile ca.conf -extensions inter_ca -in test.csr -out inter-signed.pem
openssl x509 -in inter-signed.pem -text -noout
```

&nbsp;
&nbsp;
## Reference document
[yubikey-ca](https://github.com/samngms/yubikey-ca)
