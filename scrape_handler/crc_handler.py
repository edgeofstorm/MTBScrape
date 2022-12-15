import json
import logging

import requests
from bs4 import BeautifulSoup

from .scrape_handler_abc import ScrapeHandler

logging.basicConfig(filename='scrape.log',
                    format='%(levelname)s:%(asctime)s:%(message)s', level=logging.INFO)


class CRCHandler(ScrapeHandler):

    def __init__(self) -> None:
        self.url = "https://www.chainreactioncycles.com/tr/en/s?q=dirt+jump+bike&sort=pricehigh"
        self.djs = []

    def scrape(self):
        page = requests.get(self.url, verify=False)

        soup = BeautifulSoup(page.content, "html.parser")

        print(f"{'*'*25}  CRC DIRT JUMPS BEGIN  {'*'*25}")
        for child in soup.find_all("div", class_="products_details product_details_plp"):
            self.djs.append({
                "bike": child.find('ul').find('h2').text.strip(),
                "discount": child.find('ul').find('span', class_="pixel_separator").text.strip() if child.find('ul').find('span', class_="pixel_separator") else None,
                "price": child.find('ul').find('li', class_="fromamt").text.strip().split('-')[0] if '-' in child.find('ul').find('li', class_="fromamt").text.strip() else child.find('ul').find('li', class_="fromamt").text.strip(),
                "url": f"https://www.chainreactioncycles.com{child.find('ul').find('a').get('href')}",
                "img": child.find("img").get("src").replace(' ', '%20'),
                "store": "ChainReactionCycles"
            })
        print(f"{'*'*25}  CRC DIRT JUMPS END  {'*'*25}")

        if not self.djs:
            logging.warning("Couldn't fetch bikes from CRC")

        return self.djs

    def export_json(self):
        return json.dumps(self.djs)
