from abc import ABC, abstractclassmethod


class ScrapeHandler(ABC):

    @abstractclassmethod
    def scrape():
        pass

    @abstractclassmethod
    def export_json():
        pass