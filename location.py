class Location:
    'Class that describes a location and the roles associated with it.'

    def __init__(self, number_of_players):
        self.roles = get_roles(number_of_players)
