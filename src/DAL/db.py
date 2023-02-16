from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine

from configuration import DB_CONNECTION_STRING

Base = declarative_base()
engine = create_engine(DB_CONNECTION_STRING)
Session = sessionmaker(
    engine,
    autoflush=False,
    autocommit=False
)
