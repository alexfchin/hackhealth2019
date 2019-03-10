# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import Message, MessagingResponse
import urllib
import re
from google.cloud import translate


disease_list = []
f = ""
return_list = []

# Translates some text into Russian

app = Flask(__name__)

# Instantiates a client
translate_client = translate.Client()


def detect_language(text):
    result = translate_client.detect_language(text)
    return result['language']

def translate_text(text,target):
    translation = translate_client.translate(
        text,
        target_language=target)
    translatedText = str(translation['translatedText']).lower()
    return translatedText

@app.route("/", methods=['GET', 'POST'])
def hello():
    return ("Hey there!")

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    # The text to translate
    # The target language


    resp = MessagingResponse()
    text = str(request.values.get('Body', None))
    print(text)

    detected = detect_language(text)

    translation = translate_client.translate(
        text,
        target_language='en')
    translatedText = str(translation['translatedText']).lower()
    # print(u'Text: {}'.format(text))
    # print(u'Translation: {}'.format(translation['translatedText']))
    print(translatedText)

    #doctor, clinic
    csv_info = ''

    text = str(print_disease_symptoms(translatedText))
        #resp.message("You need a doctor")
    # Add a message
#    else:
#        csv_info = 'Unrecognized Symptom'
    print(text)

    translation = translate_client.translate(
        text,
        target_language=detected)

    translatedText = str(translation['translatedText']).lower()

    resp.message(translatedText)
    return str(resp)

counter = 0

def print_disease_symptoms(wanty):

    disease = []

    f = open("sheet.csv", "r")
    lines = f.readlines()
    print("file read")
    #fill in index of disease list an symptom list
    for i in lines:
        counter = 0
        curr_line = i.split(",")
        bunny = {"name": "","symptoms":[]}
        # curr_line is an array of words
        for j in curr_line:
            if counter == 0: #disease
                bunny["name"] = j.lower()
            else: #its a symptom
                if j != "" and j != "\n":
                    bunny["symptoms"].append(j.lower())
            counter += 1

        disease.append(bunny)

    for i in disease:
        if wanty == i["name"]:
            help = str(i['symptoms'])
            help = help.replace("'","")
            help = help.replace("[","")
            help = help.replace("]","")
            return "Here are " + i["name"] + " symptoms: " + help + ". Feel Better! See a doctor when you can!"

if __name__ == "__main__":
    app.run(debug=True)
