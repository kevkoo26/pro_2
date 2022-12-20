import random


# taten auslesen lassen, nur "read"-Zugriff
def auslesen_taten():
    with open("taten.csv", "r") as open_file:
        inhalt = open_file.read()
    return inhalt


def taten_laden():
    taten = auslesen_taten()  # Taten auslesen lassen und als "taten" speichern
    taten_liste = taten.split("\n")  # taten werden bei einem Umbruch gesplittet und als Liste gespeichert
    neue_liste = []  # eine neue Liste wird erstellt
    for eintrag in taten_liste:
        tat = eintrag.split("\n")  # alle Einträge in der taten_liste werden als gesamte Zeile bei einem neuen
        # Zeilenumbruch gesplittet. Somit werden die Inhalte als ganze Sätze ausgegeben.
        neue_liste.append(tat)  # die "ganzen" Sätze werden zur neuen, leeren Liste hinzugefügt.
    auswahl = random.choice(neue_liste)  # durch die Random-Funktion wird ein zufälliger Satz ausgegeben
    return auswahl


def taten_laden_liste():
    taten = auslesen_taten()
    taten_liste = taten.split("\n")
    taten_liste = reversed(taten_liste)  # Die Liste wird dadurch verkehrt ausgegeben, die neusten Inhalte ganz oben.
    return taten_liste


def abspeichern_tat(eigene_tat):
    current_content = auslesen_taten()
    new_content = current_content + f"\n{eigene_tat}"
    with open("taten.csv", "w") as open_file:
        open_file.write(new_content)


# Wahrheiten auslesen lassen, nur "read"-Zugriff
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


def wahrheiten_laden_liste():
    wahrheiten = auslesen_wahrheiten()
    wahrheiten_liste = wahrheiten.split("\n")
    wahrheiten_liste = reversed(wahrheiten_liste)
    return wahrheiten_liste


def abspeichern_wahrheit(eigene_wahrheit):
    current_content = auslesen_wahrheiten()
    new_content = current_content + f"\n{eigene_wahrheit}"
    with open("wahrheiten.csv", "w") as open_file:
        open_file.write(new_content)


def elements():
    inhalt = auslesen_wahrheiten()
    neue_liste = []
    count = 0
    for eintrag in inhalt:
        wahrheit = eintrag.split("\n")
        neue_liste.append(wahrheit)
        count += 1
    return str(count)
