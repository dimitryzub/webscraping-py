from bs4 import BeautifulSoup
import requests, lxml

headers = {
    'User-agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

def get_related_searches():

    html = requests.get('https://search.yahoo.com/search?p=playstation 5',headers=headers, ).text
    soup = BeautifulSoup(html, 'lxml')
    
    # Top related searches
    result = soup.find('ol',class_='cardReg searchTop').text.split(':')[1].split(',')
    top_related_saearches = ''.join(result) # or ''.join(f'{result}\n')
    print('Top searches:')
    print(top_related_saearches)

    # Bottom related searches
    print('Bottom searches:')
    for result in soup.select('.pl-18'):
      print(result.text)
