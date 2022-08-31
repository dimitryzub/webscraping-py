import requests, lxml, re, json
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

# phone extracting works with different countries, languages
params = {
    "q": "mcdonalds",
    "gl": "jp",
    "hl": "ja", # japanese
}

response = requests.get("https://www.google.com/search", headers=headers, params=params)
soup = BeautifulSoup(response.text, 'lxml')

local_results = []

for result in soup.select('.VkpGBb'):
    title = result.select_one('.dbg0pd span').text
    try:
        website = result.select_one('.yYlJEf.L48Cpd')['href']
    except:
        website = None

    try:
        directions = f"https://www.google.com{result.select_one('.yYlJEf.VByer')['data-url']}"
    except:
        directions = None
        
    address_not_fixed = result.select_one('.lqhpac div').text
    # removes phone number from "address_not_fixed" variable
    # https://regex101.com/r/cwLdY8/1
    address = re.sub(r' · ?.*', '', address_not_fixed)
    phone = ''.join(re.findall(r' · ?(.*)', address_not_fixed))
    
    try:
        hours = result.select_one('.dXnVAb').previous_element
    except:
        hours = None

    try:
        options = result.select_one('.dXnVAb').text.split('·')
    except:
        options = None

    local_results.append({
        'title': title,
        'phone': phone,
        'address': address,
        'hours': hours,
        'options': options,
        'website': website,
        'directions': directions,
    })

print(json.dumps(local_results, indent=2, ensure_ascii=False))