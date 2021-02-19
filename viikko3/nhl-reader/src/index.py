#!/usr/bin/env python
from player import Player
import requests

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()
    
    players = []
    for player_dicts in response:
        players.append(Player(player_dicts['name']))

    print(players)
if __name__ == "__main__":
    main()
