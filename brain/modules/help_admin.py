from telegram import Update
from telegram.ext import ContextTypes

help_text = """
*Ayuda administradores*
Como administrador puedes moderar a los usuarios del FabLab.

*CRUD usuarios*
adduser @username - añade un usuario a la base de datos del FabLab
edituser @username - edita a un usuario de la base de datos del FabLab
deleteuser @username - borra un usuario de la base de datos del FabLab
searchuser @username - busca a un usuario en la base de datos del FabLab
listusers - muestra los ususarios registrados en la base de datos del FabLab

*Puerta*
doorpermit @username - entrega permisos de acceso a un usuario del FabLab
logdoor - entrega los últimos 10 movimientos hechos en la puerta
"""

async def help_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=help_text, parse_mode='Markdown')
