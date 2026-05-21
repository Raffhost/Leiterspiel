import json
from config import HIGHSCORE_FILE

class Highscores:
    def __init__(self, file=HIGHSCORE_FILE):
        self._highscore_file = file
        self._highscores = []

    def display(self):
        print("Highscores:")
        for str in self._highscores:
            print(f"{str['name']}: {str['count']}")

    def add_highscore(self, name, level):
        self._highscores.append({"name": name, "count": level})

    def save_highscores(self):
        with open(self._highscore_file, "w") as json_file:
            json.dump(self._highscores, json_file)
