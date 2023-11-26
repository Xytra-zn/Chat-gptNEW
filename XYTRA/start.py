from pyrogram import Client, filters

# Initialize the Pyrogram client
bot = Client(
    "my_bot",
    bot_token="6526084223:AAHRX5cIwWCyMN1vqmseXQXl1kNFFulevbs",
    api_id="6435225",
    api_hash="4e984ea35f854762dcde906dce426c2d"
)

# Define the /start command
@bot.on_message(filters.private & filters.command("start"))
async def welcome_dm(client, message):
    user_id = message.from_user.id
    welcome_msg = (
        "🌟 Hello there! Welcome to the Sasta Coder Bot! 🚀\n"
        "Feel free to use the available commands or ask for help. If you have any questions or need assistance, just let me know!"
    )

    await message.reply_text(welcome_msg, disable_web_page_preview=True)

# Start the bot
if __name__ == "__main__":
    bot.run()
