class Team:
    def __init__(self, name_of_player, number_of_players, name_of_coach):
        self.name = name_of_player
        self.players = number_of_players
        self.coach = name_of_coach
        
        name_of_coach = "John Candy"
    
    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, player_name):
        for player in self.players:
            if player_name == player:
                return True
        return False 


    






