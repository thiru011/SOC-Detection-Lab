# 🎯 MITRE ATT&CK Mapping

Detailed mapping of the attack simulated in this lab to the MITRE ATT&CK framework.

---

## Attack Overview

| Field | Details |
|-------|---------|
| Tactic | TA0006 – Credential Access |
| Technique | T1110 – Brute Force |
| Sub-technique | T1110.001 – Password Guessing |
| Tool Used | Hydra |
| Target Protocol | SSH (port 22) |
| Target OS | Ubuntu Linux |
| Log Source | /var/log/auth.log |
| Reference | https://attack.mitre.org/techniques/T1110 |

---

## What T1110 Means (Plain English)

> The attacker tries many different passwords for a known username until one works.
> Like trying every key on a keyring to open one lock.

In this lab:
- Username targeted: `testuser`
- Wordlist used: `rockyou.txt` (14 million passwords)
- Tool: Hydra (tries ~4 passwords per second)
- Result: Password `password123` found

---

## Attack Kill Chain

```
1. RECONNAISSANCE   → Attacker knows SSH is open on port 22
2. WEAPONIZATION    → Hydra loaded with rockyou.txt wordlist
3. DELIVERY         → Hydra sends login attempts to Ubuntu SSH
4. EXPLOITATION     → Weak password found: password123
5. INSTALLATION     → Attacker gains SSH shell access
6. DETECTION        → Splunk alert fires after 10+ failures/minute
```

---

## Detection Coverage

| Detection Method | SPL Query | Alert Rule |
|-----------------|-----------|------------|
| Failed login count | ✅ Query 1 | ✅ Configured |
| Brute force rate | ✅ Query 2 | ✅ Configured |
| Account compromise | ✅ Query 3 | ✅ Configured |
| Timeline visualization | ✅ Query 4 | ❌ Dashboard only |

---

## Recommended Mitigations

| Mitigation | How to Implement |
|-----------|-----------------|
| Account lockout | Lock account after 5 failed attempts |
| Strong password policy | Minimum 12 characters, mixed case + symbols |
| Multi-Factor Authentication | Require MFA for SSH access |
| Fail2ban | Auto-block IPs after repeated failures |
| SSH key authentication | Disable password login entirely |
| Port change | Move SSH from port 22 to a non-standard port |

---

## References

- MITRE ATT&CK T1110: https://attack.mitre.org/techniques/T1110/
- MITRE ATT&CK T1110.001: https://attack.mitre.org/techniques/T1110/001/
- MITRE Tactic TA0006: https://attack.mitre.org/tactics/TA0006/
