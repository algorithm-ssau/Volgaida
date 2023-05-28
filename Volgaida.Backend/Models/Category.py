from sqlalchemy import String, Integer, Column, LargeBinary
from sqlalchemy.orm import relationship

from Models.base import Base


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    image = Column(LargeBinary)
    products = relationship('Product', back_populates='category')
