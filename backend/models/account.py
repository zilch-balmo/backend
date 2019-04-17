"""
An account.

"""
from microcosm_postgres.models import EntityMixin, Model
from sqlalchemy import Column, String


class Account(EntityMixin, Model):
    __tablename__ = "account"

    name = Column(String, nullable=False, unique=True)
