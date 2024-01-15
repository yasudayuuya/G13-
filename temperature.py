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
        time = td_list[0].text.strip()
        temperature = td_list[2].text.strip()
        temperature_data.append((time, temperature))

for time, temperature  in temperature_data:
    print(f"Time: {time}, Temperature: {temperature}")
