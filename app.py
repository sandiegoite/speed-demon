from flask import Flask
app = Flask(__name__)

@app.route('/')
def greeting():
    i=0
    welcome = ""
    for chr in str("Hello world !"):
        i+= 1
        welcome += ("\n" + " "* i + chr)
    return welcome
