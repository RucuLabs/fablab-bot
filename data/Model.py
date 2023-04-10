from peewee import *


db = SqliteDatabase('fablab.db')


class BaseModel(Model):
    class Meta:
        database = db     

class Users(BaseModel):
    telegram_id = CharField(unique=True)
    name = CharField()


class Door(BaseModel):
    user = ForeignKeyField(Users, backref='door')
    role = CharField()
    limit_date = DateField()