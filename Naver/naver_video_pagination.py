import requests, json
from parsel import Selector
from playwright.sync_api import sync_playwright


def playwright_scrape_all_naver_videos():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://search.naver.com/search.naver?where=video&query=neo")

        video_results = []

        not_reached_end = True
        while not_reached_end:
            # scroll to the bottom of the page
            page.evaluate("""let scrollingElement = (document.scrollingElement || document.body);
                                 scrollingElement.scrollTop = scrollingElement scrollHeight;""")

            if page.locator("#video_max_display").is_visible():
                not_reached_end = False

        for index, video in enumerate(page.query_selector_all(".video_bx"), start=1):
            title = video.query_selector(".text").inner_text()
            link = video.query_selector(".info_title").get_attribute("href")
            thumbnail = video.query_selector(".thumb_area img").get_attribute("src")
            channel = None if video.query_selector(".channel") is None else video.query_selector(".channel").inner_text()
            origin = video.query_selector(".origin").inner_text()
            video_duration = video.query_selector(".time").inner_text()
            views = video.query_selector(".desc_group .desc:nth-child(1)").inner_text()
            date_published = None if video.query_selector(".desc_group .desc:nth-child(2)") is None else \
                video.query_selector(".desc_group .desc:nth-child(2)").inner_text()

            video_results.append({
                "position": index,
                "title": title,
                "link": link,
                "thumbnail": thumbnail,
                "channel": channel,
                "origin": origin,
                "video_duration": video_duration,
                "views": views,
                "date_published": date_published
            })

        print(json.dumps(video_results, indent=2, ensure_ascii=False))

        browser.close()

# playwright_scrape_all_naver_videos()


def parsel_scrape_all_video_results():
    params = {
        "start": 0,            # page number
        "display": "48",       # videos to display. Hard limit.
        "query": "minecraft",  # search query
        "where": "video",      # Naver videos search engine
        "sort": "rel",         # sorted as you would see in the browser
        "video_more": "1"      # required to receive a JSON data
    }

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    }

    video_results = []

    html = requests.get("https://s.search.naver.com/p/video/search.naver", params=params, headers=headers, timeout=30)
    json_data = json.loads(html.text.replace("( {", "{").replace("]})", "]}"))
    html_data = json_data["aData"]

    while params["start"] <= int(json_data["maxCount"]):
        for result in html_data:
            selector = Selector(result)

            for video in selector.css(".video_bx"):
                title = video.css(".text").xpath("normalize-space()").get().strip()
                link = video.css(".info_title::attr(href)").get()
                thumbnail = video.css(".thumb_area img::attr(src)").get()
                channel = video.css(".channel::text").get()
                origin = video.css(".origin::text").get()
                video_duration = video.css(".time::text").get()
                views = video.css(".desc_group .desc:nth-child(1)::text").get()
                date_published = video.css(".desc_group .desc:nth-child(2)::text").get()

                video_results.append({
                    "title": title,
                    "link": link,
                    "thumbnail": thumbnail,
                    "channel": channel,
                    "origin": origin,
                    "video_duration": video_duration,
                    "views": views,
                    "date_published": date_published
                })

        # 48, 96, 144, 192, 240, 288, 336, 384, 432, 480, 528, 576, 624...1008
        params["start"] += 48
        html = requests.get("https://s.search.naver.com/p/video/search.naver", params=params, headers=headers, timeout=30)
        html_data = json.loads(html.text.replace("( {", "{").replace("]})", "]}"))["aData"]

    print(json.dumps(video_results, indent=2, ensure_ascii=False))


parsel_scrape_all_video_results()