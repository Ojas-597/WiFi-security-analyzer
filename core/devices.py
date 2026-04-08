import os
from core.utils import print_header

def detect_devices():
    print_header("Connected Devices (ARP)")
    os.system("arp -a")
