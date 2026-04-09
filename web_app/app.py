from flask import Flask, render_template, redirect, request
import os

# Core modules
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
message = "🟢 System ready. Please login."


# ---------------- LOGIN ----------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    global message

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == "admin" and password == "1234":
            message = "✅ Login successful! Welcome to Wi-Fi Security Analyzer."
            return redirect('/dashboard')
        else:
            return render_template(
                "login.html",
                error="❌ Invalid credentials"
            )

    return render_template("login.html")


# ---------------- HOME ----------------
@app.route('/')
def home():
    return redirect('/login')


# ---------------- DASHBOARD ----------------
@app.route('/dashboard')
def dashboard():
    return render_template("index.html", data=message)


# ---------------- SCAN WIFI ----------------
@app.route('/scan')
def scan():
    global scan_data, message

    try:
        scan_data = scan_wifi()

        if scan_data:
            formatted_data = str(scan_data).replace("\n", "<br>")
            message = f"""
            <strong>📡 Wi-Fi Scan Completed</strong><br><br>
            {formatted_data}
            """
        else:
            message = "⚠ No Wi-Fi networks detected."

    except Exception as e:
        message = f"❌ Scan Error: {str(e)}"

    return redirect('/dashboard')


# ---------------- ANALYZE SECURITY ----------------
@app.route('/analyze')
def analyze():
    global findings, message

    if not scan_data:
        message = "⚠ Please scan Wi-Fi first."
        return redirect('/dashboard')

    try:
        findings = analyze_security(scan_data)

        if findings:
            formatted_findings = "<ul>" + "".join(
                f"<li>{item}</li>" for item in findings
            ) + "</ul>"

            message = f"""
            <strong>🛡 Security Analysis Results</strong><br><br>
            {formatted_findings}
            """
        else:
            message = "⚠ No vulnerabilities found."

    except Exception as e:
        message = f"❌ Analyze Error: {str(e)}"

    return redirect('/dashboard')


# ---------------- SIMULATE ATTACK ----------------
@app.route('/simulate')
def simulate():
    global message

    try:
        result = simulate_attack()

        if result:
            message = f"""
            <strong>⚠ Attack Simulation Result</strong><br><br>
            {str(result).replace("\n", "<br>")}
            """
        else:
            message = "⚠ Suspicious traffic simulation completed."

    except Exception as e:
        message = f"❌ Simulation Error: {str(e)}"

    return redirect('/dashboard')


# ---------------- GRAPH ----------------
@app.route('/graph')
def graph():
    global message

    try:
        show_graph()
        message = """
        <strong>📊 Graph Generated</strong><br><br>
        Security visualization processed successfully.
        """

    except Exception as e:
        message = f"❌ Graph Error: {str(e)}"

    return redirect('/dashboard')


# ---------------- ML DETECTION ----------------
@app.route('/ml')
def ml():
    global message

    try:
        result = detect_anomaly()

        if result:
            message = f"""
            <strong>🤖 ML Detection Result</strong><br><br>
            {str(result).replace("\n", "<br>")}
            """
        else:
            message = """
            <strong>🤖 ML Detection Completed</strong><br><br>
            No anomaly details returned.
            """

    except Exception as e:
        message = f"❌ ML Error: {str(e)}"

    return redirect('/dashboard')


# ---------------- REPORT ----------------
@app.route('/report')
def report():
    global message

    if not scan_data:
        message = "⚠ Please scan before generating report."
        return redirect('/dashboard')

    try:
        generate_report(scan_data, findings)

        message = """
        <strong>📄 Report Generated Successfully</strong><br><br>
        Security report has been created.
        """

    except Exception as e:
        message = f"❌ Report Error: {str(e)}"

    return redirect('/dashboard')


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
