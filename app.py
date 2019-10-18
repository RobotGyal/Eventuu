from flask import Flask, render_template, request, url_for, redirect
import os
import requests
from random import random
from pymongo import MongoClient
from bson.objectid import ObjectId

# FRAMEWORK SETUP
app = Flask(__name__)
host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Eventuu')
client = MongoClient(host=f'{host}?retryWrites=false')
db=client.get_default_database()

# DATABASES
events = db.events
time_blocks = db.time_blocks
time_blocks.drop()
events.drop()



# √
@app.route('/')
def home():
    return render_template('index.html', msg='Hiiiii', events=events.find())


# EVENTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ADD A NEW EVENT
@app.route('/event/add')
def event_add():
    '''go to event creation form'''
    return render_template('event_add.html')


# VIEW A CREATED EVENT
@app.route('/event/detail', methods=['POST'])
def event_detail():
    '''shows a single created event on a homepage'''
    event={
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'date':request.form.get('date'),
        's_time':request.form.get('s_time'),
        'e_time':request.form.get('e_time')
    }
    event_id = events.insert_one(event).inserted_id
    return redirect(url_for('home', event_id=event_id))


#Route for editing events
@app.route('/event/<event_id>/edit')
def event_edit(event_id):
    """Show the edited event"""
    event = events.find_one({'_id': ObjectId(event_id)})
    return render_template('event_edit.html', event=event, title='Edit')


#Route for updating event details
@app.route('/event/<event_id>', methods=['POST'])
def event_update(event_id):
    """For submitting a event once it's been edited"""
    updated_event = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'date':request.form.get('date'),
        's_time':request.form.get('s_time'),
        'e_time':request.form.get('e_time')
    }
    events.update_one(
        {'_id': ObjectId(event_id)},
        {'$set': updated_event})
    return redirect(url_for('home', event_id=event_id))


# Route to VIEW ONE event
@app.route('/event/detail/<event_id>')
def event_show_detail(event_id):
    """Show one event"""
    event = events.find_one({'_id': ObjectId(event_id)})
    event_time_blocks = time_blocks.find({'event_id': ObjectId(event_id)})
    return render_template('event_view.html', event=event, time_blocks=event_time_blocks)

# Route to delete an event
@app.route('/event/<event_id>/delete', methods=['POST'])
def event_delete(event_id):
    """Delete one event"""
    events.delete_one({'_id': ObjectId(event_id)})
    return redirect(url_for('home'))

# TIME BLOCKS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@app.route('/event/time_blocks', methods=['POST'])
def time_block_new():
    '''Create a new time block to be iterively added to event page'''
    time_block = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'event_id': ObjectId(request.form.get('event_id'))
    }
    print(time_block)
    time_block_id = time_blocks.insert_one(time_block).inserted_id
    print(time_block_id)
    return redirect(url_for('event_show_detail', event_id=request.form.get('event_id')))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))