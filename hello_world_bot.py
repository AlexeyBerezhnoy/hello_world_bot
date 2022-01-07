import os
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Updater


token = os.environ["TELEGRAM_BOT_TOKEN"]

updater = Updater(token=token, use_context=True)

dispatcher = updater.dispatcher

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello World!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
updater.idle()

