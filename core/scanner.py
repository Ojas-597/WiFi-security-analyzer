import subprocess
from core.utils import print_header

def scan_wifi():
    print_header("Scanning Wi-Fi Networks")

    try:
        output = subprocess.check_output(
            "netsh wlan show networks mode=bssid",
            shell=True
        ).decode(errors="ignore")

        print(output)
        return output

    except Exception as e:
        print("Error:", e)
        return ""
