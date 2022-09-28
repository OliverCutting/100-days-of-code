from bs4 import BeautifulSoup
import requests
import re

class Soup():

  def __init__(self):
    url = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15",
        "Accept-Language": "en-US"
    }
    response = requests.get(url, headers=headers)
    page = response.text
    self.soup = BeautifulSoup(page, 'html.parser')

  def get_addresses(self):
    addresses = []
    cards = self.soup.select('li article div div a')
    for card in cards:
      addresses.append(card.get_text())
    addresses = list(filter(None, addresses))
    return addresses

  def get_links(self):
    links = []
    cards = self.soup.select('li article div div a')
    for card in cards:
      links.append(card['href'])

    for link in links:
      if link[0] == '/':
        links[links.index(link)] = 'https://www.zillow.com' + link

    links = list(dict.fromkeys(links))
    return links

  def get_costs(self):
    costs = []
    costs = [item.get_text()[0:6] for item in self.soup.find_all('span', attrs={'data-test' : True})]
    return costs
