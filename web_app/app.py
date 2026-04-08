from flask import Flask, render_template, redirect
import os

# Import project modules
from core.scanner import scan_wifi
from core.analyzer import analyze_security
from core.simulator import simulate_attack
from core.graphs import show_graph
from core.ml_model import detect_anomaly
from core.report import generate_report

app = Flask(__name__)

# Global storage
scan_data = None
findings = []
message = "System ready."

# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("index.html", data=message)


# ---------------- SCAN WIFI ----------------
@app.route("/scan")
def scan():
    global scan_data, message

    try:
        scan_data = scan_wifi()
        message = "✅ Wi-Fi scan completed successfully."
    except:
        message = "⚠ Unable to scan networks. Running in demo mode."

    return redirect("/")


# ---------------- ANALYZE SECURITY ----------------
@app.route("/analyze")
def analyze():
    global findings, message

    if scan_data:
        try:
            findings = analyze_security(scan_data)
            message = "<br>".join(findings)
        except:
            message = "⚠ Security analysis failed."
    else:
        message = "⚠ Please run Wi-Fi scan first."

    return redirect("/")


# ---------------- SIMULATE ATTACK ----------------
@app.route("/simulate")
def simulate():
    global message

    try:
        simulate_attack()
        message = "⚠ Suspicious traffic simulated successfully."
    except:
        message = "⚠ Simulation module not available."

    return redirect("/")


# ---------------- GRAPH ----------------
@app.route("/graph")
def graph():
    global message

    try:
        show_graph()
        message = "📊 Graph generated."
    except:
        message = "⚠ Graph generation failed."

    return redirect("/")


# ---------------- ML DETECTION ----------------
@app.route("/ml")
def ml():
    global message

    try:
        detect_anomaly()
        message = "🤖 ML anomaly detection completed."
    except:
        message = "⚠ ML module not working."

    return redirect("/")


# ---------------- REPORT ----------------
@app.route("/report")
def report():
    global message

    if scan_data:
        try:
            generate_report(scan_data, findings)
            message = "📄 Security report generated successfully."
        except:
            message = "⚠ Report generation failed."
    else:
        message = "⚠ Please scan networks before generating report."

    return redirect("/")


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
