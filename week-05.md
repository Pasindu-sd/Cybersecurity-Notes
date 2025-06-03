# Week 05 – Web Application Security

## 🔸 OWASP Top 10 Vulnerabilities + SQL Injection
- Reviewed the **OWASP Top 10** common web application vulnerabilities.
- Focused on **SQL Injection (SQLi)**:
  - Manual testing on vulnerable forms.
  - Example payloads:
    - `' OR '1'='1`
    - `admin' --`
  - Used **Burp Suite** to intercept and modify HTTP requests for SQLi testing.

## 🔸 Burp Suite Introduction and Practice
- Installed and configured **Burp Suite Community Edition**.
- Practiced:
  - Intercepting HTTP/HTTPS requests.
  - Modifying requests.
  - Using Repeater and Intruder modules.

## 🔸 Cross-Site Scripting (XSS)
- Studied **Reflected** and **Stored XSS**.
- Tested payloads like:
  - `<script>alert('XSS')</script>`
- Identified input fields vulnerable to XSS in test environments.

## 🔸 TryHackMe – OWASP Top 10 Room
- Completed the **OWASP Top 10** room.
- Understood real-world vulnerable applications.
- Hands-on experience with:
  - SQL Injection
  - XSS
  - Broken Authentication
  - CSRF

## 🔸 DVWA (Damn Vulnerable Web App)
- Installed DVWA in a local web server.
- Practiced:
  - SQL Injection
  - XSS
  - Command Injection
- Set DVWA Security Level to **Low** and **Medium** to test vulnerabilities.

---

## 🔗 Useful References
- [OWASP Top 10 Explained](https://owasp.org/www-project-top-ten/)
- [Burp Suite Tutorial](https://portswigger.net/burp/documentation)
- [XSS for Beginners](https://portswigger.net/web-security/cross-site-scripting)
- [TryHackMe OWASP Room](https://tryhackme.com/room/owasptop10)
- [DVWA Setup Guide](http://www.dvwa.co.uk/)

---

✅ Uploaded:
- [All scripts and projects for this week](week%205/)
