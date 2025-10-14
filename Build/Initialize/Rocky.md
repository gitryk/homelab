# Rocky Initailize

**Variable declaration**

```shell
DOMAIN="domain.com"
GIT_URL="https://raw.githubusercontent.com/gitryk/homelab/refs/heads/main"
```

&nbsp;

**Environment settings**

```shell
sudo dnf update -y
sudo dnf install wget podman cockpit vim -y
sudo systemctl enable podman
sudo systemctl enable --now cockpit.socket
mkdir -p ~/.config/containers/systemd/
mkdir -p ~/.config/systemd/user
mkdir -p traefik/{config,logs}
mkdir -p devops/code-server/{config,local,workspace}
mkdir -p devops/gitea/{git,gitea}
mkdir -p devops/postgres
mkdir kms
touch traefik/config/acme.json
touch traefik/logs/access.log
touch traefik/logs/traefik.log
loginctl enable-linger $UID

podman --version
```

&nbsp;

**Firewall Setting**

```shell
# Forward Rule Create
sudo firewall-cmd --add-forward-port=port=80:proto=tcp:toport=10080 --permanent
sudo firewall-cmd --add-forward-port=port=443:proto=tcp:toport=10443 --permanent
sudo firewall-cmd --add-forward-port=port=443:proto=udp:toport=10443 --permanent
sudo firewall-cmd --zone=public --add-masquerade --permanent
sudo firewall-cmd --reload

# Checking Created Forward Rule 
sudo firewall-cmd --list-all
```

&nbsp;


**Install Cert**

```shell
wget --no-check-certificate https://ca.$DOMAIN/roots.pem
mv roots.pem traefik/root_ca.crt
sudo cp traefik/root_ca.crt /etc/pki/ca-trust/source/anchors/
sudo update-ca-trust extract
```

&nbsp;
