import requests, lxml
from bs4 import BeautifulSoup

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

params = {"q": "lasagna recipe", "hl": "en", 'gl': 'us'}

response = requests.get("https://www.google.com/search", params=params, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')

for result in soup.select('.cv2VAd'):
    title = result.select_one('.hfac6d').text
    source = result.select_one('.KuNgxf').text
    total_time = result.select_one('.L5KuY.Eq0J8').text
    # stays the list if need to extract certain ingredient
    ingredients = result.select_one('.LDr9cf').text.split(',')
    rating = result.select_one('.oqSTJd').text
    reviews = result.select_one('.KsR1A+ .Eq0J8').text.replace('(', '').replace(')', '')
    print(f'{title}\n{source}\n{total_time}\n{rating}\n{reviews}\n{ingredients}\n')
