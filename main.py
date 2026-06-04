import sqlite3
log_file = "logs/sample.log"

with open(log_file, "r") as file:
    logs = file.readlines()

print("===== LOG FILE CONTENT =====")

for log in logs:
    print(log.strip())

failed_count = 0
failed_users = {}

for log in logs:

    if "LOGIN_FAILED" in log:

        failed_count += 1

        username = log.strip().split()[-1]

        if username in failed_users:
            failed_users[username] += 1
        else:
            failed_users[username] = 1

print("\n===== ANALYSIS =====")
print("Failed Login Attempts:", failed_count)

print("\n===== FAILED USERS =====")

for user, count in failed_users.items():
    print(user, "->", count, "failed attempts")

print("\n===== THREAT DETECTION =====")

for user, count in failed_users.items():

    if count >= 3:

        print("THREAT DETECTED")
        print("User:", user)
        print("Attack Type: Potential Brute Force Attack")
        print("Risk Level: HIGH")
        print("-------------------------")
        report_file = "reports/threat_report.txt"

with open(report_file, "w") as report:

    report.write("THREAT DETECTION REPORT\n")
    report.write("=======================\n\n")

    for user, count in failed_users.items():

        if count >= 3:

            report.write(f"User: {user}\n")
            report.write("Attack Type: Potential Brute Force Attack\n")
            report.write("Risk Level: HIGH\n")
            report.write("-------------------------\n")

print("\nThreat report generated successfully.")
connection = sqlite3.connect("database/threats.db")

cursor = connection.cursor()

cursor.execute(
    """
    INSERT INTO threats(username, attack_type, risk_level)
    VALUES (?, ?, ?)
    """,
    (
        user,
        "Potential Brute Force Attack",
        "HIGH"
    )
)

connection.commit()
connection.close()