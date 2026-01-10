from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bienvenido a Desarrollo Web Pedro Alcz"

@app.route("/pedro-alcz")
def pedro():
    return render_template("pedro.html")


