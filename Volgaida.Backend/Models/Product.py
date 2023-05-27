from database import Base
from sqlalchemy import String, Integer, Column, Text, ForeignKey, BLOB
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    ingredients = Column(Text)
    pfc = Column(String(30), nullable=False)
    weight = Column(Integer)
    price = Column(Integer)
    image = Column(BLOB)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', back_populates='products')

