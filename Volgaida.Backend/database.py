from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:SuperSecretPassword@localhost/volgaida",
                       echo=True)

