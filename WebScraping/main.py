from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
article_tag = soup.find_all(name="a", class_='titlelink')
article_upvotes = soup.find_all(name='span', class_='score')
names = [x for x in article_tag]
votes = [x.get_text() for x in article_upvotes]

tagnvotes = dict(zip(names, votes))

for k, v in tagnvotes.items():
    print(f"{k.get_text()} : {v} : {k['href']}")
