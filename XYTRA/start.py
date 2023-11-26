from pyrogram import filters

@bot.on_message(filters.private & filters.command("start"))
async def welcome_dm(client, message):
    user_id = message.from_user.id
    welcome_msg = (
        "🌟 Hello there! Welcome to the Sasta Coder Bot! 🚀\n"
        "Feel free to use the available commands or ask for help. If you have any questions or need assistance, just let me know!"
    )

    await message.reply_text(welcome_msg, disable_web_page_preview=True)
  
