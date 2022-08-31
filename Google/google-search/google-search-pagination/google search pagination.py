from bs4 import BeautifulSoup
import requests
import json
import time
from random import randint


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36 Edg/79.0.309.43"
}

params = {
    "hl": "en"
}

for page_num in range(0, 91, 10):

    html = requests.get(f"https://www.google.com/search?q=london&start={page_num}", headers = headers, params = params).text

    soup = BeautifulSoup(html, 'lxml')

    content = []

    for container in soup.findAll('div', class_ = 'tF2Cxc'):
        head_text = container.find('h3', class_ = 'LC20lb DKV0Md').text
        head_sum = container.find('span', class_ = 'aCOpRe').text
        head_link = container.a['href']

        content.append({
            "Page_num": f"{page_num}",
            "Title": head_text,
            "Summary": head_sum,
            "Link": head_link,
        })

    print(json.dumps(content, indent = 2, ensure_ascii = False))
    time.sleep(randint(1,3))
