import json
import logging
import os

import requests
from bs4 import BeautifulSoup

from .scrape_handler_abc import ScrapeHandler

path = os.path.abspath(os.getcwd())
logging.basicConfig(filename=f'{path}/scrape.log',
                    format='%(levelname)s:%(asctime)s:%(message)s', level=logging.INFO)


class WiggleHandler(ScrapeHandler):

    def __init__(self) -> None:
        self.url = "https://www.wiggle.co.uk/?s=dirt+jump&o=3&prevDestCountryId=68&curr=EUR&dest=68"
        self.djs = []

    def scrape(self):
        page = requests.get(self.url, verify=False)

        soup = BeautifulSoup(page.content, "html.parser")

        for child in soup.find_all("div", class_="bem-product-list-item--grid"):
            if not "bike" in child.find('a', class_="bem-product-thumb__name--grid").text.strip().lower():
                continue
            self.djs.append({
                "bike": child.find('a', class_="bem-product-thumb__name--grid").text.strip(),
                "discount": child.find('span', class_="bem-product_price__discount").text.split()[1] if child.find('span', class_="bem-product_price__discount") else None,
                "price": child.find('span', class_="bem-product-price__unit--grid").text.strip().replace(',', ''),
                "url": child.find('a', class_="bem-product-thumb__name--grid").get('href'),
                "img": f"https:{child.find('a', class_='bem-product-thumb__image-link--grid').find('img').get('src').replace(' ', '%20')}",
                "store": "Wiggle"
            })

        if not self.djs:
            logging.warning("Couldn't fetch bikes from Wiggle")

        return self.djs

    def export_json(self):
        return json.dumps(self.djs)
