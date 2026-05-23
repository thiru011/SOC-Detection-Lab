# 🛠️ Installation & Setup Guide

Complete step-by-step setup for the SOC Detection Lab.

---

## Prerequisites

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| RAM | 8 GB | 16 GB |
| Storage | 50 GB free | 100 GB free |
| OS | Windows/Mac/Linux | Any |
| VirtualBox | 7.0+ | 7.0+ |

---

## Step 1 – Install Splunk on Kali Linux

```bash
# Download Splunk Enterprise
wget -O splunk.deb 'https://download.splunk.com/products/splunk/releases/9.2.0/linux/splunk-9.2.0-amd64.deb'

# Install
sudo dpkg -i splunk.deb

# Start Splunk and accept license
sudo /opt/splunk/bin/splunk start --accept-license

# Set admin username and password when prompted
# Username: admin
# Password: choose a strong password
```

Open Splunk in browser: `http://localhost:8000`

---

## Step 2 – Configure Splunk to Receive Logs

1. Login to Splunk at `http://localhost:8000`
2. Go to **Settings** → **Forwarding and Receiving**
3. Click **Configure Receiving** → **New Receiving Port**
4. Enter port: `9997`
5. Click **Save**

---

## Step 3 – Install Splunk Forwarder on Ubuntu VM

```bash
# Download Universal Forwarder
wget -O splunkforwarder.deb 'https://download.splunk.com/products/universalforwarder/releases/9.2.0/linux/splunkforwarder-9.2.0-amd64.deb'

# Install
sudo dpkg -i splunkforwarder.deb

# Start forwarder
sudo /opt/splunkforwarder/bin/splunk start --accept-license

# Point forwarder to Splunk (replace KALI_IP with your Kali VM IP)
sudo /opt/splunkforwarder/bin/splunk add forward-server KALI_IP:9997 -auth admin:yourpassword

# Tell forwarder to collect SSH auth logs
sudo /opt/splunkforwarder/bin/splunk add monitor /var/log/auth.log -auth admin:yourpassword

# Restart forwarder to apply changes
sudo /opt/splunkforwarder/bin/splunk restart
```

---

## Step 4 – Set Up Target User on Ubuntu

```bash
# Create a user with a weak password (intentionally vulnerable)
sudo adduser testuser
# When asked for password, enter: password123
```

---

## Step 5 – Run Brute Force Attack from Kali

```bash
# Unzip the rockyou wordlist (if not already done)
sudo gunzip /usr/share/wordlists/rockyou.txt.gz

# Launch Hydra brute-force attack
# Replace UBUNTU_IP with your Ubuntu VM IP
hydra -l testuser -P /usr/share/wordlists/rockyou.txt UBUNTU_IP ssh -t 4 -V
```

---

## Step 6 – Detect in Splunk

1. Open Splunk: `http://localhost:8000`
2. Go to **Search & Reporting**
3. Run the queries from [Detection.md](Detection.md)

---

## Networking Setup (VirtualBox)

## 🌐 Configure Networking Between Virtual Machines

### Step 1 – Create a Host Network
In VirtualBox:

```text
File → Host Network Manager → Create
```

This creates your own private virtual network for communication between VMs.

---

### Step 2 – Configure NAT Network for Internet Access
For each VM:

```text
Settings → Network
```

#### Adapter 1
- ✔ Enable Network Adapter
- Attached to: `NAT Network`
- Name: Your custom NAT Network

This provides internet connectivity to the VMs.

---

### Step 3 – (Optional) Add Host-Only Adapter
To allow direct communication between VMs and the host machine:

#### Adapter 2
- ✔ Enable Network Adapter
- Attached to: `Host-Only Adapter`
- Name: `vboxnet0`

---

### Step 4 – Start Both Virtual Machines
Boot both:
- Kali Linux VM
- Ubuntu VM

---

### Step 5 – Verify IP Addresses
Run the following command on each VM:

```bash
ip a
```

Look for IP addresses such as:

```text
Kali Linux   → 192.168.100.10
Ubuntu VM    → 192.168.100.30
```

These IP addresses will be used for:
- SSH brute-force testing
- Splunk log forwarding
- Network communication between systems

---

### Step 6 – Test Connectivity
From Kali Linux, test communication with Ubuntu:

```bash
ping 192.168.100.30
```

Successful replies confirm both VMs can communicate over the virtual network.
