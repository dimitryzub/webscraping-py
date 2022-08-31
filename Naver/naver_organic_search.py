import requests
import lxml, json
from bs4 import BeautifulSoup

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

params = {
    "query": "bruce lee",  # search query
    "where": "web"         # nexearch will produce different results
}


# function that saves HTML locally
def save_naver_organic_results():
    html = requests.get("https://search.naver.com/search.naver", params=params, headers=headers).text

    # replacing every spaces so bruce lee will become bruce_lee 
    query = params['query'].replace(" ", "_")

    with open(f"{query}_naver_organic_results.html", mode="w") as file:
        file.write(html)


# fucntion that opens local HTML and calls a parser function
def extract_naver_organic_results_from_html():
    with open("bruce_lee_naver_organic_results.html", mode="r") as html_file:
        html = html_file.read()

        # calls naver_organic_results_parser() function to parse the page
        data = naver_organic_results_parser(html)

        print(json.dumps(data, indent=2, ensure_ascii=False))


# function that make an actual request and calls a parser function
def extract_naver_organic_results_from_url():
    html = requests.get("https://search.naver.com/search.naver", params=params, headers=headers)

    # calls naver_organic_results_parser() function to parse the page
    data = naver_organic_results_parser(html)

    print(json.dumps(data, indent=2, ensure_ascii=False))


# parser that's being called by 2-3 functions
def naver_organic_results_parser(html):
    soup = BeautifulSoup(html.text, "lxml")

    data = []

    for index, result in enumerate(soup.select(".total_wrap")):
        title = result.select_one(".total_tit").text.strip()
        link = result.select_one(".total_tit .link_tit")["href"]
        displayed_link = result.select_one(".total_source").text.strip()
        snippet = result.select_one(".dsc_txt").text

        data.append({
            "position": index + 1, # starts from 1, not from 0
            "title": title,
            "link": link,
            "displayed_link": displayed_link,
            "snippet": snippet
        })

    return data