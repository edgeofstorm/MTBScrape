import json
import logging
import os

import requests
from bs4 import BeautifulSoup

from .scrape_handler_abc import ScrapeHandler

path = os.path.abspath(os.getcwd())
logging.basicConfig(filename=f'{path}/scrape.log',
                    format='%(levelname)s:%(asctime)s:%(message)s', level=logging.INFO)


class CRCHandler(ScrapeHandler):

    def __init__(self) -> None:
        self.url = "https://www.chainreactioncycles.com/tr/en/s?q=dirt+jump+bike&sort=pricehigh"
        self.djs = []

    def scrape(self):
        page = requests.get(self.url, verify=False)

        soup = BeautifulSoup(page.content, "html.parser")

        for child in soup.find_all("div", class_="products_details product_details_plp"):
            self.djs.append({
                "bike": child.find('ul').find('h2').text.strip(),
                "discount": child.find('ul').find('span', class_="pixel_separator").text.strip() if child.find('ul').find('span', class_="pixel_separator") else None,
                "price": child.find('ul').find('li', class_="fromamt").text.strip().split('-')[0] if '-' in child.find('ul').find('li', class_="fromamt").text.strip() else child.find('ul').find('li', class_="fromamt").text.strip(),
                "url": f"https://www.chainreactioncycles.com{child.find('ul').find('a').get('href')}",
                "img": child.find("img").get("src").replace(' ', '%20'),
                "stock": False,
                "store": "ChainReactionCycles"
            })

        if not self.djs:
            logging.warning("Couldn't fetch bikes from CRC")
        else:
            # in stock only
            page = requests.get(f"{self.url}&f=2247", verify=False)

            soup = BeautifulSoup(page.content, "html.parser")

            for child in soup.find_all("div", class_="products_details product_details_plp"):
                bike = child.find('ul').find('h2').text.strip()

                if index := next((index for (index, dj) in enumerate(self.djs) if dj["bike"] == bike), None):
                    self.djs[index]["stock"] = True

        return self.djs

    def export_json(self):
        return json.dumps(self.djs)
