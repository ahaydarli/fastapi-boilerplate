import logging
from abc import ABC

from peewee import Model, MySQLDatabase

from core.config import settings
from core.extensions import db


class StrictMySQLDatabase(MySQLDatabase, ABC):
    def _connect(self, **kwargs):
        return super(StrictMySQLDatabase, self)._connect()


db_connection = StrictMySQLDatabase(
        str(settings.db_name), user=str(settings.db_user),
        password=str(settings.db_password),
        host=str(settings.db_host)
    )


class BaseModel(Model):
    class Meta:
        database = db
