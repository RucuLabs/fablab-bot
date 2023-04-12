from telegram import Update
from telegram.ext import ContextTypes

async def help_c(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Información sobre los comandos")
