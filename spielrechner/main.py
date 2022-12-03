from flask import Flask
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
        rueckgabe_string = "Gespeichert: " + spielname + " um " + str(zeitpunkt)
        return rueckgabe_string

    return render_template("add_game.html")


@app.route("/spieler_hinzufügen/", methods=['GET', 'POST'])
def mitspieler_speichern():
    if request.method == 'POST':
        spielername = request.form['spielername']
        zeitpunkt, spielername = daten.mitspieler_speichern(spielername)
        rueckgabe_mitspieler = "Gespeichert: " + spielername + " um " + str(zeitpunkt)
        return rueckgabe_mitspieler

    return render_template("add_player.html")


@app.route("/liste")
def auflisten():
    spielname = daten.spielenamen_laden()

    spielname_liste = ""
    for key, value in spielname.items():
        zeile = str(key) + ": " + value + "<br>"
        spielname_liste += zeile

    return render_template("mitspieler.html", liste=spielname_liste)


if __name__ == "__main__":
    app.run(debug=True, port=5006)
