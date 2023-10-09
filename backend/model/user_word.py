from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String

from .base import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), unique=True, index=True)
    username = Column(String(255), unique=True, index=True)
    salt = Column(String(255), nullable=True)
    password_hash = Column(String(255), nullable=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    is_deleted = Column(Boolean)

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_deleted = False

    def __repr__(self):
        return "<User('%s')>" % (self.username)


class Word(Base):
    __tablename__ = "word"
    id = Column(Integer, primary_key=True, autoincrement=True)
    word = Column(String(255), unique=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    is_deleted = Column(Boolean)

    def __init__(self, word):
        self.word = word
        self.is_deleted = False

    def __repr__(self):
        return "<Word('%s')>" % (self.word)


class UserWord(Base):
    __tablename__ = "user_word"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    word_id = Column(Integer, ForeignKey("word.id"))
    interaction_count = Column(Integer, default=0)
    last_interaction = Column(DateTime, nullable=True)
    current_level = Column(Integer, default=0)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    is_deleted = Column(Boolean)

    def __init__(self, user_id, word_id):
        self.user_id = user_id
        self.word_id = word_id
        self.is_deleted = False

    def __repr__(self):
        return "<UserWord('%s', '%s')>" % (self.user_id, self.word_id)
