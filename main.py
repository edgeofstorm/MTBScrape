import logging
import os

from db_handler.db_handler import DBHandler
from email_handler.mail import EmailService
from html_handler.html_creator import HTMLCreator
from scrape_handler.handler import scrape

path = os.path.abspath(os.getcwd())
logging.basicConfig(filename=f'{path}/scrape.log',
                    format='%(levelname)s:%(asctime)s:%(message)s', level=logging.INFO)


def main():
    try:
        bikes_json = scrape()
        notifications = DBHandler().process_data(bikes_json)
        if djs := notifications["djsPriceUpdate"]:
            html = HTMLCreator().create_html(djs)
            EmailService.send_email(
                subject="DJ Bikes Price Update(s)", html=html)
            logging.info(f"{'*'*25}  DJ UPDATE EMAIL SENT  {'*'*25}")
        if djs := notifications["djsInsert"]:
            html = HTMLCreator().create_html(djs)
            EmailService.send_email(
                subject="DJ Bikes New Product(s)", html=html)
            logging.info(f"{'*'*25}  DJ INSERT EMAIL SENT  {'*'*25}")
        if djs := notifications["djsStockUpdate"]:
            html = HTMLCreator().create_html(djs)
            EmailService.send_email(
                subject="DJ Bikes Stock Update", html=html)
            logging.info(f"{'*'*25}  DJ STOCK EMAIL SENT  {'*'*25}")

    except Exception as e:
        logging.error("Exception occured", exc_info=True)
    else:
        logging.info("Script ran successfully")


if __name__ == "__main__":
    main()
