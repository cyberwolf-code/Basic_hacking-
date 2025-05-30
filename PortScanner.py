import socket
from datetime import datetime

target = input("Enter the IP address to scan: ")
start_port = 1
end_port = 1024

print(f"\nScanning {target} from port {start_port} to {end_port}")
print("Scan started at:", datetime.now())
print("-" * 50)

try:
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  

        result = sock.connect_ex((target, port))  
        if result == 0:
            print(f"Port {port}: OPEN")
        sock.close()

except KeyboardInterrupt:
    print("\nScan cancelled.")
except socket.gaierror:
    print("Hostname could not be resolved.")
except socket.error:
    print("Could not connect to server.")

print("-" * 50)
print("Scan finished at:", datetime.now())
