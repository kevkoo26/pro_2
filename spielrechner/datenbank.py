def auslesen():
    with open("mitspieler.csv", "r") as open_file:
        inhalt = open_file.read()
    return inhalt


def abspeichern(real_name, player_name):
    current_content = auslesen()
    new_content = current_content + f"\n{real_name}, {player_name}"
    with open("mitspieler.csv", "w") as open_fle:
        open_fle.write(new_content)


def spielers_laden():
    spielers = auslesen()
    spieler_liste = spielers.split("\n")
    neue_liste = []
    for eintrag in spieler_liste:
        real_name, player_name = eintrag.split(",")
        neue_liste.append([real_name, player_name])
    return neue_liste
