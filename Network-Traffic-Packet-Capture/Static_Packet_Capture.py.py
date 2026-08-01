from scapy.all import sniff

# Function to process each captured packet
def packet_callback(packet):
    print("=" * 60)
    print("Packet Captured")
    print(packet.summary())

    if packet.haslayer("IP"):
        print("Source IP      :", packet["IP"].src)
        print("Destination IP :", packet["IP"].dst)

    if packet.haslayer("TCP"):
        print("Protocol        : TCP")
        print("Source Port     :", packet["TCP"].sport)
        print("Destination Port:", packet["TCP"].dport)

    elif packet.haslayer("UDP"):
        print("Protocol        : UDP")
        print("Source Port     :", packet["UDP"].sport)
        print("Destination Port:", packet["UDP"].dport)

    elif packet.haslayer("ICMP"):
        print("Protocol        : ICMP")

    print("=" * 60)


def main():
    print("========================================")
    print(" Network Traffic Packet Capture Program ")
    print("========================================")
    print("Capturing 10 packets...\n")

    sniff(
        iface="Intel(R) Dual Band Wireless-AC 8265",
        count=10,
        prn=packet_callback,
        store=False
    )

    print("\nPacket capture completed.")


if __name__ == "__main__":
    main()
