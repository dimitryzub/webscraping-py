from bs4 import BeautifulSoup
import requests, lxml

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

html = requests.get('https://www.bing.com/search?q=john deere tractors buy', headers=headers)
soup = BeautifulSoup(html.text, 'lxml')

try:
    for expanded_ad in soup.select('.deeplink_title'):
        expanded_ad_title = expanded_ad.text
        expanded_ad_displayed_link = expanded_ad.a['href']
        print(f'{expanded_ad_title}\n{expanded_ad_displayed_link}')
except:
    pass

try:
    for inline_ad in soup.select('.b_algo .b_vList.b_divsec .b_annooverride a'):
        inline_ad_title = inline_ad.text
        inline_ad_displayed_link = inline_ad['href']
        print(f'{inline_ad_title}\n{inline_ad_displayed_link}')
except:
    pass


# parts of the output:
'''
# expanded ads
Compact Tractors
https://www.deere.com/en/tractors/compact-tractors/
View The Utility Tractors
https://www.deere.com/en/tractors/utility-tractors/

---------------------------------------------------

# inline ads
2032R
https://www.deere.com/en/tractors/compact-tractors/2-series-compact-tractors/2032r/
1025R
https://www.deere.com/en/tractors/compact-tractors/1-series-sub-compact-tractors/1025r/
'''