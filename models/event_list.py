from models.event import Event

event_1 = Event('21/06/2019', "Keith's Birthday", 15, '1', 'A birthday bash for Keith')
event_2 = Event('30/09/2007', "Sky's Graduation", 73, '9', 'Sky graduates college')
event_3 = Event('23/12/2021', "Ben's Christmas Party", 3, '4', 'An intimate gathering for christmas')

event_list = [event_1, event_2, event_3]

def add_new_event(event):
    event_list.append(event)

