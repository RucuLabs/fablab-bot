from telegram import Update
from telegram.ext import ContextTypes
import paho.mqtt.publish as publish
import logging
from brain.modules.data.FabLabRepository import FabLabRepository
import datetime as dt

MQTT_SERVER = "localhost"
MQTT_PATH = "fab/door"


# Enable logging
logging.basicConfig(filename='./logs/example.log', encoding='utf-8',
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

async def open_door(update: Update, context: ContextTypes.DEFAULT_TYPE):

    id = update.message.from_user.username
    # print(update.message.from_user.id)
    db = FabLabRepository()
    if (db.check_door_auth("@" + id)): #check!!!
        now = dt.datetime.now()
        db.add_door_log(id, now)
        logger.info(id)
        publish.single(MQTT_PATH, "open", hostname=MQTT_SERVER)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Abriendo puerta.")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="No tienes permisos para abrir la puerta.")
