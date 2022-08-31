from bs4 import BeautifulSoup
import requests
import lxml

headers = {
  "User-Agent":
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

response = requests.get(
  'https://www.google.com/search?q=site:wikipedia.com thomas edison',
  headers=headers).text

soup = BeautifulSoup(response, 'lxml')

for link in soup.find_all('div', class_='yuRUbf'):
  links = link.a['href']
  print(links)


# Alternative method using SerpApi

# import os
# from serpapi import GoogleSearch

# params = {
#     "engine": "google",
#     "q": "site:wikipedia.com thomas edison",
#     "api_key": os.getenv("API_KEY"),
# }

# search = GoogleSearch(params)
# results = search.get_dict()

# for result in results["organic_results"]:
#   print(f"Link: {result['link']}")
