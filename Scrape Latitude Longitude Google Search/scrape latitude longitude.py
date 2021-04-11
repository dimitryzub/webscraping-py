from bs4 import BeautifulSoup
import requests

headers = {
  'User-agent':
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

html = requests.get('https://www.google.com/search?q=latitude longitude of 75270 postal code paris france', headers=headers).text

soup = BeautifulSoup(html, 'lxml')

location = soup.select_one('.XcVN5d').text

print(location)
