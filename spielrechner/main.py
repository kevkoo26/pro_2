from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
import daten
import plotly.express as px
from plotly.offline import plot

from spielrechner.daten import abspeichern_tat, abspeichern_wahrheit

app = Flask("Jassen")


@app.route("/")
def start():
    return render_template("index.html", seitentitel="Start")


@app.route("/tat_oder_wahrheit")
def spiel_beginnen():
    return render_template("tat_oder_wahrheit.html", seitentitel="Tat oder Wahrheit")


@app.route("/spiel_beginnen/", methods=['GET', 'POST'])
def spiel_speichern():
    if request.method == 'POST':
        spielname = request.form['spielname']
        zeitpunkt, spielname = daten.spiel_speichern(spielname)
        return redirect(url_for("mitspieler_speichern", game_id=zeitpunkt))

    return render_template("add_game.html", seitentitel="Spiel hinzufügen")


@app.route("/spieler_hinzufügen/", methods=['GET', 'POST'])
@app.route("/spieler_hinzufügen/<game_id>", methods=['GET', 'POST'])
def mitspieler_speichern(game_id=None):
    if not game_id:
        return redirect(url_for("spiel_speichern"))
    spiele = daten.spiele_laden()
    print(spiele)
    aktuelles_spiel = spiele[game_id]
    if request.method == "GET":

        print(aktuelles_spiel)
        aktuelle_spieler = aktuelles_spiel["mitspieler"].keys()
        for spieler in aktuelle_spieler:
            print(aktuelles_spiel["mitspieler"][spieler])
        return render_template("add_player.html", seitentitel="Spieler hinzufügen")

    if request.method == 'POST':
        spielername = request.form['spielername']
        aktuelles_spiel["mitspieler"].keys() == spielername
        return "nope"


@app.route("/punkterechner")
def punkterechner():
    return render_template("punkterechner.html", seitentitel="Punkterechner")


@app.route("/statistik")
def statistik():
    spielname = daten.spiele_laden()

    spielname_liste = []
    for key, value in spielname.items():
        zeile = "Spielzeitpunkt: " + str(key) + ": " + str(value)
        spielname_liste.append(zeile)

    x = "Markus", "Hans", "Lisa", "Kevin", "Sarah", "Linda"
    y = 5, 4, 9, 13, 1, 7
    fig = px.bar(x=x, y=y)
    div = plot(fig, output_type="div")

    return render_template("statistic.html", barchart=div, seitentitel="Statistik")


@app.route("/tat")
def tat():
    taten = daten.taten_laden()
    return render_template("tat.html", liste=taten, seitentitel="tat")


@app.route("/tat_hinzufügen/", methods=['GET', 'POST'])
def tat_hinzufügen():
    if request.method == "GET":
        return render_template("tat_hinzufügen.html", seitentitel="Tat eingeben")

    if request.method == 'POST':
        eigene_tat = request.form['tat_hinzufügen']
        print(f"Request Form Tat hinzufügen: {eigene_tat}")
        abspeichern_tat(eigene_tat)
        return redirect(url_for("tat_hinzufügen"))


@app.route("/wahrheit")
def wahrheit():
    wahrheiten = daten.wahrheiten_laden()
    return render_template("wahrheit.html", liste=wahrheiten, seitentitel="wahrheit")


@app.route("/wahrheit_hinzufügen/", methods=['GET', 'POST'])
def wahrheit_hinzufügen():
    if request.method == "GET":
        return render_template("wahrheit_hinzufügen.html", seitentitel="Wahrheit eingeben")

    if request.method == 'POST':
        eigene_wahrheit = request.form['wahrheit_hinzufügen']
        print(f"Request Form Wahrheit hinzufügen: {eigene_wahrheit}")
        abspeichern_wahrheit(eigene_wahrheit)
        return redirect(url_for("wahrheit_hinzufügen"))


@app.route("/liste")
def auflisten():
    spielname = daten.spiele_laden()

    spielname_liste = []
    for key, value in spielname.items():
        zeile = "Spielzeitpunkt: " + str(key) + ": " + str(value)
        spielname_liste.append(zeile)
        länge = len(spielname_liste)
        print(länge)

    print("Es wurden bereits", len(spielname_liste), "Spiele gespielt")

    return render_template("spielerliste.html", liste=spielname_liste)


if __name__ == "__main__":
    app.run(debug=True, port=5006)
