import pcapy
import matplotlib.pyplot as plt
from collections import defaultdict

def monitor_bandwidth(interface, duration):
    capture = pcapy.open_live(interface, 65536, True, 100)

    bandwidth_usage = defaultdict(int)

    start_time = time.time()
    end_time = start_time + duration

    while time.time() < end_time:
        header, packet = capture.next()
        # Extract source and destination IP addresses
        src_ip = '.'.join(map(str, packet[26:30]))
        dst_ip = '.'.join(map(str, packet[30:34]))

        # Update bandwidth usage for source and destination IPs
        bandwidth_usage[src_ip] += len(packet)
        bandwidth_usage[dst_ip] += len(packet)

    # Generate report
    plt.bar(bandwidth_usage.keys(), bandwidth_usage.values())
    plt.xlabel('IP Address')
    plt.ylabel('Bandwidth Usage')
    plt.title('Bandwidth Usage by IP Address')
    plt.show()

monitor_bandwidth('eth0', 60)  # Monitor bandwidth for 60 seconds on interface eth0
