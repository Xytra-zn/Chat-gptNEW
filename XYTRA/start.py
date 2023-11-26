from pyrogram import Client, filters

# Initialize the Pyrogram client
bot = Client("my_bot", bot_token="6526084223:AAHRX5cIwWCyMN1vqmseXQXl1kNFFulevbs", api_id="6435225", api_hash="4e984ea35f854762dcde906dce426c2d")

@bot.on_message(filters.private & filters.command("start"))
async def welcome_dm(client, message):
    user_id = message.from_user.id
    welcome_msg = (
        "🌟 Hello there! Welcome to the Sasta Coder Bot! 🚀\n"
        "Feel free to use the available commands or ask for help. If you have any questions or need assistance, just let me know!"
    )

    await message.reply_text(welcome_msg, disable_web_page_preview=True)


@bot.on_message(filters.private & filters.command("help"))
async def help_command(client, message):
    # Help message with features
    help_msg = (
        "🚀 **Available Commands:**\n"
        "/start - Get a welcome message\n"
        "/help - Get information about available commands and how to use them\n\n"
        "💡 **Bot Features:**\n"
        "1. Sends a welcome message when you use /start\n"
        "2. Sends a leave message when someone exits the chat\n"
        "3. Responds to /help to provide information about available commands and features"
    )

    await message.reply_text(help_msg, disable_web_page_preview=True)
    
