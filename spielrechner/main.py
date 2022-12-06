from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
import daten

app = Flask("Jassen")


@app.route("/")
def start():
    return render_template("index.html", seitentitel="Start")


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
        aktuelles_spiel["mitspieler"]['spielername'] = {
            "punkte"
        }
        zeitpunkt, spielername = daten.mitspieler_speichern(spielername)
        return "nope"




@app.route("/liste")
def auflisten():
    spielname = daten.spiele_laden()

    spielname_liste = []
    for key, value in spielname.items():
        zeile = str(key) + ": " + str(value) + "<br>"
        spielname_liste.append(zeile)

    return render_template("mitspieler.html", liste=spielname_liste)


if __name__ == "__main__":
    app.run(debug=True, port=5005)
