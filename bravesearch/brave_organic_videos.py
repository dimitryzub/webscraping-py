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

def get_organic_video_results():

  html = requests.get('https://search.brave.com/search', headers=headers, params=params)
  soup = BeautifulSoup(html.text, 'lxml')

  data = []

  for video_result in soup.select('#video-carousel .card'):
    title = video_result.select_one('.title').text.strip()
    link = video_result['href']
    source = video_result.select_one('.anchor').text.strip()
    favicon = video_result.select_one('.favicon')['src']
    thumbnail = video_result.select_one('.img-bg')['style'].split(', ')[0].replace("background-image: url('", "").replace("')", "")
    try:
      video_duration = video_result.select_one('.duration').text.strip()
    except: video_duration = None

    data.append({
      'title': title,
      'link': link,
      'source': source,
      'favicon': favicon,
      'thumbnail': thumbnail,
      'video_duration': video_duration
    })

  print(json.dumps(data, indent=2, ensure_ascii=False))


get_organic_video_results()