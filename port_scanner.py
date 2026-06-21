import socket
from datetime import datetime
target =input("Enter your ip to scan")
start_port=int(input("Start port : "))
End_port=int(input("End port : "))
port_names = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    135: "Windows RPC",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3389: "RDP"
}
print(f"\nScanning {target} from port {start_port} to {End_port} ...\n")
open_ports=[]
timestamp = datetime.now(). strftime("%Y-%m-%d %H:%M:%S")
for port in range (start_port,End_port +1):
    s= socket.socket()
    s.settimeout(0.5)
    result = s.connect_ex((target,port))
    if result == 0 :
        name= port_names.get(port,"UnKnown")
        open_ports.append((port,name))
        print(f"Port {port} is open > {name}")
        s.close()
print(f"\nscan complete. , Found {len(open_ports)} open ports.")
with open("scan_results.txt","w") as f:
    f.write(f"Scan Report - {timestamp}\n")
    f.write(f"Target -{target}\n")
    f.write(f"Range: {start_port} - {End_port}\n \n")
    for port, name in open_ports :
        f.write(f"Port {port} -{name}\n")
        print("Results saved to Scan_results.txt")