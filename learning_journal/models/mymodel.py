from sqlalchemy import (
    Column,
    Integer,
    Text,
    Unicode,
    DateTime,
)

from .meta import Base


class Entry(Base):
    """Entry for journal entries."""

    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(128), unique=True)
    body = Column(Text)
    date = Column(DateTime)
