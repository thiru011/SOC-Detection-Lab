# 🔐 SOC Detection Lab – Brute Force Attack Detection

![Splunk](https://img.shields.io/badge/Splunk-000000?style=flat&logo=splunk&logoColor=green)
![Kali Linux](https://img.shields.io/badge/Kali_Linux-557C94?style=flat&logo=kali-linux&logoColor=white)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE_ATT%26CK-T1110-red)
![License](https://img.shields.io/badge/License-MIT-blue)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

> A hands-on Security Operations Center (SOC) lab for simulating and detecting SSH brute-force attacks using Splunk SIEM on Kali Linux.

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

- **SIEM Implementation** – Splunk Enterprise deployed on Kali Linux to collect and analyze authentication logs
- **Attack Simulation** – SSH brute-force attack simulated using Hydra against an Ubuntu target VM
- **Detection Engineering** – SPL (Splunk Processing Language) queries written to detect suspicious login patterns
- **Alert Configuration** – Automated alert rules configured to trigger on brute-force activity
- **MITRE ATT&CK Mapping** – Attack mapped to Technique T1110 (Brute Force)

---

## 🏗️ Architecture

