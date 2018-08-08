from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def sign_up():
    return render_template( 'hello1.html')

@app.route('/home')
def home_page():
    return render_template( 'hello.html')

app.run(debug=True)
