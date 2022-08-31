from bs4 import BeautifulSoup
import requests
import lxml

headers = {
  "User-Agent":
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

response = requests.get(
    'https://www.google.com/search?q=london weather',
    headers=headers).text

soup = BeautifulSoup(response, 'lxml')

weather_condition = soup.select_one('#wob_dc').text
tempature = soup.select_one('#wob_tm').text
precipitation = soup.select_one('#wob_pp').text
humidity = soup.select_one('#wob_hm').text
wind = soup.select_one('#wob_ws').text
current_time = soup.select_one('#wob_dts').text

print(f'Weather condition: {weather_condition}\nTempature: {tempature}°F\nPrecipitation: {precipitation}\nHumidity: {humidity}\nWind speed: {wind}\nCurrent time: {current_time}')
