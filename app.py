from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/pedro-alcz")
def pedro():
    return render_template("pedro.html")
