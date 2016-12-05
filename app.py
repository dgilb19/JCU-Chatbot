import os
import sys
import json
import random
from modules.people_module import PeopleIndex
from modules.location_module import LocationIndex
from modules.date_module import DateIndex

import re

from flask import Flask, request
import requests


app = Flask(__name__)


@app.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == os.environ["VERIFY_TOKEN"]:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world!", 200


@app.route('/', methods=['POST'])
def webhook():
    # endpoint for processing incoming messaging events

    data = request.get_json()
    log(data)  # you may not want to log every incoming message in production, but it's good for testing

    if data["object"] == "page":
        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                if messaging_event.get("message"):  # someone sent us a message
                    # opened_file = open('test.csv', 'r')

                    sender_id = messaging_event["sender"]["id"]  # the facebook ID of the person sending you the message
                    recipient_id = messaging_event["recipient"]["id"]  # the recipient's ID, which should be your page's facebook ID
                    message_text = messaging_event["message"]["text"]  # the message's text

                    reply = get_reply(message_text)
                    send_message(sender_id, reply)

                    # if re.match(r'.*log|logs|history', message_text, re.I):
                    #     pass
                    # else:

                    #     opened_file.write(message_text + ", ")
                    # opened_file.close()

                    # last_message = opened_file
                    # last_message


                    # opened_file_last_message.write(message_text)
                    # opened_file_last_message.close()




                # if messaging_event.get("delivery"):  # delivery confirmation
                #     pass
                #
                # if messaging_event.get("option"):  # option confirmation
                #     pass
                #
                # if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message
                #     pass
                    # going to leave this here in case i need it!

    return "ok", 200


def get_reply(message_text):
    ai_greetings_word_list = ["Hi", "Hello", "Howdy", "Sup my dude"]
    list_test = []
    full_list_test = []

    # if re.match(r'.*log|logs|history', message_text, re.I):
    #     pass
    # else:
    list_test.append(str(message_text))
    full_list_test.append(full_list_test + list_test)

    if re.match(r'.*hello|hey|hi(?!reverse|reversed|backwards)', message_text, re.I):
        return "{}, how can I help you today?".format(random.choice(ai_greetings_word_list))

    elif re.match(r'.*what', message_text, re.I):
        return "I know you are asking a question but I'm not that smart yet! :what"

    elif re.match(r'.*when|date', message_text, re.I):
        date_words = DateIndex(message_text)
        date_words.date_passer(message_text)
        return str(date_words)

    elif re.match(r".*who |whos |who's", message_text, re.I):
        who_words = PeopleIndex("")
        who_words.change_words_to_jerry(message_text)
        return str(who_words)

    elif re.match(r".*map|where|wheres|where's|building|looking|look [0-354]", message_text, re.I):
        location_words = LocationIndex(message_text)
        location_words.location_passer(message_text)
        return str(location_words)

    elif re.match(r'.*reverse|reversed|backwards', message_text, re.I):
        if len(message_text.split(" ")) > 1:
            text = message_text.split(" ")[1]
        else:
            text = " "
        return "Reversed: {}".format(text[::-1])

    elif re.match(r',*log', message_text, re.I):
        # with open("test.csv", "r") as opened_file:
        #     for line in opened_file:
        #         return line
        return str(list_test)

    elif re.match(r',*log list', message_text, re.I):
        # with open("test.csv", "r") as opened_file:
        #     for line in opened_file:
        #         return line
        return str(full_list_test)

    # elif re.match(r',*last message', message_text, re.I):
    #     with open("last_message.csv", "r") as opened_file_last_message:
    #         for line_last_message in opened_file_last_message:
    #             return line_last_message
    # TODO make function that can get the last user input(message_text)

    elif message_text in open("peoplelist.csv").read():
        people_words = PeopleIndex(message_text)
        people_words.people_passer(message_text)
        return str(people_words)

    else:
        return "idk what you are saying"
        # send_message(sender_id, "I don't know what you are saying! you said this: {}".format(message_text))


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


def log(message):  # simple wrapper for logging to stdout on heroku
    print(str(message))
    sys.stdout.flush()


if __name__ == '__main__':
    app.run(debug=True)
