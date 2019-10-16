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
events.drop()

# √
@app.route('/')
def test():
    return render_template('index.html', msg='Hiiiii', events=events.find())

# # VIEWING event homepage
# @app.route('/event')
# def event_display():
#     return render_template('index.html', events=events.find())



# √
# ADD A NEW EVENT
@app.route('/event/add')
def event_add():
    '''go to event creation form'''
    return render_template('event_add.html')




# VIEW A CREATED EVENT
@app.route('/event/detail', methods=['POST'])
def event_detail():
    event={
        'title': request.form.get('title'),
        'description': request.form.get('description')
    }
    event_id = events.insert_one(event).inserted_id
    return redirect(url_for('test', event_id=event_id))



# # Route to VIEW ONE event
# @app.route('/event/detail/<event_id>')
# def event_show_detail(event_id):
#     """Show a one event"""
#     event = events.find_one({'_id': ObjectId(event_id)})
#     return render_template('index.html', event=event, events=events)





if __name__ == "__main__":
    app.run(Debug=True)