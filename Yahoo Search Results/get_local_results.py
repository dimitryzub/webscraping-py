from bs4 import BeautifulSoup
import requests, lxml

headers = {
    'User-agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

def get_local_pack_results():

    html = requests.get('https://search.yahoo.com/search?p=manhattan beach coffee shops',headers=headers, ).text
    soup = BeautifulSoup(html, 'lxml')

    for result in soup.find_all('div', class_='info col'):
      # Deleting numbers e.g. "1. Blabla", "2. best coffee shop", "3. Best PC shop"
      result.find('span', class_='sn fc-26th').decompose()
      # Checks if place is verified or not by checking Green check mark
      if result.select_one('.icon-verified-10-green') is not None:
        print('Verified')
      else:
        print('Not verified')
      title = result.find('div', class_='titlewrapper').text
      title_search_link = result.find('div',class_='titlewrapper').a['href']
      place_type = result.select_one('.meta .bb-child').text
      try:
        price = result.select_one('.lcl-prcrate').text
      except:
        price = None
      reviews = result.select_one('.ml-2').text.split(' ')[0]
      try:
        hours = result.select_one('.isclosed').text
      except:
        hours = None
      address = result.find('span', class_='addr').text
      phone = result.select_one('.hoo .separator+ span').text
      website_link = result.select_one('.imgbox a')['href']

      print(f'{title}\n{title_search_link}\n{place_type}\n{price}\n{reviews}\n{hours}\n{address}\n{phone}\n{website_link}\n')
