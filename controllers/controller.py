from app import app
from flask import render_template, request, redirect
from models.event_list import *


@app.route('/events')
def index():
    return render_template('index.html', title='Event List', all_events=event_list)
