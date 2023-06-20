from peewee import *


db = SqliteDatabase('fablab.db')


class BaseModel(Model):
    class Meta:
        database = db     

class Users(BaseModel):
    id = CharField(unique=True)
    telegram_id = CharField()
    name = CharField()
    role = CharField()

class Pending(BaseModel):
    telegram_id = CharField(unique=True)
    name = CharField()
    role = CharField()


class Door(BaseModel):
    user = ForeignKeyField(Users, backref='door')
    limit_date = DateField()

class DoorLogs(BaseModel):
    user = ForeignKeyField(Users, backref='door log')
    time = DateTimeField()