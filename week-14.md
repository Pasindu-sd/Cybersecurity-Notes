# Week 14 - Threat Hunting Basic
Simple description:
The process of actively searching for threats that are already present but not identified in a network/system.

## Threat Hunting:
3 types of threat hunting:
  - Hypothesis-Driven Hunting
  - IOC-Based Hunting
  - Analytics-Driven Hunting

### Threat Hunting Process (Basic 5 Steps):
  - Step 1: Create a Hypothesis
      - "What kind of threat could be on our network?"

  - Step 2: Data Collection
      - Log files (Windows Event, Linux Syslog, Firewall, DNS)
      - Network traffic (PCAP files)
      - Endpoint data (EDR tools)

  - Step 3: Analysis
      - Using tools (SIEM, ELK Stack, Wireshark)
      - Pattern matching
      - Timeline analysis

  - Step 4: Investigation
      - Confirm suspicious activity
      - Determine scope
      - Impact assessment
    
  - Step 5: Response & Documentation
      - Notify incident response team
      - Write report
      - Lessons learned
