import requests, lxml
from bs4 import BeautifulSoup

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

params = {
    "q": "somebody toucha my spaghet",
    "tbm": "vid",
    "hl": "en" # get english results
}

response = requests.get("https://www.google.com/search", headers=headers, params=params)
soup = BeautifulSoup(response.text, 'lxml')

for results in soup.select('.tF2Cxc'):
    title = results.select_one('.DKV0Md').text
    link = results.a['href']
    displayed_link = results.select_one('.TbwUpd.NJjxre').text
    snippet = results.select_one('.aCOpRe span').text
    uploaded_by = results.select_one('.uo4vr span').text.split(' ')[2]
    upload_date = results.select_one('.fG8Fp.uo4vr').text.split(' · ')[0]
    print(f'{title}\n{link}\n{displayed_link}\n{snippet}\n{upload_date}\n{uploaded_by}\n')