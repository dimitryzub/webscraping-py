from bs4 import BeautifulSoup
import requests, lxml

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

params = {
    "q": "somebody toucha my spaghet",
    "cc": "us" # language/country of the search
}

html = requests.get('https://www.bing.com/videos/search', params=params, headers=headers)
soup = BeautifulSoup(html.text, 'lxml')

for result in soup.select('.mc_vtvc.b_canvas'):
    title = result.select_one('.b_promtxt').text
    link = f"https://www.bing.com{result.select_one('.mc_vtvc_link')['href']}"
    views = result.select_one('.mc_vtvc_meta_row:nth-child(1) span:nth-child(1)').text
    date = result.select_one('.mc_vtvc_meta_row:nth-child(1) span+ span').text
    video_platform = result.select_one('.mc_vtvc_meta_row+ .mc_vtvc_meta_row span:nth-child(1)').text
    channel_name = result.select_one('.mc_vtvc_meta_row_channel').text
    print(f'{title}\n{link}\n{channel_name}\n{video_platform}\n{date}\n{views}\n')

'''
THE THREE BEARS (1939)
https://www.bing.comhttps://www.bilibili.com/video/av18046604/
fibration
bilibili
Jan 7, 2018
566 views

SOMEBODY TOUCHA MY SPAGHET - Harmonised
https://www.bing.com/videos/search?q=somebody+toucha+my+spaghet&&view=detail&mid=A98F1E15564EFBCDA08EA98F1E15564EFBCDA08E&&FORM=VRDGAR
Mirron
YouTube
Jun 16, 2020
12K views
...
'''