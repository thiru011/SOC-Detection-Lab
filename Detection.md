# 🔍 Detection Queries

All SPL queries used in Splunk to detect the brute-force attack.

---

## Query 1 – Basic Failed Login Detection

Finds all failed SSH login attempts and counts them per attacker IP and username.

```spl
index=main sourcetype=linux_secure "Failed password"
| rex "Failed password for (?<user>\S+) from (?<src_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
| stats count by src_ip, user
| where count > 5
| sort - count
```

**What this detects:** Any IP address with more than 5 failed login attempts.
**Alert threshold:** Count > 5 is suspicious. Count > 50 confirms brute force.

---

## Query 2 – Brute Force in 1 Minute Window

Detects rapid repeated failures from the same IP within 1 minute.

```spl
index=main sourcetype=linux_secure "Failed password"
| rex "from (?<src_ip>\d+\.\d+\.\d+\.\d+)"
| bucket _time span=1m
| stats count by _time, src_ip
| where count > 10
| sort - count
```

**What this detects:** More than 10 failed logins from same IP in any single minute — classic brute force signature.

---

## Query 3 – Successful Login After Multiple Failures (Account Compromise)

The most dangerous pattern: attacker fails many times, then succeeds — meaning they guessed the password.

```spl
index=main sourcetype=linux_secure
| eval status=if(searchmatch("Failed password"), "Failed", "Success")
| rex "(?:Failed|Accepted) password for (?<user>\S+) from (?<src_ip>\S+)"
| stats values(status) as statuses, count by src_ip, user
| where count > 5 AND statuses="Success"
```

**What this detects:** IPs that failed multiple times but eventually logged in successfully.
**Why it matters:** This means the attacker got in — immediate incident response needed.

---

## Query 4 – Timeline View (Dashboard Graph)

Shows attack traffic over time as a graph — good for dashboards.

```spl
index=main sourcetype=linux_secure "Failed password"
| rex "from (?<src_ip>\d+\.\d+\.\d+\.\d+)"
| timechart count by src_ip
```

**Use this for:** Splunk dashboard to visualize the attack spike visually.

---

## MITRE ATT&CK Reference

| Query | Technique Detected |
|-------|--------------------|
| Query 1 | T1110 – Brute Force |
| Query 2 | T1110.001 – Password Guessing |
| Query 3 | T1110 + TA0001 – Initial Access |
| Query 4 | T1110 – Timeline visualization |
