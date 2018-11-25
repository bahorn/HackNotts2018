from flask import Flask
from flask_ask import Ask, session, statement, question

import random

app = Flask(__name__)
ask = Ask(app, '/alexa/')

c = 1
lines = open('../fresh.txt').read().split('\n')

def approx_match(user_input, sentence):
    split_user = user_input.split(' ')
    split_sentence = sentence.split(' ')
    count = 0
    for i in split_user:
        if i in split_sentence: count += 1
    return (count/split_sentence) > 0.8

def fetch_response(input_message):
    global c
    result = lines[c]
    c = c+2 % len(lines) 
    return "message {}".format(result)
    #return "message hodor"
    sentence = []
    for _ in range(5):
        sentence.append(random.choice(b))
    return 'message {}'.format(' '.join(sentence))
    #
    if approx_match(input_message, "maybe I'll be tracer"):
        return "I'm already Tracer"
    elif approx_match(input_message, "What about Widowmaker?"):
        return "I'm already Widowmaker"
    elif approx_match(input_message, "I'll be Bastion"):
        return "Nerf Bastion"
    return input_message+' a'

# Trigger the partner.
@ask.launch
def launched():
    return question('message hello')

# Get data
@ask.intent('message')
def message(main):
    response = fetch_response(main)
    return question(response)
