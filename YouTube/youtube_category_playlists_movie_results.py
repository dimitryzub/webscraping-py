import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_video_paylist_results():
    options = Options()
    # running selenium in headless mode
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.youtube.com/results?search_query=dnb playlist')

    youtube_playlist = []

    for result in driver.find_elements_by_xpath('//*[@id="contents"]/ytd-playlist-renderer'):
        playlist_title = result.find_element_by_css_selector('#video-title').text
        playlist_link = result.find_element_by_css_selector('.style-scope ytd-playlist-renderer a').get_attribute('href')
        channel_name = result.find_element_by_css_selector('#channel-name').text
        video_count = result.find_element_by_css_selector('#overlays > ytd-thumbnail-overlay-side-panel-renderer > yt-formatted-string').text

        youtube_playlist.append({
            'title': playlist_title,
            'link': playlist_link,
            'count': video_count,
            'channel': channel_name,
        })

    print(json.dumps(youtube_playlist, indent=2, ensure_ascii=False))


get_video_paylist_results()

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_movie_results():
    options = Options()
    # running selenium in headless mode
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.youtube.com/results?search_query=mortal kombat 2021 movie')

    for result in driver.find_elements_by_xpath('//*[@id="contents"]/ytd-movie-renderer'):
        title = result.find_element_by_xpath('//*[@id="video-title"]').text
        link = result.find_element_by_xpath('//*[@id="video-title"]').get_attribute('href')
        movie_info = result.find_element_by_xpath('//*[@id="contents"]/ytd-movie-renderer/div[2]/ul[1]/li').text
        desc = result.find_element_by_xpath('//*[@id="description-text"]').text
        additional_desc = result.find_element_by_xpath('//*[@id="contents"]/ytd-movie-renderer/div[2]/ul[2]').text
        channel_name = result.find_element_by_xpath('//*[@id="text"]/a').text
        channel_link = result.find_element_by_xpath('//*[@id="text"]/a').get_attribute('href')
        print(f'{title}\n{link}\n{movie_info}\n{desc}\n{additional_desc}\n{channel_name}\n{channel_link}\n')

get_movie_results()


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_category_results():
    options = Options()
    # running selenium in headless mode
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.youtube.com/results?search_query=mojang')

    for result in driver.find_elements_by_css_selector('#contents > ytd-vertical-list-renderer'):
        title = result.find_element_by_css_selector('#video-title > yt-formatted-string').text
        link = result.find_element_by_css_selector('#video-title').get_attribute('href')
        views = result.find_element_by_css_selector('#metadata-line > span:nth-child(1)').text
        date_posted = result.find_element_by_css_selector('#metadata-line > span:nth-child(2)').text
        snippet = result.find_element_by_css_selector('#dismissible > div > div.metadata-snippet-container.style-scope.ytd-video-renderer > yt-formatted-string').text
        channel_name = result.find_element_by_css_selector('.long-byline').text
        channel_link = result.find_element_by_css_selector('#text > a').get_attribute('href')
        try:
            badges = result.find_element_by_css_selector('#badges').text
        except:
            badges = None
        print(f'{title}\n{link}\n{views}\n{date_posted}\n{snippet}\n{channel_name}\n{channel_link}\n{badges}\n')

get_category_results()


# https://serpapi.com/
from serpapi import GoogleSearch

def get_video_paylist_results():
  params = {
    "api_key": "YOUR_API_KEY",
    "engine": "youtube",
    "search_query": "dnb playlist"
  }

  search = GoogleSearch(params)
  results = search.get_dict()

  for result in results['playlist_results']:
      playlist_title = result['title']
      playlist_link = result['link']
      videos_count = result['video_count']
      playlist_videos = result['videos']
      print(f'{playlist_title}\n{playlist_link}\n{videos_count}\n{playlist_videos}')