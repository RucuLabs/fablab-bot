from telegram import Update
from telegram.ext import ContextTypes
from brain.modules.data.FabLabRepository import FabLabRepository


async def list_users(update: Update, context: ContextTypes.DEFAULT_TYPE):
    db = FabLabRepository()
    users = db.get_all_users()
    userlist = ""
    for user in users:
        userlist += str(user.telegram_id) + ": " + user.name + "\n"
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Listando usuarios:\n" + userlist)
