from sqlalchemy import Column, CheckConstraint, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Account(Base):
    """The Account class corresponds to the "accounts" database table.
    """
    __tablename__ = 'accounts'
    id = Column(UUID(as_uuid=True), primary_key=True, autoincrement=True, nullable=False)
    username = Column(String, CheckConstraint('char_length(username) >= 5'), unique=True, nullable=False)
    password = Column(String, CheckConstraint('char_length(password) >= 5'), nullable=False)
