from sqlalchemy import Column, text
from sqlalchemy.dialects.mysql import TIMESTAMP

class TimeStampMixin(object):
    created_at = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("current_timestamp"),
        comment="作成日時"
    )
    updated_at = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("current_timestamp on update current_timestamp"),
        comment="更新日時"
    )