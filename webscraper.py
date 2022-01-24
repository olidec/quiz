from bs4 import BeautifulSoup
import requests
from random import choice
import json

def my_scraper():
    url = "https://www.srf.ch/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    headlines = [item.string for item in soup.select(".teaser__title")]
    return headlines

headlines = my_scraper()

print(f"Found a total of {len(headlines)} headlines.")

with open("headlines.json",'w') as f:
    json.dump(headlines,f)