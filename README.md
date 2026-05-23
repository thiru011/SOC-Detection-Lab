# 🔐 SOC Detection Lab - Brute Force Attack Detection

![Splunk](https://img.shields.io/badge/Splunk-000000?style=flat&logo=splunk&logoColor=green)
![Kali Linux](https://img.shields.io/badge/Kali_Linux-557C94?style=flat&logo=kali-linux&logoColor=white)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE_ATT&CK-T1110-red)

A hands-on Security Operations Center (SOC) lab for detecting brute force attacks using Splunk SIEM on Kali Linux.

## 🎯 Project Overview

This project demonstrates:
- **SIEM Implementation**: Splunk Enterprise on Kali Linux
- **Attack Simulation**: Realistic brute force attacks using multiple tools
- **Detection Engineering**: SPL queries for threat detection
- **Alert Configuration**: Automated alerting for security incidents
- **MITRE ATT&CK Mapping**: Technique T1110 (Brute Force)

## 🏗️ Architecture
┌─────────────────────────────────────────┐
│ SOC Detection Lab │
├─────────────────────────────────────────┤
│ Kali Linux (Splunk + Attack Tools) │
│ ┌────────────────────────────────────┐ │
│ │ Splunk Enterprise │ │
│ │ ├── Log Ingestion (port 9997) │ │
│ │ ├── SPL Detection Queries │ │
│ │ ├── Alert Rules │ │
│ │ └── Dashboards │ │
│ └────────────────────────────────────┘ │
│ ▲ │
│ │ Auth Logs │
│ │ │
│ ┌────────────────────────────────────┐ │
│ │ Attack Simulation Tools │ │
│ │ ├── Hydra │ │
│ │ ├── Medusa │ │
│ │ └── Custom Python Scripts │ │
│ └────────────────────────────────────┘ │
├─────────────────────────────────────────┤
│ Target: Ubuntu VM (SSH Server) │
│ ┌────────────────────────────────────┐ │
│ │ Vulnerable Users & Services │ │
│ └────────────────────────────────────┘ │
└─────────────────────────────────────────┘
