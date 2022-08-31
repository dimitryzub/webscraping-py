from bs4 import BeautifulSoup
import requests, lxml, urllib.parse

def get_listings(url):
  
  headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
  }

  html = requests.get(url, headers=headers)
  soup = BeautifulSoup(html.text, 'lxml')

  with open('links.txt', 'w') as f:
    for container in soup.select('.listItem'):
      link = urllib.parse.urljoin('https://www.tripadvisor.com', container.select_one('.prominent')['href'] + '#MAPVIEW')

      f.write(f"{link}\n")
