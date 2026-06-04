# 🛡️ AI Log Analysis & Threat Detection System

> Intelligent cybersecurity monitoring platform built using Python, Machine Learning, and Flask to detect suspicious activities from system/server logs in real-time.

---

# 🚀 Project Overview

The **AI Log Analysis & Threat Detection System** is an advanced Python-based cybersecurity project that analyzes log files, identifies malicious activities, detects anomalies using Machine Learning, and visualizes threats through an interactive dashboard.

This project simulates how real-world SOC (Security Operations Center) systems monitor and analyze suspicious events.

---

# ✨ Features

## 🔍 Smart Log Analysis

* Reads and processes system/server log files
* Detects suspicious patterns using Regex
* Supports multiple log formats

## 🤖 AI-Powered Threat Detection

* Anomaly Detection using Machine Learning
* Detects unusual login attempts and malicious activities
* Isolation Forest algorithm for threat prediction

## 📊 Interactive Dashboard

* Visual representation of threats
* Charts and analytics using Plotly & Matplotlib
* Threat statistics and reports

## 🗄️ Database Integration

* Stores detected threats securely
* SQLite/MySQL support
* Maintains historical logs and alerts

## 🚨 Real-Time Alerts

* Flags suspicious IP addresses
* Generates automated alerts
* Tracks attack frequency

## 📄 PDF Report Generation

* Export threat analysis reports
* Security audit summaries
* Incident reporting support

---

# 🧠 Technologies Used

| Component           | Technology           |
| ------------------- | -------------------- |
| 💻 Language         | Python               |
| 🌐 Backend          | Flask                |
| 🗃️ Database        | SQLite / MySQL       |
| 📑 Log Processing   | Regex, Pandas        |
| 🤖 Machine Learning | Scikit-learn         |
| 📊 Visualization    | Matplotlib, Plotly   |
| 🎨 Frontend         | HTML, CSS, Bootstrap |

---

# 🏗️ System Architecture

```text
           📁 Log Files
                  ↓
        🐍 Python Log Reader
                  ↓
       🔍 Threat Pattern Detection
                  ↓
        🤖 AI/ML Threat Analysis
                  ↓
         🗄️ Store in Database
                  ↓
        📊 Dashboard Visualization
                  ↓
           🚨 Generate Alerts
```

---
# 📁 Project Structure

```bash
AI_THREAT_DETECTION/
│
├── analyzer/
│   ├── __pycache__/
│   ├── threat_detector.py
│   ├── threat_detector_oop.py
│   └── threat.py
│
├── dashboard/
│
├── database/
│
├── logs/
│
├── reports/
│
├── templates/
│   └── dashboard.html
│
├── venv/
│
├── .gitignore
├── api_test.py
├── app.py
├── main.py
├── ml_detector.py
├── pandas_analysis.py
├── pdf_generator.py
├── Procfile
├── README.md
├── requirements.txt
├── runtime.txt
├── test_oop.py
├── test_regex.py
├── test_threat.py
├── threat_report.csv
└── threat_report.xlsx
```
---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Thalamanchi_Lavanya/AI-Log-Analysis-System.git
cd AI-Log-Analysis-System
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

# 📸 Dashboard Preview

## 📈 Threat Analytics

* Suspicious login attempts
* Failed authentication analysis
* Attack frequency graphs

## 🌍 IP Tracking

* Detects malicious IP addresses
* Tracks repeated access attempts

## ⚠️ Alert Monitoring

* Real-time threat notifications
* High-risk activity detection

---

# 🤖 Machine Learning Module

The system uses:

* ✅ Isolation Forest
* ✅ Anomaly Detection
* ✅ Traffic Pattern Analysis
* ✅ Suspicious Activity Prediction

### ML Workflow

```text
Log Data
   ↓
Feature Extraction
   ↓
ML Model Training
   ↓
Anomaly Detection
   ↓
Threat Classification
```

---

# 🔐 Cybersecurity Capabilities

* SQL Injection Detection
* Brute Force Attack Detection
* Unauthorized Access Monitoring
* Suspicious IP Analysis
* Failed Login Monitoring
* Security Event Tracking

---

# 📊 Sample Threat Output

```json
{
  "ip_address": "192.168.1.10",
  "threat_level": "High",
  "attack_type": "Brute Force",
  "status": "Blocked"
}
```

---

# 🌟 Why This Project is Impressive

✅ Real-world cybersecurity use case

✅ Strong Python backend development

✅ AI + Machine Learning integration

✅ Database management

✅ Data visualization skills

✅ REST API concepts

✅ Scalable architecture

✅ Recruiter-friendly project

---

# 👨‍💻 Skills Demonstrated

* Python Programming
* Flask Development
* Machine Learning Basics
* Data Analysis
* Cybersecurity Concepts
* API Development
* Database Handling
* Object-Oriented Programming
* Exception Handling
* Data Visualization

---

# 🔮 Future Enhancements

* 🔥 Real-time socket log monitoring
* ☁️ Cloud deployment (AWS/GCP)
* 📧 Email/SMS alerts
* 🧠 Deep Learning threat detection
* 📱 Mobile dashboard
* 🛰️ SIEM integration
* 🛡️ Advanced intrusion detection

---

# 📜 License

This project is licensed under the MIT License.

---

# 🤝 Contributing

Contributions are welcome!

```bash
Fork → Clone → Create Branch → Commit → Push → Pull Request
```

---

# ⭐ Support

If you like this project:

🌟 Star the repository
🍴 Fork the project
📢 Share with others

---

# 📬 Contact

## 👤 Developer

**THALAMANCHI LAVANYA**

📧 [thalamanchilavanya@egmail.com]

🌐 GitHub: https://github.com/Thalamanchi-Lavanya

---

# 💡 Final Note

This project demonstrates how Python, AI, and Cybersecurity can work together to build intelligent threat detection systems used in modern security operations.

> "Detect Threats Before They Become Attacks." 🛡️
