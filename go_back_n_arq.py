# import random

# frames = int(input("Enter the number of frames: "))
# window_size = int(input("Enter the window size: "))
# frames_transmitted = 0
# window_start = 1

# while window_start <= frames:
#     part = 0  # how much part is of window
#     for j in range(window_start, min(window_start + window_size, frames + 1)):
#         print("Frame sent:", j)
#         frames_transmitted += 1

#     for j in range(window_start, min(window_start + window_size, frames + 1)):
#         ack = random.randint(0, 1)  # 0 or 1
#         if ack:
#             print("Acknowledgement from frame:", j)
#             part += 1
#         else:
#             print("Acknowledgement:", j, "not received")
#             print("Retransmitting window")
#             break

#     print()
#     window_start += part

# print("Total frames transmitted:", frames_transmitted)
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
    windowSize = 3
    base = 0
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
            else:
                print(f"frame {packet} sent successfully")
                part += 1
        base += part

    print(f"Total transmitted frames are {ans}")



# Example usage
data_packets = [1, 2, 3, 4, 5]
Selective_Repeat(data_packets)
