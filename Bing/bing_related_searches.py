from bs4 import BeautifulSoup
import requests, lxml

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

html = requests.get('https://www.bing.com/search?q=lion king&hl=en', headers=headers)
soup = BeautifulSoup(html.content, 'lxml')

for related_search in soup.select('.b_rs ul li'):
    title = related_search.text
    link = f"https://www.bing.com{related_search.a['href']}"
    print(f'{title}\n{link}')

# part of the output:
'''
lion
https://www.bing.com/search?q=lion&FORM=QSRE1
jeremy irons
https://www.bing.com/search?q=jeremy+irons&FORM=QSRE2
'''