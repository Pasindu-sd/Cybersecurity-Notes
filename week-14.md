# 🛡️ Threat Hunting Basic, ELK Stack, Splunk Analysis, Threat Detection in SIEM

---


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

---


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
    - Failed login dashboard
    - Network traffic map
    - Process execution timeline
    - Threat hunting dashboards
    - SOC monitoring screens
  
  ### ELK Setup එකේ Basic Flow:
  ```
        Windows Logs / Linux Logs / Network Logs
              ↓
           Logstash
              ↓
        Elasticsearch
              ↓
            Kibana
  ```

---


## Splunk 
Splunk is a data analytics and monitoring platform that collects, indexes, analyzes, and visualizes machine-generated data (logs, events, metrics) in real time.
  - [https://www.splunk.com/en_us/download.html](https://www.splunk.com/en_us/download.html)

  ### Key Components:
  - Index
    - → A storage location for data (like a database in Splunk).
  - Source
    - → The origin of the data (e.g., a log file, network stream).
  - Sourcetype
    - → Defines the format of the data (e.g., apache:access, win:eventlog).
  - Search Processing Language (SPL)
    - → Splunk’s query language for searching and analyzing data.

  ### Main Uses:
  - IT Operations Monitoring (server logs, application errors)
  - Security Information & Event Management (SIEM) (threat detection, compliance)
  - Business Analytics (user behavior, sales data)
  - IoT & Application Performance Monitoring

  ### Why Use Splunk?
  - Real-time insights from unstructured data
  - Powerful dashboards and visualizations
  - Scalable for big data environments
  - Supports logs from any source (OS, apps, cloud, devices)

---

## Threat Detection in SIEM
SIEM = Security Information & Event Management
  - A security solution that collects, analyzes, and correlates security data from multiple sources to detect threats.
  ### How SIEM Detects Threats
  - **1. Three Detection Methods:**
    - Signature-Based – Matches known attack patterns
    - Anomaly-Based – Detects deviations from normal behavior
    - Behavioral Analytics – Monitors user/entity behavior over time
  
  - **2. Data Sources:**
    - Firewall logs
    - Server/application logs
    - Endpoint security data
    - Network traffic
    - Cloud activity logs

  ### Common Threats Detected:
  - Malware & ransomware activity
  - Brute force attacks (multiple failed logins)
  - Data exfiltration (unusual large data transfers)
  - Lateral movement (attacker moving inside network)
  - Privilege escalation
  - Phishing & social engineering attempts
  - DDoS attacks

  ### Benefits of SIEM Threat Detection:
  - Real-time monitoring – Detects threats within seconds
  - Centralized visibility – Single pane of glass for all security data
  - Compliance support – Meets PCI DSS, HIPAA, GDPR requirements
  - Forensic analysis – Helps investigate past incidents
  - Automated response – Can trigger automatic blocking actions

  ### Key Takeaway:
  SIEM transforms raw security logs into actionable threat intelligence, enabling organizations to detect, investigate, and respond to cyber threats faster and more effectively.
