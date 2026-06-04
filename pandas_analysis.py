import pandas as pd
import sqlite3

connection = sqlite3.connect(
    "database/threats.db"
)

df = pd.read_sql_query(
    "SELECT * FROM threats",
    connection
)

print(df)

print(
    "\nTotal Threats:",
    len(df)
)

print("\nRisk Analysis\n")

print(
    df["risk_level"].value_counts()
)

print("\nTop Attacked Users\n")

print(
    df["username"].value_counts()
)

df.to_csv(
    "threat_report.csv",
    index=False
)
df.to_excel(
    "threat_report.xlsx",
    index=False
)

print(
    "Excel Report Generated Successfully!"
)

print(
    "\nCSV Report Generated Successfully!"
)

connection.close()