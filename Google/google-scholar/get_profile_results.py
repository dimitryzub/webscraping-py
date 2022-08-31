from bs4 import BeautifulSoup
import requests, lxml, os

headers = {
    'User-agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

proxies = {
  'http': os.getenv('HTTP_PROXY')
}

def get_profiles():
  html = requests.get('https://scholar.google.com/citations?view_op=view_org&hl=en&org=9834965952280547731', headers=headers, proxies=proxies).text
  soup = BeautifulSoup(html, 'lxml')

  # Selecting container where all data located 
  for result in soup.select('.gs_ai_chpr'):
    name = result.select_one('.gs_ai_name a').text
    link = result.select_one('.gs_ai_name a')['href']
    # https://stackoverflow.com/a/6633693/15164646
    id = link
    id_identifer = 'user='
    before_keyword, keyword, after_keyword = id.partition(id_identifer)
    author_id = after_keyword
    affiliations = result.select_one('.gs_ai_aff').text
    email = result.select_one('.gs_ai_eml').text
    try:
      interests = result.select_one('.gs_ai_one_int').text
    except:
      interests = None
    # "Cited by 107390" = getting text string -> splitting by a space -> ['Cited', 'by', '21180'] and taking [2] index which is the number.
    cited_by = result.select_one('.gs_ai_cby').text.split(' ')[2] 
    
    print(f'{name}\nhttps://scholar.google.com{link}\n{author_id}\n{affiliations}\n{email}\n{interests}\n{cited_by}\n')
