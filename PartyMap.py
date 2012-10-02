from flask import Flask, redirect, request
import pdb
from flask.globals import current_app
from flask import render_template
from mongoengine import connect

app = Flask(__name__)
connect('celebmap')

@app.route("/")
def access():
    return render_template('PARTYMAP_HTML_TEST.html')
        
    
if __name__ == "__main__":
    app.debug = True
    app.run()
