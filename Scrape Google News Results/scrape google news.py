from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

response = requests.get(
    'https://www.google.com/search?hl=en-US&q=chicago&tbm=nws',
    headers=headers).text

soup = BeautifulSoup(response, 'lxml')

for headings in soup.findAll('div', class_='dbsr'):
    title = headings.find('div', class_='JheGif nDgy9d').text
    # summary = headings.find('div', class_='Y3v8qd').text
    link = headings.a['href']
    print(title)
    # print(summary)
    print(link)
    print()


#Alternative SerpApi method:  

# import os
# from serpapi import GoogleSearch

# params = {
#     "engine": "google",
#     "q": "best cookies",
#     "tbm": "nws",
#     "api_key": os.getenv("API_KEY"),
# }

# search = GoogleSearch(params)
# results = search.get_dict()

# for news_result in results["news_results"]:
#    print(f"Title: {news_result['title']}\n, Link: {news_result['link']}")
