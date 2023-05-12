# pylint: disable=no-else-return
import sqlite3
import math


def create_db(db_name, table_name):
    # create a database
    cnt = sqlite3.connect(db_name)
    # create a table
    cnt.execute(
        f"""CREATE TABLE IF NOT EXISTS {table_name}(
        ARTICULO INT PRIMARY KEY,
        DESCRIPCION TEXT,
        CLASIFICACION TEXT,
        CANTIDAD INTEGER NOT NULL);"""
    )

    cnt.commit()
    cnt.close()


def insert_article_df_into_db(dataframe_to_insert, db_name, table_name):
    cnt = sqlite3.connect(db_name)
    dataframe_to_insert.to_sql(table_name, cnt, if_exists="replace", index=False)
    cnt.commit()
    cnt.close()


def reset_database_quantity_for_article(db_name, table_name):
    cnt = sqlite3.connect(db_name)
    query = cnt.execute(
        f"""UPDATE {table_name}
                        SET CANTIDAD = 1
                        WHERE CLASIFICACION = 'C' """
    )
    query = cnt.execute(
        f"""UPDATE {table_name}
                        SET CANTIDAD = 2
                        WHERE CLASIFICACION = 'B' """
    )
    query = cnt.execute(
        f"""UPDATE {table_name}
                        SET CANTIDAD = 3
                        WHERE CLASIFICACION = 'A' """
    )
    cnt.commit()
    cnt.close()


def remove_quant_for_article(db_name, table_name, article):
    cnt = sqlite3.connect(db_name)
    query = cnt.execute(
        f"""UPDATE {table_name}
                      SET CANTIDAD = CANTIDAD - 1
                      WHERE ARTICULO = {article} AND CANTIDAD >= 1 """
    )
    cnt.commit()
    cnt.close()


def select_an_article(db_name, table_name, article):
    cnt = sqlite3.connect(db_name)
    query = cnt.execute(f"SELECT * FROM {table_name} WHERE ARTICULO={str(article)}")
    print(query.fetchone())
    cnt.close()


def select_random_article(db_name, table_name, category):
    cnt = sqlite3.connect(db_name)
    query = cnt.execute(
        f""" SELECT ARTICULO, DESCRIPCION, CLASIFICACION FROM {table_name}
    WHERE CLASIFICACION='{category}' AND CANTIDAD > 0
    ORDER BY random() 
    LIMIT 1"""
    )
    article = query.fetchone()
    cod = article[0]
    descrip = article[1]
    clasificacion = article[2]
    cnt.close()
    return cod, descrip, clasificacion


def check_if_article_has_quantity(db_name, table_name, article):
    cnt = sqlite3.connect(db_name)
    query = cnt.execute(
        f""" SELECT CANTIDAD FROM {table_name} WHERE ARTICULO={str(article)} """
    )
    rows = query.fetchone()
    if rows[0] == 0:
        return False
    else:
        return True
    cnt.close()


def check_if_category_has_quantity(db_name, table_name, category):
    cnt = sqlite3.connect(db_name)
    query = cnt.execute(
        f""" SELECT COUNT(*)
            FROM {table_name}
            WHERE CLASIFICACION = '{category}' AND CANTIDAD > 0; """
    )

    if query.fetchone()[0] > 0:
        return True
    else:
        return False

def check_if_item_without_count(db_name, table_name):
    cnt = sqlite3.connect(db_name)
    query = cnt.execute(
        f""" SELECT SUM(CANTIDAD) FROM {table_name} """
    )
    rows = query.fetchone()
    if rows[0] == 0:
        return False
    else:
        return True
    cnt.close()

def get_max_per_category_per_day(db_name, table_name, dates_dictionary, category):
    cnt = sqlite3.connect(db_name)
    business_days = len(dates_dictionary.keys())
    query = cnt.execute(
        f""" SELECT COUNT(*)
            FROM {table_name}
            WHERE CLASIFICACION = '{category}'; """
    )

    if(category == "A"):
        quantity = query.fetchone()[0] * 3
    elif(category == "B"):
        quantity = query.fetchone()[0] * 2
    else:
        quantity = query.fetchone()[0] * 1

    return math.floor(quantity/business_days)