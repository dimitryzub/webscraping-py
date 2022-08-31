from bs4 import BeautifulSoup
import requests
import lxml

headers = {
  "User-Agent":
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

response = requests.get(
  'https://www.google.com/search?q=swiggy company review',
  headers=headers).text

soup = BeautifulSoup(response, 'lxml')

# Selects just one Review element (using converted xPath to CSS selector):
# review = soup.select_one('#rso > div:nth-of-type(1) > div > div > div:nth-of-type(2) > div > span:nth-of-type(1)').text
# print(review)

# Selects multiple Review elements:
for rating in soup.select('.uo4vr g-review-stars+ span'):
  ratings = rating.text
  print(ratings)

# Selects just one Vote element (using converted xPath to CSS selector):
# votes = soup.select_one('#rso > div:nth-of-type(1) > div > div > div:nth-of-type(2) > div > span:nth-of-type(2)').text
# print(votes)

# Selects multiple Vote elements:
for vote in soup.select('.uo4vr span+ span'):
  votes_reviews = vote.text
  print(votes_reviews)

# Alternative method

# from serpapi import GoogleSearch
# import os

# params = {
#   "engine": "google",
#   "q": "swiggy company review",
#   "api_key": os.getenv("API_KEY"),
# }

# search = GoogleSearch(params)
# results = search.get_dict()

# # For extracting single elements:
# # rating = results['organic_results'][0]['rich_snippet']['top']['detected_extensions']['rating']
# # print(f"Rating: {rating}")

# # votes = results['organic_results'][0]['rich_snippet']['top']['detected_extensions']['votes']
# # print(f"Votes: {votes}")

# # For extracing multiple elements:
# for rating in results['organic_results']:
#   try:
#     rating = rating['rich_snippet']['top']['extensions'][0]
#     print(rating)
#   except:
#     print('No rating found')

# for vote_review in results['organic_results']:
#   try:
#     votes_reviews = vote_review['rich_snippet']['top']['extensions'][1]
#     print(votes_reviews)
#   except:
#     print('No votes or reviews found')
