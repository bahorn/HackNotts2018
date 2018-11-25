from flask import Flask
from flask_assistant import Assistant, tell, ask

import random

app = Flask(__name__)
assist = Assistant(app, route='/actions/')

b = "Alfa, Bravo, Charlie, Delta, Echo, Foxtrot, Golf, Hotel, India, Juliett, Kilo, Lima, Mike, November, Oscar, Papa, Quebec, Romeo, Sierra, Tango, Uniform, Victor, Whiskey, X-ray, Yankee, Zulu".split(', ')

c = 0
lines = open('../fresh.txt').read().split('\n')

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

@assist.action('message')
def main_action(message):
    print('>',message)
    response = fetch_response(message)
    return ask(response)
