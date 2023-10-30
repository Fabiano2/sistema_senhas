from flask import Flask, render_template

app = Flask(__name__)

@app.route("/painel")
def painel():
    senha = 100
    return render_template('painel.html', senha=senha)

@app.route("/gerar")
def gera_senha():
    return render_template("gera_senha.html")

@app.route("/senha_gerada")
def senha_gerada():
    return render_template("senha_gerada.html")

@app.route("/fila")
def fila():
    return render_template("fila.html")