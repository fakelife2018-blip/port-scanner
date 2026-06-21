# Port Scanner

A Python tool that scans a target IP address for open ports and saves the results to a file.

## Requirements
- Windows PC
- Python 3.x installed → https://python.org/downloads
- During Python install: check "Add Python to PATH"

## How to use
1. Download this repository (click green Code button → Download ZIP)
2. Extract the ZIP file
3. Double-click run_scanner.bat
4. Enter the target IP and port range when asked
5. Results are saved automatically to scan_results.txt

## What it does
- Scans any IP address for open ports
- Labels common ports (HTTP, SSH, RDP, SMB, FTP, DNS, etc.)
- Saves a timestamped report to scan_results.txt

## Example output
Scanning 192.168.1.1 from port 1 to 500...
Port 80 is OPEN  →  HTTP

Port 443 is OPEN  →  HTTPS
Scan complete. Found 2 open ports.

Results saved to scan_results.txt

## Skills used
Python, socket programming, file handling, dictionaries, datetime

## Author
Thomas Samir — AI Engineer 
