import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import brain

import os
from dotenv import load_dotenv

# get bot token from .env file
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    
    # command handlers

    # app commands
    start_handler = CommandHandler('start', brain.start)
    help_handler = CommandHandler('help', brain.help_c)
    
    # door commands
    open_handler = CommandHandler('open', brain.open_door)
    door_permit_handler = CommandHandler('doorpermit', brain.add_door_permit)
    
    # user commands
    add_user_handler = CommandHandler('adduser', brain.add_user)
    edit_user_handler = CommandHandler('edituser', brain.edit_user)
    delete_user_handler = CommandHandler('deleteuser', brain.delete_user)
    search_user_handler = CommandHandler('searchuser', brain.search_user)
    list_users_handler = CommandHandler('listusers', brain.list_users)
    
    # adding handlers to app

    # app commands
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    
    # door commands
    application.add_handler(open_handler)
    application.add_handler(door_permit_handler)
    
    # user commands
    application.add_handler(add_user_handler)
    application.add_handler(edit_user_handler)
    application.add_handler(delete_user_handler)
    application.add_handler(search_user_handler)
    application.add_handler(list_users_handler)

    application.run_polling()
