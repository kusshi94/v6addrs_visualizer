import numpy as np
import matplotlib.pyplot as plt
import ipaddress
import argparse
from typing import List
from tqdm import tqdm

def process_ipv6(ipv6: str) -> List[int]:
    ipv6 = ipaddress.ip_address(ipv6)
    ipv6_hex = ipv6.exploded.replace(':', '')
    return [int(char, 16) for char in ipv6_hex]

def plot_ipv6_distribution(ips: List[str]):
    # Initialize the distribution matrix
    distribution = np.zeros((16, 32))

    # Process each IP with a progress bar
    for ip in tqdm(ips, desc='Processing IPs'):
        # Skip comments
        if ip.startswith('#'):
            continue
        nibbles = process_ipv6(ip)
        for i, nibble in enumerate(nibbles):
            distribution[nibble][i] += 1

    # Display the distribution as a heatmap
    plt.figure(figsize=(10, 6))
    plt.imshow(distribution, cmap='Blues', interpolation='nearest', origin='lower', aspect='equal')
    plt.colorbar(label='Frequency')

    plt.xlabel('Nibble Index')
    plt.ylabel('Nibble Value')
    plt.title('Nibble Distribution of IPv6 Addresses')

    # Change y-axis labels to hexadecimal
    plt.yticks(range(16), [hex(i)[2:] for i in range(16)])

    plt.show()

def load_ips_from_file(filename: str) -> List[str]:
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

# Create parser and define arguments
parser = argparse.ArgumentParser(description='Process and plot IPv6 distribution.')
parser.add_argument('filename', type=str, help='Name of the file containing IPv6 addresses')

# Parse arguments
args = parser.parse_args()

# Load IP addresses from file
ips = load_ips_from_file(args.filename)

plot_ipv6_distribution(ips)
