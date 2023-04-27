from brain.modules.data import Model
from brain.modules.data.FabLabRepository import FabLabRepository
import datetime
import peewee
import os
from dotenv import load_dotenv

# get bot token from .env file
load_dotenv()
ADMIN_USER = os.getenv('ADMIN_USER')
ADMIN_NAME = os.getenv('ADMIN_NAME')

if __name__ == '__main__':
    db = Model.db
    db.create_tables([Model.Users, Model.Door])
    FabLabRepository().add_user(ADMIN_USER, ADMIN_NAME, "Admin")
    