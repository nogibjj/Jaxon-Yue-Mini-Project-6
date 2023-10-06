import csv
import sqlite3

def load(dataset="Development of Average Annual Wages.csv"):
    # Connect to SQLite database
    conn = sqlite3.connect('wages.db')
    cursor = conn.cursor()

    # Create a table named 'wages'
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS wages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Country TEXT,
        year_2000 DOUBLE,
        year_2010 DOUBLE,
        year_2020 DOUBLE,
        year_2022 DOUBLE
    )
    ''')

    # Read the CSV file and insert data into the SQLite database
    with open(dataset, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            cursor.execute('''
            INSERT INTO wages (Country, year_2000, year_2010, year_2020, year_2022) 
            VALUES (?, ?, ?, ?, ?)
            ''', (row["Country"], row["year_2000"], row["year_2010"], row["year_2020"], row["year_2022"]))

    # Commit changes and close the SQLite connection
    conn.commit()
    conn.close()

