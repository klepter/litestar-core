from hashlib import sha256

from litestar.contrib.sqlalchemy.base import BigIntAuditBase
from sqlalchemy import String
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column


class User(BigIntAuditBase):
    __tablename__ = 'user'

    first_name: Mapped[str] = mapped_column(String(255))
    last_name: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    _password: Mapped[str] = mapped_column('password', String(255))

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, value: str):
        hash_new_value = sha256(value.encode('UTF-8')).hexdigest()
        self._password = hash_new_value
