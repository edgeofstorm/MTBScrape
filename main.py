import logging
import os

from db_handler.db_handler import DBHandler
from email_handler.mail import EmailService
from html_handler.html_creator import HTMLCreator
from scrape_handler.handler import scrape
from custom_logging.formatters import CloudLoggingFormatter


path = os.path.abspath(os.getcwd())
logger = logging.getLogger()
handler = logging.FileHandler(f'{path}/scrape.log')
formatter = CloudLoggingFormatter(fmt="%(levelname)s:%(asctime)s:%(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


def main():
    try:
        bikes_json = scrape()
        notifications = DBHandler().process_data(bikes_json)
        if djs := notifications["djsPriceUpdate"]:
            html = HTMLCreator().create_html(djs)
            EmailService.send_email(
                subject="DJ Bikes Price Update(s)", html=html)
            logger.info(f"{'*'*25}  DJ UPDATE EMAIL SENT  {'*'*25}")
        if djs := notifications["djsInsert"]:
            html = HTMLCreator().create_html(djs)
            EmailService.send_email(
                subject="DJ Bikes New Product(s)", html=html)
            logger.info(f"{'*'*25}  DJ INSERT EMAIL SENT  {'*'*25}")
    except Exception as e:
        logger.error("Exception occured", exc_info=True)
    else:
        logger.info("Script ran successfully")


if __name__ == "__main__":
    main()
