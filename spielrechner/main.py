from flask import Flask
from flask import render_template
from flask import request
import plotly.express as px
from plotly.offline import plot

from Spielrechner.datenbank import abspeichern, auslesen


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
        return "funktioniert"



if __name__ == "__main__":
    app.run(debug=True, port=5008)
