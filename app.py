from flask import Flask, render_template, request, redirect, url_for
import os  # Para obtener el puerto de la variable de entorno

app = Flask(__name__)

# Credenciales
USUARIO = "teamo"
CLAVE = "1234"

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def do_login():
    usuario = request.form.get("usuario")
    clave = request.form.get("clave")
    if usuario == USUARIO and clave == CLAVE:
        return redirect(url_for("carta"))
    else:
        return "<h2 style='color:red;'>Usuario o contraseña incorrectos. <a href='/'>Volver</a></h2>"

@app.route("/carta")
def carta():
    return render_template("carta.html")

# Este bloque solo se usa al correr localmente
if __name__ == "__main__":
    from os import environ
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)