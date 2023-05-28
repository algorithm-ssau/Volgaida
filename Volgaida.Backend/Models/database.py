from os import getcwd

from psycopg2 import connect, extensions, Binary
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, Session

from Models.base import Base
from Models.Product import Product
from Models.Category import Category


class DatabaseServer:
    DEFAULT_HOST = "localhost"
    DEFAULT_PORT = 5432
    DEFAULT_USERNAME = "postgres"
    DEFAULT_PASSWORD = "password"
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
    return getcwd() + f"\\Images\\{filename}.jpg"


def fill_database(host, port, user, password, database_name):
    connection = connect(host=host, port=port, user=user, password=password, dbname=database_name)
    connection.set_isolation_level(extensions.ISOLATION_LEVEL_AUTOCOMMIT)

    cursor = connection.cursor()
    categories_names = ["Горячие блюда", "Десерты", "Закуски", "Салаты", "Барная карта", "Напитки"]
    categories_photos = ["Паста карбонара", "Тирамису", "Куриный бутерброд на деревянной доске",
                         "Салат с пряной говядиной", "Джонни Сильверхенд", "Шмель"]
    for i in range(1, 7):
        binary_image = open(get_image_file(categories_photos[i - 1]), 'rb').read()
        cursor.execute(f"INSERT INTO categories (id, name, image) VALUES(%s,%s,%s)",
                       (i, categories_names[i - 1], Binary(binary_image)))

    hot_dish_photo = ["Паста Карбонара", "Судак на гриле", "Мясо с тушеным картофелем", "Пицца Четыре сыра",
                      "Пицца с ветчиной и грибами", "Пицца с куриной грудкой"]
    hot_dish_comp = ["Спагетти, бекон, сливки, сыр пармезан, яйца, зелень", "Судак, лимон, зелень",
                     "Говядина, томаты, морковь, лук репчатый", "Пармезан, чеддер, дор блю, гауда",
                     "Томатный соус, ветчина, шампиньоны, сыр гауда",
                     "Томатный соус, куриная грудка, свежие томаты, сыр гауда"]
    hot_dish_weight = [270, 350, 250, 350, 330, 380]
    hot_dish_price = [355, 389, 359, 369, 349, 359]
    hot_dish_pfc = ["13/13/31", "22/1/0", "20/3/25", "15/21/32", "13/11/38", "15/8/40"]
    for i in range(len(hot_dish_comp)):
        binary_image = open(get_image_file(hot_dish_photo[i]), 'rb').read()
        cursor.execute(
            f"INSERT INTO products (id, name, ingredients, pfc, weight, price, image, category_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
            (i + 1, hot_dish_photo[i], hot_dish_comp[i], hot_dish_pfc[i], hot_dish_weight[i], hot_dish_price[i],
             Binary(binary_image), 1))

    dessert_photo = ["Меренга с малиной", "Пломбир с клубничным сиропом", "Чизкейк", "Тирамису", "Панна котта",
                     "Морковный торт"]
    dessert_comp = ["Яичный белок, сахар, ваниль, малина, сливки", "Пломбир, шоколад, клубничный сироп",
                    "Сливочный сыр, песочное тесто, сливки, вишневый сироп",
                    "Маскарпоне, бисквит савоярди, кофейный мусс с ромом",
                    "Сливки, яичный желток, сахар, ваниль, желатин, клубничный соус",
                    "Морковный бисквит с грецкими орехами, цедрой цитрусовых и корицей, крем из творожного сыра"]
    dessert_weight = [150, 50, 110, 100, 100, 120]
    dessert_price = [189, 99, 275, 290, 210, 210]
    dessert_pfc = ["35/12/4", "3/15/20", "5/8/20", "4/ 21/24", "6/19/31", "4/20/35"]
    for i in range(len(dessert_comp)):
        binary_image = open(get_image_file(dessert_photo[i]), 'rb').read()
        cursor.execute(
            f"INSERT INTO products (id, name, ingredients, pfc, weight, price, image, category_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
            (i + 7, dessert_photo[i], dessert_comp[i], dessert_pfc[i], dessert_weight[i], dessert_price[i],
             Binary(binary_image), 2))

    snacks_photo = ["Круассаны с лососем и творожным сыром", "Чесночные гренки с соусом Тар-тар",
                    "Луковые кольца с чесночным соусом", "Тар-тар из лосося", "Сырный зуб",
                    "Куриный бутерброд на деревянной доске", "Картофель фри", "Картофель айдахо"]
    snacks_comp = ["Круассан, лосось слабой соли, лист салата, огурец, творожный сыр", "Чесночные гренки, соус Тар-тар",
                   "Луковые кольца, чесночный соус", "Лосось филе, кабачок, огурец, семена льна",
                   "Пармезан, чеддер, сулугуни, дор блю, грецкий орех, оливки",
                   "Курица деревенская, белый хлеб, помидоры, листья салата, плавленный сыр, огурцы, соус",
                   "Картофель, соус на выбор", "Картофель, соус на выбор"]
    snacks_weight = [244, 210, 170, 250, 250, 300, 189, 199]
    snacks_price = [325, 185, 149, 330, 349, 359, 189, 199]
    snacks_pfc = ["10/7/20", "12/30/50", "1/2/4", "11/14/18", "30/39/23", "7/9/17", "2/14/25", "2/14/25"]
    for i in range(len(snacks_comp)):
        binary_image = open(get_image_file(snacks_photo[i]), 'rb').read()
        cursor.execute(
            f"INSERT INTO products (id, name, ingredients, pfc, weight, price, image, category_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
            (i + 13, snacks_photo[i], snacks_comp[i], snacks_pfc[i], snacks_weight[i], snacks_price[i],
             Binary(binary_image), 3))

    salad_photo = ["Цезарь с курицей", "Греческий", "Салат с розовыми помидорами", "Салат с пряной говядиной",
                   "Салат цезарь с креветками", "Салат с сыром сулугуни"]
    salad_comp = ["Листья салата, томаты, куриное филе, яйца, сыр пармезан, соус Цезарь, сухарики",
                  "Свежие томаты, огурцы, красный лук, паприка, листья салата, маслины, сыр фета, соус Песто",
                  "Микс салата, томаты, горчица зернистая, мед, масло оливковое, говядина, микрозелень",
                  "Говяжья вырезка, перец болгарский, огурец, салат айсберг, редис, томаты, соус лимонно-горчичный, зелень",
                  "Креветки, салат айсберг, помидоры черри, сыр пармезан",
                  "Микс салата, сыр сулугуни, салат айсберг, панировочные сухари, наршараб, оливковое масло, томаты"]
    salad_weight = [200, 310, 160, 210, 160, 170]
    salad_price = [369, 310, 265, 235, 239, 199]
    salad_pfc = ["14/4/6", "1/0/3", "3/5/4", "10/7/4", "6/4/3", "8/16/4"]
    for i in range(len(salad_comp)):
        binary_image = open(get_image_file(salad_photo[i]), 'rb').read()
        cursor.execute(
            f"INSERT INTO products (id, name, ingredients, pfc, weight, price, image, category_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
            (i + 21, salad_photo[i], salad_comp[i], salad_pfc[i], salad_weight[i], salad_price[i],
             Binary(binary_image), 4))

    drink_photo = ["Огуречный лимонад", "Милкшейк", "Шмель", "Бабл гам", "Арбузный слинг", "Апельсиновый Сок"]
    drink_comp = ["Медовый сироп, огурцы свежие, апельсин, лайм, мята, фреш лимона, Бон Аква, спрайт",
                  "Молоко, мороженое, сироп в ассортименте, взбитые сливки",
                  "Карамельный сироп, апельсиновый сок, эспрессо, мята", "Сироп баблгам, фреш лимона, спрайт, лайм",
                  "Сироп арбуз, фреш лимона, спрайт, лайм", "Апельсиновый сок"]
    drink_weight = [940, 250, 150, 190, 170, 250]
    drink_price = [260, 145, 80, 100, 100, 150]
    drink_pfc = ["0/3/2", "4/3/18", "0/0/10", "0/0/14", "0/0/10", "0/0/10"]
    for i in range(len(drink_comp)):
        binary_image = open(get_image_file(drink_photo[i]), 'rb').read()
        cursor.execute(
            f"INSERT INTO products (id, name, ingredients, pfc, weight, price, image, category_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
            (i + 27, drink_photo[i], drink_comp[i], drink_pfc[i], drink_weight[i], drink_price[i],
             Binary(binary_image), 5))

    bar_card_photo = ["Мокрый лёд", "Голубая лагуна", "Джонни Сильверхенд", "Пина Колада", "Белый Русский",
                      "Текила Санрайз"]
    bar_card_comp = ["Мартини бьянко, швепс, лайм", "Водка хаски, сироп блю кюрасао, фреш лимона, спрайт, лимон",
                     "белая текила, апельсиновый биттер, сироп агавы, темное пиво, перец-чили, лед",
                     "Бакарди карта бланко, кокосовый ликер, ананасовый сок, сливки, взбитые сливки, коктейльная вишня",
                     "Капучино ликёр, водка, сливки, лед", "Текила, апельсиновый сок, сироп гренадин, апельсин"]
    bar_card_weight = [235, 200, 120, 175, 200, 220]
    bar_card_price = [269, 140, 277, 320, 400, 310]
    bar_card_pfc = ["0/0/13", "0/0/10", "0/0/9", "0/2/22", "0/1/4", "0/0/10"]
    for i in range(len(bar_card_comp)):
        binary_image = open(get_image_file(bar_card_photo[i]), 'rb').read()
        cursor.execute(
            f"INSERT INTO products (id, name, ingredients, pfc, weight, price, image, category_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
            (i + 33, bar_card_photo[i], bar_card_comp[i], bar_card_pfc[i], bar_card_weight[i], bar_card_price[i],
             Binary(binary_image), 6))

    cursor.close()
    connection.close()


def init_database_server():
    DatabaseServer.Engine = create_engine(DatabaseServer.DEFAULT_URL, echo=True)
    DatabaseServer.SessionLocal = sessionmaker(autocommit=False, bind=DatabaseServer.Engine)


def create_tables():
    Base.metadata.create_all(DatabaseServer.Engine)


def select_categories():
    init_database_server()
    session = Session(DatabaseServer.Engine)
    # smtp = select(Category.name, Category.id)
    # categories = session.scalars(smtp)
    categories = session.execute(
        select(Category.id, Category.name)
    )
    return categories


def select_category_image_by_id(category_id: int = 1):
    init_database_server()
    session = Session(DatabaseServer.Engine)
    image = session.execute(
        select(Category.image).where(Category.id == category_id)
    )
    return image.scalar()


def select_full_product_by_id(product_id: int = 1):
    init_database_server()
    session = Session(DatabaseServer.Engine)
    product = session.execute(
        select(Product.name,
               Product.ingredients,
               Product.pfc,
               Product.weight,
               Product.price).where(Product.id == product_id)
    )
    return product


def select_short_products():
    init_database_server()
    session = Session(DatabaseServer.Engine)
    products = session.execute(
        select(Product.id,
               Product.name)
    )
    return products


def select_product_image_by_id(product_id: int = 1):
    init_database_server()
    session = Session(DatabaseServer.Engine)
    image = session.execute(
        select(Product.image).where(Product.id == product_id)
    )
    return image.scalar()


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
