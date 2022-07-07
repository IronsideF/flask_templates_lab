from crypt import methods
from app import app
from flask import render_template, request, redirect
from models.event_list import *


@app.route('/events')
def index():
    return render_template('index.html', title='Event List', all_events=event_list)

@app.route('/events', methods=['POST'])
def add_event():
    date = request.form['date']
    name = request.form['name']
    guest_num = request.form['guest_num']
    room = request.form['room']
    desc = request.form['desc']
    new_event = Event(date, name, guest_num, room, desc)
    add_new_event(new_event)
    return redirect('/events')