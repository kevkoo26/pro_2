def auslesen():
    with open("spielerliste.csv", "r") as open_file:
        inhalt = open_file.read()
    return inhalt


def abspeichern(real_name, player_name):
    current_content = auslesen()
    new_content = current_content + f"\n{real_name}, {player_name}"
    with open("spielerliste.csv", "w") as open_fle:
        open_fle.write(new_content)
