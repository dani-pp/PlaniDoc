from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/agendar")
def agendar():
    return render_template("agendar.html")

@app.route("/iniciar-sesion")
def iniciar():
    return render_template("iniciar_sesion.html")

if __name__ == "__main__":
    app.run(debug=True)