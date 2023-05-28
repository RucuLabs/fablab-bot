from telegram import Update
from telegram.ext import ContextTypes
from brain.modules.data.FabLabRepository import FabLabRepository

# Checks DB status, creates and gets test user.
async def health(update: Update, context: ContextTypes.DEFAULT_TYPE):
    db = FabLabRepository()
    msg = "Database is "
    try:
        db.add_user("1337", "test")
        if (db.get_user("1337").name == "test"):
            msg += "healthy."
        else:
            msg += "unhealthy."


    except:
        msg += "unhealthy."

    await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)
