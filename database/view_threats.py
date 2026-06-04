import sqlite3

connection = sqlite3.connect("database/threats.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM threats")

records = cursor.fetchall()

for row in records:
    print(row)

connection.close()