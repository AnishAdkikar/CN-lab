import time
import random

def send_packet(packet):
    print("Sending packet:", packet)
    time.sleep(1)  # Simulate transmission delay
    return random.choice([True, False])  # Simulate random success/failure


def receive_ack():
    time.sleep(1)  # Simulate reception delay
    return random.choice([True, False])  # Simulate random success/failure


def Selective_Repeat(data_packets):
    not_recieved = set()
    x = set()
    windowSize = 3
    base = 0
    totalFrames = len(data_packets)
    while len(x) != totalFrames:
        window = data_packets[base: min(base + windowSize, totalFrames + 1)]
        for packet in window:
            sent = send_packet(packet)
            if not sent:
                print(f"frame {packet} not sent")
                not_recieved.add(packet)
            else:
                print(f"frame {packet} sent successfully")
                x.add(packet)
        while not (not_recieved == set()):
            # print(not_recieved)
            for packet in not_recieved.copy():
                sent = send_packet(packet)
                if not sent:
                    print(f"frame {packet} not sent")
                else:
                    print(f"frame {packet} sent successfully")
                    x.add(packet)
                    not_recieved.remove(packet)
        print()
        # print(base+windowSize)
        base += windowSize



# Example usage
data_packets = [1, 2, 3, 4, 5]
Selective_Repeat(data_packets)
