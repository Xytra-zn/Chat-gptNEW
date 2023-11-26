import random
from XYTRA.messages import welcome_msgs
from XYTRA.exit import exit_msgs

@bot.on_message(filters.group & filters.new_chat_members)
async def welcome_new_members(client, message):
    chat_id = message.chat.id
    for user in message.new_chat_members:
        # Check if the new member has a username
        username = user.username or "New Member"
        # Generate a random welcome message
        welcome_msg = random.choice(welcome_msgs).format(username=username)
        # Send the welcome message to the group
        await bot.send_message(chat_id, welcome_msg)

@bot.on_message(filters.group & filters.left_chat_member)
async def send_exit_message(client, message):
    chat_id = message.chat.id
    user = message.left_chat_member
    # Check if the leaving member has a username
    username = user.username or "Former Member"
    # Generate a random exit message
    exit_msg = random.choice(exit_msgs).format(username=username)
    # Send the exit message to the group
    await bot.send_message(chat_id, exit_msg)
