from flask import Flask, render_template, request, redirect,url_for, session, flash
from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()
app = Flask(__name__)

mongo_uri = os.getenv("MONGO_URI")
client=MongoClient(mongo_uri)
db = client.get_database("usuarios")
usuarios = db.usuarios

app.secret_key= os.getenv("SECRET_KEY")


@app.route("/")
def index():
    nombre=session.get("nombre")
    return render_template("index.html", nombre=nombre)

@app.route("/buscador")
def buscador():
    termino = request.args.get("busqueda", "").lower()
    todos_los_usuarios = list(db.usuarios.find())
    if termino:
        resultados = [
            usuario for usuario in todos_los_usuarios
            if termino in usuario.get("nombre", "").lower()
        ]
    else:
        resultados = todos_los_usuarios

    return render_template("buscador.html", resultados=resultados)


@app.route("/agendar")
def agendar():
    return render_template("buscador.html")

@app.route("/registro")
def registro():
    return render_template("registro.html")

@app.route("/iniciar-sesion")
def iniciar():
    return render_template("iniciar_sesion.html")

@app.route("/cerrar-sesion")
def cerrar():
    session.clear()
    return redirect(url_for('index'))


@app.route("/iniciarsesion", methods=["POST"] )
def login():
    email = request.form.get("email")
    password= request.form.get("password")
    
    usuario= usuarios.find_one({
        "correo":email,
        "contrasena": password
    })
    
    if usuario:
        session["nombre"] = usuario.get("nombre")
        return redirect(url_for("index"))
    else:
        flash("Correo o contraseña incorrecto")
        return redirect(url_for("iniciar"))

if __name__ == "__main__":
    app.run(debug=True)