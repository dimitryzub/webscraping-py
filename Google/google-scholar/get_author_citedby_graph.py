from bs4 import BeautifulSoup
import requests, lxml, os

headers = {
    'User-agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

proxies = {
  'http': os.getenv('HTTP_PROXY')
}

def get_graph():
  html = requests.get('https://scholar.google.com/citations?hl=en&user=D41VK7AAAAAJ', headers=headers, proxies=proxies).text

  soup = BeautifulSoup(html, 'lxml')

  years = [graph_year.text for graph_year in soup.select('.gsc_g_t')]
  citations = [graph_citation.text for graph_citation in soup.select('.gsc_g_a')]

  data = []

  for year, citation in zip(years,citations):
    print(f'{year} {citation}\n')

    data.append({
      'year': year,
      'citation': citation,
    })

  # print(json.dumps(data, indent=2))
