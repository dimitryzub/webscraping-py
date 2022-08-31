from bs4 import BeautifulSoup
import requests
import lxml

headers = {
  "User-Agent":
  "Mozilla/5.0 (Linux; Android 10; HD1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 EdgA/46.1.2.5140"
}
 
response = requests.get('https://www.baidu.com/s?&tn=baidu&wd=lasagna', headers=headers).text

soup = BeautifulSoup(response, 'lxml')

for link in soup.select('.result .t a'):
  links = link['href']
  print(links)

# Alternative method using SerpApi

# import os
# from serpapi import GoogleSearch

# params = {
#     "engine": "baidu",
#     "q": "lasagna",
#     "api_key": os.getenv("API_KEY"),
# }

# search = GoogleSearch(params)
# results = search.get_dict()

# for organic_result in results["organic_results"]:
#   if 'link' in organic_result:
#     print(f"Link: {organic_result['link']}")
