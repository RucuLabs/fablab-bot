from telegram import Update
from telegram.ext import ContextTypes
import paho.mqtt.publish as publish
import logging
from brain.modules.data.FabLabRepository import FabLabRepository
import datetime as dt

MQTT_SERVER = "localhost"
MQTT_PATH = "fab/door"


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

async def open_door(update: Update, context: ContextTypes.DEFAULT_TYPE):

    id = update.message.from_user.username
    db = FabLabRepository()
    if (db.check_door_auth(id)):
        now = dt.datetime.now()
        logger.info("El usuario " + id + " abrió la puerta a las: " + str(now))
        publish.single(MQTT_PATH, "open", hostname=MQTT_SERVER)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Abriendo puerta.")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="No tienes permisos para abrir la puerta.")
