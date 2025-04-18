#!/usr/bin/python3

import can
from can.interface import Bus
import re
import time
import argparse

def send_can_message(id_hex, dlc, data_hex, interface, bus):
    data = bytes.fromhex(data_hex)
    print(id_hex)
    print(int(id_hex, 16))
    message = can.Message(arbitration_id=int(id_hex, 16), dlc=dlc, data=data, is_extended_id=False, is_fd=True)
    
    try:
        bus.send(message)
        print(f"Message sent: ID=0x{int(id_hex, 16):X}, DLC={dlc}, Data={data.hex()}")
    except can.CanError:
        print("Error sending the message")

def can_inject(interface, args):
    bus = Bus(interface='socketcan', channel=interface, fd=True)

    print(f"Injecting data as per your input {interface}")
    dlc = 3
    data_hex = args.value
    id = args.component
    print(id)
    send_can_message(id, dlc, data_hex, "vcan0", bus)
    bus.shutdown()

parser = argparse.ArgumentParser()
parser.add_argument("--component", required=True, choices=['19B', '188', '244'], help="Component to inject data to; 19B for doors, 188 for indictator and 244 for speed")
parser.add_argument("--value", required=True, help="Value to send")
args = parser.parse_args()

can_inject("vcan0", args)