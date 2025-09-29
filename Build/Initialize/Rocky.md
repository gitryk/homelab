# Rocky Initailize
**Environment settings**

```shell
sudo dnf install podman cockpit vim -y
sudo systemctl enable podman
sudo systemctl enable --now cockpit.socket
mkdir -p ~/.config/containers/systemd/
mkdir -p ~/.config/systemd/user
loginctl enable-linger $UID

podman --version
```

&nbsp;

**Firewall Setting**

```shell
# Forward Rule Create
sudo firewall-cmd --add-forward-port=port=80:proto=tcp:toport=10080 --permanent
sudo firewall-cmd --add-forward-port=port=443:proto=tcp:toport=10443 --permanent
sudo firewall-cmd --zone=public --add-masquerade --permanent
sudo firewall-cmd --reload

# Checking Created Forward Rule 
sudo firewall-cmd --list-all
```

&nbsp;
