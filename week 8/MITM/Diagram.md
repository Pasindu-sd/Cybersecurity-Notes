<!-- ===== MITM Diagram (Mermaid) ===== -->
### MITM Diagram

flowchart LR
  Client["Client\n(192.168.1.100)"]
  Router["Router / Gateway\n(192.168.1.1)"]
  Attacker["Attacker\n(impersonates 192.168.1.1)"]
  Server["Remote Server\n(eg. example.com)"]

  Client ---|Sends traffic| Attacker
  Attacker ---|Forwards / Modifies| Router
  Router ---|Forwards to Internet| Server

  subgraph Local_Net [Local Network]
    Client
    Attacker
    Router
  end

  %% Annotations
  Attacker -. "ARP spoofing / DNS spoofing\nEvil-twin / Rogue AP" .-> Client
  Attacker -. "Traffic capture, injection,\nsession hijacking (possible)" .-> Router
  note right of Attacker
    MITM: attacker intercepts & may alter
    traffic while remaining between
    client and router/server.
  endnote
