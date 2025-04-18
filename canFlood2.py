#!/usr/bin/python3

import can
import threading

NUM_THREADS = 100  # You can increase this to stress the system more

def flood_can_bus(interface):
    bus = can.interface.Bus(channel=interface, interface='socketcan', fd=True)
    while True:
        try:
            message = can.Message(
                arbitration_id=0x2,
                dlc=8,
                data=[0xFF] * 8,
                is_extended_id=True,
                is_fd=True
            )
            bus.send(message)
            # Commenting out to reduce IO overhead and speed things up
            # print(f"Flooding message: ID=0x2, Data={message.data.hex()}")
        except can.CanError as e:
            print(f"Error sending message: {e}")
            break

def start_flooding(interface):
    threads = []
    for _ in range(NUM_THREADS):
        t = threading.Thread(target=flood_can_bus, args=(interface,))
        t.daemon = True  # Makes sure threads exit when main thread exits
        threads.append(t)
        t.start()
    
    # Keep the main thread alive
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nFlooding interrupted by user.")

if __name__ == "__main__":
    start_flooding("vcan0")