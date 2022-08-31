import requests, os, json
from parsel import Selector  # https://parsel.readthedocs.io/
from serpapi import NaverSearch


def parsel_naver_related_results():
    # https://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls
    params = {
        "query": "minecraft",  # search query
        "where": "web"         # web results. works with nexearch as well
    }

    # https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36",
    }

    # make a request
    html = requests.get("https://search.naver.com/search.naver", params=params, headers=headers, timeout=30)
    
    # process a returned HTML
    selector = Selector(html.text)

    # where temporary data will be stored
    related_results = []

    # https://www.programiz.com/python-programming/methods/built-in/enumerate
    for index, related_result in enumerate(selector.css(".related_srch .keyword"), start=1):
        keyword = related_result.css(".tit::text").get().strip()
        link = f'https://search.naver.com/search.naver{related_result.css("a::attr(href)").get()}'

        related_results.append({
            "position": index,    # 1,2,3..
            "title": keyword,
            "link": link
        })


    print(json.dumps(related_results, indent=2, ensure_ascii=False))

parsel_naver_related_results()

def serpapi_naver_related_results():
    params = {
        # https://docs.python.org/3/library/os.html#os.getenv
        "api_key": os.getenv("API_KEY"),  # your serpapi api key
        "engine": "naver",                # search engine to parse results from
        "query": "minecraft",             # search query
        "where": "web"                    # web results
    }

    search = NaverSearch(params)          # where data extraction happens
    results = search.get_dict()           # JSON -> Python dictionary

    related_results = []

    for related_result in results["related_results"]:
        related_results.append({
            "position": related_result["position"],
            "title": related_result["title"],
            "link": related_result["link"]
        })

    print(json.dumps(related_results, indent=2, ensure_ascii=False))
