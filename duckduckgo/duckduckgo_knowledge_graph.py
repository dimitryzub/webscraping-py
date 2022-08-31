from selenium import webdriver

driver = webdriver.Chrome(executable_path='path/to/chromedriver.exe')

# &iax=about - expanded knowledge graph that appears after you click on arrow down icon
driver.get('https://duckduckgo.com/?q=elon musk&kl=us-en&ia=web&iax=about')


title = driver.find_element_by_css_selector('.module__title__link').text

try:
    website = driver.find_element_by_css_selector('.js-about-item-link').text
except:
    website = None

description = driver.find_element_by_css_selector('.js-about-item-abstr').text.strip()
description_link = driver.find_element_by_css_selector('.js-about-item-more-at-inline').get_attribute('href')
thumbnail = driver.find_element_by_css_selector('.module__image img').get_attribute('src')
print(f"{title}\n{website}\n{description}\n{description_link}\n{thumbnail}")

for knowledge_graph_fact in driver.find_elements_by_css_selector('.js-about-module-content .about-info-box__info-row'):
    key_element = knowledge_graph_fact.find_element_by_css_selector('.js-about-module-content .about-info-box__info-label').text.replace(':', '').strip()
    key_value = knowledge_graph_fact.find_element_by_css_selector('.js-about-module-content .about-info-box__info-value').text.strip()
    print(f"{key_element}: {key_value}\n")

for profile in driver.find_elements_by_css_selector('.js-about-profile-link'):
    profile_name = profile.get_attribute('title')
    profile_link = profile.get_attribute('href')
    profile_thumbnail = f"https://duckduckgo.com{profile.find_element_by_css_selector('.js-about-profile-link .about-profiles__img').get_attribute('src')}"
    print(f'{profile_name}\n{profile_link}\n{profile_thumbnail}\n')

driver.quit()
