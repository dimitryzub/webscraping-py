import lxml, json, requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

params = {
    "query": "minecraft",
    "where": "news",
}


# function that parses content from local copy of html
def extract_news_from_html():
    with open("minecraft_naver_news.html", mode="r") as html_file:
        html = html_file.read()

        # calls naver_parser() function to parse the page
        data = naver_parser(html)

        print(json.dumps(data, indent=2, ensure_ascii=False))


# function that makes an actual request
def extract_naver_news_from_url():
    html = requests.get("https://search.naver.com/search.naver", params=params, headers=headers)

    # calls naver_parser() function to parse the page
    data = naver_parser(html)

    print(json.dumps(data, indent=2, ensure_ascii=False))


# parser that accepts html argument from extract_news_from_html() or extract_naver_news_from_url()
def naver_parser(html):
    soup = BeautifulSoup(html.text, "lxml")

    news_data = []

    for news_result in soup.select(".list_news .bx"):
        title = news_result.select_one(".news_tit").text
        link = news_result.select_one(".news_tit")["href"]
        thumbnail = news_result.select_one(".dsc_thumb img")["src"]
        snippet = news_result.select_one(".news_dsc").text

        press_name = news_result.select_one(".info.press").text
        news_date = news_result.select_one("span.info").text

        news_data.append({
            "title": title,
            "link": link,
            "thumbnail": thumbnail,
            "snippet": snippet,
            "press_name": press_name,
            "news_date": news_date
        })
      
    return news_data