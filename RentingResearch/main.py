from soup import Soup
from research import Research

soup = Soup()

addresses = soup.get_addresses()
costs = soup.get_costs()
links = soup.get_links()

research = Research()

research.input(addresses, links, costs)