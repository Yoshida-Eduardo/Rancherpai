import os
import logging
from command_handler import handle_command
from telegram.ext import Updater, MessageHandler, Filters

#AUTHORIZED CHAT ID

AUTHORIZED_CHAT=os.environ.get('AUTHORIZED_CHAT')
TELEGRAM_BOT_TOKEN=os.environ.get('TELEGRAM_BOT_TOKEN')

def parse_bot_commands(message):
  command, sep, tail = message.partition(" @")
  return command.strip('/')

def respond_command(bot, update):
  command = parse_bot_commands(update.message.text)
  response = handle_command(command)
  bot.send_message(chat_id=update.message.chat_id, text=response)

if __name__ == "__main__":
  updater = Updater(token=TELEGRAM_BOT_TOKEN)
  # updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True) for version 12
  logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                         level=logging.INFO)

  dispatcher = updater.dispatcher
  #TODO USE TELEGRAM.EXT.COMMANDHANDLER INSTEAD OF MessageHandler
  # REQUIRES REFACTORING OF command_handler.py functions
  handler = MessageHandler(Filters.chat(int(AUTHORIZED_CHAT)) & Filters.entity('mention'), respond_command)
  dispatcher.add_handler(handler)

  updater.start_polling(poll_interval=1)
  print("Rancher Bot is running!")
