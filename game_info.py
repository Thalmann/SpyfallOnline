import random

class GameInfo:
    'Class that contains the game state.'

    def __init__(self):
        self.location = get_location()

    def get_location():
        locations = ['beach', 'others']
        return random.choice(locations)
