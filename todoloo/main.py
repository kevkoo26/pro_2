from flask import Flask
from flask import render_template
from flask import request

from todoloo.datenbank import abspeichern, auslesen

app = Flask("todoloo")


@app.route("/")
def start():
    todos = auslesen()
    todos_html = todos.replace("\n", "<br>")
    todo_liste = todos.split("\n")
    neue_liste = []
    for eintrag in todo_liste:
        aufgabe, deadline = eintrag.split(",")
        neue_liste.append([aufgabe, deadline])
    print(neue_liste)
    return render_template("index.html", liste=neue_liste)


@app.route("/add", methods=["GET", "POST"])
def add_new_todo():
    if request.method == "GET":
        return render_template("todo_form.html")

    if request.method == "POST":
        aufgabe = request.form['aufgabe']
        deadline = request.form['deadline']
        print(f"Request Form Aufgabe: {aufgabe}")
        print(f"Request Form Deadline: {deadline}")
        abspeichern(aufgabe, deadline)
        return "funktioniert"


@app.route('/grid', methods=["GET", "POST"])
def add_player():
    if request.method == "GET":
        return render_template("grid.html")

    if request.method == "POST":
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        print(f"Request Form Vorname: {firstname}")
        print(f"Request Form Nachname: {lastname}")
        abspeichern(firstname, lastname)
        return render_template("grid.html")


@app.route('/grid')
def players():
    players = auslesen()
    players_html = players.replace("\n", "<br>")
    player_liste = players.split("\n")
    neue_liste = []
    for spieler in player_liste:
        firstname, lastname = spieler.split(",")
        neue_liste.append([firstname, lastname])
    print(neue_liste)
    return render_template("grid.html", liste=neue_liste)


@app.route('/players')
def neu():
    players = auslesen()
    players_html = players.replace("\n", "<br>")
    player_liste = players.split("\n")
    neue_liste = []
    for spieler in player_liste:
        firstname, lastname = spieler.split(",")
        neue_liste.append([firstname, lastname])
    print(neue_liste)
    return render_template("players.html", liste=neue_liste)


if __name__ == "__main__":
    app.run(debug=True, port=5003)
