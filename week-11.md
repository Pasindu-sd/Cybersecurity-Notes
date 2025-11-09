# 🛡️ Types of Teams, MITRE ATT&CK, Cobalt Strike
---

### Types of teams:
1. Red Team(Ethical Hacker, Pentester)
2. Blue Team(Security Analyst, Security Engineer)
3. Purple Team

## Red Team

### What is a red team?
   The National Institute of Standards and Technology (NIST) defines a red team as “a group of people authorized and organized to emulate a potential adversary’s attack or exploitation capabilities against an enterprise’s security posture [1].” The red team plays the part      of the attacker or competitor with the intention of identifying vulnerabilities in a system. 
### Skills:
   - Software development
   - Penetration testing
   - Social engineering
   - Threat intelligence and reverse engineering
   - Creativity

### Certifications:
   - Certified Ethical Hacker (CEH)
   - Licensed Penetration Tester (LPT) Master
   - CompTIA PenTest+
   - GIAC Penetration Tester (GPEN)
   - GIAC Exploit Researcher and Advanced Penetration Tester (GXPN)
   - OffSec Certified Professional (OSCP+ and OSCP) certification
   - Certified Red Team Operations Professional (CRTOP)

## Blue Team

### What is a blue team?
   NIST defines a blue team as “the group responsible for defending an enterprise’s use of information systems by maintaining its security posture against a group of mock attackers [6].” If the red team is playing offense, the blue team is playing defense to protect an        organization’s critical assets.
### Skills:
   - Risk assessment
   - Threat intelligence
   - Hardening techniques
   - Monitoring and detection systems

### Certifications:
   - Certified Information Systems Security Professional (CISSP)
   - Certified Information Systems Auditor (CISA)
   - CompTIA Security+
   - GIAC Security Essentials (GSEC)
   - GIAC Certified Incident Handler (GCIH)
   - Systems Security Certified Practitioner (SSCP)
   - CompTIA SecurityX

---

# MITRE ATT&CK
The MITRE ATT&CK framework (MITRE ATT&CK) is a universally accessible, continuously updated knowledge base for modeling, detecting, preventing, and fighting cybersecurity threats based on cybercriminals’ known adversarial behaviors.

- [MITRE ATT&CK Resoureces Web Page](https://attack.mitre.org/)

## MITRE ATT&CK matrices
   - [Enterprise Matrix](https://attack.mitre.org/matrices/enterprise/)
   - [Mobile Matrix](https://attack.mitre.org/matrices/mobile/)
   - [ICS Matrix](https://attack.mitre.org/matrices/ics/)

### Key components of the MITRE ATT&CK framework
   - Tactics:       represent the overarching goals or objectives of an adversary, such as execution, persistence, or lateral movement. Tactics describe why an attacker performs a certain action.
   - Techniques:    detail how an attacker achieves a specific tactic. For example, credential dumping is a technique used to access account credentials.
   - Procedures:    refer to the real-world implementations of techniques and sub-techniques as observed in actual cyber incidents. For example, these often include named malware families or custom scripts used by threat actors.

---

# Cobalt Strike Basic
Cobalt Strike is a powerful platform for conducting offensive cyber operations. It contains a wide variety of tools for conducting spear phishing and web drive-by attacks to gain initial access. Through the artefact kit, Cobalt Strike also has a flexible obfuscation framework. However, it is in the arena of post-exploitation that Cobalt Strike really shines. It has a custom implant, called Beacon, which can handle command and control (C2) communications via HTTP(S), DNS, and even SMB named pipes. Beacon has numerous options for lateral movement, e.g., WMI and psexec, as well as the ability to load PowerShell and .NET assemblies for additional modules such as Mimikatz.

### How Cobalt Strike Works: Key Features
   - Covert Communication
   - Attack Packages
   - Beacon Configuration
   - Post-Exploitation Modules
   - Command and Control (C2)
   - Custom Scripts

### Why Is a Cobalt Strike Attack So Dangerous?
Cobalt Strike attacks, when carried out by malicious attackers, are particularly dangerous due to their sophistication, stealth, and the tool’s extensive capabilities in carrying out cyber threats:

   - Sophisticated attack capabilities: The ability of Cobalt Strike to carry out the tactics, techniques, and procedures (TTPs) of advanced persistent threats (APTs) allows attackers to conduct highly targeted and complex operations. This level of sophistication makes it challenging for organizations to detect and respond to attacks before significant damage is done.
   - Stealthiness: Cobalt Strike uses covert communication channels, such as beaconing and data exfiltration over DNS or HTTP(S). These techniques enable attackers to maintain a low profile, avoiding detection by traditional security measures. The stealthy nature of these communications means that breaches can go unnoticed for extended periods, allowing attackers to escalate privileges and move laterally with little resistance.
   - Post-exploitation and C2: The tool’s post-exploitation modules and customizable command and control (C2) capabilities allows attackers to adapt their strategies to the specific environment they are targeting. This adaptability makes Cobalt Strike attacks highly effective, as they can bypass security defenses tailored to more generic threat profiles.

   The combination of sophistication, stealth, and adaptability makes Cobalt Strike a formidable tool in the hands of malicious actors, posing a significant threat to organizations worldwide.

---

# Red Team Simulation
Simulate realistic attacker actions in an isolated lab to test detection and response.

### Core phases
Reconnaissance – host/port scans, AD enumeration.
Initial Access – phishing, malicious payloads, stagers.
Privilege Escalation – enumerate misconfigs, escalate to Admin/SYSTEM.
Credential Access – dump creds/hashes (Mimikatz, LSASS).
Lateral Movement – PsExec/WMI/SMB, use harvested creds.
Persistence & Evasion – scheduled tasks, registry run keys, obfuscation.
Cleanup & Reporting – remove artifacts, revert snapshots, write timeline + detections.

Quick checklist

Lab isolated (host-only/internal)

VM snapshots taken before tests

Logging enabled (Sysmon/Windows Event/EDR)

Capture commands, timestamps, screenshots

Clean up and restore snapshots after tests

Top tools (lab-only)

Kali: msfvenom, msfconsole, nmap, crackmapexec, impacket

Windows: Mimikatz, winPEAS, PowerView, SharpHound

C2: Cobalt Strike (licensed) / Sliver / Metasploit

Logging: Sysmon, Wazuh/ELK
