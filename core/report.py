from core.utils import get_timestamp

def generate_report(scan_data, findings):
    with open("report.txt", "w") as f:
        f.write("Wi-Fi Security Report\n")
        f.write("="*40 + "\n")
        f.write("Generated: " + get_timestamp() + "\n\n")

        f.write("Scan Data:\n")
        f.write(scan_data + "\n")

        f.write("\nFindings:\n")
        for item in findings:
            f.write(item + "\n")

    print("✅ report.txt generated")
