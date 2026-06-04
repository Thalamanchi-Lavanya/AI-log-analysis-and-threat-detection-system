import sqlite3
import re


def analyze_log(log_path):

    with open(log_path, "r") as file:
        logs = file.readlines()

    failed_users = {}

    for log in logs:

        pattern = r"(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2})\s+(LOGIN_FAILED|LOGIN_SUCCESS)\s+(\w+)"

        match = re.search(pattern, log)

        if match:

            date = match.group(1)
            time = match.group(2)
            event = match.group(3)
            username = match.group(4)

            print(
                f"Date: {date}, Time: {time}, Event: {event}, User: {username}"
            )

            if event == "LOGIN_FAILED":

                if username in failed_users:
                    failed_users[username] += 1
                else:
                    failed_users[username] = 1

    connection = sqlite3.connect("database/threats.db")
    cursor = connection.cursor()
    print("Failed Users:", failed_users)

    for user, count in failed_users.items():

        if count >= 6:

            threat_score = 90

            cursor.execute(
                """
                INSERT INTO threats(username, attack_type, risk_level)
                VALUES (?, ?, ?)
                """,
                (
                    user,
                    "Account Lockout Attempt",
                    "HIGH"
                )
            )

        elif count >= 3:

            threat_score = 60

            cursor.execute(
                """
                INSERT INTO threats(username, attack_type, risk_level)
                VALUES (?, ?, ?)
                """,
                (
                    user,
                    "Potential Brute Force Attack",
                    "MEDIUM"
                )
            )

    connection.commit()
    connection.close()