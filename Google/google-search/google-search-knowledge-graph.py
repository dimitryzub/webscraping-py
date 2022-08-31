from bs4 import BeautifulSoup
import requests, lxml

headers = {
    'User-agent':
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
        "Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}


def get_knowledge_graph():
    html = requests.get('https://www.google.com/search?q=dell&hl=en', headers=headers)
    soup = BeautifulSoup(html.text, 'lxml')

    title = soup.select_one('#rhs .mfMhoc span').text
    subtitle = soup.select_one('.wwUB2c span').text
    try:
        snippet = soup.select_one('.zsYMMe+ span').text
    except:
        snippet = None

    print(f"{title}\n{subtitle}\n{snippet}\n")

    for result in soup.select(".rVusze"):
        key_element = result.select_one(".w8qArf").text
        if result.select_one(".kno-fv"):
            value_element = result.select_one(".kno-fv").text.replace(": ", "")
        else:
            value_element = None
        key_link = f'https://www.google.com{result.select_one(".w8qArf a")["href"]}'
        try:
            key_value_link = f'https://www.google.com{result.select_one(".kno-fv a")["href"]}'
        except:
            key_value_link = None

        print(f"{key_element}{value_element}\nkey_link: {key_link}\nkey_value_link: {key_value_link}")


get_knowledge_graph()