# more on replit: https://replit.com/@DimitryZub1/Scrape-Yahoo-Finance-Home-Page-with-Python#main.py

import requests, lxml, json, re, datetime
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                  "(KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

html = requests.get('https://finance.yahoo.com/', headers=headers)
soup = BeautifulSoup(html.text, 'lxml')

all_script_tags = soup.select('script')

# https://regex101.com/r/IJloEU/2
matched_string = ''.join(re.findall(r'root\.App\.main = (.*);\n+}\(this\)\);\n+</script>', str(all_script_tags)))
matched_string_json = json.loads(matched_string)


def yahoo_get_header_stock_data():
    for key, value in dict(matched_string_json['context']['dispatcher']['stores']['StreamDataStore']['quoteData']).items():
        symbol = value['symbol']
        exchange = value['exchange']
        full_exchange_name = value['fullExchangeName']

        try:
            short_name = value['shortName']
        except:
            short_name = 'no shorten name'

        exchange_time_zone_name = value['exchangeTimezoneName']
        regular_market_change = value['regularMarketChange']['fmt']
        regular_market_previous_close = value['regularMarketPreviousClose']['fmt']
        regular_market_price = value['regularMarketPrice']['fmt']
        regular_market_change_percent = value['regularMarketChangePercent']['fmt']
        market_state = value['marketState']
        market = value['market']
        quote_type = value['quoteType']


        print(f'Symbol: {symbol}\n'
              f'Short name: {short_name}\n'
              f'Exchange: {exchange}\n'
              f'Full exchange name: {full_exchange_name}\n'
              f'Exchange timezone: {exchange_time_zone_name}\n'
              f'Market state: {market_state}\n'
              f'Market name: {market}\n'
              f'Quote type: {quote_type}\n'
              f'Market price: {regular_market_price}\n'
              f'Market change: {regular_market_change}\n'
              f'Market % change: {regular_market_change_percent}\n'
              f'Market previous close: {regular_market_previous_close}\n')



def yahoo_get_top_news_data():
    matched_string_json_stream = matched_string_json['context']['dispatcher']['stores']['ThreeAmigosStore']['data']['ntk']['stream']

    for top_news_result_index, top_news in enumerate(matched_string_json_stream):
        teaser = top_news['editorialContent']['teaser']
        title = top_news['editorialContent']['title']

        try:
            source = top_news['editorialContent']['content']['provider']['displayName']
        except:
            source = None

        try:
            source_site_link = top_news['editorialContent']['content']['provider']['url']
        except:
            source_site_link = None

        try:
            canonical_url = top_news['editorialContent']['content']['canonicalUrl']['url']
        except:
            canonical_url = None

        try:
            canonical_url_website = top_news['editorialContent']['content']['canonicalUrl']['site']
        except:
            canonical_url_website = None

        try:
            click_through_url = top_news['editorialContent']['content']['clickThroughUrl']['url']
        except:
            click_through_url = None

        try:
            click_through_url_website = top_news['editorialContent']['content']['clickThroughUrl']['site']
        except:
            click_through_url_website = None


        print(f'News result number: {top_news_result_index}\n'
              f'Teaser: {teaser}\n'
              f'Title: {title}\n'
              f'Source: {source}\n'
              f'Source website: {source_site_link}\n'
              f'Canonical URL: {canonical_url}\n'
              f'Canonical URL source: {canonical_url_website}\n'
              f'Click through URL: {click_through_url}\n'
              f'Click through website: {click_through_url_website}\n')

        for resolution in top_news['editorialContent']['thumbnail']['resolutions']:
            thumbnail_size = resolution['tag']
            thumbnail_link = resolution['url']
            print(f'{thumbnail_size} {thumbnail_link}')


def yahoo_get_top_news_video_results():
    matched_string_json_video = matched_string_json['context']['dispatcher']['stores']['ThreeAmigosStore']['data']['videos']['stream']

    for top_news_video_index, top_news_video in enumerate(matched_string_json_video):
        video_title = top_news_video['content']['title']
        video_summary = top_news_video['content']['summary']
        video_duration_not_fixed = top_news_video['content']['duration']

        # seconds converted to minutes
        video_duration_fixed_time = datetime.timedelta(seconds=video_duration_not_fixed)
        video_publication_date = top_news_video['content']['pubDate']
        vide_provider_name = top_news_video['content']['provider']['displayName']
        video_canonical_url = top_news_video['content']['canonicalUrl']['url']
        video_click_through_url = top_news_video['content']['clickThroughUrl']['url']

        print(f'Video number: {top_news_video_index}\n'
              f'Title: {video_title}\nSummary: {video_summary}\n'
              f'Duration: {video_duration_fixed_time}\n'
              f'Publication date: {video_publication_date}\n'
              f'Provider: {vide_provider_name}\n'
              f'Canonical URL: {video_canonical_url}\n'
              f'Click through URL: {video_click_through_url}\n')

        for resolution in top_news_video['content']['thumbnail']['resolutions']:
            thumbnail_size = resolution['tag']
            thumbnail_link = resolution['url']
            print(f'{thumbnail_size} {thumbnail_link}')


def yahoo_get_multiuse_news_results():
    matched_string_json_multiuse = matched_string_json['context']['dispatcher']['stores']['ThreeAmigosStore']['data']['multiuse']['stream']

    for multiuse_index, multiuse_news in enumerate(matched_string_json_multiuse):

        multiuse_title = multiuse_news['content']['title']
        multiuse_content_type = multiuse_news['content']['contentType']
        multiuse_summary = multiuse_news['content']['summary']
        multiuse_provider_name = multiuse_news['content']['provider']['displayName']
        multiuse_provider_url = multiuse_news['content']['provider']['url']
        multiuse_canonical_url = multiuse_news['content']['canonicalUrl']['url']
        multiuse_click_through_url = multiuse_news['content']['clickThroughUrl']['url']
        
        print(f'Multiuse news number: {multiuse_index}\n'
              f'Title: {multiuse_title}\n'
              f'Content type: {multiuse_content_type}\n'
              f'Summary: {multiuse_summary}\n'
              f'Provider: {multiuse_provider_name}\n'
              f'Provider URL: {multiuse_provider_url}\n'
              f'Canonical URL: {multiuse_canonical_url}\n'
              f'Click through URL: {multiuse_click_through_url}\n')

        for resolution in multiuse_news['content']['thumbnail']['resolutions']:
            thumbnail_size = resolution['tag']
            thumbnail_link = resolution['url']
            print(f'{thumbnail_size} {thumbnail_link}')


def yahoo_get_news_results():
    for yahoo_news_index in matched_string_json['context']['dispatcher']['stores']['StreamStore']['streams']['mega.c']['data']['stream_items']:
        title = yahoo_news_index['title']
        summary = yahoo_news_index['summary']
        news_property = yahoo_news_index['property']
        source = yahoo_news_index['publisher']
        original_publication_url = yahoo_news_index['url']
        yahoo_url = f"https://finance.yahoo.com{yahoo_news_index['link']}"

        try:
            thumbnail_medium = yahoo_news_index['images']['img:440x246']['url']
        except:
            thumbnail_medium = None

        try:
            thumbnail_small = yahoo_news_index['images']['img:220x123']['url']
        except:
            thumbnail_small = None

        print(f'Title: {title}\n'
              f'Summary: {summary}\n'
              f'Property: {news_property}\n'
              f'Source: {source}\n'
              f'Original URL: {original_publication_url}\n'
              f'Yahoo URL: {yahoo_url}\n'
              f'Medium thumbnail: {thumbnail_medium}\n'
              f'Small thumbnail: {thumbnail_small}\n')