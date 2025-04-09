# tcp-hawk

## Overview
This is a simple yet effective Python-based TCP port scanner that performs a full range scan (ports 0–65535) on a given target using multithreading to maximize speed and responsiveness.

## Features
- Scans all 65,535 TCP ports
- Uses multithreading for faster scanning (up to 100 threads)
- Displays open ports in real-time
- Handles timeouts gracefully
- Lightweight and easy to use

## Prerequisites 
- Python 3.x

## Installation
```bash
git clone https://github.com/Pritt014/tcp-hawk.git
cd tcp-hawk
```

## Usage
```bash
python3 port_scan.py
```
You will be prompted to enter a hostname or IP address to scan.

### Example
```
Enter host for scanning: scanme.nmap.org
Starting scanning on host: 45.33.32.156
Port 22: OPEN
Port 80: OPEN
...
Time taken: 14.32 seconds
```

## Disclaimer
This tool is intended for **educational and authorized use only**. Unauthorized port scanning may be illegal and is strictly discouraged.

## Author
**Pritt Nyerere**  
Python Developer | Security Automation | DFIR Practitioner

## What’s Next?
- Add UDP scanning support
- Output to file
- Basic banner grabbing for open ports

## License
This project is licensed under the MIT License.
