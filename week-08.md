# 🛡️ Week 08 - NSE, Wireshark, MITM Attacks

## Overview:
This week focuses on Advanced Nmap Features (NSE), Deep Traffic Analysis with Wireshark, and Basic MITM Attacks

---

## Learning Objectives:
- Nmap Scripting Engine (NSE) Usage
- Wireshark: Deep Traffic Analysis
- Man-in-the-Middle (MITM) Attacks on Networks
- TryHackMe "Network Security" Room Challenges
- Practical Exercise: Network Testing and Analysis

---

## Nmap Script Engine

### Basic NSE Usage
```
# Default scripts
nmap -sC target.com

# Specific script categories
nmap --script vuln 192.168.1.1
nmap --script safe 10.0.0.1
nmap --script discovery target.com

# Multiple script categories
nmap --script "vuln and safe" target.com
```

### Advanced NSE
```
# Update NSE scripts
nmap --script-updatedb

# Run specific script
nmap --script http-title target.com
nmap --script ssl-enum-ciphers target.com

# Debug scripts
nmap --script-trace target.com
```

---

## Wireshark 

### Core Features
- Packet Analyzer: Capture and inspect network traffic in real-time
- Protocol Support: HTTP, DNS, TCP, UDP, and 1000+ protocols
- Live Capture: Monitor active network interfaces
- Filter System: Isolate specific traffic patterns

### Essential Filters
```
  http                              # HTTP traffic
  dns                               # DNS queries
  ip.addr == 192.168.1.1            # Specific IP
  tcp.port == 80                    # Port filtering
  http.request                      # HTTP requests only
  http.host contains "google.com"   # Specific domain
```

### Practical Applications
- Website Traffic Analysis: Monitor HTTP/HTTPS requests
- DNS Monitoring: Track domain resolution
- Network Troubleshooting: Identify connectivity issues
- Security Analysis: Detect suspicious traffic patterns

---

## Man-In-The-Middle (MITM)

### Common MITM Techniques
- **ARP spoofing / ARP poisoning** — corrupting local IP→MAC mappings so traffic is routed via the attacker.  
- **DNS spoofing / DNS cache poisoning** — returning malicious IPs for legitimate hostnames.  
- **Rogue Wi-Fi / Evil Twin access points** — attacker runs a fake network to capture traffic.  
- **TLS/SSL downgrade & stripping** — forcing unencrypted connections or intercepting weakly protected channels.  
- **Man-in-the-Browser / proxying** — malware or an intercepting proxy modifies traffic inside the client.
- [MITM Diagram](week-08/MITM/Diagram.md)
### Realistic Impacts
- Credential theft (logins, cookies, tokens).  
- Data exposure (plain HTTP, misconfigured TLS).  
- Transaction manipulation (financial fraud) and session hijacking. :contentReference[oaicite:3]{index=3}

### Detection Signs (what to look for)
- Browser TLS/Certificate warnings (unexpected certificate changes).  
- Duplicate IP / conflicting MAC addresses in the LAN (`arp -a` or `ip neigh show`).  
- Unexpected redirects or DNS replies that return suspicious IPs.

---

## Key Achievements:

- **Automated Scanning:** Mastered the Nmap Scripting Engine (NSE) to automate vulnerability detection and information gathering.
- **Protocol Deep Dive:** Developed the ability to perform deep packet inspection using Wireshark to detect anomalies and malicious traffic patterns.
- **Attack Simulation:** Understood and simulated Man-in-the-Middle (MITM) attacks (e.g., ARP spoofing) to grasp network interception techniques.
- **Self-Assessment:** Conducted a practical exercise to test the security posture of a private network.

---
