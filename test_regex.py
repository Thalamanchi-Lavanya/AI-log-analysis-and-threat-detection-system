import re

log = "2026-06-01 10:01:25 LOGIN_FAILED user2"

pattern = r"(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2})\s+(LOGIN_FAILED|LOGIN_SUCCESS)\s+(\w+)"

match = re.search(pattern, log)

if match:
    print("Date:", match.group(1))
    print("Time:", match.group(2))
    print("Event:", match.group(3))
    print("User:", match.group(4))