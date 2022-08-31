from bs4 import BeautifulSoup
import requests, lxml, json

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

html = requests.get('https://www.bing.com/search?q=sf lunch&hl=en', headers=headers)
soup = BeautifulSoup(html.text, 'lxml')

local_map_results = []

for result in soup.select('.b_scard.b_scardf.b_scardh'):
    place_id = result.div.div['data-ypid']
    title = result.select_one('.lc_content h2').text
    rating = result.select_one('.csrc.sc_rc1')['aria-label'].split(' ')[1]
    reviews = result.select_one('.b_factrow a').text.split(' ')[1].replace('(', '').replace(')', '')
    reviews_link = result.select_one('.b_factrow a')['href']
    try:
        location = result.select_one('.b_address').text
    except:
        location = None
    try:
        hours = result.select_one('.opHours > span').text
    except:
        hours = None
    directions = f"https://www.bing.com{result.select_one('a.ibs_2btns')['href']}"
    website = result.select_one('.bm_dir_overlay+ .ibs_2btns .ibs_btn').parent['href']
    latitude = json.loads(result.select_one('.bm_dir_overlay')['data-directionoverlay'])['waypoints'][0]['point']['latitude']
    longitude = json.loads(result.select_one('.bm_dir_overlay')['data-directionoverlay'])['waypoints'][0]['point']['longitude']

    local_map_results.append({
        'place_id': place_id,
        'title': title,
        'rating': rating,
        'reviews': reviews,
        'reviews_link': reviews_link,
        'hours': hours,
        'website': website,
        'directions': directions,
        'location': location,
        'latitude': latitude,
        'longitude': longitude,
    })

print(json.dumps(local_map_results, indent = 2, ensure_ascii = False))


# part of the output:
'''
[
  {
    "place_id": "YN114x189818795",
    "title": "Absinthe Brasserie & Bar",
    "rating": "4",
    "reviews": "596",
    "reviews_link": "https://www.tripadvisor.com/Restaurant_Review-g60713-d349444-Reviews-Absinthe_Brasserie_Bar-San_Francisco_California.html?m=17457",
    "hours": "Closed · Opens tomorrow 11 am",
    "website": "http://absinthe.com/",
    "directions": "https://www.bing.com/maps/directions?rtp=adr.~pos.37.7769889831543_-122.42288970947266_398+Hayes+St%2c+San+Francisco%2c+CA+94102_Absinthe+Brasserie+%26+Bar_(415)+551-1590",
    "location": "398 Hayes St, San Francisco, CA 94102",
    "latitude": 37.7769889831543,
    "longitude": -122.42288970947266
  }
]
'''