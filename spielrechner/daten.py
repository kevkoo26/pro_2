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


def auslesen_taten():
    with open("taten.csv", "r") as open_file:
        inhalt = open_file.read()
    return inhalt


def taten_laden():
    taten = auslesen_taten()
    taten_liste = taten.split("\n")
    neue_liste = []
    for eintrag in taten_liste:
        tat = eintrag.split("\n")
        neue_liste.append(tat)
    auswahl = random.choice(neue_liste)
    return auswahl


def abspeichern_tat(eigene_tat):
    current_content = auslesen_taten()
    new_content = current_content + f"\n{eigene_tat}"
    with open("taten.csv", "w") as open_file:
        open_file.write(new_content)


def auslesen_wahrheiten():
    with open("wahrheiten.csv", "r") as open_file:
        inhalt = open_file.read()
    return inhalt


def wahrheiten_laden():
    wahrheiten = auslesen_wahrheiten()
    wahrheiten_liste = wahrheiten.split("\n")
    neue_liste = []
    for eintrag in wahrheiten_liste:
        wahrheit = eintrag.split("\n")
        neue_liste.append(wahrheit)
    auswahl = random.choice(neue_liste)
    return auswahl


def abspeichern_wahrheit(eigene_wahrheit):
    current_content = auslesen_wahrheiten()
    new_content = current_content + f"\n{eigene_wahrheit}"
    with open("wahrheiten.csv", "w") as open_file:
        open_file.write(new_content)
