# MITM Diagram

<!-- Mermaid diagram (GitHub may render this if Mermaid is enabled) -->
```mermaid
flowchart LR
  Client["Client\n(192.168.1.100)"]
  Attacker["Attacker\n(MITM)\n(impersonates 192.168.1.1)"]
  Router["Router / Gateway\n(192.168.1.1)"]
  Server["Remote Server\n(example.com)"]

  Client -- "Sends traffic" --> Attacker
  Attacker -- "Forwards / Modifies" --> Router
  Router -- "To Internet" --> Server

  subgraph Local_Network
    Client
    Attacker
    Router
  end

  Attacker -. "Techniques: ARP spoofing, DNS spoofing, Evil-Twin" .-> Client
  Attacker -. "Can capture, modify, inject, or drop traffic" .-> Router
