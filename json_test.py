import json

object = [{"name": "Bakera", "count": 1}, {"name": "Kaiser", "count": 2}]


# json.dump() Bekommt einen j_object und schreibt ihn direkt in j_file
with open("test.json", "w") as file:
    json.dump(object, file)

# json.dumps() Setzt einen j_object in json Zeile um, aber braucht noch write dazu
with open("test.json", "w") as file: 
    file.write(json.dumps(object))

# json.load() Liest j_file und gibt einen Python-Object zurück
with open("test.json", "r") as file:
    object = json.load(file)

# json.loads() Setzt eine json Zeile in Python-Object um, aber braucht noch read dazu
with open("test.json", "r") as file:
    object = json.loads(file.read())



# Alle git Befehle die ich brauche:
'''
git --global user.name "Name"           # Initialisiert den Namen für git
git --global user.email "Email"         # Initialisiert die Email für git
git init                                # Erstellt ein neues git Repository
git clone <repository>                  # Kopiert ein git Repository von github auf den Computer
git add .   oder   git add <file>       # Fügt Dateien zum Commit hinzu, entweder alle oder einzelne
git commit -m "Message"                 # Speichert die Änderungen mit einer Nachricht
git push                                # Läd die Änderungen auf github hoch
git pull                                # Läd die Änderungen von github herunter
git status                              # Zeigt was geändert wurde (nur Dateinamen), nicht committet
git diff                                # Zeigt was genau geändert wurde (Code Zeilen), nicht committet
git log                                 # Zeigt die Historie aller Commits an
git branch   oder   git branch <name>   # Zeigt alle Branches an, oder erstellt einen
git checkout <branch>                   # Wechselt zu einem anderen Branch
'''
