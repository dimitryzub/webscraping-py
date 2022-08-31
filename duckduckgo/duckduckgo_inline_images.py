from selenium import webdriver
import re, urllib.parse

driver = webdriver.Chrome(executable_path='path/to/chromedriver.exe')
driver.get('https://duckduckgo.com/?q=elon musk dogecoin&kl=us-en&ia=web')

for result in driver.find_elements_by_css_selector('.js-images-link'):
    title = result.find_element_by_css_selector('.js-images-link a img').get_attribute('alt')
    link = result.find_element_by_css_selector('.js-images-link a').get_attribute('href')
    thumbnail_encoded = result.find_element_by_css_selector('.js-images-link a img').get_attribute('src')

    # https://regex101.com/r/4pgG5m/1
    match_thumbnail_urls = ''.join(re.findall(r'https\:\/\/external\-content\.duckduckgo\.com\/iu\/\?u\=(.*)&f=1', thumbnail_encoded))

    # https://www.kite.com/python/answers/how-to-decode-a-utf-8-url-in-python
    thumbnail = urllib.parse.unquote(match_thumbnail_urls).replace('&h=160', '')
    image = result.get_attribute('data-id')

    print(f'{title}\n{link}\n{thumbnail}\n{image}\n')

driver.quit()