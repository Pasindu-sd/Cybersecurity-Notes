# 🛡️ Week 08 - NSE, Wireshark, MITM Attacks

## 📚 Overview:
This week focuses on Advanced Nmap Features (NSE), Deep Traffic Analysis with Wireshark, and Basic MITM Attacks

---

## 🎯 Learning Objectives:
- Nmap Scripting Engine (NSE) Usage
- Wireshark: Deep Traffic Analysis
- Man-in-the-Middle (MITM) Attacks on Networks
- TryHackMe "Network Security" Room Challenges
- Practical Exercise: Network Testing and Analysis

---

## Nmap Script Engine

---

## Wireshark 

### Core Features
- Packet Analyzer: Capture and inspect network traffic in real-time
- Protocol Support: HTTP, DNS, TCP, UDP, and 1000+ protocols
- Live Capture: Monitor active network interfaces
- Filter System: Isolate specific traffic patterns

### Essential Filters
  http                    # HTTP traffic
  dns                     # DNS queries
  ip.addr == 192.168.1.1  # Specific IP
  tcp.port == 80          # Port filtering
  http.request            # HTTP requests only
  http.host contains "google.com"  # Specific domain
  
---

## 📌 Key Achievements:

- **Automated Scanning:** Mastered the Nmap Scripting Engine (NSE) to automate vulnerability detection and information gathering.
- **Protocol Deep Dive:** Developed the ability to perform deep packet inspection using Wireshark to detect anomalies and malicious traffic patterns.
- **Attack Simulation:** Understood and simulated Man-in-the-Middle (MITM) attacks (e.g., ARP spoofing) to grasp network interception techniques.
- **Self-Assessment:** Conducted a practical exercise to test the security posture of a private network.

---
