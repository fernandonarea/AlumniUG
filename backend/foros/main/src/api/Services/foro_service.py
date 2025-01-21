from flask import request
from flask_restful import Resource
from src.api.Components.foros_component import ForosComponent
from src.utils.general.logs import HandleLogs
from src.utils.general.response import response_error, response_success, response_inserted
from src.api.Components.jwt_component import JWTComponent

class ForoService(Resource):
    @staticmethod
    def get():
        try:
            HandleLogs.write_log('Servicio de foros iniciado')
            token = request.headers['token']
            validar_token = JWTComponent.token_validate(token)

            if not token:
                return response_error('No se recibió ningun token')
            elif not validar_token:
                return response_error('token invalido')

            result = ForosComponent.get_foros()

            if result['result']:
                return response_success(result['data'])
            else:
                return response_error(result['message'])
        except Exception as error:
            HandleLogs.write_log(error)
            return response_error("Error en el servicio -> " + error.__str__())

    @staticmethod
    def post():
        try:
            HandleLogs.write_log('Creación de foro')
            token = request.headers['token']
            validar_token = JWTComponent.token_validate(token)

            if not token:
                return response_error('No se recibió ningun token')
            elif not validar_token:
                return response_error('token invalido')

            reques_data = request.get_json()

            forum_title = reques_data['forum_title']
            forum_description = reques_data['forum_description']

            result = ForosComponent.create_foro(forum_title, forum_description)

            if result['result']:
                return response_inserted(result['data'])
            else:
                return response_error(result['message'])

        except Exception as error:
            HandleLogs.write_log(error)
            return response_error("Error en el servicio -> " + error.__str__())

class getForoService(Resource):
    @staticmethod
    def get(id_forum):
        try:
            HandleLogs.write_log('Obtener foro especifico')
            token = request.headers['token']
            validar_token = JWTComponent.token_validate(token)

            if not token:
                return response_error('No se recibió ningun token')
            elif not validar_token:
                return response_error('token invalido')

            result = ForosComponent.get_foro(id_forum)

            if result['result']:
                return response_success(result['data'])
            else:
                return response_error(result['message'])

        except Exception as error:
            HandleLogs.write_log(error)
            return response_error("Error en el servicio -> " + error.__str__())


