import json

from scrape_handler.crc_handler import CRCHandler
from scrape_handler.wiggle_handler import WiggleHandler
from scrape_handler.simplebikestore_handler import SimpleBikeStoreHandler


def scrape():
    crc = CRCHandler().scrape()
    wiggle = WiggleHandler().scrape()
    simple_bike_store = SimpleBikeStoreHandler().scrape()

    djs = [*crc, *wiggle, *simple_bike_store]
    djs = sorted(djs, key=lambda bike: float(
        bike.get("price").strip('$€')), reverse=True)

    return djs
