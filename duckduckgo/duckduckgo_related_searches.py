from selenium import webdriver

driver = webdriver.Chrome(executable_path='/path/to/chromedriver.exe')
driver.get('https://duckduckgo.com/?q=fus ro dah&kl=us-en&ia=web')

for result in driver.find_elements_by_css_selector('.result__a.related-searches__link'):
    query = result.text
    link = result.get_attribute('href')
    print(f'{query}\n{link}\n')

driver.quit()