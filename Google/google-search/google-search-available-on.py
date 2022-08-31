import requests, lxml
from bs4 import BeautifulSoup

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

params = {
    "q": "spider man watch online",
    "hl": "en",
    "gl": "us",
}

html = requests.get("https://www.google.com/search", params=params, headers=headers)
soup = BeautifulSoup(html.text, 'lxml')

for result in soup.select('.JkUS4b'):
    name = result.select_one('.i3LlFf').text
    link = result['href']
    price = result.select_one('.V8xno').text
    print(f'{name}\n{link}\n{price}\n')