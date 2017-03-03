from peewee import *
from connect_database import ConnectDatabase


class BaseModel(Model):

    class Meta:
        database = ConnectDatabase.db


class Food(BaseModel):
    name = CharField(null=True)
    ingredients = TextField(null=True)
    recipe = TextField(null=True)
    category = CharField(null=True)
    image = CharField(null=True)