from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'senhas'
mysql = MySQL(app)

@app.route("/painel")
def painel():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT senhas.senha FROM senhas")
    data = cursor.fetchone()
    senha = data

    cursor.execute("SELECT senhas_chamadas.senha FROM senhas.senhas_chamadas;")
    chamadas = cursor.fetchall()
    cursor.close()
    return render_template('painel.html', senha=senha, chamadas=chamadas)

@app.route("/gerar")
def gera_senha():
    return render_template("gera_senha.html")

@app.route("/senha_gerada")
def senha_gerada():
    return render_template("senha_gerada.html")

@app.route("/fila")
def fila():
    return render_template("fila.html")