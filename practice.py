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
    i = 0
    ans = 1
    totalFrames = len(data_packets)
    while base <= totalFrames-1:
        part = 0
        window = data_packets[base: min(base + windowSize, totalFrames + 1)]
        for packet in window:
            sent = send_packet(packet)
            ans += 1
        for packet in window:
            if receive_ack():
                print(f"frame {packet} not sent")
                break
                # not_recieved.add(packet)
            else:
                print(f"frame {packet} sent successfully")
                part += 1
                # x.add(packet)
        # i += 1
        base += part

    print(f"Total transmitted frames are {ans}")



# Example usage
data_packets = [1, 2, 3, 4, 5]
Selective_Repeat(data_packets)
