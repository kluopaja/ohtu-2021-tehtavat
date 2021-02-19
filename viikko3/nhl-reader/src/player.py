class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
    
    def get_points(self):
        return self.goals + self.assists

    def __str__(self):
        return f'{self.name:20} {self.team} {str(self.goals):2} + {str(self.assists):2} = {str(self.goals + self.assists):2}'

    def __repr__(self):
        return f"Player(name='{self.name}', \
nationality='{self.nationality}', \
assists='{self.assists}', \
goals='{self.goals}', \
penalties='{self.penalties}', \
team='{self.team}', \
games='{self.games}')"

