import json
import logging
import os

import requests
from bs4 import BeautifulSoup

from .scrape_handler_abc import ScrapeHandler


logger = logging.getLogger()


class SimpleBikeStoreHandler(ScrapeHandler):

    def __init__(self) -> None:
        self.url = "https://www.simplebikestore.eu/en/bikes/mountainbike/dirt-jump/?sort=highest&brand=0&mode=grid&sort=highest&max=6000&min=0&limit=72&sort=highest"
        self.djs = []

    def scrape(self):
        page = requests.get(self.url, verify=False)

        soup = BeautifulSoup(page.content, "html.parser")

        for child in soup.find_all("div", class_="product-block"):
            self.djs.append({
                "bike": f"{child.find('div', class_='product-col-brand').text.strip()} {child.find('a', class_='product-block-title').text.strip()}",
                "discount": child.find('div', class_="product-sale").text.strip()[1:] if child.find('div', class_="product-sale") else None,
                "price": child.find('div', class_="product-block-price").find('span', class_="price-excl bold").text.strip().replace('.', '').replace(',', '.'),
                "url": child.find('a', class_="product-block-title").get('href'),
                "img": (child.find('img').get('src') or child.find('img').get('data-src')).replace(' ', '%20'),
                "store": "SimpleBikeStore"
            })

        if not self.djs:
            logger.warning("Couldn't fetch bikes from SimpleBikeStore")

        return self.djs

    def export_json(self):
        return json.dumps(self.djs)
