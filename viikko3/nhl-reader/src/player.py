class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
    
    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"Player(name='{self.name}', \
nationality='{self.nationality}', \
assists='{self.assists}', \
goals='{self.goals}', \
penalties='{self.penalties}', \
team='{self.team}', \
games='{self.games}')"

