from selenium import webdriver

driver = webdriver.Chrome(executable_path='path/to/chromedriver.exe')
driver.get('https://duckduckgo.com/?q=minecraft&kl=us-en&ia=web')

for result in driver.find_elements_by_css_selector('.results--ads .result__body.links_main.links_deep'):
    title = result.find_element_by_css_selector('.js-result-title-link').text
    link = result.find_element_by_css_selector('.js-result-title-link').get_attribute('href')
    source = result.find_element_by_css_selector('.js-result-extras-url').text
    snippet = result.find_element_by_css_selector('.js-result-snippet > a').text
    print(f'{title}\n{source}\n{snippet}\n{link}\n')

for sitelink in driver.find_elements_by_css_selector('.js-sitelinks-title'):
    sitelink_title = sitelink.text
    sitelink_url = sitelink.get_attribute('href')
    print(f'{sitelink_title}\n{sitelink_url}\n')

driver.quit()
