from bs4 import BeautifulSoup
import requests
import lxml
import json

headers = {
  "User-Agent":
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

response = requests.get(
  'https://www.google.com/search?q=minecraft+toys&tbm=shop',
  headers=headers).text

soup = BeautifulSoup(response, 'lxml')

data = []

for container in soup.findAll('div', class_='sh-dgr__content'):
  title = container.find('h4', class_='A2sOrd').text
  price = container.find('span', class_='a8Pemb').text
  supplier = container.find('div', class_='aULzUe IuHnof').text

  data.append({
    "Title": title,
    "Price": price,
    "Supplier": supplier,
  })

print(json.dumps(data, indent = 2, ensure_ascii = False))

# Alternative solution using SerpApi:

# from serpapi import GoogleSearch
# import os 

# params = {
#   "engine": "google",
#   "q": "minecraft toys",
#   "tbm": "shop",
#   "api_key": os.getenv("API_KEY"),
# }

# search = GoogleSearch(params)
# results = search.get_dict()

# for result in results['shopping_results']:
#   print(f"Title: {result['title']}\nPrice: {result['price']}\nSupplier: {result['source']}\n")
