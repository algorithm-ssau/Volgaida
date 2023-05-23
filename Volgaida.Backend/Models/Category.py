from database import Base
from sqlalchemy import String, Integer, Column, Text
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    image = Column(Text)
    products = relationship('Product', back_populates='category')
