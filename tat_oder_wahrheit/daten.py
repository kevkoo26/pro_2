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
    return taten_liste


def abspeichern_tat(eigene_tat):
    current_content = auslesen_taten()
    new_content = current_content + f"\n{eigene_tat}" #der Neue Content soll auf einer neuen Zeile geschrieben werden
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
    return wahrheiten_liste


def abspeichern_wahrheit(eigene_wahrheit):
    current_content = auslesen_wahrheiten()
    new_content = current_content + f"\n{eigene_wahrheit}"
    with open("wahrheiten.csv", "w") as open_file:
        open_file.write(new_content)


def eintrag_loeschen(text, listen_name):  # Um Einträge aus der Liste zu entfernen
    if listen_name == "wahrheit":
        inhalt = wahrheiten_laden_liste()
        index = inhalt.index(text)  # es wird der Ort gesucht, an welchem sich das zu löschende Element befindet. Dieses wird anschliessend als Index deklariert.
        del inhalt[index]  # das Element Index und somit der gewünschte Inhalt wird aus der Liste entfernt.
        inhalt = inhalt[:-1]  # die Liste soll nun vom erstem bis letzten Element wieder alles erneut anzeigen.
        with open("wahrheiten.csv", "w") as open_file:
            for line in inhalt: #die "neue" Liste soll wieder angezeigt werden.
                open_file.write(line + "\n")
                if line in inhalt == "":
                    del line
    if listen_name == "tat":
        inhalt = taten_laden_liste()
        index = inhalt.index(text)
        del inhalt[index]
        inhalt = inhalt[:-1]
        with open("taten.csv", "w") as open_file:
            for line in inhalt:
                open_file.write(line + "\n")
