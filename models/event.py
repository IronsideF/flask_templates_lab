from unicodedata import name


class Event:
    def __init__(self, _date, _name, _number_of_guests, _room, _description):
        self.date = _date
        self.name= _name
        self.guest_num = _number_of_guests
        self.room = _room
        self.desc = _description
