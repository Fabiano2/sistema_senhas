from flask import Flask, render_template,request, redirect, url_for
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
    cursor.execute("SELECT senha FROM senhas_chamadas order by senha desc")
    data = cursor.fetchone()
    senha = data
    cursor.execute("SELECT senhas_chamadas.senha FROM senhas.senhas_chamadas order by senha desc;")
    chamadas = cursor.fetchall()
    cursor.close()
    return render_template('painel.html', senha=senha, chamadas=chamadas)

@app.route("/gerar", methods=["GET", "POST"])
def gera_senha():
    if request.method == 'POST':
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT senhas.senha FROM senhas order by id desc")
        ultima_senha = cursor.fetchone()
        ultima_senha = ultima_senha[0]
        nova_senha = int(ultima_senha) +1
        cursor.execute(f"INSERT INTO senhas.senhas (senha) VALUES ({nova_senha})")
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('senha_gerada'))

    return render_template("gera_senha.html")

@app.route("/senha_gerada")
def senha_gerada():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT senhas.senha FROM senhas.senhas order by id desc;")
    senha = cursor.fetchone()   
    cursor.close()
    return render_template("senha_gerada.html", senha=senha)

@app.route("/fila", methods=["GET", "POST"])
def fila():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT senhas.senha FROM senhas")
    senha = cursor.fetchone()
    fila = cursor.fetchall()

    if request.method == 'POST':
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT senhas.senha FROM senhas.senhas")
        senha = cursor.fetchone()
        cursor.execute(f"INSERT INTO senhas.senhas_chamadas (senha) VALUES ({senha[0]});")
        mysql.connection.commit()
        cursor.execute(f"DELETE FROM senhas.senhas WHERE (senha= '{senha[0]}');")
        mysql.connection.commit()
        cursor.close()

    return render_template("fila.html", senha=senha, fila=fila)