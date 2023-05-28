import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from psycopg2 import connect, extensions, Binary
from os import getcwd
from base import Base
from Product import Product
from Category import Category


class DatabaseServer:
    DEFAULT_HOST = "localhost"
    DEFAULT_PORT = 5432
    DEFAULT_USERNAME = "postgres"
    DEFAULT_PASSWORD = "postgres"
    DEFAULT_DATABASE_NAME = "volgaida"

    DEFAULT_URL = f"postgresql://{DEFAULT_USERNAME}:{DEFAULT_PASSWORD}@{DEFAULT_HOST}:{DEFAULT_PORT}/{DEFAULT_DATABASE_NAME}"

    Engine = None
    SessionLocal = None


def create_database(host, port, user, password, database_name):
    connection = connect(host=host, port=port, user=user, password=password)
    connection.set_isolation_level(extensions.ISOLATION_LEVEL_AUTOCOMMIT)

    cursor = connection.cursor()

    cursor.execute(f"DROP DATABASE IF EXISTS {database_name};")
    cursor.execute(f"CREATE DATABASE {database_name};")

    cursor.close()
    connection.close()


def get_image_file(filename):
    return os.getcwd() + f"\\Images\\{filename}.jpg"


def fill_database(host, port, user, password, database_name):
    connection = connect(host=host, port=port, user=user, password=password, dbname=database_name)
    connection.set_isolation_level(extensions.ISOLATION_LEVEL_AUTOCOMMIT)

    cursor = connection.cursor()
    categories_names = ["Горячие блюда", "Десерты", "Закуски", "Салаты", "Барная карта", "Напитки"]
    categories_photos = ["Паста карбонара", "Тирамису", "Куриный бутерброд на деревянной доске",
                         "Салат с пряной говядиной", "Джонни Сильверхенд", "Шмель"]
    for i in range(1, 7):
        binary_image = open(get_image_file(categories_photos[i]), 'rb').read()
        cursor.execute(f"INSERT INTO categories (id, name, image) VALUES(%s,%s,%s)",
                       (i, categories_names[i], Binary(binary_image)))

    hot_dish_photos = ["Паста Карбонара", "Судак на гриле", "Мясо с тушеным картофелем", "Пицца Четыре сыра",
                       "Пицца с ветчиной и грибами", "Пицца с куриной грудкой"]
    hot_dish_comp = ["Спагетти, бекон, сливки, сыр пармезан, яйца, зелень", "Судак, лимон, зелень",
                     "Говядина,томаты, морковь, лук репчатый", "пармезан, чеддер, дор блю, гауда",
                     "томатный соус, ветчина, шампиньоны, сыр гауда",
                     "томатный соус, куриная грудка, свежие томаты, сыр гауда"]
    hot_dish_weight = [270, 350, 250, 350, 330, 380]
    hot_dish_price = [355, 389, 359, 369, 349, 359]
    hot_dish_pfc = ["13/13/31", "22/1/0", "20/3/25", "46/62/97", "41/35/116", "47/28/120"]

    cursor.close()
    connection.close()


def init_database_server():
    DatabaseServer.Engine = create_engine(DatabaseServer.DEFAULT_URL, echo=True)
    DatabaseServer.SessionLocal = sessionmaker(autocommit=False, bind=DatabaseServer.Engine)


def create_tables():
    Base.metadata.create_all(DatabaseServer.Engine)


def main():
    create_database(
        DatabaseServer.DEFAULT_HOST,
        DatabaseServer.DEFAULT_PORT,
        DatabaseServer.DEFAULT_USERNAME,
        DatabaseServer.DEFAULT_PASSWORD,
        DatabaseServer.DEFAULT_DATABASE_NAME
    )

    init_database_server()
    create_tables()

    fill_database(
        DatabaseServer.DEFAULT_HOST,
        DatabaseServer.DEFAULT_PORT,
        DatabaseServer.DEFAULT_USERNAME,
        DatabaseServer.DEFAULT_PASSWORD,
        DatabaseServer.DEFAULT_DATABASE_NAME
    )


main()
