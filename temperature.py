from bs4 import BeautifulSoup
import requests
import time

url = "https://www.data.jma.go.jp/obd/stats/etrn/view/hourly_a1.php?prec_no=45&block_no=1236&year=2024&month=01&day=1&view=p1"
temperature_data = []
time.sleep(0.1)

res = requests.get(url)
html = res.text
soup = BeautifulSoup(res.text, 'html.parser')
time.sleep(0.1)

for tr in soup.find_all('tr', class_='mtx'):
    td_list = tr.find_all('td')
    if len(td_list) >= 3:
        time_values = td_list[0].text.strip()
        temperature_values = td_list[2].text.strip()
        sunshine_hours_values = td_list[8].text.strip()
        temperature_data.append({'time': time_values, 'temperature_open': temperature_values, 'sunshine_hour': sunshine_hours_values})

for item  in temperature_data:
    print(f"Time: {item['time']}, Temperature_open: {item['temperature_open']}, Sunshine_hours: {item['sunshine_hour']}")

import sqlite3

con = sqlite3.connect('google_database.db')
cur = con.cursor()

sql_createtable_DSp = 'CREATE TABLE IF NOT EXISTS sql_DS (time TEXT, temperature_open TEXT, sunshine_hour TEXT)'
cur.execute(sql_createtable_DSp)

for item in temperature_data:
    cur.execute('INSERT INTO sql_DS (time, temperature_open, sunshine_hour) VALUES (?, ?, ?)', (item['time'], item['temperature_open'], item['sunshine_hour']))

con.commit()

con.close()

con = sqlite3.connect('google_database.db')
cur = con.cursor()

cur.execute('SELECT * FROM sql_DS')
rows = cur.fetchall()

for row in rows:
    print(row)

con.close() 