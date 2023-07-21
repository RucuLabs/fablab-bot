import logging

from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler, CommandHandler, MessageHandler, filters
from brain.modules.data.FabLabRepository import FabLabRepository


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

NAME = range(1)

async def add_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    try:
        user = update.message.from_user.username
        db = FabLabRepository()
        if(db.get_role("@" + user) == "Super"):
            user_id = context.args[0]
            context.user_data["id"] = user_id
            await update.message.reply_text(
                "Ingrese nombre completo del nuevo admin. Para cancelar escriba /cancel"
            )
            return NAME
        else:
            await update.message.reply_text(
                "No tienes permisos suficientes."
            )
            return ConversationHandler.END

    except Exception as ex:
        logger.info("Error: %s", ex)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Hubo un error, falta parámetro de usuario.")

        return ConversationHandler.END


async def name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores name and ends the conversation."""
    name = update.message.text
    context.user_data["name"] = name
    logger.info("Received name: %s %a",  name, context.user_data["id"])
    db = FabLabRepository()
    db.add_pending(context.user_data["id"], context.user_data["name"], "Admin")
    await update.message.reply_text("Se agrego al admin " + context.user_data["id"] + " " + context.user_data["name"])

    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    await update.message.reply_text(
        "Operación cancelada"
    )

    return ConversationHandler.END

add_admin_handler = ConversationHandler(
    entry_points=[CommandHandler("addadmin", add_admin)],
    states={
        NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, name)],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)