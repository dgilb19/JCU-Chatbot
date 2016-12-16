# coding=utf-8
import os
import sys
import json
import random
from modules.people_module import PeopleIndex
from modules.location_module import LocationIndex
from modules.date_module import DateIndex
from modules.what_module import WhatIndex
# from modules.timetable_module import TimetableIndex

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
    ###
    people_name = tuple()
    building_name = tuple()
    class_name = tuple()


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

                    with open("peoplelist.csv") as peoplelist:
                        for line in peoplelist:
                            if message_text in line and len(message_text) >= 3:
                                with open("last_name_message.csv", 'w') as last_name:
                                    last_name.write(line.split(", ")[0])

                    with open("buildinglist.csv") as buildinglist:
                        for line in buildinglist:
                            if message_text in line and len(message_text) >= 3:
                                with open("last_building_message.csv", 'w') as last_building:
                                    last_building.write(line.split(", ")[0])

                    with open("peoplelist.csv") as people_name_list:
                        for line in people_name_list:
                            line = line.split(", ")[0]
                            people_name += tuple(line.split(", "))
                            line = line.split(" ")
                            people_name += tuple(line)

                    with open("buildinglist.csv") as building_name_list:
                        for line in building_name_list:
                            line = line.split(", ")[1]
                            building_name += tuple(line.split(", "))
                            line = line.split(" ")
                            for part in line:
                                if len(part) >= 5:
                                    building_name += tuple(line)


                    with open("classlist.csv") as class_name_list:
                        for line in class_name_list:
                            line = line.split(", ")[-1].strip("\n")
                            print line
                            if line not in class_name:
                                class_name += tuple(line.split(", "))

                    print class_name

                    # print last_name_message(latest_name='')
                    # print building_name

                    reply = get_reply(message_text, people_name, building_name)
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
    with open("last_name_message.csv", "r") as last_name:
        for line in last_name:
            latest_name = line
        return latest_name


def last_building_message(latest_building):
    with open("last_name_message.csv", "r") as last_building:
        for line in last_building:
            latest_building = line
        return latest_building


def get_reply(message_text, people_name, building_name):
    ai_greetings_word_list = ["Hi", "Hello", "Howdy", "Sup my dude"]

    if re.match(r'hello|hey|hi|yo(?!reverse|reversed|backwards)', message_text, re.I):
        return "{}, how can I help you today?".format(random.choice(ai_greetings_word_list))

    elif re.match(r'.*what', message_text, re.I):
        what_words = WhatIndex(message_text)
        if re.match(r'.*email', message_text, re.I):
            for name in people_name:
                if name in message_text:
                    what_words.email_passer_with_name(name)
                    return str(what_words)
            else:
                what_words.email_passer(last_name_message(latest_name=''))
                return str(what_words)

        elif re.match(r'.*happening|going on|today', message_text, re.I):
            return "there is nothing going on today, go home"

        else:
            return "I know you are asking a question but I'm not that smart yet! :what"


#### TODO: make this work
    elif re.match(r'.*when|.*whens|.*date|.*exam|.*exams', message_text, re.I):
        date_words = DateIndex(message_text)
        if re.match(r'.*class|.*lecture|.*practical|.*prac', message_text, re.I):
                date_words.next_class_passer()
                return str(date_words)
        elif re.match(r'.*exam', message_text, re.I):
            # date_words.exam_passer(message_text)
            # return str(date_words)
            with open("examlist.csv") as examlist:
                for line in examlist:
                    if line.split(", ")[0] in message_text:
                        return "the {} exam is on the {}".format(line.split(", ")[0], str(line.split(', ')[1]))
                else:
                    return "this aint workin"
        else:
            date_words.date_passer(message_text)
            return str(date_words)
####

    elif message_text >= 5 and message_text in open("examlist.csv").read():
        date_words = DateIndex(message_text)
        date_words.exam_list_passer(message_text)
        return str(date_words)

    elif message_text >= 5 and message_text in open("datelist.csv").read():
        date_words = DateIndex(message_text)
        date_words.date_passer(message_text)
        return str(date_words)

    elif re.match(r".*who|who's", message_text, re.I):
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

    elif re.match(r".*map|.*where|.*wheres|.*building|.*looking|.*look [0-354]", message_text, re.I):
        location_words = LocationIndex(message_text)

        if re.match(r'.*office|.*desk', message_text, re.I):
            for name in people_name:
                if name in message_text:
                    location_words.office_passer_with_name(name)
                    return str(location_words)
            else:
                location_words.office_passer_new(last_name_message(latest_name=''))
                return str(location_words)
        elif message_text in building_name:
                print "kekHHHHHHHHHHHHHH"
            # with open("buildinglist.csv") as buildinglist:
            #     for line in buildinglist:
            #         if line in message_text:
            #             location_words.location_name_passer(message_text)
            #             return "tjimgugj"
            #     building_name:
            #         if message_text in line:
            #     print "kek"

        else:
            print "not sure mate"
            print building_name
            location_words.location_passer(message_text)
            return str(location_words)

    elif any(message_text.find(s) >= 0 for s in building_name):
        location_words = LocationIndex(message_text)
        location_words.location_name_passer(message_text)
        return str(location_words)

    elif re.match(r'.*reverse|.*reversed', message_text, re.I):
        if len(message_text.split(" ")) > 1:
            if re.match(r".*reverse", message_text, re.I):
                text = message_text[8:]
            else:
                text = message_text[9:]
        else:
            text = " "
        return "Reversed: {}".format(text[::-1])
    elif re.match(r'.*timetable|.*schedule|.*class|.*practical|.*prac', message_text, re.I):
        if re.match(r'.*show', message_text, re.I):
            return 'http://i.imgur.com/wKBDSfM.png'
        else:
            return "what about your schedule?"

    elif re.match(r'.*help', message_text, re.I):
        return "Ask me where a certain building is, ask for a map, or about someone(im not a very good bot so i only " \
               "know a few people(try Daniel)) "

    elif re.match(r'allan|cameron|cam|sanio|jesse|ramisa|remi|bangarang', message_text, re.I):
        if re.match(r'.*allan', message_text, re.I):
            return "Allan you are a drongo"
        elif re.match(r".*cameron|cam", message_text, re.I):
            return "Rena loves yogurt"
        elif re.match(r".*sanio", message_text, re.I):
            return "Sorry"
        elif re.match(r".*jesse", message_text, re.I):
            return "heres Jesse's number; 0412263945"
        elif re.match(r'.*bangarang', message_text, re.I):
            return "Allan stop, thats not a word, its a skrillex song"
        else:
            return "ａｅｓｔｈｅｔｉｃ"

    elif re.match(r'exit|shut up|go away|ill end you', message_text, re.I):
        pass

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
