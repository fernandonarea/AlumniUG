from flask import request
from flask_restful import Resource
from src.api.Components.likes_component import LikesComponent
from src.utils.general.logs import HandleLogs
from src.utils.general.response import response_error, response_success
from src.api.Components.jwt_component import JWTComponent

class LikesService(Resource):

    @staticmethod
    def get(id_post):
        try:
            HandleLogs.write_log('Servicio de interacciones iniciado')
            token = request.headers.get('token')
            validar_token = JWTComponent.token_validate(token)

            if not validar_token:
                return response_error('Token Invalido')

            result = LikesComponent.get_interactions(id_post)

            if result['result']:
                return response_success(result['data'])
            else:
                return response_error(result['message'])

        except Exception as error:
            HandleLogs.write_log(error)
            return response_error("Error en el servicio -> " + error.__str__())

    @staticmethod
    def post(post_id, user_id):
        try:
            HandleLogs.write_log('Servicio de creacion de interaccion creado')
            token = request.headers.get('token')
            validar_token = JWTComponent.token_validate(token)

            if not validar_token:
                return response_error('Token Invalido')

            result = LikesComponent.create_interaction(post_id, user_id)

            if result['result']:
                return response_success(result['data'])
            else:
                return response_error(result['message'])

        except Exception as error:
            HandleLogs.write_log(error)
            return response_error("Error en el servicio -> " + error.__str__())

    @staticmethod
    def delete(user_id, post_id):
        try:
            HandleLogs.write_log('Servicio de Likes Iniciado')

            token = request.headers.get('token')
            if not token:
                return response_error('No se recibió ningún token')

            validar_token = JWTComponent.token_validate(token)

            if not validar_token:
                return response_error('Token Invalido')

            result = LikesComponent.delete_interaction(user_id, post_id)
            print(result)

            if result['result']:
                return response_success(result['data'])
            else:
                return response_error(result['message'])
        except Exception as error:
            HandleLogs.write_error(error)
            return response_error(f"Error en el servicio -> {error.__str__()}")