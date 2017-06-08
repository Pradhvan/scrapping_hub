import requests 
from bs4 import BeautifulSoup
from collections import deque
data = {} 
base_url = ("http://www.imdb.com/year")
page = requests.get(base_url)
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="main")
forecast_items = seven_day.find_all(class_="splash")
tonight = forecast_items[0]
for i in tonight.find_all("a"):
	link = (base_url +i.get("href"))
	year = i.text
	data = {link : year}
	

