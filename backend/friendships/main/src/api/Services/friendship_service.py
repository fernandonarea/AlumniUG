from flask import request
from flask_restful import Resource
from src.utils.general.logs import HandleLogs
from src.utils.general.response import response_error, response_success, response_inserted
from src.api.Components.jwt_component import JWTComponent
from src.api.Components.friendship_component import FriendShipComponent

class FriendShipService(Resource):
    @staticmethod
    def post(user_id, amigo_id):
        try:
            HandleLogs.write_log('Servicio para Añadir Amigo ejecutando')

            result = FriendShipComponent.add_friend(user_id, amigo_id)

            if result['result']:
                return response_inserted(result['data'])
            else:
                return response_error(result['message'])

        except Exception as error:
            HandleLogs.write_log(error)
            return response_error("Error en el servicio -> " + error.__str__())

class GetNumFriendsService(Resource):
    @staticmethod
    def get(user_id):
        try:
            HandleLogs.write_log('Número de amigos iniciado')

            token = request.headers.get('token', None)
            validar_token = JWTComponent.token_validate(token)

            if not token:
                return response_error('No se recibió ningún token')
            elif not validar_token:
                return response_error('Token inválido')

            result = FriendShipComponent.get_num_friends(user_id)

            if result['result']:
                return response_success(result['data'])
            else:
                return response_error(result['message'])

        except Exception as error:
            HandleLogs.write_log(error)
            return response_error("Error en el servicio -> " + error.__str__())

