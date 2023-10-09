from sqlalchemy import Column, Integer, String

from model import Base


class Translation(Base):
    __tablename__ = "translation"

    id = Column(Integer, primary_key=True, autoincrement=True)
    from_language = Column(String, default="", index=True)
    to_language = Column(String, default="", index=True)
    from_text = Column(String, default="", index=True)
    to_text = Column(String, default="", index=True)
