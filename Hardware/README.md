# Overview
![Rack_Architecture](https://raw.githubusercontent.com/gitryk/homelab/main/Images/Hardware/Rack.png)
&nbsp;

## Aluminum Profile Rack
|Component|Item|Remark|
|---|---|---|
|Frame|2020 Aluminum Profile||
|Outline Plate|Tinted Polycarbonate 4.5T|Smog Black|
|Door Plate|Tinted Polycarbonate 3T|Smog Black|
|Rack Rail|RackPath 16U Vertical Server Rack Rail|[Link](https://www.amazon.com/RackPath-Vertical-Server-Build-Screws/dp/B09FJQDYL1)|

&nbsp;

## 6Bay HDD Enclosure

<img src="https://raw.githubusercontent.com/gitryk/homelab/main/Images/Hardware/HDD-01.jpg" width="50%" height="50%">

<img src="https://raw.githubusercontent.com/gitryk/homelab/main/Images/Hardware/HDD-02.jpg" width="50%" height="50%">

<img src="https://raw.githubusercontent.com/gitryk/homelab/main/Images/Hardware/HDD-03.jpg" width="50%" height="50%">

|Component|Item|Remark|
|---|---|---|
|Case|3D Print Model by Seller|120x185x236|
|Backplane|nas-03-6p|Seller-made PCB|
|Cable|4x SATA to SFF-8644|2EA|
|Fan|Thermalright TL-C12C|120mm Fan|
|PSU|12V 10A Adapter|5525|
|ACC|DC to DC StepDown Module|-|

buy on Xianyu

&nbsp;

[Check out the additional work...](https://github.com/gitryk/homelab/tree/main/Hardware/HDD)

&nbsp;

## HJS-480-0-24

<img src="https://raw.githubusercontent.com/gitryk/homelab/main/Images/Hardware/smps.png" width="40%" height="40%">

|Category|Spec|Remark|
|---|---|---|
|Input Voltage|AC110/220V|-|
|Output Voltage|DC0-24V 20A|Adjustable|
|Rated power|480W|-|
|Size|215x115x50|-|

It Used with Lenovo Slimtip 135w Cable that length-adjusted

buy on Aliexpress 2 Unit

&nbsp;

## Lenovo P360Tiny

<img src="https://raw.githubusercontent.com/gitryk/homelab/main/Images/Hardware/p360tiny.jpg" width="40%" height="40%">

|Component|Item|
|---|---|
|CPU|Intel i5-13600 ES3(Q1BQ)|
|RAM|DDR5-4800 32GB So-Dimm|
|OS|Proxmox VE 9.1|
|SSD/OS|Samsung PM961 NVMe 120GB * 2|
|SSD/Data|SK Hynix PC711 SATA 512GB|

**Proxmox VE Server**

&nbsp;

## Lenovo M75q Gen 2

<img src="https://raw.githubusercontent.com/gitryk/homelab/main/Images/Hardware/m70q.png" width="40%" height="40%">

|Component|Item|
|---|---|
|CPU|AMD R3-5300GE ES|
|RAM|DDR4-3200 16GB So-Dimm|
|OS|Talos Linux 1.12|
|SSD/OS|Samsung PM961 NVMe 120GB|

**Kubernates Control-Plane**

&nbsp;

[Check out the additional work...](https://github.com/gitryk/homelab/tree/main/Hardware/Tiny)

&nbsp;

## Lenovo Tiny M720q (Worker)

<img src="https://raw.githubusercontent.com/gitryk/homelab/main/Images/Hardware/m720q.jpg" width="50%" height="50%">

|Component|Item|
|---|---|
|CPU|Intel i7-8700 ES(QN8H)|
|RAM|DDR4-3200 16GB So-Dimm|
|OS|Talos Linux v1.12|
|SSD/OS|Samsung PM961 NVMe 120GB|
|SSD/Data|Intel DC S3500 SATA 480GB|

**Kubernetes Cluster For Worker-Node(For Prod)** / Running on 3 units.

&nbsp;

## Lenovo Tiny M720q (NAS)

```Same Picture Previous Section```

|Component|Item|
|---|---|
|CPU|Intel i7-8700T ES(QN8J)|
|RAM|DDR4-3200 32GB So-Dimm|
|OS|TrueNAS Scale 25.10.1|
|HBA|LSI SAS 9300-8e + Custom Cooler|
|SSD/OS|SK Hynix BC501A NVMe 120GB|
|SSD/Cache|Intel Optane Memory M10 64GB |

**NAS** / For NFS, iSCSI, S3 Compatible

&nbsp;

## KP-9000-9XHML-X

<img src="https://raw.githubusercontent.com/gitryk/homelab/main/Images/Hardware/25switch.jpg" width="50%" height="50%">

**keepLink 9-Port 2.5G Switch**

|Category|Spec|Remark|
|---|---|---|
|Uplink Port|1 Port SFP+|-|
|Switching Capacity|60Gbps|-|

buy on Aliexpress

&nbsp;
