📌 Project Overview

This project is developed as part of the CodeAlpha Cyber Security Internship. The objective is to build a Python-based Network Packet Sniffer that captures live network traffic, analyzes packet information, and displays important details such as source/destination IP addresses, protocols, ports, and packet size using the Scapy library.

The project consists of two versions:

Static Packet Capture – Captures packets using a predefined network interface.
Dynamic Packet Capture – Allows the user to select the network interface, protocol, and number of packets dynamically.

🎯 Objectives:

Capture live network packets.
Analyze packet structure and content.
Understand how data flows through a network.
Identify network protocols (TCP, UDP, ICMP).
Display useful packet information.
Save captured packet details into a log file.

🚀 Features:

Displays all available network interfaces.
User selects the desired interface.
Supports protocol filtering:
TCP
UDP
ICMP
ALL
Displays packet details in real time.
Shows packet summary.
Displays:
Source IP Address
Destination IP Address
Protocol
Source Port
Destination Port
Packet Size
Generates a capture summary.
Saves captured packets into capture_log.txt.

🛠 Technologies Used:

Python 3.x
Scapy
Npcap (Windows)
VS Code / IDLE

📚 Python Libraries:

from scapy.all import sniff, get_if_list
from datetime import datetime


▶️ How to Run:

Static Packet Capture:
python Static_Packet_Capture.py

Dynamic Packet Capture:
python Dynamic_Packet_Capture.py

Dynamic Packet Capture Workflow:

Display available network interfaces.
User selects the interface.
User selects the protocol (TCP/UDP/ICMP/ALL).
User enters the number of packets to capture.
Program starts packet capturing.
Each captured packet is analyzed.
Packet details are displayed.
Capture summary is generated.
Packet information is saved in capture_log.txt.
Packet Information Displayed

For every captured packet, the program displays:

Timestamp
Packet Number
Packet Summary
Source IP Address
Destination IP Address
Protocol Type
Source Port
Destination Port
Packet Size
Payload (if available)
Sample Output
========== Available Network Interfaces ==========

1. Intel(R) Dual Band Wireless-AC 8265
2. Loopback Adapter

Select Interface Number : 1

Enter Protocol (TCP/UDP/ICMP/ALL): TCP

Enter Number of Packets to Capture: 10

Capturing Packets...

Example Packet:

Packet #1

Protocol : TCP

Source IP : 192.168.1.10

Destination IP : 142.250.183.78

Source Port : 50447

Destination Port : 443

Packet Size : 74 Bytes

Practical Working:

The application first retrieves all available network interfaces using Scapy. The user selects an interface and chooses the protocol to monitor. The sniff() function captures live packets from the selected interface. Each packet is processed through a callback function, where the program identifies the protocol, extracts IP addresses, port numbers, and packet size, and displays the information on the screen. Finally, a summary of captured packets is generated and saved to a log file.

Protocols Supported:

TCP:
Reliable communication
Connection-oriented
Used for HTTPS, HTTP, FTP, Email

UDP:
Fast communication
Connectionless
Used for Streaming, Gaming, DNS

ICMP:
Network diagnostics
Used by the Ping command

Learning Outcomes:

After completing this project, I learned:

How network packets are captured.
How TCP, UDP, and ICMP protocols work.
How data flows across a network.
How to use the Scapy library for packet sniffing.
How to analyze packet structure.
How to extract IP addresses, protocols, and port numbers.
How to log captured packet information for future analysis.

Future Enhancements:

GUI using Tkinter or PyQt.
Packet filtering by IP address.
Save captured packets as .pcap files.
Display packet payload in a readable format.
Real-time network traffic graphs.
Export captured data to CSV or Excel.
