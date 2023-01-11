from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
import daten
import plotly.express as px
from plotly.offline import plot
from tat_oder_wahrheit.daten import abspeichern_tat, abspeichern_wahrheit

app = Flask("Tat oder Wahrheit")


@app.route("/")
def start():
    return render_template("index.html", seitentitel="Start")


@app.route("/tat_oder_wahrheit")
def spiel_beginnen():
    return render_template("tat_oder_wahrheit.html", seitentitel="Tat oder Wahrheit")


@app.route("/tat")
def tat():
    taten = daten.taten_laden()
    return render_template("tat.html", liste=taten, seitentitel="tat")


@app.route("/tat_hinzufügen/", methods=['GET', 'POST'])
def tat_hinzufügen():
    if request.method == "GET":  # eigene Taten, die hinzugefügt wurden, werden hier abgeholt und angezeigt in Liste.
        auflistung = daten.taten_laden_liste()
        number_of_taten = len(auflistung)
        return render_template("tat_hinzufügen.html", liste=auflistung, number_of_taten=number_of_taten,
                               seitentitel="Tat eingeben")

    if request.method == 'POST':  # Formular, welches die eingegebenen Taten abholt --> Eingaben werden abgespeichert.
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
    if request.method == "GET":  # eigene Wahrheiten, die hinzugefügt wurden, werden hier abgeholt und angezeigt in Liste.
        auflistung = daten.wahrheiten_laden_liste()
        number_of_wahrheiten = len(auflistung)
        return render_template("wahrheit_hinzufügen.html", liste=auflistung, number_of_wahrheiten=number_of_wahrheiten,
                               seitentitel="Wahrheit eingeben")

    if request.method == 'POST':  # Formular, welches die eingegebenen Wahrheiten abholt --> Eingaben werden abgespeichert.
        eigene_wahrheit = request.form['wahrheit_hinzufügen']
        print(f"Request Form Wahrheit hinzufügen: {eigene_wahrheit}")
        abspeichern_wahrheit(eigene_wahrheit)
        return redirect(url_for("wahrheit_hinzufügen"))


@app.route("/loeschen", methods=["GET", "POST"])
def loeschen():
    if "tat_löschen" in request.form:
        item = request.form['tat_löschen']
        daten.eintrag_loeschen(item, "tat") #Formular, welches via Butten das gewünschte Element aus der Liste löscht.
        return redirect(url_for("tat_hinzufügen"))
    if "wahrheit_löschen" in request.form:
        item = request.form['wahrheit_löschen']
        daten.eintrag_loeschen(item, "wahrheit")
        return redirect(url_for("wahrheit_hinzufügen"))

@app.route("/viz")  # Seite, welche anzeigt, ob eine Tat oder Wahrheit doppelt vorhanden ist.
def grafik():
    taten = daten.taten_laden_liste()
    inhalt = {}
    for tat in taten:
        if tat not in inhalt:
            inhalt[tat] = 1
        else:
            inhalt[tat] += 1  # Funktion nimmt Inhalte aus Liste und setzt 1 als Standardwert. Sollte Inhalt nochmals
            # vorkommen, wird eine 1 hinzugefügt, was Wert 2 ergibt und somit entsprechend in Grafik angezeigt wird.

    x = inhalt.values()
    y = inhalt.keys()

    fig = px.bar(x=x, y=y)
    div = plot(fig, output_type="div")

    wahrheiten = daten.wahrheiten_laden_liste()
    inhalt2 = {}
    for wahrheit in wahrheiten:
        if wahrheit not in inhalt2:
            inhalt2[wahrheit] = 1
        else:
            inhalt2[wahrheit] += 1

    x = inhalt2.values()
    y = inhalt2.keys()

    fig = px.bar(x=x, y=y)
    div2 = plot(fig, output_type="div")

    return render_template("viz.html", barchart=div, barchart2=div2, seitentitel="Piechart")


if __name__ == "__main__":
    app.run(debug=True, port=5007)
