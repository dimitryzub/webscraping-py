import requests, json
from bs4 import BeautifulSoup

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    "(KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}


response = requests.get("https://serpapi.com/searches/00664d3f0c817ad7/60df062e797ac6552141b3d4.html", headers=headers)
soup = BeautifulSoup(response.text, 'lxml')

events_data = []

for event in soup.select('.PaEvOc'):
    title = event.select_one('.YOGjf').text
    link = event.select_one('.odIJnf a')['href']
    date_day = event.select_one('.gsrt.v14Sh.OaCVOb .UIaQzd').text
    date_month = event.select_one('.gsrt.v14Sh.OaCVOb .wsnHcb').text
    when = event.select_one('.cEZxRc:nth-child(1)').text
    address_street = event.select_one('.cEZxRc:nth-child(2)').text
    address_city = event.select_one('.cEZxRc:nth-child(3)').text

    events_data.append({
        'title': title,
        'link': link,
        'date': {'start_date': f'{date_day} ' + date_month, 'when': when},
        'address': f'{address_street} - {address_city}',
    })

    print(json.dumps(events_data, indent=2, ensure_ascii=False))