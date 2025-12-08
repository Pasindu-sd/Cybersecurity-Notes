# Week 14 - Threat Hunting Basic, ELK Stack
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

## ELK Stack
- ELK:
    - E → Elasticsearch
    - L → Logstash
    - K → Kibana

  When these three come together, it is a powerful log management + analytics platform that can be used to collect, process, search, analyze, and visualize logs.
  ELK is a main toolset for Threat Hunting, Monitoring, SIEM setup, Security Onion, Wazuh, SOC operations.

  ### 1. Elasticsearch – (Search + Store Engine)
  Elasticsearch is:
    - A high-speed search engine
    - A database that stores logs
    - An index-based system that handles big data
    - Real-time search & analytics support
    
  Two basic concepts:
    Index = Log collections (like a DB table)
    Document = Individual log entry (like a Row)
    
  You use Elasticsearch to find logs by entering a search query.
    
  For example:
    - “Show failed logins”
    - “Search PowerShell events”
    - “Find suspicious IPs”

  ### 2. Logstash – (Log Collector + Processor)
  Logstash is:
    - A tool to collect logs
    - A tool to filter, clean, parse, normalize logs
    - A tool to convert logs to formats (JSON, CSV, Sysmon, Winlogs)
    - A tool to push logs to ElasticSearch

  The Logstash pipeline has 3 steps:

  **1. Input**
    - Logs received from:
    - Windows Event Logs
    - Sysmon
    - Wazuh
    - Network logs
    - Firewall logs
  
  **2. Filter**
  - Log parsing:
  - extract fields
  - grok patterns
  - remove noise
  - add tags

  **3. Output**
    - Logs to Elasticsearch

  ### 3. Kibana – (Dashboard + Visualization)
  Kibana means:
    - Visual dashboard builder
    - Threat Hunting visualizer
    - Query analyzer
    - Real-time log viewer
    - Tool to create charts, maps, graphs, timelines

Using Kibana:

Failed login dashboard

Network traffic map

Process execution timeline

Threat hunting dashboards

SOC monitoring screens
