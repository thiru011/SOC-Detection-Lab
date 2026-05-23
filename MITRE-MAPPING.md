# MITRE ATT&CK Mapping

## Attack Technique Identified

| Field          | Details                              |
|----------------|--------------------------------------|
| Tactic         | TA0006 – Credential Access           |
| Technique      | T1110 – Brute Force                  |
| Sub-technique  | T1110.001 – Password Guessing        |
| Tool Used      | Hydra  |
| Target Service | SSH (port 22)                        |
| Log Source     | /var/log/auth.log                    |

## Detection Coverage

| Detection Method     | SPL Query | Alert |
|----------------------|-----------|-------|
| Failed login count   | ✅        | ✅    |
| Account compromise   | ✅        | ✅    |
| IP-based rate limit  | ✅        | ❌    |

## References
- https://attack.mitre.org/techniques/T1110/
- https://attack.mitre.org/tactics/TA0006/
