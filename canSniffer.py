#!/usr/bin/python3

from can.interface import Bus

file = open('dump.log','w')

def can_sniffer(interface):
    bus = Bus(interface='socketcan', channel=interface, fd=True)
    print(f"Listening on {interface}")
    try:
        while True:
            msg = bus.recv(timeout=1)
            if msg:
                line = "ID: {:X}, DLC: {}, Data: {}".format(msg.arbitration_id, msg.dlc, msg.data.hex())
                file.write(line + "\n")
                print(f"Received line: {line}")
    except KeyboardInterrupt:
        print("Sniffer stopped.")

can_sniffer("vcan0")