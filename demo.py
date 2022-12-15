# todo Create a sqlite db
# each domain has its own table like crc and wiggle
# windows task configure with everyday 8 am or have another table and hold last pull time
# compare db
# notify any difeerence with email

import requests
import time
import sqlite3
from sqlite3 import Error
from pathlib import Path

from bs4 import BeautifulSoup


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        sql_create_wiggle_table = """CREATE TABLE IF NOT EXISTS wiggle (
                                id integer PRIMARY KEY,
                                bike text NOT NULL,
                                price text NOT NULL,
                                url text,
                                discount text,
                                img text
                            );"""

        sql_create_crc_table = """CREATE TABLE IF NOT EXISTS crc (
                                id integer PRIMARY KEY,
                                bike text NOT NULL,
                                price text NOT NULL,
                                url text,
                                discount text,
                                img text
                            );"""

        conn.execute(sql_create_wiggle_table)
        conn.execute(sql_create_crc_table)

        sql = ''' INSERT INTO wiggle(bike,price,url,discount,img)
        VALUES(?,?,?,?,?) '''
        cur = conn.cursor()
        bike = ('Nukeproof Giga 297 RS Carbon Bike (X01 Eagle)',
                '€7999.99', None, None, None)
        cur.execute(sql, bike)
        bike = ('Vitus Sentier 27 Mountain Bike', '€1169.99',
                'https://www.chainreactioncycles.com/tr/en/vitus-sentier-27-mountain-bike/rp-prod206946', '10%', None)
        cur.execute(sql, bike)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def main():
    path = Path().resolve()
    create_connection(f"{path}\\sqlite.db")

    # URL = "https://www.wiggle.co.uk/?s=dirt+jump&o=3&prevDestCountryId=68&curr=EUR&dest=68"
    # # URL = "https://www.chainreactioncycles.com/tr/en/s?q=dirt+jump+bike"
    # page = requests.get(URL, verify=False)

    # soup = BeautifulSoup(page.content, "html.parser")

    # print(f"{'*'*25}  WIGGLE DIRT JUMPS BEGIN  {'*'*25}")
    # for child in soup.find_all("div", class_="bem-product-list-item--grid"):
    #     if not "bike" in child.find('a', class_="bem-product-thumb__name--grid").text.strip().lower():
    #         continue
    #     print("bike: ", child.find('a', class_="bem-product-thumb__name--grid").text.strip())
    #     discount = child.find('span', class_="bem-product_price__discount").text.split()[1] if child.find('span', class_="bem-product_price__discount") else None
    #     print("discount: ", discount)
    #     print("price: ", child.find('span', class_="bem-product-price__unit--grid").text.strip())
    #     print("url: ", child.find('a', class_="bem-product-thumb__name--grid").get('href'))
    #     print("img: ", f"https:{child.find('a', class_='bem-product-thumb__image-link--grid').find('img').get('src').replace(' ', '%20')}")
    # print(f"{'*'*25}  WIGGLE DIRT JUMPS END  {'*'*25}")

    URL = "https://www.chainreactioncycles.com/tr/en/s?q=dirt+jump+bike&sort=pricehigh"
    page = requests.get(URL, verify=False)

    soup = BeautifulSoup(page.content, "html.parser")

    print(f"{'*'*25}  DIRT JUMPS BEGIN  {'*'*25}")
    for index, child in enumerate(soup.find_all("div", class_="products_details product_details_plp"), start=1):
        print(index)
        print("bike: ", child.find('ul').find('h2').text.strip())
        discount = child.find('ul').find('span', class_="pixel_separator")
        print("discount: ", None if not discount else discount.text.strip())
        print("price: ", child.find('ul').find(
            'li', class_="fromamt").text.strip())
        print(
            "url: ", f"https://www.chainreactioncycles.com{child.find('ul').find('a').get('href')}")
    print(f"{'*'*25}  DIRT JUMPS END  {'*'*25}")
    time.sleep(5)

    print(f"{'*'*25}  ALL MOUNTAIN BIKES BEGIN  {'*'*25}")
    page_no = 1
    per_page = 48
    while True:
        URL = f"https://www.chainreactioncycles.com/tr/en/mtb/mountain-bikes?f=2232&page={page_no}"
        # wiggle = "https://www.wiggle.co.uk/cycle/mountain-bikes?o=3&g=1" g=49 g=97
        page = requests.get(URL, verify=False)

        soup = BeautifulSoup(page.content, "html.parser")

        for index, child in enumerate(soup.find_all("div", class_="products_details product_details_plp"), start=(per_page*(page_no-1) if page_no > 1 else 1)):
            print(index)
            print("bike: ", child.find('ul').find('h2').text.strip())
            discount = child.find('ul').find('span', class_="pixel_separator")
            print("discount: ", None if not discount else discount.text.strip())
            print("price: ", child.find('ul').find(
                'li', class_="fromamt").text.strip())
            print(
                "url: ", f"https://www.chainreactioncycles.com{child.find('ul').find('a').get('href')}")

        if len(soup.find_all("div", class_="products_details product_details_plp")) < 48:
            break
        page_no += 1
        time.sleep(5)
    print(f"{'*'*25}  ALL MOUNTAIN BIKES END  {'*'*25}")


if __name__ == "__main__":
    main()
