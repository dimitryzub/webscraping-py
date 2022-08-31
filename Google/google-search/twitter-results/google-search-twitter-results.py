import requests, lxml
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

params = {
    "q": "garyvee twitter",
    "hl": "en",
    "gl": "us"
}

response = requests.get("https://www.google.com/search", headers=headers, params=params)
soup = BeautifulSoup(response.text, 'lxml')

for result in soup.select('[jscontroller=yz368b]'):
    title = result.select_one('g-link .a-no-hover-decoration .NsiYH').text
    link = result.select_one('g-link .a-no-hover-decoration')['href']
    displayed_link = result.select_one('g-link .a-no-hover-decoration .V0XQK').text
    print(f'{title}\n{link}\n{displayed_link}\n')

    for tweet in result.select('g-scrolling-carousel.rQgnxe .dHOsHb g-inner-card'):
        tweet_link = tweet.select_one('.h4kbcd')['href']
        tweet_snippet = tweet.select_one('.xcQxib').text
        tweet_published = tweet.select_one('.kLhEKe .f:nth-child(3)').text
        print(f'{tweet_link}\n{tweet_snippet}\n{tweet_published}')