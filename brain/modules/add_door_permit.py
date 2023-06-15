import logging

from telegram import Update
from telegram.ext import ContextTypes
from brain.modules.data.FabLabRepository import FabLabRepository

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

async def add_door_permit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        id = update.message.from_user.id
        db = FabLabRepository()
        if((db.get_role(id) == "Admin") or (db.get_role(id) == "Super")):
            telegram_id = context.args[0]
            db.add_user_to_door(telegram_id)
            user = db.get_user_by_username(telegram_id).name
            await context.bot.send_message(chat_id=update.effective_chat.id, text="El usuario " + user + " ahora tiene permisos de puerta.")
        
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="No tienes permisos suficientes.")

    except Exception as ex:
        logger.info("Error: %s", ex)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="No se pudo dar permisos al usuario")
