from sqlalchemy import Column, Integer, String

from model import Base


class Translation(Base):
    __tablename__ = "translation"

    id = Column(Integer, primary_key=True, autoincrement=True)
    from_language = Column(String(255), default="", index=True)
    to_language = Column(String(255), default="", index=True)
    from_text = Column(String(4096), default="", index=True)
    to_text = Column(String(4096), default="", index=True)
