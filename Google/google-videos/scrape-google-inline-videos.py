import requests, lxml
from bs4 import BeautifulSoup

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

response = requests.get("https://www.google.com/search?q=the last of us 2 reviews", headers=headers)
soup = BeautifulSoup(response.text, 'lxml')

for result in soup.select('.WpKAof'):
    title = result.select_one('.p5AXld').text
    link = result['href']
    channel = result.select_one('.YnLDzf').text.replace(' · ', '')
    video_platform = result.select_one('.hDeAhf').text
    date = result.select_one('.rjmdhd span').text
    duration = result.select_one('.MyDQSe span').text
    print(f'{title}\n{link}\n{video_platform}\n{channel}\n{date}\n{duration}\n')
