# modules/start_module.py

from telegram import Update, ParseMode
from telegram.ext import CallbackContext
from messages import WELCOME_MESSAGE

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(WELCOME_MESSAGE, parse_mode=ParseMode.MARKDOWN)
  
