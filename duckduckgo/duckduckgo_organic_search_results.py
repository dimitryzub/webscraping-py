from requests_html import HTMLSession

session = HTMLSession()
response = session.get('https://duckduckgo.com/?q=fus+ro+dah&kl=us-en')
response.html.render()

for result in response.html.find('.links_deep'):
    title = result.find('.js-result-title-link', first=True).text
    link = result.find('.result__extras__url', first=True).text
    snippet = result.find('.js-result-snippet', first=True).text
    icon = f"https:{result.find('img.result__icon__img', first=True).attrs['data-src']}"
    print(f'{title}\n{link}\n{snippet}\n{icon}\n')