from selenium import webdriver
import time


def get_people_also_ask():

    driver = webdriver.Chrome()
    driver.get("https://search.yahoo.com/search?p=playstation 5")

    # Just to print titles
    # for result in driver.find_elements_by_css_selector(".bingrelqa"):
    #     print(result.text)

    # Buffer for page to load. 
    time.sleep(1)
    # Clicks on every arrow
    for arrow_down in driver.find_elements_by_css_selector(".outl-no"):
        # Arrow click
        arrow_down.click()
        # Waits for 1 sec until next click
        time.sleep(1)

    # Container that pops up after clicked on every drop-down arrow
    for container in driver.find_elements_by_css_selector('#web .mt-0'):
        question = container.find_element_by_css_selector('.lh-17.va-top').text
        snippet = container.find_element_by_css_selector('#web .d-b').text
        reference_link = container.find_element_by_css_selector('.pt-10 a').get_attribute('href')
        more_results_link = container.find_element_by_css_selector('.fz-s a').get_attribute('href')

        print(f'{question}\n{snippet}\n{reference_link}\n{more_results_link}\n')
    driver.quit()
