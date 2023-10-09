from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from model import Base


class Language(Base):
    __tablename__ = "language"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, default="", index=True)
    code = Column(String, default="", index=True)
    description = Column(String, default="")
    created = Column(DateTime, default=datetime.utcnow)
    updated = Column(DateTime, default=datetime.utcnow)
