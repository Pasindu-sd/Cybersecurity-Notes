# 🛡️ SIEM Learning Path, Windows Event Logs Analysis, Linux Logs Analysis, Wazuh (OSSEC)

## Overview:
This week focuses on Basic SIEM(Security Information and Event Management) 

---

## Learning Objectives:
- Foundational Concepts
- Splunk Core Skills
- ELK Stack Core Skills
- Practical Implementation (Analyze real-world scenarios)
- Threat intelligence integration

---

### Core SIEM Concepts
- SIEM architecture & fundamentals
- Log management & correlation rules
- Security use cases & threat detection

---

### Splunk Skills
- SPL (Search Processing Language)
- Data onboarding & field extraction
- Enterprise Security (ES) app
- Correlation searches & dashboards
    - [Resources File](week%209/Splunk%20Sample%20img)

### ELK Stack Skills
- Elasticsearch, Logstash, Kibana setup
- Beats for data collection
- KQL (Kibana Query Language)
- Elastic Security detections
    - [Resources File](week%209/ELK%20Stack%20img)

---

### Windows Event Logs Analysis
Critical Event IDs to Monitor:
- 4624 - Successful logon
- 4625 - Failed logon
- 4648 - Logon with explicit credentials
- 4720 - User account created
- 4732 - Member added to security group
- 7045 - New service installed
- 4688 - New process created

Security Use Cases:
- Brute force attack detection
- Account lockout analysis
- Privilege escalation monitoring

---

### Linux Logs Analysis(Syslog, Auth.log) 
Critical Log Files & Analysis:
- ```/var/log/auth.log``` - Authentication & SSH events
- ```/var/log/syslog``` - System-wide events
- ```/var/log/secure``` - Security-related events (RHEL/CentOS)

Key Security Monitoring:
- SSH brute force attacks detection
- Failed login attempts analysis
- sudo command monitoring

Essential Linux Commands:
```
grep "Failed password" /var/log/auth.log                # SSH failure analysis

grep "Accepted" /var/log/auth.log                       # Successful logins

grep "sudo" /var/log/auth.log                           # sudo privilege escalation
```
---

### Wazuh (OSSEC)
 - Install Wazuh agent and server
 - Test log collection and alerts
 - Use Wazuh dashboard for monitoring and analysis

---
*Cybersecurity SIEM Specialization - Hands-on approach for SOC roles*
