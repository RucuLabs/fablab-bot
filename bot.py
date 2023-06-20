import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, CommandHandler, ContextTypes, ConversationHandler, MessageHandler

import brain

import os
from dotenv import load_dotenv

# get bot token from .env file
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')



if __name__ == '__main__':
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    
    # command handlers

    # app commands
    start_handler = CommandHandler('start', brain.start)
    help_handler = CommandHandler('help', brain.help_c)
    help_admin_handler = CommandHandler('helpadmin', brain.help_admin)
    health_handler = CommandHandler('health', brain.health)
    
    # door commands
    open_handler = CommandHandler('open', brain.open_door)
    door_permit_handler = CommandHandler('doorpermit', brain.add_door_permit)
    
    # user commands
    add_pending_handler = brain.add_pending_handler # adduser pendiente
    add_admin_handler = brain.add_admin_handler # add admin
    edit_user_handler = CommandHandler('edituser', brain.edit_user)
    delete_user_handler = CommandHandler('deleteuser', brain.delete_user)
    search_user_handler = CommandHandler('searchuser', brain.search_user)
    list_users_handler = CommandHandler('listusers', brain.list_users)
    join_pending_handler = CommandHandler('join', brain.join_pending)
    confirm_pending_handler = CallbackQueryHandler(brain.confirm_pending)
    
    # adding handlers to app

    # app commands
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(help_admin_handler)
    application.add_handler(health_handler)
    
    # door commands
    application.add_handler(open_handler)
    application.add_handler(door_permit_handler)
    
    # user commands
    application.add_handler(add_pending_handler)
    application.add_handler(add_admin_handler)
    application.add_handler(edit_user_handler)
    application.add_handler(delete_user_handler)
    application.add_handler(search_user_handler)
    application.add_handler(list_users_handler)
    application.add_handler(join_pending_handler)
    application.add_handler(confirm_pending_handler)

    application.run_polling()
