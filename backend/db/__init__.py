from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from config import Config
from model import Base

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Session:
    assert Session is not None

    db = Session()
    try:
        yield db
    finally:
        db.close()


def create_tables():
    Base.metadata.create_all(bind=engine, checkfirst=True)


breakpoint()
