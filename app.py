from flask import Flask, render_template, request, url_for, redirect
import requests
import os
from random import random
from pymongo import MongoClient
from bson.objectid import ObjectId


app = Flask(__name__)


client = MongoClient()
db=client.Eventuu  
events = db.events

@app.route('/')
def test():
    return render_template('index.html', msg='Hiiiii')

# add event page
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
    event_id = events.insert_one(event).inserted_id
    return redirect(url_for('event_view', event_id=event_id))

# Route to VIEW ONE event
@app.route('/event/<event_id>')
def event_show(event_id):
    """Show a one event"""
    event = events.find_one({'_id': ObjectId(event_id)})
    return render_template('event_view.html', event=event, events=events)



if __name__ == "__main__":
    app.run(Debug=True)