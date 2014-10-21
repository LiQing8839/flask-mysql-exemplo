from flask import Flask, render_template, request, redirect
import MySQLdb

app = Flask(__name__)
db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="hellodb")


@app.route("/")
def presidentes():
    cur = db.cursor() # Criando um cursor para executar query SQL
    cur.execute("SELECT * FROM presidentes;") # Executando uma query SQL
    presidentes = cur.fetchall() # Armazena os resultados em uma variavel
    cur.close() # Fecha o cursos que usamos para obter a lista de presidentes
    return render_template("presidentes.html", presidentes=presidentes) # Renderiza e passa os presidentes ao template

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    nome = request.form['nome']
    cpf = request.form['cpf']
    nascimento = request.form['nascimento'] # A data deve ser no formato yyyy-mm-dd, caso contrario sera None
    cur = db.cursor() 
    # Lembrando que na linguagem SQL string deve ser colocado em aspas
    cur.execute("INSERT INTO presidentes(nome, cpf, nascimento) VALUES('%s', '%s', '%s');" % (nome, cpf, nascimento))
    db.commit()
    cur.close()
    return redirect("/") # Apos cadastrar, redirecionar para a rota que exibe os presidentes


@app.route("/formulario")
def formulario():
    return render_template("formulario.html")

if __name__ == '__main__':
    app.run(debug=True)