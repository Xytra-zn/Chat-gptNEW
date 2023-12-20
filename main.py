# main.py

import os
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackContext
from modules import start, help_module, message_module
from config import TOKEN

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Add command handlers from modules
    dispatcher.add_handler(CommandHandler("start", start_module.start))
    dispatcher.add_handler(CommandHandler("help", help_module.help_command))

    # Add message handler from message module
    dispatcher.add_handler(MessageHandler(Filters.all, message_module.process_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
  
