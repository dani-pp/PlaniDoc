from flask import Flask, render_template, request, redirect,url_for, session, flash
from dotenv import load_dotenv
import os
from pymongo import MongoClient
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


load_dotenv()
app = Flask(__name__)

mongo_uri = os.getenv("MONGO_URI")
client=MongoClient(mongo_uri)
db = client.get_database("usuarios")
usuarios = db.usuarios
especialistas= db.usuarios.especialistas
app.secret_key= os.getenv("SECRET_KEY")


@app.route("/")
def index():
    nombre=session.get("nombre")
    return render_template("index.html", nombre=nombre)

@app.route("/buscador")
def buscador():
    termino = request.args.get("busqueda", "").lower()
    todos_los_usuarios = list(db.especialistas.find())
    if termino:
        resultados = [
            usuario for usuario in todos_los_usuarios
             if termino in usuario.get("nombre", "").lower() or termino in usuario.get("especialidad", "").lower()
        ]
    else:
        resultados = todos_los_usuarios

    return render_template("buscador.html", resultados=resultados)


@app.route("/agendar")
def agendar():
    todos_los_usuarios= list(db.especialistas.find())
    return render_template("buscador.html", resultados = todos_los_usuarios)

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

@app.route("/registrar", methods=["POST"])
def registrar():
    email = request.form.get("correo")
    password= request.form.get("password")
    contrasena_segura= generate_password_hash(password)
    nombres = request.form.get("nombres")
    apellidos= request.form.get("apellidos")
    rut = request.form.get("rut")
    telefono = request.form.get("telefono")
    fecha_nac = request.form.get("fecha_nac")
    sexo = request.form.get("sexo")
    direccion = request.form.get("direccion")
    prevision = request.form.get("prevision")
    
    usuarios.insert_one({
        "nombre" : nombres,
        "apellidos" : apellidos,
        "fecha_nac" :  fecha_nac,
        "correo" : email,
        "contrasena" : contrasena_segura,
        "telefono" : telefono,
        "direccion" : direccion,
        "fecha_registro" : datetime.utcnow(),
        "estado" : "activo",
        "rol" : "usuario",
        "rut": rut,
        "sexo" : sexo,
        "prevision" : prevision 
    })
    
    return redirect(url_for("iniciar"))


@app.route("/iniciarsesion", methods=["POST"] )
def login():
    email = request.form.get("email")
    password= request.form.get("password")
    
    usuario= usuarios.find_one({"correo":email})
    if usuario and check_password_hash(usuario["contrasena"], password):
        session["nombre"] = usuario.get("nombre")
        return redirect(url_for("index"))   
    else:
        flash("Correo o contraseña incorrecto")
        return redirect(url_for("iniciar"))

if __name__ == "__main__":
    app.run(debug=True)