import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("[#] Enter your ip address to scan port")
s_port = int(input("Enter start port number"))
e_port = int(input("Enter end port number"))

def scan(port):
   if sock.connect_ex((host,port)):
      print("[!!] port %d is closed" %port)
   else:
      print("[*] port %d is open   [=>]" %port)
      
for port in range(s_port, e_port):
   scan(port)