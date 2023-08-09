from flask import Flask, Response, render_template, request, redirect
from interactions import  buscar_evento, novo_evento, obter_imagem_do_banco, buscar_todos, inscricao, inscritos_todos
import base64

# app = Flask(__name__, template_folder='C:/Users/Wagner/UNBeventos/templates')
# app._static_folder = 'C:/Users/Wagner/UNBeventos/static'
app = Flask(__name__, template_folder='C:/Users/wagner.junior/UNBeventos/templates')
app._static_folder = 'C:/Users/wagner.junior/UNBeventos/static'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@127.0.0.1:3306/UNBeventos'

#Pagina inicial
@app.route("/", methods = ['GET', 'POST'])
def homepage():
    return render_template("homepage.html")

@app.route('/login', methods=['POST'])
def login():
    senha = request.values.get('senha')
    if senha == 'UNBeventos123':
        return redirect("/")
    else:
        return redirect("/confirmacao-inscricao")
    
@app.route('/cadastrar')
def cadatrar_evento():
    return render_template('Cadastro de Evento.html')

@app.route('/criados')
def criados():
    return render_template('Eventos Criados.html')

@app.route('/cadastrar-dados', methods = ['POST'])
def cadastrar_dados():
    titulo = request.form['titulo']
    data = request.form['data']
    horario = request.form['horario']
    local = request.form['local']
    categorias = request.form['categorias']
    descricao = request.form['descricao']
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    imagem = request.files.get('myFile')
    
    if imagem is not None:
        imagem_bytes = imagem.read()

        # Codificar a imagem em base64
        imagem_base64 = base64.b64encode(imagem_bytes)
        
    else:
        imagem_base64 = 0
    
    novo_evento(titulo, data, horario, local, categorias, descricao, nome, email, telefone, imagem_base64)
    return confirmar_evento()

@app.route('/evento/<id>', methods = ['GET'])
def pagina_evento(id):
    ### buscar no banco id do evento
    conteudo = buscar_evento(id)
    
    return render_template('Evento Template.html', conteudo = conteudo)

@app.route('/usuario')
def perfil_usuario():
    dados = inscritos_todos()
    return render_template('Perfil do Usuario.html', conteudo = dados)

@app.route('/confirmacao-evento')
def confirmar_evento():
    return render_template("Confirmacao de Evento Cadastrado.html")

@app.route('/confirmacao-inscricao')
def confirmar_inscricao():

    return render_template("Confirmacao de Inscricao.html")

@app.route("/confirmacao", methods=["POST"])
def confirmacao_inscricao():
    dados_json = request.get_json()

    inscricao(dados_json)

    # Retornar uma resposta adequada
    return "Dados do evento recebidos com sucesso!"

@app.route('/teste', methods = ['GET'])
def teste():
    return render_template("a.html")

@app.route('/imagem/<imagem_id>')
def exibir_imagem(imagem_id):
    # Obtenha a imagem do banco de dados usando o ID ou nome
    imagem = obter_imagem_do_banco(imagem_id)
    
    # Verifique se a imagem foi encontrada
    if imagem is not None:
        # Retorne a imagem como resposta HTTP com o tipo MIME apropriado
        return Response(imagem, mimetype='image/jpeg')
    
    # Se a imagem não for encontrada, retorne uma imagem padrão ou uma mensagem de erro
    return "Imagem não encontrada"

@app.route('/todos', methods = ['GET'])
def pagina_todos():
    eventos = buscar_todos()

    return render_template('todos_eventos.html', conteudo = eventos) 


@app.route('/favoritos')
def favoritos_pagina():

    return render_template("Favoritos.html")

app.run()
