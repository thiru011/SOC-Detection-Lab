# 🔐 SOC Detection Lab – Brute Force Attack Detection

![Splunk](https://img.shields.io/badge/Splunk-000000?style=flat&logo=splunk&logoColor=green)
![Kali Linux](https://img.shields.io/badge/Kali_Linux-557C94?style=flat&logo=kali-linux&logoColor=white)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE_ATT%26CK-T1110-red)
![License](https://img.shields.io/badge/License-MIT-blue)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

> A hands-on Security Operations Center (SOC) lab for simulating and detecting SSH brute-force attacks using Splunk SIEM.

---

## 📋 Table of Contents
- [Project Overview](#-project-overview)
- [Architecture](#️-architecture)
- [Tools Used](#️-tools-used)
- [Installation](Installation.md)
- [Detection Queries](Detection.md)
- [MITRE ATT&CK Mapping](#-mitre-attck-mapping)
- [Key Results](#-key-results)
- [Screenshots](#-screenshots)
- [Disclaimer](#️-disclaimer)

---

## 🎯 Project Overview

This project demonstrates:

- **SIEM Implementation** – Splunk Enterprise on Kali Linux
- **Attack Simulation** – SSH brute-force attack using Hydra
- **Detection Engineering** – SPL queries for threat detection
- **Alert Configuration** – Automated alerting for security incidents
- **MITRE ATT&CK Mapping** – Technique T1110 (Brute Force)

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────┐
│           SOC Detection Lab             │
├─────────────────────────────────────────┤
│   Kali Linux (Splunk + Attack Tools)    │
│  ┌────────────────────────────────────┐ │
│  │        Splunk Enterprise           │ │
│  │  ├── Log Ingestion (port 9997)     │ │
│  │  ├── SPL Detection Queries         │ │
│  │  ├── Alert Rules                   │ │
│  │  └── Dashboards                    │ │
│  └────────────────────────────────────┘ │
│                   ▲                     │
│                   │ Auth Logs           │
│                   │                     │
│  ┌────────────────────────────────────┐ │
│  │     Attack Simulation Tools        │ │
│  │  └── Hydra (SSH Brute Force)       │ │
│  └────────────────────────────────────┘ │
├─────────────────────────────────────────┤
│     Target: Ubuntu VM (SSH Server)      │
│  ┌────────────────────────────────────┐ │
│  │    Vulnerable Users & Services     │ │
│  │  ├── SSH (port 22)                 │ │
│  │  ├── Weak Credentials              │ │
│  │  └── Auth Log Forwarding           │ │
│  └────────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

---

## 🛠️ Tools Used

| Tool | Version | Purpose |
|------|---------|---------|
| Splunk Enterprise | 9.2.0 | SIEM – Log collection & detection |
| Kali Linux | 2024.1 | Attacker machine |
| Hydra | 9.4 | Brute-force attack simulation |
| Ubuntu Server | 22.04 LTS | Target victim machine |
| VirtualBox | 7.0 | Virtualization platform |

---

## 🎯 MITRE ATT&CK Mapping

| Field | Details |
|-------|---------|
| Tactic | TA0006 – Credential Access |
| Technique | T1110 – Brute Force |
| Sub-technique | T1110.001 – Password Guessing |
| Reference | https://attack.mitre.org/techniques/T1110 |

---

## 📊 Key Results

| Metric | Value |
|--------|-------|
| Attack tool | Hydra |
| Login attempts generated | 500+ in 60 seconds |
| Detection threshold | 10 failed attempts / minute |
| Alert triggered | Within 5 minutes |
| Log source | /var/log/auth.log |
| Technique detected | T1110 – Brute Force |

---

## 📸 Screenshots

> Add your Splunk dashboard and attack screenshots here after completing the lab.

---

## ⚙️ Quick Start

See [Installation.md](Installation.md) for full setup guide.

```bash
# 1. Install Splunk on Kali
sudo dpkg -i splunk-9.2.0-amd64.deb
sudo /opt/splunk/bin/splunk start --accept-license

# 2. Run brute force attack
hydra -l testuser -P /usr/share/wordlists/rockyou.txt <TARGET_IP> ssh -t 4

# 3. Detect in Splunk (SPL)
index=main "Failed password" | stats count by src_ip | where count > 10
```

---

## ⚠️ Disclaimer

> This project is for **educational purposes only**.  
> All attacks were performed in an **isolated lab environment**.  
> Never use these techniques on systems you do not own.

---

## 👤 Author

**Thiru** – [GitHub](https://github.com/thiru011)
