class Player:
    def __init__(self, name, team, goals, assists):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists

    @property
    def points(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name} {self.team} {self.goals} + {self.assists} = {self.points}"

    def __repr__(self):
        return f"Player(name: {self.name}, team: {self.team}, goals: {self.goals}, assists: {self.assists})"

    def __eq__(self, other):
        if isinstance(other, Player):
            return self.__dict__ == other.__dict__
        return NotImplemented
