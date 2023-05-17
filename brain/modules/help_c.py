from telegram import Update
from telegram.ext import ContextTypes

help_text = """
*Ayuda*
Este bot maneja la red IoT del FabLab de la FCFM. Para registrarte debes hablar con algún administrador, lo mismo para los permisos.

*Comandos generales*
help - información sobre los comandos

*Comandos usuarios con acceso a puerta*
open - abre la puerta del FabLab
"""

async def help_c(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=help_text, parse_mode='Markdown')
