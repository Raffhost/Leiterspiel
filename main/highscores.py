import json
from config import HIGHSCORE_FILE

class Highscores:
    def __init__(self, file=HIGHSCORE_FILE):
        self._highscore_file = file
        self._highscore = []

    def display(self):
        print("Highscores:")
        for str in self._highscore:
            print(f"{str['name']}: {str['count']}")

    def add_highscore(self, name, level):
        self._highscore.append({"name": name, "count": level})

    def save_highscores(self):
        with open(self._highscore_file, "w") as json_file:
            json.dump(self._highscore, json_file)
