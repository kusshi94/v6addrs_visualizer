import sys
import logging
from scapy.config import conf
from scapy.layers.inet6 import IPv6
from scapy.all import rdpcap

def extract_destination_ipv6(pcap_file: str, output_file: str) -> None:
    # Disable IPv4 address-related warnings
    conf.ipv6_enabled = False
    logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

    # Read the pcap file
    packets = rdpcap(pcap_file)

    # Extract destination IPv6 addresses and write them to the output file
    with open(output_file, 'w') as file:
        for packet in packets:
            if IPv6 in packet:
                destination_ipv6 = packet[IPv6].dst
                file.write(destination_ipv6 + '\n')

    print("Extraction of destination IPv6 addresses completed.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python filename.py pcap_file_path output_file_path")
        sys.exit(1)

    pcap_file = sys.argv[1]
    output_file = sys.argv[2]

    extract_destination_ipv6(pcap_file, output_file)
