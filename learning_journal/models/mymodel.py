from sqlalchemy import (
    Column,
    Integer,
    Text,
    Unicode,
    UnicodeText,
    DateTime,
)

from .meta import Base


class Entry(Base):
    """Entry for journal entries."""

    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(128), unique=True)
    body = Column(UnicodeText)
    date = Column(DateTime)

# datetime.datetime.utcnow
# now = datetime.datetime.utcnow()
# now.strftime(*Stuff)
# ptz worldtime timezone library