# -*- coding: utf-8 -*-

"""Documentation file routes.py."""
# -*- coding: utf-8 -*-

from app.restplus import api, ns_client, responses, auth_required
from app.serializers.client import client_serializer

from flask import request, Blueprint
from flask_restplus import Resource

from app.models.database import Database
from app.settings.configuration import Configuration
from app.settings.log import Logging
from flask import current_app as app

from pprint import pprint


config = Configuration()
log = Logging().logger

def build_response(id=None, name=None):
    db = Database()

    client = db.fetchone("select * from client where name='{}';".format(name)) if id is None else db.fetchone("select * from client where id='{}';".format(id))

    return {"id": client[0],
            "name": client[1], 
            "mail": client[2]}


@ns_client.route('/<string:client_id>')
class ClientQuery(Resource):

    """
    Metodo para remover um
    client do banco de dados
    """
    @auth_required
    @api.doc(description="Route to delete a client", responses=responses)
    def delete(self, client_id=None):
        result = {}
        try:
            db = Database()
            client = db.fetchone('select id, name, mail from client where id={};'.format(client_id))

            if client is None:
                log.warning(f"{request.authorization.username} - 400 - DELETE - No find client with id {client_id}")
                return {"message": "No find client with id {}".format(client_id), "data": {}, "status": 400}, 400

            result = build_response(id=client_id)
            if db.execute('delete from client where id=%s;', (client_id))[0]:  
                log.info(f"{request.authorization.username} - 200 - DELETE - successfully to removed client with id {client_id}")
                return {"message": "successfully to removed",
                        "data": result,
                        "status": 200}, 200
            else:
                log.error(f"{request.authorization.username} - 400 - DELETE - failed to removed client with id {client_id}")
                return {"message": "failed to removed", 
                        "data": {}, 
                        "status": 400}, 400
        except Exception as e:
            log.error(f"{request.authorization.username} - 400 - DELETE - {str(e)}")
            return {"message": str(e), "data": {}, "status": 400}, 400

    """
    Metodo para recuperar informações
    de determinado client pela
    sua id de acesso, ou retornar todos 
    os client salvos
    """
    @auth_required
    @api.doc(description="Route to get info from client by id", responses=responses)
    def get(self, client_id=None):
        try:
            db = Database()
            client = db.fetchone('select id, name, mail from client where id={};'.format(client_id))

            if client is None:
                log.warning(f"{request.authorization.username} - 400 - GET - No find client with id {client_id}")
                return {"message": "No find client with id {}".format(client_id), "data": {}, "status": 400}, 400

            log.info(f"{request.authorization.username} - 200 - DELETE - successfully to get client with id {client_id}")
            return {"message": "successfully in get client id {}".format(client_id),
                    "data": build_response(id=client_id), 
                    "status": 200}
        except Exception as e:
            log.error(f"{request.authorization.username} - 400 - GET - {str(e)}")
            return {"message": str(e), "data": {}, "status": 400}, 400

    """
    Metodo para alterar
    informações de determinado client
    """
    @auth_required
    @api.expect(client_serializer, validate=True)
    @api.doc(description="Route to update a client on application by id", responses=responses)
    def put(self, client_id=None):
        try:
            db = Database()
            data = api.payload

            # Verificar se o nome já existe para alguem com id diferente
            if db.fetchone("select * from client where name='{}' and id!={};".format(data['name'], client_id)) is not None:
                log.warning(f"{request.authorization.username} - 400 - PUT - failed in update client with id {client_id}. This name is already registered in the database.")                
                return {"message": "failed in update client with id {}. This name is already registered in the database.".format(client_id),
                        "data": {}, 
                        "status": 400}, 400

            client = db.fetchone("select id, name, mail from client where id={};".format(client_id))

            if client is None:
                log.warning(f"{request.authorization.username} - 400 - PUT - No find client with id {client_id}")
                return {"message": "No find client with id {}".format(client_id), "data": {}, "status": 400}, 400

            update = db.execute("update client set name=%s,mail=%s where id=%s;", (data['name'], data['mail'], client_id))

            if update[0]:
                log.info(f"{request.authorization.username} - 200 - PUT - successfully in update client with id {client_id}")
                return {"message": "successfully in update client with id {}".format(client_id),
                        "data": build_response(id=client_id), 
                        "status": 200}, 200
            else:
                log.error(f"{request.authorization.username} - 400 - PUT - failed in update client with id {client_id}. {update[1]}")
                return {"message": "failed in update client with id {}. {}".format(client_id, update[1]),
                        "data": {}, 
                        "status": 400}, 400
        except Exception as e:
            log.error(f"{request.authorization.username} - 400 - PUT - {str(e)}")
            return {"message": str(e), "data": {}, "status": 400}, 400



@ns_client.route('')
class ClientNoQuery(Resource):

    """
    Metodo para adicionar
    novo client
    """
    @auth_required
    @api.expect(client_serializer, validate=True)
    @api.doc(description="Route to add new client on application", responses=responses)
    def post(self):
        try:
            db = Database()
            data = api.payload

            if db.fetchone("select id, name, mail from client where name='{}';".format(data['name'])) is not None:
                log.warning(f"{request.authorization.username} - 200 - POST - Client {data['name']} is already registered")                
                return {"message": f"Client {data['name']} is already registered",
                        "data": build_response(name=data['name']),
                        "status": 400}, 400

            insert = db.execute("insert into client (name, mail) values (%s, %s);", (data['name'], data['mail']))

            if insert[0]:
                client = db.fetchone("select id from client where name='{}';".format(data['name']))
                response = build_response(id=client[0])
                log.info(f"{request.authorization.username} - 200 - POST - successfully add new client with id {client[0]}")
                return {"message": "successfully add new client",
                        "data": response,
                        "status": 200}, 200
            else:
                log.error(f"{request.authorization.username} - 400 - POST - failed in add new client. {insert[1]}")
                return {"message": "failed in add new client. {}".format(insert[1]), "data": {}, "status": 400}, 400

        except Exception as e:
            log.error(f"{request.authorization.username} - 400 - POST - {str(e)}")
            return {"message": str(e), "data": {}, "status": 400}, 400

    """
    Metodo para recuperar informações
    de todos os clients
    """
    @auth_required
    @api.doc(description="Route to get info from all clients", responses=responses)
    def get(self):
        try:
            db = Database()
            result = []
            clients = db.fetchall('select id, name, mail from client;')

            if len(clients) == 0:
                log.warning(f"{request.authorization.username} - 400 - GET - No registered client")
                return {"message": "No registered client", "data": [], "status": 400}, 400

            for client in clients:
                result.append(build_response(id=client[0]))

            log.info(f"{request.authorization.username} - 200 - GET - successfully in get datas")
            return {"message": "successfully in get datas",
                    "data": result,    
                    "status": 200}
        except Exception as e:
            log.error(f"{request.authorization.username} - 400 - GET - {str(e)}")
            return {"message": str(e), "data": [], "status": 400}, 400
