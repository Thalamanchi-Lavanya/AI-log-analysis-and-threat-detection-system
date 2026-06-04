import re


class ThreatDetector:

    def __init__(self, system_name):

        self.system_name = system_name

        print("Threat Detector Started")

    def welcome(self):

        print(
            f"Welcome to {self.system_name}"
        )

    def analyze_log(self, log_path):

        print(
            f"\nAnalyzing log file: {log_path}\n"
        )

        with open(log_path, "r") as file:

            logs = file.readlines()

        failed_users = {}

        pattern = r"(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2})\s+(LOGIN_FAILED|LOGIN_SUCCESS)\s+(\w+)"

        for log in logs:
            print(repr(log))
            match = re.search(pattern, log)

            if match:

                date = match.group(1)
                time = match.group(2)
                event = match.group(3)
                username = match.group(4)

                print(
                    f"Date: {date} | Time: {time} | Event: {event} | User: {username}"
                )

                if event == "LOGIN_FAILED":

                    if username in failed_users:
                        failed_users[username] += 1
                    else:
                        failed_users[username] = 1

        print("\n===== ANALYSIS =====\n")

        for user, count in failed_users.items():

            print(
                f"{user} -> {count} failed attempts"
            )