# Binaryxploit

This is a versatile penetration testing tool designed to perform reconnaissance, scanning, and exploitation tasks. It integrates Nmap for network scanning and Metasploit for exploitation using various payloads.

## Features

- Perform Nmap scans on target hosts with different scan types.
- Exploit vulnerabilities using Metasploit payloads.

## Installation

1. Clone this repository:

   
```
git clone https://github.com/clasikpaige/Binaryxploit.git
cd Binaryxploit
```
## install requiments 
```
 pip install -r requirements.txt
 ```
Configure the Metasploit RPC connection details in `penetration_testing.py`.

## Usage

Run the Binaryxploit using the following command:
```
python main.py –target <target_ip> –scan-type <scan_type> –payloads <num_payloads>
```
```python
- `<target_ip>`: The target IP address for testing.
- `<scan_type>`: Specify the Nmap scan type (`quick`, `intense`, or `udp`).
- `<num_payloads>`: Number of Metasploit payloads to use.
Example:

``
python main.py –target 192.168.1.10 –scan-type intense –payloads 5
```


## Legal Disclaimer

This tool is intended for educational and testing purposes only. Make sure you have explicit permission before using it against any network or system. i wont be responsible for any misuse or damage caused.


