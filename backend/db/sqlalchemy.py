from config import Config
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Float,
    Boolean,
    Sequence,
    ForeignKey,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


Base = declarative_base()

"""
CREATE TABLE `japanese_english` (
 `c7` REAL DEFAULT 0,
 `created` TEXT DEFAULT "" NOT NULL,
 `frequency` REAL DEFAULT 0,
 `id` TEXT PRIMARY KEY,
 `meaning` TEXT DEFAULT '',
 `pronounciation` TEXT DEFAULT '',
 `tags1` TEXT DEFAULT '',
 `tags2` TEXT DEFAULT '',
 `tags3` TEXT DEFAULT '',
 `updated` TEXT DEFAULT "" NOT NULL,
 `word` TEXT DEFAULT '');
"""


class JapaneseEnglish(Base):
    __tablename__ = "japanese_english"

    id = Column(String, primary_key=True)
    word = Column(String, default="")
    pronounciation = Column(String, default="")
    meaning = Column(String, default="")
    tags1 = Column(String, default="")
    tags2 = Column(String, default="")
    tags3 = Column(String, default="")
    frequency = Column(Float, default=0)
    c7 = Column(Float, default=0)
    created = Column(String, default="")
    updated = Column(String, default="")


def create_tables():
    Base.metadata.create_all(bind=engine)
