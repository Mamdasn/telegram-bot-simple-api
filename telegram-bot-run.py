from flask.wrappers import Response
from flask import Flask
from flask import request, abort
from telegram_bot_api import parse_message, \
                                send_message, \
                                deleteMessage, \
                                editMessageText
from xposedornot_api import check_password

from credentials import config

token = config.TG_BOT_TOKEN

app = Flask(__name__)

def manage_messages(msg):
    parsed_message = parse_message(msg)
    chat_id, message_info, chat_type = parsed_message
    if chat_type == 'message':
        handle_message(chat_id, message_info)
        
def handle_commands(message):
    if message == '/start':
        reply = ''' Hey,
Send me your password to cross check it over the <a href='https://xposedornot.com/'><b>xposedornot.com</b></a> dataset to check whether your password has been already exposed.
'''
    else:
        count, wordlist = check_password(message)
        if count!=None:
            reply = f"How many times it has been repeated in password breaches: {count}"
    return reply
    
def handle_message(chat_id, message_info):
    message, message_id = message_info
    reply = handle_commands(message) 
    r = send_message(
            chat_id=chat_id, 
            text=reply,
            reply_to_message_id=message_id,
            )
    print(r)
    
@app.route('/', methods=['POST'])
def index():
    message = request.get_json(force=True)
    print(message)
    manage_messages(message)
    return Response('Ok', status=200)

def main():
    pass
 

if __name__ == "__main__": 


    app.run(host="0.0.0.0", port=5000)

