# Python Port Scanner

This is a simple Python-based port scanner that allows users to scan a range of ports on a specified IP address or domain. The tool checks if a port is open or closed and logs the results to a file.

## Features

- Scan ports on a target IP or domain
- Log open/closed ports to a `scan_results.txt` file
- Load a list of ports to scan from a `ports.txt` file
- Timeout set to 1 second per port scan to avoid long delays

## Requirements

- python>=3.6

### Libraries

- Python's built-in `socket` library for networking functionality
- `datetime` for timestamping the scan

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/python-port-scanner.git
   cd python-port-scanner
