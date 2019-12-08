from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import json
import requests

updater = Updater(token='969240756:AAEdpmAVfy8-w9_oUnA9mGL9GSk9kmGykuY', use_context=True)

dispatcher = updater.dispatcher
logging.basicConfig ( format = ' % (asctime) s - % (nom) s - % (levelname)s - % (message)s' ,
                      level = logging.INFO )

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello I am a bot !")
    context.bot.send_message(chat_id=update.effective_chat.id, text="I can tell you the number of forks from the repository of Fedora-Infra")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Just give me the repository name!")

def echo(update, context):
    msg_client=update.message.text
    response = requests.get("https://api.github.com/orgs/fedora-infra/repos")
    repo_infos = response.json()

    for repo in repo_infos:
        if repo['name'].upper() == msg_client.upper():
            msg_bot="The "+str(repo['name'])+" repository have been forks "+str(repo['forks'])+" Times."
            context.bot.send_message(chat_id=update.effective_chat.id, text=msg_bot)
            return 
    context.bot.send_message(chat_id=update.effective_chat.id, text="The "+str(msg_client)+" repository not found.")

start_handler = CommandHandler('start' , start) 
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
