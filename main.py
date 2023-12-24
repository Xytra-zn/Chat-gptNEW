from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from XYTRA import start_module, help_module, message_module
from config import TOKEN

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Add command handlers from modules
    dispatcher.add_handler(CommandHandler("start", start_module.start))
    dispatcher.add_handler(CommandHandler("help", help_module.help_command))

    # Add message handlers from modules
    dispatcher.add_handler(MessageHandler(Filters.text | Filters.voice, message_module.process_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
