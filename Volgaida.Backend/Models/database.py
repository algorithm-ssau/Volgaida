from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DB_URL = "mysql://root:SuperSecretPassword@127.0.0.1:3306/volgaida"
engine = create_engine(DB_URL, echo=True)

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, bind=engine)
