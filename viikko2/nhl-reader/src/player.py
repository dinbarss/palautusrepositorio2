class Player:
    def __init__(self, player_data):
        self.name = player_data["name"]
        self.nationality = player_data["nationality"]
        self.assists = player_data["assists"]
        self.goals = player_data["goals"]
        self.team = player_data["team"]

    def __str__(self):
        return (
            f"{self.name:20}{self.team:15}"
            f"{self.goals} + {self.assists} = {self.goals + self.assists}"
        )

    @property
    def points(self):
        return self.goals + self.assists
