from flask import request
from flask_restful import Resource
from src.api.Components.message_component import MessageComponent
from src.utils.general.logs import HandleLogs
from src.utils.general.response import response_error, response_success, response_inserted
from src.api.Components.jwt_component import JWTComponent

class MessageService(Resource):
    @staticmethod
    def post(forum_id, user_id):
        try:
            HandleLogs.write_log('Creación de mensaje iniciado')
            token = request.headers['token']
            validar_token = JWTComponent.token_validate(token)

            if not token:
                return response_error('No se recibió ningun token')
            elif not validar_token:
                return response_error('token invalido')

            request_data = request.get_json()

            message_content = request_data['message_content']

            result = MessageComponent.post_messages(forum_id, user_id, message_content)

            if result['result']:
                return response_inserted(result['data'])
            else:
                return response_error(result['message'])

        except Exception as error:
            HandleLogs.write_log(error)
            return response_error("Error en el servicio -> " + error.__str__())