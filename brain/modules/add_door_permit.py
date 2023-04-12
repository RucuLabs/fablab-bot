from telegram import Update
from telegram.ext import ContextTypes

async def add_door_permit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Agregando permisos a usuario")
