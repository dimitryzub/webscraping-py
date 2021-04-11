from bs4 import BeautifulSoup
import requests
import lxml

headers = {
  "User-Agent":
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

response = requests.get(
"https://www.bing.com/search?q=lasagna", headers=headers).text

soup = BeautifulSoup(response, 'lxml')

for container in soup.select('.b_algo h2 a'):
  links = container['href']
  print(links)


# Alernative method using SerpApi.

# import os
# from serpapi import GoogleSearch

# params = {
#   "q": "lasagna",
#   "engine": "bing",
#   "api_key": os.getenv("API_KEY"),
# }

# search = GoogleSearch(params)
# results = search.get_dict()

# for link in results["organic_results"]:
#   print(f"Link: {link['link']}")
