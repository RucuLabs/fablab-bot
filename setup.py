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
ADMIN_ID = os.getenv('ADMIN_ID')

if __name__ == '__main__':
    db = Model.db
    db.create_tables([Model.Users, Model.Pending, Model.Door, Model.DoorLogs])
    FabLabRepository().add_user(ADMIN_ID,ADMIN_USER, ADMIN_NAME, "Super")
    