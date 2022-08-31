from selenium import webdriver
import re, urllib.parse

driver = webdriver.Chrome(executable_path='path/to/chromedriver.exe')
driver.get('https://duckduckgo.com/?q=elon musk dogecoin&kl=us-en&ia=web')

for result in driver.find_elements_by_css_selector('#m3-0 .has-image'):
    title = result.find_element_by_css_selector('#m3-0 .js-carousel-item-title').text
    link = result.find_element_by_css_selector('#m3-0 .module--carousel__body a').get_attribute('href')

    try:
        views = result.find_element_by_css_selector('#m3-0 .module--carousel__extra-row').text
    except:
        views = None

    try:
        video_duration = result.find_element_by_css_selector('#m3-0 .image-labels__label').text
    except:
        video_duration = None

    date = result.find_element_by_css_selector('#m3-0 .tile__time').text
    platfrom_ = result.find_element_by_css_selector('.module--carousel__gray-text').text
    thumbnail_encoded = result.find_element_by_css_selector('#m3-0 .is-center-image').get_attribute('style')

    # https://regex101.com/r/VjOLjj/1
    match_thumbnail_urls = ''.join(
        re.findall(r'background-image: url\(\"\/\/external-content\.duckduckgo\.com\/iu\/\?u=(.*)&f=1\"\);',
                   thumbnail_encoded))

    # https://www.kite.com/python/answers/how-to-decode-a-utf-8-url-in-python
    thumbnail = urllib.parse.unquote(match_thumbnail_urls)

    print(f'{title}\n{link}\n{platfrom_}\n{views}\n{date}\n{video_duration}\n{thumbnail}\n')

driver.quit()