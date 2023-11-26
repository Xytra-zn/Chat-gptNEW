import random
from pyrogram import Client, filters

from XYTRA.welcome import welcome_msgs
from XYTRA.exit import exit_msgs

# Create a new Pyrogram client (replace 'your_token' with your actual bot token)
bot = Client("my_bot", bot_token="6526084223:AAHRX5cIwWCyMN1vqmseXQXl1kNFFulevbs")

@bot.on_message(filters.group & filters.new_chat_members)
async def welcome_new_members(client, message):
    chat_id = message.chat.id
    for user in message.new_chat_members:
        # Generate a random welcome message
        welcome_msg = random.choice(welcome_msgs)
        # Send the welcome message to the group
        await bot.send_message(chat_id, welcome_msg)

@bot.on_message(filters.group & filters.left_chat_member)
async def send_exit_message(client, message):
    chat_id = message.chat.id
    user = message.left_chat_member
    # Generate a random exit message
    exit_msg = random.choice(exit_msgs)
    # Send the exit message to the group
    await bot.send_message(chat_id, exit_msg)

# Start the bot
bot.run()

