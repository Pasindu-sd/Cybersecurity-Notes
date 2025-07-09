# 🛡️ Week 07 - Advanced Web Hacking (OWASP Top 10 Advanced)

## 📚 Overview:
This week focused on mastering advanced Web Application attacks, diving deeper into high-risk vulnerabilities listed in the OWASP Top 10. Using tools like Burp Suite, I practiced hands-on exploitation and security testing techniques to identify and mitigate threats such as CSRF, SSRF, and XXE. Additionally, I reinforced my learning through real-world lab environments including DVWA and TryHackMe's Web Security room.

---

## 🎯 Learning Objectives:
- Gain in-depth knowledge of advanced OWASP Top 10 vulnerabilities and their impact on web security.
- Learn how to craft and use custom payloads to exploit vulnerabilities.
- Perform complex request manipulations using Burp Suite's Intruder and Repeater.
- Understand the attack vectors and consequences of:
  - **CSRF (Cross-Site Request Forgery):** Forcing authenticated users to perform unwanted actions.
  - **SSRF (Server-Side Request Forgery):** Exploiting server requests to internal or restricted resources.
  - **XXE (XML External Entity Injection):** Abusing XML parsers to read files or perform internal network scans.
- Complete practical labs to solidify theoretical knowledge.

---

## 🛠️ Tools Used:
- **Burp Suite Community Edition:** Intercepting proxy, Intruder, and Repeater modules for intercepting and manipulating HTTP(S) requests.
- **DVWA (Damn Vulnerable Web Application):** Vulnerable web app used for testing CSRF, SSRF, and XXE attacks in a controlled environment.
- **TryHackMe:** Web Security room to practice exploitation techniques in realistic scenarios.
- **PortSwigger Web Security Academy:** Official educational platform to understand and test OWASP vulnerabilities.

---

## 📝 Activities:
- **CSRF Attacks:**
  - Intercepted HTTP requests and identified CSRF tokens.
  - Crafted malicious HTML forms to exploit endpoints lacking proper CSRF protection.
  - Tested various scenarios where session cookies could be exploited without user consent.
- **SSRF Exploitation:**
  - Learned common SSRF payload patterns.
  - Tested SSRF vulnerabilities by manipulating URLs to access internal network services and metadata endpoints (e.g., cloud provider metadata).
  - Experimented with bypass techniques to evade input validation filters.
- **XXE Attacks:**
  - Crafted XML payloads with external entity references.
  - Exploited XXE to read sensitive files (like `/etc/passwd`) on the server.
  - Understood how XXE can lead to server-side request forgery or denial-of-service.
- **Burp Suite Practice:**
  - Used the Intruder tool for automating injection points.
  - Employed Repeater for manual request modification and response analysis.
  - Configured custom payload sets and attack types for maximum effectiveness.
- **Lab Completion:**
  - Solved TryHackMe Web Security challenges involving OWASP Top 10 vulnerabilities.
  - Documented step-by-step exploitation process and mitigation strategies.

---

## 📌 Key Takeaways:
- **CSRF:** Importance of using anti-CSRF tokens, validating HTTP headers, and implementing same-site cookies.
- **SSRF:** Critical impact on cloud and internal services, highlighting the need for strict input validation and network segmentation.
- **XXE:** XML parsers must be configured to disable external entity processing; input should be sanitized.
- **Burp Suite Skills:** Mastery of Intruder and Repeater tools accelerates vulnerability discovery and exploitation.
- **Hands-on Experience:** Practical labs reinforce theoretical knowledge and prepare for real-world pentesting scenarios.

---

## 💡 Challenges & Solutions:
- **Challenge:** Bypassing SSRF filters that blocked common payloads.  
  **Solution:** Used URL encoding and alternative payload formats to bypass input validation.
- **Challenge:** Identifying missing CSRF protections in complex web apps.  
  **Solution:** Analyzed request headers and response tokens carefully, crafted custom exploits.
- **Challenge:** Understanding XML parser configurations to exploit XXE.  
  **Solution:** Tested multiple XML formats and researched parser vulnerabilities to confirm attack vectors.

---

## 🔗 References & Resources:
- [OWASP Top 10 Project](https://owasp.org/www-project-top-ten/)
- [PortSwigger Web Security Academy - CSRF](https://portswigger.net/web-security/csrf)
- [PortSwigger Web Security Academy - SSRF](https://portswigger.net/web-security/ssrf)
- [PortSwigger Web Security Academy - XXE](https://portswigger.net/web-security/xxe)
- [TryHackMe - Web Security Room](https://tryhackme.com/room/websecurity)
- [DVWA Official Website](http://www.dvwa.co.uk/)
- Uploaded Files: [My Resources](week%207)

