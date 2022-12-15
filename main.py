from scrape_handler.handler import scrape
from db_handler.db_handler import DBHandler
from email_handler.mail import EmailService
from html_handler.html_creator import HTMLCreator


def main():
    bikes_json = scrape()
    notifications = DBHandler().process_data(bikes_json)
    if djs := notifications["djsPriceUpdate"]:
        html = HTMLCreator().create_html(djs)
        EmailService.send_email(subject="DJ Bikes Price Update(s)", html=html)
        print(f"{'*'*25}  DJ UPDATE EMAIL SENT  {'*'*25}")
    if djs := notifications["djsInsert"]:
        html = HTMLCreator().create_html(djs)
        EmailService.send_email(subject="DJ Bikes New Product(s)", html=html)
        print(f"{'*'*25}  DJ INSERT EMAIL SENT  {'*'*25}")


if __name__ == "__main__":
    main()
