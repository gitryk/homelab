# Debian Initailize
**In root(su root)...**

```shell
apt update && apt upgrade -y
apt install -y sudo curl vim gpg

export USER_NAME=tryk #Modify USER_NAME!
useradd -s /bin/bash -m $USER_NAME
usermod -aG sudo $USER_NAME
passwd $USER_NAME
```

&nbsp;

**Disable IPv6(for VM, Not LXC)**

```
sudo vi /etc/sysctl.d/99-sysctl.conf
```

```
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1
```

```
sudo sysctl -p
sudo systemctl restart procps
```

&nbsp;

**Static IP Setting(for VM, Not LXC)**

```
sudo vi /etc/network/interfaces
```

```
iface enpXsX inet static
address 192.168.81.100
netmask 255.255.255.0
gateway 192.168.81.1
dns-nameservers 192.168.81.1
```

```
sudo systemctl restart networking
```

&nbsp;

**If Need**
```shell
timedatectl set-timezone Asia/Seoul
```

&nbsp;

```
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
