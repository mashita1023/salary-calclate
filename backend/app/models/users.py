from ..database import Base
from .mixins import TimeStampMixin
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy_utils import UUIDType
from uuid import uuid4

class User(Base, TimeStampMixin):
    __tablename__ = "users"
    __table_args__ = {"comment": "ユーザー"}

    id = Column(
        UUIDType(binary=False),
        primary_key=True,
        default=uuid4,
        comment="ユーザーID"
    )
    name = Column(
        String(length=100),
        nullable=False,
        comment="ユーザーの名前"
    )
    mail = Column(
        String(length=100),
        nullable=False,
        comment="ユーザーのメールアドレス"
    )