import json
import os
import sqlite3
from pathlib import Path
from sqlite3 import Error


class DBHandler():
    def __init__(self) -> None:
        self.conn = self.create_connection()
        self.create_tables()

    def create_connection(self):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            db_dir = os.path.dirname(os.path.abspath(__file__))
            db_file = os.path.join(db_dir, "sqlite.db")
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
            raise e
        return conn

    def create_tables(self):
        sql_create_dj_table = """CREATE TABLE IF NOT EXISTS DJ (
                        id integer PRIMARY KEY,
                        bike text NOT NULL,
                        price text NOT NULL,
                        url text,
                        discount text,
                        img text,
                        store text NOT NULL,
                        UNIQUE(bike,store)
                    );"""

        sql_create_all_mtb_table = """CREATE TABLE IF NOT EXISTS ALLMTB (
                                id integer PRIMARY KEY,
                                bike text NOT NULL UNIQUE,
                                price text NOT NULL,
                                url text,
                                discount text,
                                img text,
                                store text NOT NULL,
                                UNIQUE(bike,store)
                            );"""

        self.conn.execute(sql_create_dj_table)
        self.conn.execute(sql_create_all_mtb_table)

        # sql = ''' INSERT INTO DJ(bike,price,url,discount,img,store)
        # VALUES(?,?,?,?,?,?) '''
        # cur = self.conn.cursor()
        # bike = ('Nukeproof Giga 297 RS Carbon Bike (X01 Eagle)',
        #         '€7999.99', None, None, None, "wiggle")
        # cur.execute(sql, bike)
        # bike = ('Vitus Sentier 27 Mountain Bike', '€1169.99',
        #         'https://www.chainreactioncycles.com/tr/en/vitus-sentier-27-mountain-bike/rp-prod206946', '10%', None, "CRC")
        # cur.execute(sql, bike)
        # self.conn.commit()

    def process_data(self, bike_data: str):
        # bike_data = json.loads(self.bike_data)
        # djs = bike_data.get("djs", [])
        # mtbs = bike_data.get("mtbs", [])
        notifications = {"djsInsert": [], "djsPriceUpdate": []}

        for dj in bike_data:
            cur = self.conn.cursor()
            # WHERE bike=?", (dj["bike"],))
            cur.execute(
                "SELECT bike, price, url, discount, img, store FROM DJ WHERE bike=? AND store=?", (dj["bike"], dj["store"],))

            rows = cur.fetchall()

            if not rows:
                insert_sql = ''' INSERT INTO DJ(bike,price,url,discount,img,store)
                VALUES(?,?,?,?,?,?) '''
                # cur = conn.cursor()
                bike = (dj["bike"], dj["price"], dj["url"],
                        dj["discount"], dj["img"], dj["store"],)
                cur.execute(insert_sql, bike)
                self.conn.commit()
                notifications["djsInsert"].append({**dj, "oldPrice": ""})
                continue

            bike, price, url, discount, img, store = rows[0]
            if price != dj["price"]:
                update_sql = ''' UPDATE DJ
                        SET price = ? ,
                            discount = ?
                        WHERE bike = ? AND store = ?'''
                bike_updated = (dj["price"], dj["discount"],
                                dj["bike"], dj["store"],)
                cur.execute(update_sql, bike_updated)
                self.conn.commit()
                notifications["djsPriceUpdate"].append(
                    {**dj, "oldPrice": price})

        if self.conn:
            self.conn.close()

        return notifications
