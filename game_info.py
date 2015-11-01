import random
import time

class GameInfo:
    'Class that contains the game state.'

    def __init__(self, host, players):
        self.host = host
        players.append(host)
        self.players = players
        self.location = get_location()
        self.time = get_time_in_minutes()

    def get_location():
        locations = ['beach', 'others']
        return random.choice(locations)

    def get_time_in_minutes(players):
        if len(players) > 4:
            return 8
        return 7

    def start_game():
        while self.time:
            minutes, seconds = divmod(t, 60)
            time.sleep(1)
            self.time -= 1
