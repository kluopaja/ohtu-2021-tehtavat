#!/usr/bin/env python
from player import Player
import requests

def extract_nationality_players(players, nationality):
    result = []
    for player in players:
        if player.nationality == nationality:
            result.append(player)
    return result

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()
    
    players = []
    for player_dict in response:
        new_player = Player(name=player_dict['name'],
                            nationality=player_dict['nationality'],
                            assists=player_dict['assists'],
                            goals=player_dict['goals'],
                            penalties=player_dict['penalties'],
                            team=player_dict['team'],
                            games=player_dict['games'])
        players.append(new_player)

    
    finnish_players = extract_nationality_players(players, "FIN")
    sorted_finnish = sorted(finnish_players, key = lambda x: -(x.goals + x.assists))
    print("Finnish players sorted by total points (descending):");
    for player in sorted_finnish:
        print(player)

if __name__ == "__main__":
    main()
