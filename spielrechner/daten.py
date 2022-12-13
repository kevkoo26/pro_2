import random
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


def mitspieler_speichern(spielername):
    datei_name = "spielenamen.json"
    punkte = 0
    spieldaten = (aktuelles_spiel["mitspieler"].keys())
    speichern(datei_name, punkte, spieldaten)
    return spielername, punkte


def spiele_laden():
    datei_name = "spielenamen.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt


def auslesen():
    with open("taten.csv", "r") as open_file:
        inhalt = open_file.read()
    return inhalt


def taten_laden():
    taten = auslesen()
    taten_liste = random.choice(taten.split("\n"))
    neue_liste = []
    for eintrag in taten_liste:
        tat = eintrag.split(" ")
        neue_liste.append([tat])
    return neue_liste
    # taten = auslesen()
    # taten_liste = random.choice(taten.split("\n"))
    # return taten_liste


def abspeichern(eigene_tat):
    current_content = auslesen()
    new_content = current_content + f"\n{eigene_tat}"
    with open("taten.csv", "w") as open_file:
        open_file.write(new_content)