#Arquivo pra criar as interações com o banco de dados i.e. Criar eventos novos, favoritar/desfavoritar eventos, criar os eventos iniciais do site.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from db import Eventos,Usuario, incricao
import json
import base64


Base = declarative_base()

engine = create_engine('mysql://root:admin@127.0.0.1:3306/UNBeventos')

Session = sessionmaker(bind=engine)

session = Session()

# def buscar_evento(id):
#     evento_objeto = session.query(Evento.id, Evento.nome, Evento.imagem, Evento.data, Evento.hora, Evento.local, Evento.resumo).filter(Evento.id == id).first()
#     evento_json = []
#     evento_json.append({"id": evento_objeto[0], "nome": evento_objeto[1], "imagem": evento_objeto[2], 
#                          "data": evento_objeto[3], "hora": evento_objeto[4], "local": evento_objeto[5], "resumo": evento_objeto[6]})
#     evento_json = json.dumps(evento_json)

#     return evento_json

def buscar_usuario(id):
    usuario_objeto = session.query(Usuario.id, Usuario.nome, Usuario.matricula, Usuario.curso, Usuario.email, Usuario.foto, Usuario.favoritos).filter(Usuario.id == id).first()
    usuario_json = []
    usuario_json.append({"id": usuario_objeto[0], "nome": usuario_objeto[1], })
    usuario_json = json.dumps(usuario_json)

    return usuario_json


def novo_evento(titulo, data, horario, local, categorias, descricao, nome, email, telefone, imagem_bin):
    evento = Eventos(nome = titulo, imagem = imagem_bin, data = data, hora = horario, local = local, resumo = descricao, organizadores = nome, telefone = telefone, email = email, categorias = categorias )
    session.add(evento)
    session.commit()

# def adicionar_usuario(id, nome, matricula, curso, email, foto, id_favorito):
#     favorito = session.query(Favoritos).filter_by(id == id_favorito).first()
#     user = Usuario(id = id, nome = nome, matricula = matricula, curso = curso, email = email, foto = foto , favoritos = favorito)
    
#     session.add(user)
#     session.commit()
    
    
    
# adicionar_usuario(1, 'Wagner',  '200044494','Ciencia da computação', '200044494@aluno.unb.br',"00000000" , 1)

def obter_imagem_do_banco(id):
    
    imagem = session.query(Eventos.imagem).filter(id == id).first()
    print(imagem)
    return imagem

def buscar_evento(id):
    evento_objeto = session.query(Eventos.nome, Eventos.imagem, Eventos.data, Eventos.hora, Eventos.categorias, Eventos.resumo, Eventos.local, Eventos.organizadores, Eventos.id).filter(Eventos.id == id).first()
    pessoa_json = []
    #print(evento_objeto[1])
    my_date_string = evento_objeto[2].isoformat()
    my_time_string = evento_objeto[3].strftime("%H:%M:%S")
    my_string = evento_objeto[1].decode('utf-8')
    
    pessoa_json.append({"nome": evento_objeto[0], "imagem": my_string, "data": my_date_string, "hora": my_time_string, "categoria": evento_objeto[4], "descricao": evento_objeto[5], "local": evento_objeto[6], "organizador": evento_objeto[7], "id":evento_objeto[8]})
    
    pessoa_json = json.dumps(pessoa_json)

    return pessoa_json

def buscar_todos():
    eventos_objetos = session.query(Eventos.id,Eventos.nome, Eventos.imagem, Eventos.data, Eventos.hora, Eventos.categorias, Eventos.resumo, Eventos.local, Eventos.organizadores).all()
    eventos_json = []

    for evento_objeto in eventos_objetos:
        my_date_string = evento_objeto[3].isoformat()
        my_time_string = evento_objeto[4].strftime("%H:%M:%S")
        if evento_objeto[2] is not None:
            my_string = evento_objeto[2].decode('utf-8')
        else:
            my_string = ''

        evento_json = {
            "id": evento_objeto[0],
            "nome": evento_objeto[1],
            "imagem": my_string,
            "data": my_date_string,
            "hora": my_time_string,
            "categoria": evento_objeto[5],
            "descricao": evento_objeto[6],
            "local": evento_objeto[7],
            "organizador": evento_objeto[8]
        }

        eventos_json.append(evento_json)

    eventos_json = json.dumps(eventos_json)
    return eventos_json

def inscricao(dados):
    pessoa = incricao(nome = dados['nome'], id_evento = dados['id_evento'])
    session.add(pessoa)
    session.commit()

def inscritos_todos():
    inscritos_objetos = session.query(incricao.nome, incricao.id_evento).all()
    inscritos_json = []

    for inscrito_objeto in inscritos_objetos:
        inscrito_json = {
            "nome": inscrito_objeto[0],
            "id_evento": inscrito_objeto[1]
        }

        inscritos_json.append(inscrito_json)

    inscritos_json = json.dumps(inscritos_json)
    return inscritos_json
