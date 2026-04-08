from flask import Flask, render_template, redirect
from core.scanner import scan_wifi
from core.analyzer import analyze_security

app = Flask(__name__)

scan_data = ""

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/scan')
def scan():
    global scan_data
    scan_data = scan_wifi()
    return redirect('/')

@app.route('/analyze')
def analyze():
    analyze_security(scan_data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
