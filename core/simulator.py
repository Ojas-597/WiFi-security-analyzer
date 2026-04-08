import random
import time
from core.utils import print_header

def simulate_attack():
    print_header("Simulated Attack Detection")

    fake_ips = ["192.168.1.2", "192.168.1.5", "192.168.1.10"]

    for _ in range(10):
        src = random.choice(fake_ips)
        dst = random.choice(fake_ips)

        print(f"{src} -> {dst}")
        time.sleep(0.3)

        if src == dst:
            print("⚠ Suspicious Activity Detected!")
