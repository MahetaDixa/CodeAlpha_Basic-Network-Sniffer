from scapy.all import sniff, get_if_list
from datetime import datetime

# Show available interfaces
interfaces = get_if_list()

print("\n========== Available Network Interfaces ==========\n")
for i, iface in enumerate(interfaces):
    print(f"{i+1}. {iface}")

choice = int(input("\nSelect Interface Number: "))
selected_iface = interfaces[choice - 1]

protocol = input("Enter Protocol (TCP/UDP/ICMP/ALL): ").upper()
packet_count = int(input("Enter Number of Packets to Capture: "))

tcp_count = 0
udp_count = 0
icmp_count = 0
total = 0

log = open("capture_log.txt", "w")

def packet_callback(packet):
    global tcp_count, udp_count, icmp_count, total

    total += 1

    print("\n" + "=" * 60)
    print(f"Packet #{total}")
    print("Time :", datetime.now().strftime("%H:%M:%S"))

    log.write("\n" + "=" * 60 + "\n")
    log.write(f"Packet #{total}\n")
    log.write(f"Time : {datetime.now().strftime('%H:%M:%S')}\n")

    print(packet.summary())
    log.write(packet.summary() + "\n")

    if packet.haslayer("IP"):
        print("Source IP      :", packet["IP"].src)
        print("Destination IP :", packet["IP"].dst)

        log.write("Source IP      : " + packet["IP"].src + "\n")
        log.write("Destination IP : " + packet["IP"].dst + "\n")

    if packet.haslayer("TCP"):
        tcp_count += 1
        print("Protocol       : TCP")
        print("Source Port    :", packet["TCP"].sport)
        print("Destination Port:", packet["TCP"].dport)

    elif packet.haslayer("UDP"):
        udp_count += 1
        print("Protocol       : UDP")
        print("Source Port    :", packet["UDP"].sport)
        print("Destination Port:", packet["UDP"].dport)

    elif packet.haslayer("ICMP"):
        icmp_count += 1
        print("Protocol       : ICMP")

    print("Packet Size    :", len(packet), "Bytes")

    log.write("Packet Size    : " + str(len(packet)) + " Bytes\n")


def packet_filter(packet):
    if protocol == "ALL":
        return True
    elif protocol == "TCP":
        return packet.haslayer("TCP")
    elif protocol == "UDP":
        return packet.haslayer("UDP")
    elif protocol == "ICMP":
        return packet.haslayer("ICMP")
    return False


print("\nCapturing Packets...\n")

sniff(
    iface=selected_iface,
    timeout=10,
    lfilter=packet_filter,
    prn=packet_callback,
    store=False
)

print("\n========== Capture Summary ==========")
print("Total Packets :", total)
print("TCP Packets   :", tcp_count)
print("UDP Packets   :", udp_count)
print("ICMP Packets  :", icmp_count)

log.write("\n========== Capture Summary ==========\n")
log.write(f"Total Packets : {total}\n")
log.write(f"TCP Packets   : {tcp_count}\n")
log.write(f"UDP Packets   : {udp_count}\n")
log.write(f"ICMP Packets  : {icmp_count}\n")

log.close()

print("\nLog saved as capture_log.txt")
