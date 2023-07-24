import csv
import sqlite3

csv_file = 'most_ordered_dishes.csv' 
db_file = 'restaurant.db'

def create_table(cursor):
    #Define the table schema
    cursor.execute('''CREATE TABLE IF NOT EXISTS most_ordered_dishes (
        number INTEGER,
        date TEXT,
        time TEXT,
        most_ordered_dish TEXT,
        category TEXT,
        price REAL
        )''')

def insert_data(cursor, row):
    # Insert a row of data into the table
    cursor.execute("INSERT INTO most_ordered_dishes (number, date, time, most_ordered_dish, category, price) VALUES (?, ?, ?, ?, ?, ?)", row)

# Connect to the SQLite database
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create the table
create_table(cursor)

# Read the CVS file and insert the data into the database

with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    next(reader) # Skip the header row if it exists
    for row in reader:
        insert_data(cursor, row)
        print(row[3])

    # Commit the changes and close the connection
    conn.commit()
    conn.close()