# Cybersecurity-Notes 
<p align="right">
  <img src="https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg" alt="pasindu-sd" />
</p>

    | My notes on Cybersecurity, Linux, Ethical Hacking, and Tools |
    
    🔐 Ethics Reminder/
          |- For educational purposes only 
          |- Never attack systems without explicit permission

# 🔐 Cybersecurity Notes by Pasindu

## 📅 Week 1 - Introduction to Cybersecurity

- What is Cybersecurity? ➤ The field focused on protecting systems, networks, and data.
- Cybersecurity has 3 major areas: Blue Team, Red Team, and GRC (Governance, Risk & Compliance).
- TryHackMe: Complete the "Introduction to Cybersecurity" Room.
- Install Kali Linux on VirtualBox and practice basic terminal commands:
  - `ls`, `cd`, `pwd`, `mkdir`

---

## 📅 Week 2 - Linux & Networking Basics

- Learn how to navigate the Linux command line.
- Important commands to practice:
  - `chmod`, `rm`, `nano`, `touch`
- Understand File Permissions:
  - Read (`r`), Write (`w`), Execute (`x`)
- Basic Networking Concepts:
  - IP address, MAC address, DNS, and Gateway
- TryHackMe: Complete "Linux Fundamentals Part 1"

---

## 📅 Week 3 - Nmap , Wiershark & Metasploit Framework

- Learned basic networking concepts: IP address, Ports, Protocols, and Subnets.
- Understood how Nmap is used for network scanning:
  - Performed host discovery and port scanning using `-sS`, `-sV`, `-A`, `-O`.
  - Explored Nmap scripting engine for vulnerability scanning.
- Used Wireshark to analyze HTTP traffic and packet-level data.
- TryHackMe Rooms:
  - Completed "Network Fundamentals"
  - Completed "Nmap"
- Introduced to the Metasploit Framework and its components.
- Learned how to search for exploits and configure payloads and listeners.
- Practiced using `msfconsole` for launching exploits.
- TryHackMe: Completed the "Metasploit" room.
- Set up a vulnerable environment using DVWA for hands-on practice.

---

## 📅 Week 4 - Python, Port Scanner & Password Cracker

- Python basics: variables, loops, functions.
- Basic Socket Programming.
- How to build a Port Scanner.
- Password Checker (Brute Force simulation).
- TryHackMe: Python for Pentesters module.

### Tools used:
- Python 3.12
- VS Code
- GitHub

---

## 📅 Week 5 – OWASP Top 10, SQL Injection, Burp Suite & Web App Security

- Studied the OWASP Top 10 vulnerabilities list.
- Practiced SQL Injection basics and manual testing.
- Learned and used Burp Suite for intercepting and testing HTTP requests.
- Understood XSS (Cross-Site Scripting) with examples.
- Completed OWASP Top 10 room on TryHackMe.
- Set up and practiced with DVWA (Damn Vulnerable Web Application).

---

## 📅 Week 6 -   Active Directory Hacking
- **AD Fundamentals**  
  Domain structure, DC roles, OUs, and GPOs
- **Credential Attacks**  
  Mimikatz for LSASS dumping & golden ticket attacks
- **Enumeration Tools**  
  BloodHound for path visualization and attack mapping
- **Privilege Escalation**  
  Kerberoasting and ACL-based attacks
- **Defense Evasion**  
  OPSEC considerations for red team operations

### Tools Used
- Mimikatz
- BloodHound
- Impacket

---

## 📅 Week 7 - Advanced Web Hacking (OWASP Top 10 Advanced)
- Focused on advanced web vulnerabilities: CSRF, SSRF, XXE.
- Used Burp Suite Intruder & Repeater for hands-on exploitation.
- Completed TryHackMe Web Security Room.
- Learned about bypassing filters, crafting payloads, and real-world attack scenarios.
- Gained practical experience with DVWA vulnerable endpoints.

### Tools Used
- Burp Suite Community Edition
- DVWA
- TryHackMe
- PortSwigger Web Security Academy

---

## 📅 Week 8 - NSE, Wireshark, MITM Attacks
- Nmap Scripting Engine (NSE) Usage
- Wireshark: Deep Traffic Analysis
- Man-in-the-Middle (MITM) Attacks on Networks
- TryHackMe "Network Security" Room Challenges
- Practical Exercise: Network Testing and Analysis

### Tools Used
- Nmap
- Wireshark

---

## 📅 Week 9 - SIEM, Windows and Linux Event Logs Analysis, Wazuh (OSSEC)
- SIEM architecture & fundamentals(Splunk & ELK Stack)
- Windows Event Logs Analysis
- Linux log analysis (/var/log/auth.log, /var/log/syslog) and useful grep/journalctl commands
- Wazuh (OSSEC) installation, agent/server testing, and alert verification

Expected Outcomes
 - Understand basic SIEM workflows and data flow.
 - Able to analyze Windows and Linux logs for common security events.
 - Successfully install and test Wazuh agents and verify alerts.

---

## 📅 Week 10 - Dark Web & OSINT
- Understand the fundamentals, risks, and use-cases of Tor and Onion services.
- Learn safe practices for using the Tor Browser.
- Learn OSINT methodology and how to gather and analyze publicly available information.
- Practice investigating Dark Web scenarios and mapping relationships using OSINT tools.

Tools Used
  - Tor Browser — Browsing .onion services through the Tor network.
  - Maltego — Link analysis and visualization for OSINT investigations.
  - TryHackMe – Dark Web Room — Practical labs and challenges.
  - Additional utilities: WHOIS/DNS tools, breach checkers (e.g., Have I Been Pwned), paste sites, metadata extractors.

---

## 📅 Week 11 - Types of Teams, MITRE ATT&CK, Cobalt Strike
- Understand Red Team vs Blue Team roles and the full attack lifecycle.
- Map attack steps to the MITRE ATT&CK framework.
- Learn basics of Cobalt Strike / Beacon concepts (listeners, staging, C2) — lab-only.
- Complete TryHackMe Red Team room for practical exercises.
- Run safe Atomic Red Team tests and collect telemetry to evaluate detection.
- Produce an attack timeline, detection findings, and mitigation recommendations.

---

## 📚 Weekly Notes
- [Week 1 - Introduction to Cybersecurity](week-01.md)
- [Week 2 - Linux & Networking Basics](week-02.md)
- [Week 3 - Ethical Hacking & Metasploit Framework](week-03.md)
- [Week 4 - Python, Port Scanner & Password Cracker](week-04.md)
- [Week 5 - Web Application Security](week-05.md)
- [Week 6 - Active Directory Hacking](week-06.md)
- [Week 7 - Advanced Web Hacking (OWASP Top 10 Advanced)](week-07.md)
- [Week 8 - NSE, Wireshark, MITM Attacks](week-08.md)
- [Week 9 - SIEM, Windows and Linux Event Logs Analysis, Wazuh (OSSEC)](week-09.md)
- [Week 10 - Dark Web & OSINT](week-10.md)

