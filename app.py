import os
import sys
import json
import random
import csv

import re
import requests
from flask import Flask, request


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
    # endpoint for processing incoming messaging events

    ai_greetings_word_list = ["Hi", "Hello", "Howdy", "Sup my dude"]

    data = request.get_json()
    log(data)  # you may not want to log every incoming message in production, but it's good for testing

    if data["object"] == "page":

        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:

                if messaging_event.get("message"):  # someone sent us a message

                    sender_id = messaging_event["sender"]["id"]  # the facebook ID of the person sending you the message
                    recipient_id = messaging_event["recipient"]["id"]  # the recipient's ID, which should be your page's facebook ID
                    message_text = messaging_event["message"]["text"]  # the message's text

                    if re.match(r'.*hello|hey|hi(?!reverse|reversed|backwards)', message_text, re.I):
                        send_message(sender_id, "{}, how can I help you today?".format(random.choice(ai_greetings_word_list)))

                    elif re.match(r'.*what|when|date|who|where', message_text, re.I):
                        if re.match(r'.*what', message_text, re.I):
                            question_message_text = "I know you are asking a question but I'm not that smart yet! :what"

                        elif re.match(r'.*when|date', message_text, re.I):
                            question_message_text = "I know you are asking when something is, but I'm not that smart yet!"

                        elif re.match(r'.*who', message_text, re.I):
                            question_message_text = "I know you are asking about someone, but I'm not that smart yet!"

                        elif re.match(r'.*where', message_text, re.I):
                            question_message_text = "I know you are asking where something is, but I'm not that smart yet!!"
                            if re.match(r'.*building|library|hall|lab', message_text, re.I):
                                pass
                            elif re.match(r'.*map', message_text, re.I):
                                send_message(sender_id, "here is a map!\n https://www.facebook.com/l.php?u=https%3A%2F%2Fmaps.jcu.edu.au%2Fcampus%2Ftownsville%2F&h=JAQEGOwnq&s=1&enc=AZPrNaWH_-wfCoY3B3YLHSBXj7rQSTOlUQpj7vXz_sdjW20781VLb6km7oC_LjAGYgLJusluHOgjHqN4xba_rDgsg7Chi6porGvizTKLFMmwHg&__mref=message_bubble")



                        else:
                            question_message_text = "I don't even know how you got here"
                        send_message(sender_id, "{}".format(question_message_text))

                    elif re.match(r'.*reverse|reversed|backwards', message_text, re.I):
                        if len(message_text.split(" ")) > 1:
                            text = message_text.split(" ")[1]
                        else:
                            text = " "
                        send_message(sender_id, "Reversed: {}".format(text[::-1]))

                    elif re.match(r'.*id', message_text):
                        send_message(sender_id, recipient_id)

                    else:
                        send_message(sender_id, "I don't know what you are saying! you said this: {}".format(message_text))



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


def times_greeted(times_greeted):
    with open("test.csv"):
        times_greeted += 1
        delimit_file = csv.reader(file, delimiter=",")
        times_greeted = []
        for line in delimit_file:
            times_greeted.append(line)



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