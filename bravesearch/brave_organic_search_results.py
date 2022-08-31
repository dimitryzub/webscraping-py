from bs4 import BeautifulSoup
import requests, lxml, json

headers = {
  'User-agent':
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

params = {
  'q': 'dune film',
  'source': 'web'
}

def get_organic_results():

  html = requests.get('https://search.brave.com/search', headers=headers, params=params)
  soup = BeautifulSoup(html.text, 'lxml')

  data = []

  for result, sitelinks in zip(soup.select('.snippet.fdb'), soup.select('.deep-results-buttons .deep-link')):
    title = result.select_one('.snippet-title').text.strip()
    title_img = result.select_one('.favicon')['src']
    link = result.a['href']
    displayed_link = result.select_one('.snippet-url').text.strip().replace('\n', '')

    try:
      # removes "X time ago" -> split by \n -> removes all whitespaces to the LEFT of the string
      snippet = result.select_one('.snippet-content .snippet-description').text.strip().split('\n')[1].lstrip()
      snippet_img = result.select_one('.snippet-content .thumb')['src']
    except: 
      snippet = None
      snippet_img = None
    
    # list comprehension for creating key-value pair of title/link from sitelink results 
    sitelinks = [
          {
            title: sitelink.text.strip(),
            link: sitelink['href']
          } for sitelink in result.select('.deep-results-buttons .deep-link')]

    try:
      rating = result.select_one('.ml-10').text.strip().split(' - ')[0]
      votes = result.select_one('.ml-10').text.strip().split(' - ')[1]
    except: 
      rating = None
      votes = None

    data.append({
      'title': title,
      'title_img': title_img,
      'link': link,
      'displayed_link': displayed_link,
      'snippet': snippet,
      'snippet_img': snippet_img,
      'rating': rating,
      'votes': votes,
      'sitelinks': sitelinks
    })
      
  print(json.dumps(data, indent=2, ensure_ascii=False))


get_organic_results()
