from peewee import *


db = SqliteDatabase('fablab.db')


class BaseModel(Model):
    class Meta:
        database = db     

class Users(BaseModel):
    telegram_id = CharField(unique=True)
    name = CharField()
    role = CharField()


class Door(BaseModel):
    user = ForeignKeyField(Users, backref='door')
    limit_date = DateField()

class DoorLogs(BaseModel):
    telegram_id = CharField()
    time = DateTimeField()