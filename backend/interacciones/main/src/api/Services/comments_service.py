from flask import request
from flask_restful import Resource
from src.api.Components.comments_component import CommentsComponent
from src.utils.general.logs import HandleLogs
from src.utils.general.response import response_error, response_success
from src.api.Components.jwt_component import JWTComponent

class CommentService(Resource):

    @staticmethod
    def get(post_id):
        try:
            HandleLogs.write_log('Servicio de Comentarios iniciado')
            token = request.headers.get('token')
            validar_token = JWTComponent.token_validate(token)

            if not validar_token:
                return response_error('Token Invalido')

            result = CommentsComponent.get_comments(post_id)

            if result['result']:
                return response_success(result['data'])
            else:
                return response_error(result['message'])

        except Exception as error:
            HandleLogs.write_log(error)
            return response_error("Error en el servicio -> " + error.__str__())

    @staticmethod
    def post(user_id, post_id):
        try:
            HandleLogs.write_log('Servicio de creacion de comentario iniciado')
            token = request.headers.get('token')
            validar_token = JWTComponent.token_validate(token)

            if not validar_token:
                return response_error('Token Invalido')

            request_data = request.get_json()
            if not request_data:
                return response_error('No se recibió contenido en la solicitud')

            comment_text = request_data.get('comment_text')
            if not comment_text:
                return response_error('El contenido del comentario es obligatorio')

            result = CommentsComponent.create_comment(user_id, post_id, comment_text)

            if result['result']:
                return response_success(result['data'])
            else:
                return response_error(result['message'])

        except Exception as error:
            HandleLogs.write_log(error)
            return response_error("Error en el servicio -> " + error.__str__())

    @staticmethod
    def delete(user_id, id_comments):
        try:
            HandleLogs.write_log('Servicio de Creación de Publicación Iniciado')

            token = request.headers.get('Authorization')
            if not token:
                return response_error('No se recibió ningún token')

            validar_token = JWTComponent.token_validate(token)

            if not validar_token:
                return response_error('Token Invalido')

            result = CommentsComponent.delete_comment(user_id, id_comments)
            print(result)

            if result['result']:
                return response_success(result['data'])
            else:
                return response_error(result['message'])
        except Exception as error:
            HandleLogs.write_error(error)
            return response_error(f"Error en el servicio -> {error.__str__()}")
