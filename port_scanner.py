import socket
from datetime import datetime

def scan_port(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = scanner.connect_ex((ip, port)) 
    scanner.close()
    return result == 0

def load_ports(filename):
    ports = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            
            if line and not line.startswith('#'):
                try:
                    ports.append(int(line.split()[0])) 
                except ValueError:
                    continue
    return ports

def scan_ports(ip, ports):
    open_ports = []
    print(f"Starting port scan on {ip} at {datetime.now()}...\n")

    for port in ports:
        if scan_port(ip, port):
            print(f"[+] Port {port} is open")
            open_ports.append(port)
        else:
            print(f"[-] Port {port} is closed")

    with open("scan_results.txt", "w") as result_file:
        result_file.write(f"Scan report for {ip} at {datetime.now()}\n")
        result_file.write(f"Open Ports: {open_ports if open_ports else 'None'}\n")
        print("\nScan complete. Results saved to 'scan_results.txt'.")

if __name__ == "__main__":
    target_ip = input("Enter the IP address or domain to scan: ")
    ports = load_ports("ports.txt")
    scan_ports(target_ip, ports)
