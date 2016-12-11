# coding=utf-8
import os
import sys
import json
import random
from modules.people_module import PeopleIndex
from modules.location_module import LocationIndex
from modules.date_module import DateIndex
from modules.what_module import WhatIndex

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

                    sender_id = messaging_event["sender"]["id"]  # the facebook ID of the person sending you the message
                    recipient_id = messaging_event["recipient"]["id"]  # the recipient's ID, which should be your page's facebook ID
                    message_text = messaging_event["message"]["text"]  # the message's text
                    if "?" in message_text:
                        message_text = message_text[:-1]
                    else:
                        pass
                    last_word_used = message_text

                    #### Testing area

                    with open("last_name_message.csv") as last_name:
                        for line in last_name:
                            if message_text in line and len(message_text) >= 3:

                                last_name.write(line)
    # TODO finish this, make it so it saves all names to a csv file
                    # with open("peoplelist.csv") as peoplelist:
                    #     for line in peoplelist:
                    #         if message_text in line and len(message_text) >= 3:
                    #             last_name_used = line.split(", ")[0]
                    #             # with open("last_name_message.csv") as last_name_message:
                    #             #     last_name_message.write(line)
                    #         else:
                    #             last_name_used = "unused"

                    last_name_message(last_name)

                    # with open("name_save.json", 'r') as name_save:
                    #     send_message(sender_id, str(json.load(name_save)))

                    # TODO fix this, i need it to save the last name used, but right now it is resetting it every
                        # message TODO, so it prints the variable stated above


# TODO fix this so that it takes and remembers only names without causing errors

                    print last_word_used
                    print last_name_message(latest_name='')

                    ###
                    reply = get_reply(message_text, last_word_used)
                    send_message(sender_id, reply)

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

def last_name_message(latest_name):
    with open("last_name_message.csv", "r") as last_name_message:
        for line in last_name_message:
            latest_name = line.split(', ')[:1]
        return latest_name
# TODO make it so this gets latest entry from the csv file

def get_last_name_used(message_text):
    with open("peoplelist.csv") as peoplelist:
        for line in peoplelist:
            if message_text in line and len(message_text) >= 3:
                last_name_used = line.split(", ")[0]
                return last_name_used


def get_reply(message_text, last_word_used):
    ai_greetings_word_list = ["Hi", "Hello", "Howdy", "Sup my dude"]

    if re.match(r'.*hello|hey|hi|yo(?!reverse|reversed|backwards)', message_text, re.I):
        return "{}, how can I help you today?".format(random.choice(ai_greetings_word_list))

    elif re.match(r'.*what', message_text, re.I):
        if re.match(r'.*email', message_text, re.I):
            what_words = WhatIndex(message_text)
            what_words.email_passer(last_word_used)
            return str(what_words)

        else:
            return "I know you are asking a question but I'm not that smart yet! :what"

    # TODO fix it so it take last input(list_test) or (last_name_used)

    elif re.match(r'.*when|whens|date|exam|exams', message_text, re.I):
        date_words = DateIndex(message_text)
        if message_text in open("datelist.csv").read():
            date_words.date_passer(message_text)
            return str(date_words)
        elif re.match(r'.*exam|exams', message_text, re.I):
            date_words.exam_list_passer(message_text)
            return str(date_words)
        else:
            date_words.date_passer(message_text)
            return str(date_words)

    elif message_text >= 5 and message_text in open("examlist.csv").read():
        date_words = DateIndex(message_text)
        date_words.exam_list_passer(message_text)
        return str(date_words)
# TODO fix this, its broken

    elif message_text >= 5 and message_text in open("datelist.csv").read():
        date_words = DateIndex(message_text)
        date_words.date_passer(message_text)
        return str(date_words)

    elif re.match(r".*who|whos|who's", message_text, re.I):
        if message_text in open("peoplelist.csv").read():
            people_words = PeopleIndex(message_text)
            people_words.people_passer(message_text)
            return str(people_words)
        else:
            who_words = PeopleIndex(message_text)
            who_words.change_words_to_jerry(message_text)
            return str(who_words)

    elif len(message_text) >= 3 and message_text in open("peoplelist.csv").read():
        with open("peoplelist.csv") as peoplelist:
            for line in peoplelist:
                if message_text in line:
                    return "What about {}?".format(line.title().split(", ")[0])

    elif re.match(r".*map|where|wheres|where's|building|looking|look [0-354]", message_text, re.I):
        if message_text in open("buildinglist.csv").read():
            location_words = LocationIndex(message_text)
            location_words.location_name_passer(message_text)
            return str(location_words)
        else:
            location_words = LocationIndex(message_text)
            location_words.location_passer(message_text)
            return str(location_words)

    elif len(message_text) >= 5 and message_text in open("buildinglist.csv").read():
        location_words = LocationIndex(message_text)
        location_words.location_name_passer(message_text)
        return str(location_words)

    elif re.match(r'.*reverse|reversed|backwards', message_text, re.I):
        if len(message_text.split(" ")) > 1:
            if re.match(r".*reverse", message_text, re.I):
                text = message_text[8:]
            else:
                text = message_text[9:]
        else:
            text = " "
        return "Reversed: {}".format(text[::-1])

    elif re.match(r'.*last message', message_text, re.I):
        return last_word_used

    # elif re.match(r'.*last name used', message_text, re.I):
    #     return last_name_used

    elif re.match(r".*version", message_text, re.I):
        """"add number to this every time you push it"""
        return "version 28"

    elif re.match(r'.*help', message_text, re.I):
        return "Ask me where a certain building is, ask for a map, or about someone(im not a very good bot so i only know a few people(try Daniel))"

    elif re.match(r'.*allan|cameron|cam|sanio|jesse|ramisa|remi', message_text, re.I):
        if re.match(r'.*allan', message_text, re.I):
            return "Allan you are a drongo"
        elif re.match(r".*cameron|cam", message_text, re.I):
            return "Rena loves yogurt"
        elif re.match(r".*sanio", message_text, re.I):
            return "Sorry"
        elif re.match(r".*jesse", message_text, re.I):
            return "heres Jesse's number; 0412263945"
        else:
            return "ａｅｓｔｈｅｔｉｃ"

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
