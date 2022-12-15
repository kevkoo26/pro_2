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




@app.route("/statistik")
def statistik():
    taten = daten.elements()

    x = "Markus", "Hans", "Lisa", "Kevin", "Sarah", "Linda"
    y = 5, 4, 9, 13, 1, 7
    fig = px.bar(x=x, y=y)
    div = plot(fig, output_type="div")

    return render_template("statistic.html", barchart=div, liste=taten, seitentitel="Statistik")


@app.route("/tat")
def tat():
    taten = daten.taten_laden()
    return render_template("tat.html", liste=taten, seitentitel="tat")


@app.route("/tat_hinzufügen/", methods=['GET', 'POST'])
def tat_hinzufügen():
    if request.method == "GET":
        auflistung = daten.taten_laden_liste()
        return render_template("tat_hinzufügen.html", liste=auflistung, seitentitel="Tat eingeben")

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
        auflistung = daten.wahrheiten_laden_liste()
        return render_template("wahrheit_hinzufügen.html", liste=auflistung, seitentitel="Wahrheit eingeben")

    if request.method == 'POST':
        eigene_wahrheit = request.form['wahrheit_hinzufügen']
        print(f"Request Form Wahrheit hinzufügen: {eigene_wahrheit}")
        abspeichern_wahrheit(eigene_wahrheit)
        return redirect(url_for("wahrheit_hinzufügen"))



@app.route("/viz")
def grafik():
    taten = daten.taten_laden_liste()
    inhalt = {}
    for tat in taten:
        if tat [1] not in inhalt:
            inhalt[tat[1]] = 1
        else:
            inhalt[tat[1]] += 1

    x = inhalt.keys()
    y = inhalt.values()

    fig = px.bar(x=x, y=y)
    div = plot(fig, output_type="div")

    return render_template("viz.html", barchart=div, seitentitel="Piechart")


if __name__ == "__main__":
    app.run(debug=True, port=5007)
