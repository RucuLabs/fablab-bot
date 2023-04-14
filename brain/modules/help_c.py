from telegram import Update
from telegram.ext import ContextTypes

help_text = """
    **usuarios**
    open - abre la puerta del FabLab
    help - información sobre los comandos
    
    **admin**
    adduser - añade un usuario a la base de datos del FabLab
    edituser - edita un usuario de la base de datos del FabLab
    deleteuser - borra un usuario de la base de datos del FabLab
    searchuser - busca a un usuario en la base de datos del FabLab
    doorpermit - entrega permisos de acceso a un usuario del FabLab
"""

async def help_c(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=help_text)
