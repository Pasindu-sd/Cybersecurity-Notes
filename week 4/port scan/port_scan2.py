import socket

# Get Target IP Address
target = input("Enter the ip address to scan: ")

# Get Port range
start_port = int(input("Start Port: "))
end_port = int(input("End Port: "))

print(f"\n{target} , {start_port} to {end_port} ports scan...\n")

# Port scan function
def scan_port(ip, port):
    try:
        # Creat Socket Object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)  # timeout set (half second)
        result = s.connect_ex((ip, port))  # Check Port open

        if result == 0:
            print(f"Port {port} is OPEN ")
        s.close()

    except:
        pass

# Port range scan
for port in range(start_port, end_port+1):
    scan_port(target, port)
