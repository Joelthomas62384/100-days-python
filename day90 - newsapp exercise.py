import requests


cat = input("Enter the category you want to see : ")
url = f"https://newsapi.org/v2/top-headlines?country=in&category={cat}&apiKey=ca6fc773a58b4952899289d6f522efda"
response = requests.get(url)
js = response.json()

for id , news in enumerate(js.get('articles'),start=1):
    print(f"{id}.  {news.get('title')}",end="\n\n")