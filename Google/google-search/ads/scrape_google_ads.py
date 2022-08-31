from parsel import Selector
import requests, json

# https://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls
params = {
    "q": "coffee beans buy",
    "hl": "en",
    "gl": "us"
}

# https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36",
}

html = requests.get("https://www.google.com/search", params=params, headers=headers)
selector = Selector(html.text)

ad_results = []

for index, ad_result in enumerate(selector.css(".uEierd"), start=1):
    title = ad_result.css(".v0nnCb span::text").get()
    website_link = ad_result.css("a.sVXRqc::attr(data-pcu)").get()
    ad_link = ad_result.css("a.sVXRqc::attr(href)").get()
    displayed_link = ad_result.css(".qzEoUe::text").get()
    tracking_link = ad_result.css(".v5yQqb a.sVXRqc::attr(data-rw)").get()
    snippet = ad_result.css(".MUxGbd div span").xpath("normalize-space()").get()
    phone = ad_result.css("span.fUamLb span::text").get()

    inline_link_text = None if ad_result.css("div.bOeY0b .XUpIGb a::text").getall() == [] else ad_result.css("div.bOeY0b .XUpIGb a::text").getall()
    inline_link = None if ad_result.css("div.bOeY0b .XUpIGb a::attr(href)").getall() == [] else ad_result.css("div.bOeY0b .XUpIGb a::attr(href)").getall()

    ad_results.append({
        "position": index,
        "title": title,
        "phone": phone,
        "website_link": website_link,
        "displayed_link": displayed_link,
        "ad_link": ad_link,
        "tracking_link": tracking_link,
        "snippet": snippet,
        "sitelinks": [{"titles": inline_link_text, "links": inline_link}]
    })

print(json.dumps(ad_results, indent=2))