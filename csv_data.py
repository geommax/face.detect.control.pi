import sqlite3
import csv
from datetime import datetime
import os

def attendance_file(directory='csv_export'):
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name, time, date, major FROM attendance")
    attendance_data = cursor.fetchall()
    conn.close()

    if not attendance_data:
        print(f"No attendance data found in the database.")
        return
    
    current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    csv_filename = os.path.join(directory, f"attendance_export_{current_time}.csv")

    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Name", "Time", "Date", "Major"])
        csv_writer.writerows(attendance_data)

    print(f"Attendance data exported successfully to {csv_filename}")

attendance_file()
