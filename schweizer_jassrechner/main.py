from flask import Flask
from flask import request
from flask import render_template

app = Flask("Jassen")


@app.route('/jassen')
def style():
    return render_template("style_versuch1.html")









if __name__ == "__main__":
    app.run(debug=True, port=5007)


