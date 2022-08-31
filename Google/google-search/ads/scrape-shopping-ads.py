from parsel import Selector
import requests, json

# https://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls
params = {
    "q": "graphics card buy",
    "hl": "en",
    "gl": "us"
}

# https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
}

html = requests.get("https://www.google.com/search", params=params, headers=headers, timeout=30)
selector = Selector(html.text)

data = []

# if top block shopping ads appears
if selector.css(".commercial-unit-desktop-top").get():
    for index, shopping_ad in enumerate(selector.css(".mnr-c.pla-unit"), start=1):
        title = shopping_ad.css(".pymv4e::text").get()
        link = shopping_ad.css(".pla-unit-title-link::attr(href)").get()
        price = shopping_ad.css(".e10twf::text").get()
        source = shopping_ad.css(".LbUacb .zPEcBd::text").get()

        data.append({
            "position": index,
            "block_position": "top_block",
            "title": title,
            "link": link,
            "price": price,
            "source": source
            })

# if right block shopping ads appears
elif selector.css(".commercial-unit-desktop-rhs").get():
    for index, shopping_ad in enumerate(selector.css(".mnr-c.pla-unit"), start=1):
        title = shopping_ad.css(".pymv4e::text").get()
        link = shopping_ad.css(".pla-unit-title-link::attr(href)").get()
        price = shopping_ad.css(".e10twf::text").get()
        source = shopping_ad.css(".LbUacb::text, .zPEcBd::text").get()

        data.append({
            "position": index,
            "block_position": "right_block",
            "title": title,
            "link": link,
            "price": price,
            "source": source
            })

print(json.dumps(data, indent=2, ensure_ascii=False))

"""
Top block:
[
  {
    "position": "top_block",
    "title": "Відеокарта Gigabyte GeForce RTX 3080 Ti Gaming OC 12288MB (GV-N308TGAMING OC-12GD)",
    "link": "https://telemart.ua/ua/products/gigabyte-geforce-rtx-3080-ti-gaming-oc-12288mb-gv-n308tgaming-oc-12gd/",
    "price": "UAH 61,999.00",
    "source": "telemart.ua"
  }, ... other results
  {
    "position": "top_block",
    "title": "Gigabyte GeForce RTX 3080 VISION OC 10G (rev. 2.0) NVIDIA 10 GB GDDR6X",
    "link": "https://www.grooves.land/gigabyte-geforce-rtx-3080-vision-10g-rev-grafikkarten-rtx-3080-gddr6x-pcie-x16-hdmi-displayport-gigabyte-hardware-electronic-pZZa1-2100509896.html?language=en&currency=EUR&_z=ua",
    "price": "UAH 38,359.03",
    "source": "Grooves.Land"
  }
]

---------------
Right block:
[
  {
    "position": "right_block",
    "title": "MSI GeForce RTX 2060 Ventus 12G OC NVIDIA 12 GB GDDR6",
    "link": "https://www.grooves.land/msi-geforce-rtx-2060-ventus-12gb-grafikkarte-msi-hardware-electronic-pZZa1-2100485027.html?language=en&currency=EUR&_z=ua",
    "price": "UAH 16,210.82",
    "source": "Grooves.Land"
  }, ... other results
 {
    "position": "right_block",
    "title": "RTX 3060Ti 8GB MSI VENTUS 2X 8G OCV1 LHR Hardware/Electronic",
    "link": "https://www.grooves.land/msi-geforce-rtx-3060-ventus-ocv1-lhr-grafikkarten-rtx-3060-gddr6-pcie-hdmi-displayport-msi-hardware-electronic-pZZa1-2100386549.html?language=en&currency=EUR&_z=ua",
    "price": "UAH 20,997.98",
    "source": "Grooves.Land"
  }
]
"""