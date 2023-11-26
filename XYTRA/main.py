import random
from XYTRA.welcome import welcome_msgs


@bot.on_message(filters.group & filters.new_chat_members)
async def welcome_new_members(client, message):
    chat_id = message.chat.id
    for user in message.new_chat_members:
        # Generate a random welcome message
        welcome_msg = get_welcome_message(username=user.username)
        # Send the welcome message to the group
        await bot.send_message(chat_id, welcome_msg)
        
