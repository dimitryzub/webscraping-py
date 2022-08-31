from bs4 import BeautifulSoup
import requests, lxml, json

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; HD1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 EdgA/46.1.2.5140"
}

params = {
    "q": "minecraft",
    "t": "web"
}

html = requests.get("https://www.qwant.com/", params=params, headers=headers, timeout=20)
soup = BeautifulSoup(html.text, "lxml")


def scrape_organic_results():

    organic_results_data = []

    for index, result in enumerate(soup.select("[data-testid=webResult]"), start=1):
        title = result.select_one(".WebResult-module__title___MOBFg").text
        link = result.select_one(".Stack-module__VerticalStack___2NDle.Stack-module__Spacexxs___3wU9G a")["href"]
        snippet = result.select_one(".Box-module__marginTopxxs___RMB_d").text

        try:
            displayed_link = result.select_one(".WebResult-module__permalink___MJGeh").text
            favicon = result.select_one(".WebResult-module__iconBox___3DAv5 img")["src"]
        except:
            displayed_link = None
            favicon = None

        organic_results_data.append({
            "position": index,
            "title": title,
            "link": link,
            "displayed_link": displayed_link,
            "snippet": snippet,
            "favicon": favicon
        })

    print(json.dumps(organic_results_data, indent=2))


def scrape_ad_results():

    ad_results_data = []

    for index, ad_result in enumerate(soup.select("[data-testid=adResult]"), start=1):
        ad_position = index + 1
        ad_title = ad_result.select_one(".WebResult-module__title___MOBFg").text
        ad_link = ad_result.select_one(".Stack-module__VerticalStack___2NDle a")["href"]
        ad_displayed_link = ad_result.select_one(".WebResult-module__domain___1LJmo").text
        ad_snippet = ad_result.select_one(".Box-module__marginTopxxs___RMB_d").text
        ad_favicon = ad_result.select_one(".WebResult-module__iconBox___3DAv5 img")["src"]

        ad_results_data.append({
            "ad_position": index,
            "ad_title": ad_title,
            "ad_link": ad_link,
            "ad_displayed_link": ad_displayed_link,
            "ad_snippet": ad_snippet,
            "ad_favicon": ad_favicon
        })

    print(json.dumps(ad_results_data, indent=2))