import logging

from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler, CommandHandler, MessageHandler, filters
from brain.modules.data.FabLabRepository import FabLabRepository

logger = logging.getLogger(__name__)

NAME = range(1)

async def add_pending(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    try:
        id = update.message.from_user.id
        db = FabLabRepository()
        if((db.get_role(id) == "Admin") or (db.get_role(id) == "Super")):
            user_id = context.args[0]
            context.user_data["id"] = user_id
            await update.message.reply_text(
                "Ingrese nombre completo del usuario. Para cancelar escriba /cancel"
            )
            return NAME
        else:
            await update.message.reply_text(
                "No tienes permisos suficientes."
            )
            return ConversationHandler.END

    except Exception as ex:
        logger.error("Error: %s", ex)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Hubo un error, falta parámetro de usuario.")

        return ConversationHandler.END


async def name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores name and ends the conversation."""
    name = update.message.text
    context.user_data["name"] = name
    logger.info("Received name: %s %a",  name, context.user_data["id"])
    db = FabLabRepository()
    db.add_pending(context.user_data["id"], context.user_data["name"], "Default")
    await update.message.reply_text("Se agrego al usuario " + context.user_data["id"] + " " + context.user_data["name"] + " a la lista de pendientes." )

    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    await update.message.reply_text(
        "Operación cancelada"
    )

    return ConversationHandler.END

add_pending_handler = ConversationHandler(
    entry_points=[CommandHandler("adduser", add_pending)],
    states={
        NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, name)],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)