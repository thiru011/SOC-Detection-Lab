# 🛠️ Installation Guide

## Prerequisites
- VirtualBox installed
- Kali Linux VM running
- Ubuntu Server VM running
- Both VMs on Host-Only network

---

## Step 1 – Install Splunk on Kali Linux

```bash
# Download Splunk
wget -O splunk.deb 'https://download.splunk.com/products/splunk/releases/9.2.0/linux/splunk-9.2.0-amd64.deb'

# Install
sudo dpkg -i splunk.deb

# Start Splunk
sudo /opt/splunk/bin/splunk start --accept-license
```

Access Splunk at: `http://localhost:8000`

---

## Step 2 – Install Splunk Forwarder on Ubuntu

```bash
# Download forwarder
wget -O splunkforwarder.deb 'https://download.splunk.com/products/universalforwarder/releases/9.2.0/linux/splunkforwarder-9.2.0-amd64.deb'

# Install
sudo dpkg -i splunkforwarder.deb

# Start
sudo /opt/splunkforwarder/bin/splunk start --accept-license

# Send logs to Splunk (replace with your Kali IP)
sudo /opt/splunkforwarder/bin/splunk add forward-server <KALI_IP>:9997

# Monitor auth logs
sudo /opt/splunkforwarder/bin/splunk add monitor /var/log/auth.log
```

---

## Step 3 – Run Brute Force Attack

```bash
# On Kali Linux
hydra -l testuser -P /usr/share/wordlists/rockyou.txt <UBUNTU_IP> ssh -t 4 -V
```

---

## Step 4 – Detect in Splunk

```spl
index=main sourcetype=linux_secure "Failed password"
| rex "from (?<src_ip>\d+\.\d+\.\d+\.\d+)"
| stats count by src_ip
| where count > 10
```
