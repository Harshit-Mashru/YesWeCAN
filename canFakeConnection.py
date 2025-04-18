#!/usr/bin/python3

import can
from can.interface import Bus
import re
import time

def send_can_message(id_hex, dlc, data_hex, interface, bus):
    data = bytes.fromhex(data_hex)
    message = can.Message(arbitration_id=int(id_hex, 16), dlc=dlc, data=data, is_extended_id=True, is_fd=True)
    
    try:
        bus.send(message)
        print(f"Message sent: ID=0x{int(id_hex, 16):X}, DLC={dlc}, Data={data.hex()}")
    except can.CanError:
        print(f"Error sending this message: {message}")

def can_replay(interface):

    print(f"Replaying data on {interface}")
    with open('send.log', 'r') as file:
        lines = file.readlines()    
        bus = can.interface.Bus(channel=interface, interface='socketcan', fd=True)
        line = lines[0]
        match = re.match(r"ID:\s*(\w+),\s*DLC:\s*(\d+),\s*Data:\s*(\w+)", line.strip())
        if match:
            id_hex, dlc, data_hex = match.groups()
            dlc = int(dlc)
            send_can_message(id_hex, dlc, data_hex, "vcan0", bus)
            print("=================================================================")
            time.sleep(1)
        server_line = ""
        try:
            while True:
                msg = bus.recv(timeout=1)
                if msg:
                    line = "ID: {:X}, DLC: {}, Data: {}".format(msg.arbitration_id, msg.dlc, msg.data.hex())
                    # file.write(line + "\n")
                    print(f"Received line: {line}")
                    if msg.data.hex().startswith('0100'):
                        print("voila")
                        server_line = line
                        break
        except KeyboardInterrupt:
            print("Sniffer stopped.")
        
        
        bus.shutdown()
can_replay("vcan0")