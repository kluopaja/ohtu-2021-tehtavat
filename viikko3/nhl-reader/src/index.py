#!/usr/bin/env python
from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    sorted_finnish = stats.top_scorers_by_nationality("FIN")
    
    print("Finnish players sorted by total points (descending):");
    for player in sorted_finnish:
        print(player)

if __name__ == "__main__":
    main()
