from flask import Flask
from flask import request
from flask import render_template

app = Flask("Rechner")


@app.route('/test', methods=["GET", "POST"])
def test():
    print(f'Method: {request.method}')
    if request.method == "GET":
        return render_template("pretty_rechner.html")

    if request.method == "POST":
        print(f'Form data: {request.form}')
        summe = int(request.form['zahl_0']) + int(request.form['zahl_1'])

        return render_template("pretty_rechner.html", ergebnis=summe)

    return "Iergendwas ist falsch"


@app.route('/kopf')
def kopf():
    return render_template("header.html")


@app.route('/style')
def style():
    return render_template("style_versuch1.html")




@app.route('/add', methods=["GET", "POST"])
def add():
    print(f'Method: {request.method}')
    if request.method == "GET":
        return render_template("calc:html.html")

    if request.method == "POST":
        print(f'Form data: {request.form}')
        summe = int(request.form['zahl_0']) + int(request.form['zahl_1'])

        return render_template("calc:html.html", ergebnis=summe)

    return "Iergendwas ist falsch"


if __name__ == "__main__":
    app.run(debug=True, port=5008)
