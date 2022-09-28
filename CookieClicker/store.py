import re
from selenium.webdriver.common.by import By


class Store():

    def __init__(self, driver):
        self.items = driver.find_elements(By.CSS_SELECTOR, '.product')
        self.driver = driver

    def item_costs(self):
        available_items = list(filter(None, [item.text for item in self.items]))
        item_costs = [re.sub(',', '', item.split('\n')[1]) for item in available_items]
        for price in item_costs:
            if 'million' in price:
                item_costs[item_costs.index(price)] = int(float(price.split(' ')[0]) * 1000000)
            else:
                item_costs[item_costs.index(price)] = int(price)
        return item_costs

    def purchase_upgrade(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, '#upgrade0.crate.upgrade').click()
        except:
            pass

    def purchase_item(self, current_cookies):
        item_costs = self.item_costs()
        x = 0
        while x + 1 < len(item_costs):
            if item_costs[x] < item_costs[x + 1] / 5 and current_cookies >= item_costs[x]:
                self.items[x].click()
            x += 1

    def make_purchase(self):
        self.purchase_upgrade()
        current_cookies = int(re.sub(',', '', self.driver.find_element('xpath', '//*[@id="cookies"]').text.split(' ')[0]))
        self.purchase_item(current_cookies)
    