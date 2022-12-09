from datetime import datetime
import json


def speichern(datei, key, value):
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[str(key)] = value

    # print(datei_inhalt)

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)


def spiel_speichern(spielname):
    datei_name = "spielenamen.json"
    zeitpunkt = datetime.now()
    spieldaten = {
        "name": spielname,
        "mitspieler": {
            "spielername": {
                "Punkte": {},
                "Anzahl_Spiele": {}
            }
        }
    }
    speichern(datei_name, zeitpunkt, spieldaten)
    return zeitpunkt, spielname


def mitspieler_speichern(spielername, spielname):
    datei_name = "spielenamen.json"
    zeitpunkt = datetime.now()
    spieldaten = {
        "name": spielname,
        "mitspieler": {
            spielername: {
                "Punkte": {},
                "Anzahl_Spiele": {}
            }
        }
    }
    speichern(datei_name, zeitpunkt, spieldaten)
    return zeitpunkt, spielname, spielername


def spiele_laden():
    datei_name = "spielenamen.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt
