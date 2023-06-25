import random
import time

def send_packet(packet):
    print("Sending packet:", packet)
    time.sleep(1)  # Simulate transmission delay
    return random.choice([True, False])  # Simulate random success/failure

def receive_ack():
    time.sleep(1)  # Simulate reception delay
    return random.choice([True, False])  # Simulate random success/failure

def stop_and_wait(data_packets):
    for packet in data_packets:
        while True:
            success = send_packet(packet)
            if success:
                ack_received = receive_ack()
                if ack_received:
                    print("ACK received for packet", packet)
                    break
                else:
                    print("NACK received for packet", packet)
                    print("Retransmitting packet", packet)
            else:
                print("Packet", packet, "not transmitted successfully")
                print("Retransmitting packet", packet)
    
    print("All packets have been successfully transmitted.")

# Example usage
data_packets = [1, 2, 3, 4, 5]
stop_and_wait(data_packets)
