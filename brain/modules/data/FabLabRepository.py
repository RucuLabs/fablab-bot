from brain.modules.data import Model
import datetime
import peewee


class FabLabRepository:

    def __init__(self):
        self.db = Model.db
        self.db.create_tables([Model.Users, Model.Door])
    
    def add_user(self, id, name):
        try:
            with self.db.atomic():
                return Model.Users.create(telegram_id = id, name = name)
        except peewee.IntegrityError:
            return Model.Users.get(Model.Users.telegram_id == id)


    def get_user(self, id):
        user = Model.Users.get(Model.Users.telegram_id == id)
        return user
    
    def get_all_users(self):
        return Model.Users.select() 

    def add_user_to_door(self, id):
        user = self.get_user(id)
        new_door = Model.Door.create(user=user, role="Default", limit_date = datetime.date.today())
        new_door.save()


