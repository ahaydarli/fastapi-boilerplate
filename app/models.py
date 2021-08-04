from peewee import CharField, IntegerField, BigIntegerField, AutoField, SQL, TextField, BigAutoField, FloatField, \
    DateField

from core.database import BaseModel


class User(BaseModel):
    id = AutoField()
    created = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    email = CharField(constraints=[SQL("DEFAULT ''")])
    hash = CharField(constraints=[SQL("DEFAULT ''")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    password = CharField(constraints=[SQL("DEFAULT ''")])
    surname = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'users'
