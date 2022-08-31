from bs4 import BeautifulSoup
import requests, lxml, json

headers = {
  'User-agent':
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

params = {
  'q': 'dune 2021',
  'source': 'web'
}

def get_organic_news_results():

  html = requests.get('https://search.brave.com/search', headers=headers, params=params)
  soup = BeautifulSoup(html.text, 'lxml')

  data = []

  for news_result in soup.select('#news-carousel .card'):
    title = news_result.select_one('.title').text.strip()
    link = news_result['href']
    time_published = news_result.select_one('.card-footer__timestamp').text.strip()
    source = news_result.select_one('.anchor').text.strip()
    favicon = news_result.select_one('.favicon')['src']
    thumbnail = news_result.select_one('.img-bg')['style'].split(', ')[0].replace("background-image: url('", "").replace("')", "")

    data.append({
      'title': title,
      'link': link,
      'time_published': time_published,
      'source': source,
      'favicon': favicon,
      'thumbnail': thumbnail
    })

  print(json.dumps(data, indent=2, ensure_ascii=False))


get_organic_news_results()
