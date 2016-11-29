import os
import sys
import json
import random

import requests
from flask import Flask, request
from matplotlib.delaunay.testfuncs import data

app = Flask(__name__)


@app.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == os.environ["VERIFY_TOKEN"]:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world: lets see if this changes", 200


@app.route('/', methods=['POST'])
def webhook():

    greetings = ['HI', 'Hi', 'hi', 'HELLO', 'Hello', 'hello', 'HEY', 'Hey', 'hey', 'HOW ARE YOU']
    reversed_word_list = ['reversed', 'reverse', 'backwards']
    asking_word_list = ['what', 'whats', "what's", 'when', 'whens', "when's"]

    ai_greetings_word_list = ["Hi", "Hello", "Howdy", "Sup my dude"]

    # endpoint for processing incoming messaging events

    data = request.get_json()
    log(data)  # you may not want to log every incoming message in production, but it's good for testing

    if data["object"] == "page":

        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:

                if messaging_event.get("message"):  # someone sent us a message

                    sender_id = messaging_event["sender"]["id"]        # the facebook ID of the person sending you the message
                    recipient_id = messaging_event["recipient"]["id"]  # the recipient's ID, which should be your page's facebook ID
                    message_text = messaging_event["message"]["text"]  # the message's text

                    message_words = message_text.split(' ', 1)
                    message_text_split = message_text.split
                    command = message_words[0]
                    message_text_length = len(message_text.split(' '))




                    if len(message_words) > 1:
                        text = message_words[1]
                    else:
                        text = ""

                    if message_text in greetings:
                        # new_message_text = message_text_length

                        new_message_text = '{}, how can I help you today? \nEvent dates: \nEnter other things here later'.format(random.choice(ai_greetings_word_list))

                    elif command == 'reverse':
                        new_message_text = "reversed: {}".format(text[::-1])

                    elif message_text.split(" ")[0] in asking_word_list:
                        new_message_text = "I know you are asking a question but im not that smart yet!"
                        test_message = test_function()


#                     elif message_text != "":
#                         while message_text_split_length != 0:
#                             if message_text_split[message_text_split_length] in ['what', 'why']:
#                                 new_message_text_thing = 'I know you are asking a question but im not that smart yet!'
                    
#                             else:
#                                 pass
#                         new_message_text = new_message_text_thing

                    else:
                        new_message_text = 'echo: {}'.format(message_text)

                    send_message(sender_id, '{}'.format(new_message_text))
                    if message_text.split(" ")[0] in asking_word_list:
                        send_message(sender_id, '{}'.format(test_message))

                if messaging_event.get("delivery"):  # delivery confirmation
                    pass

                if messaging_event.get("option"):  # option confirmation
                    pass

                if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message
                    pass

    return "ok", 200


def test_function(test_message):
    if data["object"] == "page":

        for entry in data["entry"]:

            for messaging_event_two in entry["messaging"]:
                if messaging_event_two.get("message"):
                    sender_id = messaging_event_two["sender"]["id"]
                    recipient_id_two = messaging_event_two["recipient"]["id"]
                    message_text_two = messaging_event_two["message"]["text"]

                    return 'test'

                    # send_message(sender_id, 'hello my good friend')
                if messaging_event_two.get("delivery"):
                    pass

                if messaging_event_two.get("option"):
                    pass

                if messaging_event_two.get("postback"):
                    pass


def send_message(recipient_id, message_text):

    log("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))

    params = {
        "access_token": os.environ["PAGE_ACCESS_TOKEN"]
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": message_text
        }
    })
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        log(r.status_code)
        log(r.text)


# def question_asking(message_text):
#     message_text = message_text.split
#     message_text_length = len(message_text)
#     while message_text != 0:
#         if message_text[message_text_length] in ['what', 'whats', "what's", 'when', 'whens', "when's"]:
#
#             return message_text




def log(message):  # simple wrapper for logging to stdout on heroku
    print(str(message))
    sys.stdout.flush()


if __name__ == '__main__':
    app.run(debug=True)
