from bs4 import BeautifulSoup
import requests, lxml

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

html = requests.get('https://www.bing.com/search?q=lion king&hl=en', headers=headers).text
soup = BeautifulSoup(html, 'lxml')

for result in soup.select('.b_algo'):
    try:
        title = result.select_one('.b_algo h2 a').text
    except:
        title = None

    try:
        link = result.select_one('.b_algo h2 a')['href']
    except:
        link = None

    try:
        displayed_link = result.select_one('.b_caption cite').text
    except:
        displayed_link = None

    try:
        snippet = result.select_one('#b_results p').text
    except:
        snippet = None

    try:
        for inline in result.select('.sa_uc a'):
            inline_title = inline.text
            inline_link = inline['href']
            print(f'{inline_title}\n{inline_link}')
    except:
        inline_title = None
        inline_link = None

    print(f'\n{title}\n{link}\n{displayed_link}\n{snippet}\n')

# part of the output:
'''
# inline links
Full Cast and Crew
https://www.imdb.com/title/tt6105098/fullcredits
Plot Summary
https://www.imdb.com/title/tt6105098/plotsummary

# organic results
The Lion King (2019) - IMDb
https://www.imdb.com/title/tt6105098/
https://www.imdb.com/title/tt6105098
12/07/2019 · Directed by Jon Favreau. With Donald Glover, Beyoncé, Seth Rogen, Chiwetel Ejiofor. After the murder of his father, a young lion prince flees his kingdom only to learn the true meaning of responsibility and bravery.
Full Cast and Crew
https://www.imdb.com/title/tt6105098/fullcredits
'''