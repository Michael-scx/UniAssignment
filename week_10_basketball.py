


def parse_game_log(score_log):
    game_dict = {}

    for entry in score_log:
        parts = entry.split("#")
        player = parts[0]
        play_type = parts[1]
        points = int(parts[2])

        
        if player not in game_dict:
            game_dict[player] = []
            
        game_dict[player].append((play_type, points))
    return game_dict

def print_player_totals(game_dict):
    for player, plays in game_dict.items():
        total_points = 0
        for play in plays:
            total_points+=play[1]
        print(f"{player}: {total_points} points total")



score_log = [
    "Jordan#Dunk#2",
    "Curry#3Pointer#3",
    "Jordan#FreeThrow#1",
    "LeBron#Layup#2",
    "Curry#Layup#2",
    "LeBron#3Pointer#3"
]
game_dict = parse_game_log(score_log)
print_player_totals(game_dict)




