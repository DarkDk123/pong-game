from bs4 import BeautifulSoup
import requests
from pprint import pprint
date = input("ENTER THE DATE YOU WANT TO DIVE IN [YYYY-MM-DD]: ")
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/"+ date)
web = response.text
soup = BeautifulSoup(web, 'html.parser')
data = soup.find_all('span',class_= "chart-element__information__song text--truncate color--primary")

names = [item.text for item in data]




