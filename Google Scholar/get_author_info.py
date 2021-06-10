from bs4 import BeautifulSoup
import requests, lxml, os

headers = {
    'User-agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

proxies = {
  'http': os.getenv('HTTP_PROXY')
}


def get_author_info():
  html = requests.get('https://scholar.google.com/citations?hl=en&user=m8dFEawAAAAJ', headers=headers, proxies=proxies).text
  soup = BeautifulSoup(html, 'lxml')

  # Author info
  name = soup.select_one('#gsc_prf_in').text
  affiliation = soup.select_one('#gsc_prf_in+ .gsc_prf_il').text

  try:
    email = soup.select_one('#gsc_prf_ivh').text
  except:
    email = None

  try:
    interests = soup.select_one('#gsc_prf_int').text
  except:
    interests = None

  print('Author info:')
  print(f'{name}\n{affiliation}\n{email}\n{interests}\n')
