from telegram import Update
from telegram.ext import ContextTypes
from brain.modules.data.FabLabRepository import FabLabRepository


async def door_log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    db = FabLabRepository()
    id = update.message.from_user.id
    if((db.get_role(id) == "Admin") or (db.get_role(id) == "Super")):
        logs = db.get_door_logs()
        log_list = ""
        for log in logs:
            log_list += f"{log.time} : {log.user.telegram_id} - {log.user.name}\n"
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Listando registros:\n" + log_list)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="No tienes permisos suficientes.")
