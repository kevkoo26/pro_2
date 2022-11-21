def auslesen():
    with open("database.csv", "r") as open_file:
        inhalt = open_file.read()
    return inhalt


def abspeichern(aufgabe, deadline):
    current_content = auslesen()
    new_content = current_content + f"\n{aufgabe}, {deadline}"
    with open("database.csv", "w") as open_file:
        open_file.write(new_content)


def auslesen():
    with open("spielerliste.csv", "r") as open_file:
        inhalt = open_file.read()
    return inhalt


def abspeichern(firstname, lastname):
    current_content = auslesen()
    new_content = current_content + f"\n{firstname}, {lastname}"
    with open("spielerliste.csv", "w") as open_file:
        open_file.write(new_content)
