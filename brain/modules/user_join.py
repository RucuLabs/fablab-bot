import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackQueryHandler, ContextTypes, ConversationHandler, CommandHandler, MessageHandler, filters
from brain.modules.data.FabLabRepository import FabLabRepository

logger = logging.getLogger(__name__)

CONFIRM = range(1)

async def join_pending(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    try:
        user = update.message.from_user.username
        db = FabLabRepository()
        if db.is_pending('@' + user):
            keyboard = [
                [InlineKeyboardButton("Sí", callback_data="1")],
                [InlineKeyboardButton("No", callback_data="2")],
            ]

            reply_markup = InlineKeyboardMarkup(keyboard)

            pending_user = db.get_pending('@' + user)
            await update.message.reply_text(
                "Confirma tus datos con sí o no:\n{0}\n{1}\n ".format(pending_user.telegram_id, pending_user.name),
                reply_markup = reply_markup
            )
        else:
            await update.message.reply_text(
                "No has sido agregado por un admin."
            )


    except Exception as ex:
        logger.info("Error: %s", ex)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Hubo un error")

async def confirm_pending(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    db = FabLabRepository()
    query = update.callback_query  #respuesta boton
    await query.answer()
    pending_user = db.get_pending('@' + query.from_user.username)

    
    if query.data == "1":
        #join
        id_user = query.from_user.id
        db.add_user(id_user, pending_user.telegram_id, pending_user.name, pending_user.role)
        pending_user.delete_instance()  #Elimina

        
        await query.edit_message_text(text ="Has sido agregado.")
    elif query.data == "2":
        pending_user.delete_instance()  #Elimina
        await query.edit_message_text(text ="Se canceló tu creación de usuario, hable con un admin.")
