from datetime import datetime

from sqlalchemy import Column, DateTime, Float, String

from .base import Base


class LanguageDictionary(Base):
    __abstract__ = True

    id = Column(String, primary_key=True)
    word = Column(String, default="", index=True)
    pronounciation = Column(String, default="", index=True)
    meaning = Column(String, default="")
    created = Column(DateTime, default=datetime.utcnow)
    updated = Column(DateTime, default=datetime.utcnow)


class JapaneseEnglish(LanguageDictionary):
    __tablename__ = "japanese_english"

    tags1 = Column(String, default="")
    tags2 = Column(String, default="")
    tags3 = Column(String, default="")
    frequency = Column(Float, default=0)
    c7 = Column(Float, default=0)
