from flask import Flask
from flask_ask import Ask, statement

app = Flask(__name__)
ask = Ask(app, '/')

@ask.intent('hello')
def hello(name):
    speech_text = "Hello %s" % name
    return statement(speech_text).simple_card('Hello', speech_text)

if __name__ == '__main__':
    app.run()
