from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from model import Base


class Language(Base):
    __tablename__ = "language"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), default="", index=True)
    code = Column(String(255), default="", index=True)
    description = Column(String(255), default="")
    created = Column(DateTime, default=datetime.utcnow)
    updated = Column(DateTime, default=datetime.utcnow)
