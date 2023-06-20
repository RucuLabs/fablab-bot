from brain.modules.data import Model
import datetime
import peewee


class FabLabRepository:

    def __init__(self):
        self.db = Model.db
    
    def add_pending(self, telegram_id, name, role):
        try:
            with self.db.atomic():
                return Model.Pending.create(telegram_id = telegram_id, name = name, role = role)
        except peewee.IntegrityError:
            return Model.Pending.get(Model.Pending.telegram_id == telegram_id)

        
    def add_user(self, id, telegram_id, name, role):
        try:
            with self.db.atomic():
                return Model.Users.create(id=id, telegram_id = telegram_id, name = name, role = role)
        except peewee.IntegrityError:
            return Model.Users.get(Model.Users.id == id)

    def get_user_by_username(self, telegram_id):
        try:
            user = Model.Users.get(Model.Users.telegram_id == telegram_id)
            return user
        except Exception as ex:
            return ex
    
    def get_user_by_id(self, id):
        try:
            user = Model.Users.get(Model.Users.id == id)
            return user
        except Exception as ex:
            return ex
            

    def get_all_users(self):
        return Model.Users.select() 

    def add_user_to_door(self, telegram_id):
        user = self.get_user_by_username(telegram_id)
        new_door = Model.Door.create(user=user, limit_date = datetime.date.today())
        new_door.save()
    
    def check_door_auth(self, id):
        try:
            user = self.get_user_by_id(id)
            if (user.role == "Admin") or (user.role == "Super"):
                return True
            door = Model.Door.get(Model.Door.user == user)
            return True
        
        except Exception as ex:
            return False
        
    def get_role(self, id):
        try:
            role = self.get_user_by_id(id).role
            return role

        except:
            return None
        
    def add_door_log(self, user, time):
        return Model.DoorLogs.create(user = user, time = time)

    def is_pending(self, telegram_id):
        query = Model.Pending.select().where(Model.Pending.telegram_id == telegram_id)
        return query.exists()

    def get_pending(self, telegram_id):
        try:
            user = Model.Pending.get(Model.Pending.telegram_id == telegram_id)
            return user
        except Exception as ex:
            return ex