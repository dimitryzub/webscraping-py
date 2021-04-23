from bs4 import BeautifulSoup
import requests, json
import lxml

headers = {
  "User-Agent":
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

html = requests.get(
    'https://www.ebay.com/sch/i.html?_from=R40&_nkw=minecraft+creeper+figure&_sacat=0&LH_TitleDesc=0&rt=nc&Year=2020&_dcat=75708',
    headers = headers).text

soup = BeautifulSoup(html, 'lxml')

data = []

for item in soup.findAll('div', class_ = 's-item__wrapper clearfix'):
  try:
      price = item.find('span', class_ = 's-item__price').text
  except:
      price = None
  try:
      title = item.find('h3', class_='s-item__title').text
  except:
      title = None
  try:
      condition = item.find('span', class_='SECONDARY_INFO').text
  except:
      condition = None

  data.append({
      "Title": title,
      "Price": price,
      "Item Condition": condition,
  })

print(json.dumps(data, indent = 2, ensure_ascii = False))
