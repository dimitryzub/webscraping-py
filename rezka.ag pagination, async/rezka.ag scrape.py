from bs4 import BeautifulSoup
import grequests
import json
import time

start = time.time()

urls = []
for x in range(1, 61):
    url = f'https://rezka.ag/cartoons/page/{x}'
    urls.append(url)

rq = [grequests.get(link) for link in urls]
rs = grequests.map(rq)

for r in rs:
    soup = BeautifulSoup(r.text, 'lxml')
    container = soup.findAll('div', class_='b-content__inline_item')

    for item in container:
        title = item.find('div', class_='b-content__inline_item-link').a.text
        link = item.find('div', class_='b-content__inline_item-link').a['href']
        year = item.find('div', class_='b-content__inline_item-link').div.text.split(',')[0]
        country = item.find('div', class_='b-content__inline_item-link').div.text.split(',')[1]
        try:
            genre = item.find('div', class_='b-content__inline_item-link').div.text.split(',')[2]
        except:
            genre = 'No Genre'
        thumbnail = item.find('div', class_='b-content__inline_item-cover').a.img['src']

        content = {
            "Title": title,
            "Link": link,
            "Year": year,
            "Country": country,
            "Genre": genre,
            "Thumbnail": thumbnail,
        }

        print(content) 
        time.sleep(0.1) # Slow. Safe buffer, could be lower. Otherwise won't scrape everything. Of course there's some solution to fix it. Learning.
        # print(json.dumps(content, indent = 2, ensure_ascii = False))

end = time.time()
print(f'It took {end - start} seconds to scrape it.')
