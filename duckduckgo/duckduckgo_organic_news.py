from selenium import webdriver
import urllib.parse, re

driver = webdriver.Chrome(executable_path='C:/Users/dimit/PycharmProjects/pythonProject/Scrape Search Engines/Walmart/chromedriver.exe')
driver.get('https://duckduckgo.com/?q=elon musk&kl=us-en&ia=web')

for result in driver.find_elements_by_css_selector('#m1-0 .has-image'):
    title = result.find_element_by_css_selector('#m1-0 .js-carousel-item-title').text.strip()
    link = result.find_element_by_css_selector('#m1-0 .js-carousel-item-title').get_attribute('href')
    source = result.find_element_by_css_selector('#m1-0 .result__url').text
    date = result.find_element_by_css_selector('#m1-0 .tile__time').text
    thumbnail_encoded = result.find_element_by_css_selector('#m1-0 .module--carousel__image').get_attribute('style')

    # https://regex101.com/r/98r2qW/1
    match_thumbnail_urls = ''.join(re.findall(r'background-image: url\(\"\/\/external-content\.duckduckgo\.com\/iu\/\?u=(.*)&f=1&h=110\"\);', thumbnail_encoded))

    # https://www.kite.com/python/answers/how-to-decode-a-utf-8-url-in-python
    thumbnail = urllib.parse.unquote(match_thumbnail_urls)
    print(f'{title}\n{link}\n{source}\n{date}\n{thumbnail}\n')