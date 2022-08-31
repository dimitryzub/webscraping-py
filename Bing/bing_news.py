from bs4 import BeautifulSoup
import requests, lxml

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

html = requests.get('https://www.bing.com/news/search?q=faze+clan', headers=headers)
soup = BeautifulSoup(html.text, 'lxml')

for result in soup.select('.card-with-cluster'):
    title = result.select_one('.title').text
    link = result.select_one('.title')['href']
    snippet = result.select_one('.snippet').text
    source = result.select_one('.source a').text
    date_posted = result.select_one('#algocore span+ span').text
    print(f'{title}\n{link}\n{source}\n{date_posted}\n{snippet}\n')

# part of the output:
'''
FaZe Clan shows off new execute for Mirage against Furia Esports
https://win.gg/news/8521/faze-clan-shows-off-new-execute-for-mirage-against-furia-esports
WIN.gg
2h
During a match against Team Furia in the Gamers Without Borders Cup, the camera spotted an interesting interaction between ...
'''