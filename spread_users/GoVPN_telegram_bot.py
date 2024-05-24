

"""I need usernames and passwords of my users in telegram...
so I write this program get a backup of mikrotik and find information of users and send it in a telegram bot
"""

import logging
import re
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

def spread_users():
    try:
        file = open("users2.txt" , 'r')
        text = file.read()
        result = re.findall('name=.*password=.....'  ,  text)
        file.close()
    except:
        print("error")
    users = {}
    for item in result:
        user , password = item.split(' ')
        user = user.split('=')[1]
        password = password.split('=')[1]
        users[user] = password
    
    return users

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")

async def get_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /get is issued."""
    users = spread_users()
    for user , passw in users.items():
        await update.message.reply_text(f"user: {user}\npass: {passw}\n\n")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("7048848485:AAHRTZZQZ9SzfO6c2SceYhuplS780OcJ0po").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("get", get_command))
    application.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()