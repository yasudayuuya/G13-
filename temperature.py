from bs4 import BeautifulSoup
import requests
import time

url = "https://www.data.jma.go.jp/obd/stats/etrn/view/daily_a1.php?prec_no=45&block_no=1236&year=2024&month=1&day=&view="
d_list = []
time.sleep(1)

res = requests.get(url)
html = res.text
soup = BeautifulSoup(res.text, 'html.parser')