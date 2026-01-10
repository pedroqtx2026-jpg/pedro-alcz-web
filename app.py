from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Desarrollo Web Pedro Alcz</h1>
    <p>Mi primera web publicada en internet</p>
    <a href="/pedro-alcz">Ir a mi enlace personalizado</a>
    """

@app.route("/pedro-alcz")
def pedro():
    return "<h2>Bienvenido a la web de Pedro Alcz</h2>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)