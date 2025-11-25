import random


game_name = "The Mirror"
print(f"Welcome to {game_name}!")  
print(f"{'=' * (len(game_name) + 13)}")

name = "Antonio"
print(f"Great! Your character's name is {name}.")

player = {
    "name": name,
    "health": 100,
    "coin": 67   # still starting with 67 coins
}

events = ["find a coin", "meet a monster", "do nothing"]

# randomly choose one event
event = random.choice(events)
print(f"While exploring, you {event}!")

if event == "find a coin":
    player["coin"] += 1
    print(f"{player['name']} found a coin, {player['name']} now has {player['coin']} coins.")
elif event == "meet a monster":
    player["health"] -= 10
    print(f"{player['name']} got hurt during the combat with monster, health is now {player['health']}.")
else:
    # do nothing
    pass