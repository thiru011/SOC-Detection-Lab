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

Both VMs must be on the same Host-Only network:

1. VirtualBox → **File** → **Host Network Manager** → **Create** (Your's Own Network)
2. For each VM → **Settings** → **Network** → **Create A NAT Network of your own** → **NAT Network** → **Your's Network**
3. Start both VMs and run `ip a` to get their IPs
