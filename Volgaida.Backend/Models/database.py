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
    dessert_photos = ["Меренга с малиной", "Пломбир с клубничным сиропом", "Чизкейк", "Тирамису", "Панна котта",
                      "Морковный торт"]
    dessert_comp = ["яичный белок, сахар, ваниль, малина, сливки", "пломбир, шоколад, клубничный сироп",
                    "сливочный сыр, песочное тесто, сливки, вишневый сироп",
                    "маскарпоне, бисквит савоярди, кофейный мусс с ромом",
                    "сливки, яичный желток, сахар, ваниль, желатин, клубничный соус",
                    "Морковный бисквит с грецкими орехами, цедрой цитрусовых и корицей, крем из творожного сыра"]
    dessert_weight = [150, 50, 110, 100, 100, 120]
    dessert_price = [189, 99, 275, 290, 210, 210]
    dessert_pfc = ["35/12/4", "3/15/20", "5/8/20", "4/ 21/24", "6/19/31", "4/20/35"]
    snacks_photos = ["Круассаны с лососем и творожным сыром", "Чесночные гренки с соусом Тар-тар",
                     "Луковые кольца с чесночным соусом", "Тар-тар из лосося", "Сырный зуб",
                     "Куриный бутерброд на деревянной доске", "Картофель фри", "Картофель айдахо"]
    snacks_comp = ["круассан, лосось слабой соли, лист салата, огурец, творожный сыр", "Чесночные гренки, соус Тар-тар",
                   "Луковые кольца, чесночный соус", "Лосось филе, кабачок, огурец, семена льна",
                   "пармезан, чеддер, сулугуни, дор блю, грецкий орех, оливки",
                   "Курица деревенская, белый хлеб, помидоры, листья салата, плавленный сыр, огурцы, соус",
                   "картофель, соус на выбор", "картофель, соус на выбор"]
    snacks_weight = [244, 210, 170, 250, 250, 300, 189, 199]
    snacks_price = [325, 185, 149, 330, 349, 359, 189, 199]
    snacks_pfc = ["10/7/20", "12/30/50", "1/2/4", "11/14/18", "30/39/23", "7/9/17", "2/14/25", "2/14/25"]
    salad_photo = ["Цезарь с курицей", "Греческий", "Салат с розовыми помидорами", "Салат с пряной говядиной",
                   "Салат цезарь с креветками", "Салат с сыром сулугуни"]
    salad_comp = ["листья салата, томаты, куриное филе, яйца, сыр пармезан, соус Цезарь, сухарики",
                  "свежие томаты, огурцы, красный лук, паприка, листья салата, маслины, сыр фета, соус Песто",
                  "Микс салата, томаты, горчица зернистая, мед, масло оливковое, говядина, микрозелень",
                  "Говяжья вырезка, перец болгарский, огурец, салат айсберг, редис, томаты, соус лимонно-горчичный, зелень",
                  "креветки, салат айсберг, помидоры черри, сыр пармезан",
                  "Микс салата, сыр сулугуни, салат айсберг, панировочные сухари, наршараб, оливковое масло, томаты"]
    salad_weight = [200, 310, 160, 210, 160, 170]
    salad_price = [369, 310, 265, 235, 239, 199]
    salad_pfc = ["14/4/6", "1/0/3", "3/5/4", "10/7/4", "6/4/3", "8/16/4"]
    ["", "", "", "", "", ""]
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
