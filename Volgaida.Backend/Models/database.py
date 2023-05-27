from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from psycopg2 import connect, extensions

from Models.base import Base
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


main()
