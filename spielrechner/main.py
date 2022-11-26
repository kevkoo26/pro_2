from flask import Flask
from flask import render_template
from flask import request

from spielrechner.datenbank import auslesen, abspeichern, spielers_laden

app = Flask("Jassen")


@app.route("/")
def start():
    return render_template("index.html", seitentitel="Start")


@app.route("/add_player", methods=["GET", "POST"])
def add_player():
    if request.method == "GET":
        return render_template("add_player.html", seitentitel="Spieler hinzufügen")

    if request.method == "POST":
        real_name = request.form['real_name']
        player_name = request.form['player_name']
        print(f"Request Form real_name: {real_name}")
        print(f"Request Form player_name: {player_name}")
        abspeichern(real_name, player_name)
        return render_template("add_player.html", seitentitel="Spieler hinzufügen")


@app.route("/mitspieler")
def new():
    spielers = spielers_laden()
    return render_template("mitspieler.html", liste=spielers, seitentitel="mitspieler")

    spielers = auslesen()
    mitspieler.html = spielers.replace("\n", "<br>")
    spieler_liste = spielers.split("\n")
    neue_liste = []
    for spieler in spieler_liste:
        real_name, player_name = spieler.split(",")
        neue_liste.append([real_name, player_name])
    print(neue_liste)
    return render_template("mitspieler.html", liste=neue_liste)


@app.route("/vergangenheit")
def past_games():
    return render_template("past_games.html", seitentitel="vergangene")


if __name__ == "__main__":
    app.run(debug=True, port=5007)
