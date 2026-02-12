from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

datas_disponiveis = {
    "2026-02-15": ["08:00", "13:00"],
    "2026-02-18": ["09:00", "13:00"],
    "2026-02-22": ["07:00", "13:00"]
}

@app.route("/")
def index():
    return render_template("index.html",
                           pagina="form",
                           datas_disponiveis=datas_disponiveis)

@app.route("/agendar", methods=["POST"])
def agendar():

    nome = request.form.get("nome")
    especialidade = request.form.get("especialidade")
    telefone = request.form.get("telefone")
    cpf = request.form.get("cpf")
    data_consulta = request.form.get("data_consulta")
    horario_consulta = request.form.get("horario_consulta")

    # ===== VALIDAÇÕES =====

    if not telefone.isdigit() or not cpf.isdigit():
        return "Telefone e CPF devem conter apenas números."

    if len(cpf) != 11:
        return "CPF deve ter exatamente 11 números."

    if len(telefone) not in [10, 11]:
        return "Telefone deve ter DDD + número (10 ou 11 dígitos)."

    return render_template("index.html",
                           pagina="resultado",
                           nome=nome,
                           especialidade=especialidade,
                           telefone=telefone,
                           cpf=cpf,
                           data_consulta=data_consulta,
                           horario_consulta=horario_consulta)

if __name__ == "__main__":
    app.run(debug=True)