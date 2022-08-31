import requests, re, json
from parsel import Selector

# https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
headers = {
    "User-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36"
    }

params = {
    "q": "dune actors",  # search query
    "gl": "us",          # country to search from
    }


def parsel_get_top_carousel():
    html = requests.get('https://www.google.com/search', headers=headers, params=params)
    selector = Selector(text=html.text)

    carousel_name = selector.css(".yKMVIe::text").get()
    all_script_tags = selector.css("script::text").getall()

    data = {f"{carousel_name}": []}

    decoded_thumbnails = []

    for _id in selector.css("img.d7ENZc::attr(id)").getall():
        # https://regex101.com/r/YGtoJn/1
        thumbnails = re.findall(r"var\s?s=\'([^']+)\';var\s?ii=\['{_id}'];".format(_id=_id), str(all_script_tags))
        thumbnail = [
            bytes(bytes(img, "ascii").decode("unicode-escape"), "ascii").decode("unicode-escape") for img in thumbnails
            ]
        decoded_thumbnails.append("".join(thumbnail))

    for result, image in zip(selector.css('.QjXCXd.X8kvh'), decoded_thumbnails):

        title = result.css(".JjtOHd::text").get()
        link = f"https://www.google.com{result.css('.QjXCXd div a::attr(href)').get()}"
        extensions = result.css(".ellip.AqEFvb::text").getall()

        if title and link and extensions is not None:
            data[carousel_name].append({
                "title": title,
                "link": link,
                "extensions": extensions,
                "thumbnail": image
                })

    print(json.dumps(data, indent=2, ensure_ascii=False))


parsel_get_top_carousel()