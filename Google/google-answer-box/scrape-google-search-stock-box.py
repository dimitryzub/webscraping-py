import requests
import lxml
from bs4 import BeautifulSoup

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

html = requests.get('https://www.google.com/search?q=Nasdaq composite', headers=headers).text

soup = BeautifulSoup(html, 'lxml')

print(soup.select_one('.wT3VGc').text)
