from flask import Flask, render_template, request, redirect, send_file
from analyzer.threat_detector import analyze_log
from pdf_generator import generate_pdf
import os
import sqlite3
import requests

app = Flask(__name__)

UPLOAD_FOLDER = "logs"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def dashboard():

    connection = sqlite3.connect("database/threats.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM threats")
    threats = cursor.fetchall()

    user_count = {}

    for threat in threats:

        username = threat[1]

        if username in user_count:
            user_count[username] += 1
        else:
            user_count[username] = 1

    if user_count:
        top_user = max(
            user_count,
            key=user_count.get
        )
        top_user_count = user_count[top_user]
    else:
        top_user = "None"
        top_user_count = 0

    total_threats = len(threats)

    high_risk = sum(
        1 for threat in threats
        if threat[3] == "HIGH"
    )

    medium_risk = sum(
        1 for threat in threats
        if threat[3] == "MEDIUM"
    )

    low_risk = sum(
        1 for threat in threats
        if threat[3] == "LOW"
    )

    alert_message = "System Secure"
    alert_class = "alert-low"

    if high_risk >= 1:
        alert_message = "HIGH RISK THREAT DETECTED"
        alert_class = "alert-high"

    elif medium_risk >= 1:
        alert_message = "MEDIUM RISK ACTIVITY DETECTED"
        alert_class = "alert-medium"

    try:

        response = requests.get(
            "https://api.github.com",
            timeout=5
        )

        api_status = "ONLINE"

    except:

        api_status = "OFFLINE"

    connection.close()

    return render_template(
        "dashboard.html",
        threats=threats,
        total_threats=total_threats,
        high_risk=high_risk,
        medium_risk=medium_risk,
        low_risk=low_risk,
        top_user=top_user,
        top_user_count=top_user_count,
        alert_message=alert_message,
        alert_class=alert_class,
        api_status=api_status
    )


@app.route("/upload", methods=["POST"])
def upload_file():

    if "logfile" not in request.files:
        return redirect("/")

    file = request.files["logfile"]

    if file.filename == "":
        return redirect("/")

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)

    analyze_log(filepath)

    return redirect("/")


@app.route("/download-report")
def download_report():

    report_path = "reports/threat_report.txt"

    return send_file(
        report_path,
        as_attachment=True
    )


@app.route("/download-pdf")
def download_pdf():

    generate_pdf()

    return send_file(
        "reports/Threat_Report.pdf",
        as_attachment=True
    )


if __name__ == "__main__":
    if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)