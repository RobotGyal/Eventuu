from flask import Flask, render_template, request, url_for, redirect
import requests
import os
from random import random
from pymongo import MongoClient

app = Flask(__name__)


client = MongoClient()
db=client.Eventuu  
events = db.events

@app.route('/')
def test():
    return render_template('index.html', msg='Hiiiii')

# add event
@app.route('/event/add')
def event_add():
    return render_template('event_add.html')

# add event
@app.route('/event/submit', methods=['POST'])
def event_submit():
    event={
        'title': request.form.get('title'),
        'description': request.form.get('description')
    }
    events.insert_one(event)
    return redirect(url_for('event_view.html'))



if __name__ == "__main__":
    app.run(Debug=True)