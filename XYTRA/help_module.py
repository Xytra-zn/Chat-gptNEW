# modules/help_module.py

from telegram import Update, ParseMode
from telegram.ext import CallbackContext
from messages import HELP_MESSAGE

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(HELP_MESSAGE, parse_mode=ParseMode.MARKDOWN)
  
