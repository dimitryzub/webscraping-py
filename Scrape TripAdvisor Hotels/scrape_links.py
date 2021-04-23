# Very basic and simple scraper 

from bs4 import BeautifulSoup
import requests, lxml, json

def scrape():
  
  with open('links.txt') as link:
    for line in link:
      url = line

      headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
      }
      
      data = []

      html = requests.get(url, headers=headers)
      soup = BeautifulSoup(html.text, 'lxml')

      title = soup.select_one('#HEADING').text

      if soup.select_one('._1WEIRhGY') is not None:
        location = soup.select_one('._1WEIRhGY').text
      else:
        None

      if soup.select_one('._3Z-kyXHr ._3ErVArsu') is not None:
        phone = soup.select_one('._3Z-kyXHr ._3ErVArsu').text
      else:
        None

      reviews = soup.select_one('._33O9dg0j').text

      if soup.select_one('.CEf5oHnZ') or soup.select_one('._36QMXqQj') is not None: 
        price = soup.select_one('.CEf5oHnZ') or soup.select_one('._36QMXqQj')
        price_formatted = price.text
      else:
        None
      
      data.append({
        "Title": title,
        "Location": location,
        "Reviews": reviews,
        "Phone": phone,
        "Price": price_formatted,
      })

      print(json.dumps(data, indent = 2, ensure_ascii = False))
