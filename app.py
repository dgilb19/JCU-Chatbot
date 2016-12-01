import os
import sys
import json
import random
from modules import location_module

import re

from flask import Flask, request
import requests


app = Flask(__name__)

# global LocationPasser


class Main:
    def __init__(self):
        self.location = location_module


#TODO make location things work so i can put where(location) part in different module


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
    # endpoint for processing incoming messaging events

    ai_greetings_word_list = ["Hi", "Hello", "Howdy", "Sup my dude"]

    data = request.get_json()
    log(data)  # you may not want to log every incoming message in production, but it's good for testing

    if data["object"] == "page":
        pass

        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                pass

                if messaging_event.get("message"):  # someone sent us a message
                    pass

                    sender_id = messaging_event["sender"]["id"]  # the facebook ID of the person sending you the message
                    recipient_id = messaging_event["recipient"]["id"]  # the recipient's ID, which should be your page's facebook ID
                    message_text = messaging_event["message"]["text"]  # the message's text

###

                    if re.match(r'.*hello|hey|hi(?!reverse|reversed|backwards)', message_text, re.I):
                        send_message(sender_id, "{}, how can I help you today?".format(random.choice(ai_greetings_word_list)))

                    elif re.match(r'.*what', message_text, re.I):
                        send_message(sender_id, "I know you are asking a question but I'm not that smart yet! :what")

                    elif re.match(r'.*when|date', message_text, re.I):
                        send_message(sender_id, "I know you are asking when something is, but I'm not that smart yet!")

                    elif re.match(r'.*who', message_text, re.I):
                        send_message(sender_id, "I know you are asking about someone, but I'm not that smart yet!")

                    elif re.match(r".*map|where|wheres|where's|building|looking|look", message_text, re.I):

                        send_message(sender_id, "{}".format(location_module.LocationPasser.process_message()))





                        # if re.match(r'.*map', message_text, re.I):
                        #     send_message(sender_id, "Here's a map! \nhttps://maps.jcu.edu.au/campus/townsville/")

                        # elif re.match(r'.*library|18', message_text, re.I):
                        #     send_message(sender_id, "Are you looking for the Library? \nhttps://maps.jcu.edu.au/campus/townsville/?location=18")
                        #
                        # elif re.match(r'.*Facility of Science and Engineering|Science and Engineering|17', message_text, re.I):
                        #     send_message(sender_id, "Are you looking for the Facility of Science and Engineering?\nhttps://maps.jcu.edu.au/campus/townsville/?location=17")
                        #
                        # elif re.match(r'.*pool|swim|swimming', message_text, re.I):
                        #     send_message(sender_id, "Are you looking for the pool man?\nhttps://maps.jcu.edu.au/campus/townsville/?location=241")
                        # else:
                        #     send_message(sender_id, "I know you are asking where something is, but I'm not that smart yet!!")

                    elif re.match(r'.*reverse|reversed|backwards', message_text, re.I):
                        if len(message_text.split(" ")) > 1:
                            text = message_text.split(" ")[1]
                        else:
                            text = " "
                        send_message(sender_id, "Reversed: {}".format(text[::-1]))

                    elif re.match(r'.*id', message_text):
                        send_message(sender_id, recipient_id)

                    else:
                        send_message(sender_id, "idk what you are saying")
                        # send_message(sender_id, "I don't know what you are saying! you said this: {}".format(message_text))


###
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


def get_reply(message_text):
    if re.match(r'.*hello|hey|hi(?!reverse|reversed|backwards)', message_text, re.I):
        return "Hello, how can I help you today?"

    elif re.match(r'.*what', message_text, re.I):
        return "I know you are asking a question but I'm not that smart yet! :what"

    elif re.match(r'.*when|date', message_text, re.I):
        return "I know you are asking when something is, but I'm not that smart yet!"

    elif re.match(r".*who|whos|who's", message_text, re.I):
        return "I know you are asking about someone, but I'm not that smart yet!"

    elif re.match(r".*map|where|wheres|where's", message_text, re.I):

        if re.match(r'.*map', message_text, re.I):
            return "Here's a map!"

        else:
            return "I know you are asking where something is, but I'm not that smart yet!!"
    elif re.match(r'.*reverse|reversed|backwards', message_text, re.I):
        if len(message_text.split(" ")) > 1:
            text = message_text.split(" ")[1]
        else:
            text = " "
        return "Reversed: {}".format(text[::-1])

    else:
        return "idk what you are saying"


def log(message):  # simple wrapper for logging to stdout on heroku
    print(str(message))
    sys.stdout.flush()


if __name__ == '__main__':
    app.run(debug=True)
