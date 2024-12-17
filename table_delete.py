import sqlite3

conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

# Drop the existing table
cursor.execute("DROP TABLE IF EXISTS attendance")

# Recreate the table with the 'major' column
create_table_sql = """
CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    time TEXT NOT NULL,
    date DATE NOT NULL,
    major TEXT NOT NULL,
    UNIQUE(name, date)
)
"""
cursor.execute(create_table_sql)
conn.commit()
conn.close()
