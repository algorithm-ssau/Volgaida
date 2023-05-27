from database import Base, engine
from sqlalchemy import text
from Category import Category
from Product import Product

with engine.connect() as conn:
    create_str = text("CREATE DATABASE IF NOT EXISTS volgaida;")
    use_str = text("USE volgaida;")
    conn.execute(create_str)
    conn.execute(use_str)
    Base.metadata.create_all(bind=engine)
