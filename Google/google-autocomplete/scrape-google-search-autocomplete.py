import requests, json

headers = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

response = requests.get('http://google.com/complete/search?client=firefox&q=minecraft is the best game', headers = headers)

for result in json.loads(response.text)[1]:
  print(result)
