from bs4 import BeautifulSoup
import requests, lxml
from user_agent import generate_user_agent

USER_AGENT = generate_user_agent(device_type="desktop")

headers = {'User-agent': f'{USER_AGENT}'}

html = requests.get('https://www.google.com/search?q=java', headers=headers)
soup = BeautifulSoup(html.text, 'lxml')

for container in soup.findAll('div', class_='TbwUpd NJjxre'):
  link = container.text
  print(link)
  
  
  
# Alternative method using SerpApi: 

import os
from serpapi import GoogleSearch

params = {
    "engine": "google",
    "q": "java",
    "api_key": os.getenv("API_KEY"),
}

search = GoogleSearch(params)
results = search.get_dict()

for result in results["organic_results"]:
   print(f"Link: {result['displayed_link']}")
