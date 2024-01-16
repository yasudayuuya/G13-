import csv
import pandas as pd
import sqlite3

con = sqlite3.connect('local_database.db')
cur = con.cursor()

sql_createtable_local = 'CREATE TABLE IF NOT EXISTS local_data (time TEXT, temperature TEXT, sunshine_hour TEXT)'
cur.execute(sql_createtable_local)

with open('/Users/yasudayuuya/class/DSprogramming/DSfinal/local.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
        cur.execute('INSERT INTO local_data (time, temperature, sunshine_hour) VALUES (?, ?, ?)', (row[0], row[1], row[2]))

con.commit()

con.close()

con = sqlite3.connect('local_database.db')
cur = con.cursor()

cur.execute('SELECT * FROM local_data')
rows = cur.fetchall()
for row in rows:
    print(row)

con.close()