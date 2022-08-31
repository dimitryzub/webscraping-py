from bs4 import BeautifulSoup
import requests, lxml

headers = {
    'User-agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

def get_ad_results():

    html = requests.get('https://search.yahoo.com/search?p=playstation 5',headers=headers, ).text
    soup = BeautifulSoup(html, 'lxml')

    # Ad results
    # Expanded ads
    for expanded_ad in soup.select('.mt-16'):
      title = expanded_ad.select_one('.lh-1_2x').text
      snippet = expanded_ad.select_one('.tc p').text
      ad_link_expanded = expanded_ad.select_one('.lh-1_2x')['href']

      # print(f'{title}\n{snippet}\n{ad_link_expanded}\n')

    # Inline ads
    # There're will be "Cached" word that needs to be filtered.
    for inline_ad in soup.select('#main .txt a'):
      title = inline_ad.text
      link = inline_ad['href']
      print(f'{title}\n{link}\n')

    # # Orgrahic Results
    # for result in soup.find_all('div', class_='layoutMiddle'):
    #   title = result.find('h3', class_='title tc d-ib w-100p').text
    #   link = result.find('h3', class_='title tc d-ib w-100p').a['href']
    #   displayed_link = result.select_one('.compTitle div').text
    #   snippet = result.find('div',class_='compText aAbs').text

    #   print(f'{title}\n{link}\n{displayed_link}\n{snippet}\n')
