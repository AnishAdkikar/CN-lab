import time
import random

def send_packet(packet):
    print("Sending packet:", packet)
    time.sleep(1)  # Simulate transmission delay
    return True # Simulate random success/failure


def receive_ack(ans):
    time.sleep(1)  # Simulate reception delay
    # return random.choice([True, False])  # Simulate random success/failure
    return False if ans>3 and ans%5 == 0 else True

def GBARQ(data_packets):
    not_recieved = set()
    x = set()
    windowSize = 3
    base = 0
    count = 0
    ans = 1
    totalFrames = len(data_packets)
    while base <= totalFrames-1:
        part = 0
        window = data_packets[base: min(base + windowSize, totalFrames + 1)]
        for packet in window:
            sent = send_packet(packet)
        for packet in window:
            if receive_ack(ans):
                print(f"frame {packet} sent successfully")
                ans += 1
                part += 1
                # not_recieved.add(packet)
            else:
                print(f"frame {packet} not sent")
                ans += 1
                break
                
                # x.add(packet)
        # i += 1
        base += part

    print(f"Total transmitted frames are {ans}")



# Example usage
data_packets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
GBARQ(data_packets)
