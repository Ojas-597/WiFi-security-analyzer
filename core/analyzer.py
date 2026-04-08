from core.utils import print_header

def analyze_security(scan_output):
    print_header("Security Analysis")

    findings = []

    if not scan_output:
        print("⚠ No scan data available")
        return findings

    if "WEP" in scan_output:
        findings.append("⚠ Weak Security: WEP detected")

    if "Open" in scan_output:
        findings.append("⚠ Open Network detected")

    if "WPA2" in scan_output:
        findings.append("✔ WPA2 (Secure)")

    if "WPA3" in scan_output:
        findings.append("✔ WPA3 (Highly Secure)")

    if not findings:
        findings.append("No major issues detected")

    for f in findings:
        print(f)

    return findings
