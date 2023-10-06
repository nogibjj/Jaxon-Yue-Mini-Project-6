import sqlite3

# Establish a connection
conn = sqlite3.connect('wages.db')
cursor = conn.cursor()

# CREATE: Insert a new country's data
def create_wages_data(country, year_2000, year_2010, year_2020, year_2022):
    cursor.execute('INSERT INTO wages (country, year_2000, year_2010, year_2020, year_2022) VALUES (?, ?, ?, ?, ?)', 
                   (country, year_2000, year_2010, year_2020, year_2022))
    conn.commit()
    data = [country, year_2000, year_2010, year_2020, year_2022]
    print("Wages data created: " + ', '.join(map(str, data)))

# READ: Get all data
def read_all_wages_data():
    cursor.execute("SELECT * FROM wages")
    return cursor.fetchall()

def read_wages_data_by_country(country):
    cursor.execute("SELECT * FROM wages WHERE country=?", (country,))
    # Fetch the result
    data = cursor.fetchone()
    print("Wages data for " + country + ": " + str(data))

# UPDATE: Update data based on the country
def update_wages_data(country, year_2000, year_2010, year_2020, year_2022):
    cursor.execute("UPDATE wages SET year_2000=?, year_2010=?, year_2020=?, year_2022=? WHERE country=?", 
                   (country, year_2000, year_2010, year_2020, year_2022))
    conn.commit()
    data = [country, year_2000, year_2010, year_2020, year_2022]
    print("Wages data for " + country + " successfully updated to: " + ', '.join(map(str, data)))

# DELETE: Delete data by country
def delete_wages_data(country):
    cursor.execute("DELETE FROM wages WHERE country=?", (country,))
    conn.commit()
    print("Wages data for " + country + " deleted")

# Close the connection (Make sure to call this when done with database operations)
def close_connection():
    conn.close()
