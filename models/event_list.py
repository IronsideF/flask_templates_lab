from models.event import Event

event_1 = Event('2019-07-05', "Keith's Birthday", 15, '1', 'A birthday bash for Keith', True)
event_2 = Event('2007-05-12', "Sky's Graduation", 73, '9', 'Sky graduates college', False)
event_3 = Event('2021-12-23', "Ben's Christmas Party", 3, '4', 'An intimate gathering for christmas', True)

event_list = [event_1, event_2, event_3]

def add_new_event(event):
    event_list.append(event)

def find_event_by_name(name):
    for event in event_list:
        if event.name == name:
            return event

def remove_event(name):
    event_list.remove(find_event_by_name(name))
