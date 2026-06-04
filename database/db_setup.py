import sqlite3

connection = sqlite3.connect("database/threats.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS threats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    attack_type TEXT,
    risk_level TEXT
)
""")

connection.commit()

connection.close()

print("Database created successfully.")