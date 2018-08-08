from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def sign_up():
    exersices=["PULL UP" , "PUSH-UP ", "MUCLE UP ", "SIT UP ", "PLANCHE ", "SQUAT , PISTOL SQUAT  " , "HANDSTAND PUSH-UP","FRONT LEVER , BACK LEVER", "SUPERMAN PUSH-UP","HUMAN FLAG" ]
    return render_template(
     "hello1.html",
     exersices=exersices)

@app.route('/home')
def home_page():
    return render_template( 'hello.html')

app.run(debug=True)
