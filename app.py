from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Web de Pedro Alcz funcionando correctamente"

@app.route("/pedro-alcz")
def pedro():
    return "Ruta personalizada Pedro Alcz"
