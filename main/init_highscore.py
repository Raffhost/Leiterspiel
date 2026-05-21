import json

json_obj = [
    {"name": "Bakera",       "count": 1},
    {"name": "Kaiser",       "count": 2}
]

with open("highscores.json", "w") as json_file:
    json.dump(json_obj, json_file)

