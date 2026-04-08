import tkinter as tk
from core.scanner import scan_wifi
from core.analyzer import analyze_security
from core.devices import detect_devices
from core.simulator import simulate_attack

scan_data = ""

def run_scan():
    global scan_data
    scan_data = scan_wifi()

def run_analysis():
    analyze_security(scan_data)

root = tk.Tk()
root.title("Wi-Fi Security Analyzer")
root.geometry("300x250")

tk.Button(root, text="Scan Wi-Fi", command=run_scan).pack(pady=5)
tk.Button(root, text="Analyze Security", command=run_analysis).pack(pady=5)
tk.Button(root, text="Detect Devices", command=detect_devices).pack(pady=5)
tk.Button(root, text="Simulate Attack", command=simulate_attack).pack(pady=5)

root.mainloop()
