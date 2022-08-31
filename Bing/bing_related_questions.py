from bs4 import BeautifulSoup
import requests, lxml

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

html = requests.get('https://www.bing.com/search?q=lion king&hl=en', headers=headers)
soup = BeautifulSoup(html.content, 'lxml')

for related_question in soup.select('#relatedQnAListDisplay .df_topAlAs'):
    question = related_question.select_one('.b_1linetrunc').text
    snippet = related_question.select_one('.rwrl_padref').text
    title = related_question.select_one('#relatedQnAListDisplay .b_algo p').text
    link = related_question.select_one('#relatedQnAListDisplay .b_algo a')['href']
    displayed_link = related_question.select_one('#relatedQnAListDisplay cite').text
    print(f'{question}\n{snippet}\n{title}\n{link}\n{displayed_link}\n')

# part of the output:
'''
What kind of game is The Lion King?
Jump on top of giraffe’s head and eat bugs in this awesome classic platformer game. The Lion King is a classic 1994 platformer video game based on the multi-award winning animated film of the same name. The game takes place after the death of Simba’s father where Simba was told a lie and forced to hide.
The Lion King - Play Game Online - ArcadeSpot.com
https://arcadespot.com/game/the-lion-king/
arcadespot.com/game/the-lion-king/
'''