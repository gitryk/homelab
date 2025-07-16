# Debian Initailize
**In root(su root)...**

```shell
apt update && apt upgrade -y
apt install -y sudo curl vim gpg

export USER_NAME=tryk #Modify USER_NAME!
echo "$USER_NAME ALL=(ALL) NOPASSWD:ALL" | tee /etc/sudoers.d/$USER_NAME > /dev/null
chmod 440 /etc/sudoers.d/$USER_NAME
```
&nbsp;

**If Need**
```shell
timedatectl set-timezone Asia/Seoul
```
