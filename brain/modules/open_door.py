from telegram import Update
from telegram.ext import ContextTypes
import paho.mqtt.publish as publish
import logging
from brain.modules.data.FabLabRepository import FabLabRepository
import datetime as dt

MQTT_SERVER = "localhost"
MQTT_PATH = "fab/door"

door_logger = logging.getLogger(__name__)
door_logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler('./logs/door.log')
file_handler.setFormatter(formatter)
door_logger.addHandler(file_handler)

async def open_door(update: Update, context: ContextTypes.DEFAULT_TYPE):

    id = update.message.from_user.id
    db = FabLabRepository()
    if (db.check_door_auth(id)): 
        user = db.get_user_by_id(id)
        now = dt.datetime.now()
        db.add_door_log(user, now)
        door_logger.info(f"{user.name} ha abierto la puerta.",)
        publish.single(MQTT_PATH, "open", hostname=MQTT_SERVER)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Abriendo puerta.")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="No tienes permisos para abrir la puerta.")
