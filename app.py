from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "<h1>Bienvenido a la web de Pedro Alcz</h1><p>Mi primera página web online</p>"

@app.route("/pedro-alcz")
def pedro():
    return "<h2>Proyecto Desarrollo Web - Pedro Alcz</h2>"

if __name__ == "__main__":
    app.run()
