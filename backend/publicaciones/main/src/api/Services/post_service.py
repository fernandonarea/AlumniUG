from flask import request
from flask_restful import Resource
from src.api.Components.posts_component import PostComponent
from src.api.Model.Request.update_post_request import UpdatePostRequest
from src.utils.general.logs import HandleLogs
from src.utils.general.response import response_error, response_success, response_inserted
from src.api.Components.jwt_component import JWTComponent

class PostService(Resource):

    @staticmethod
    def get():
        try:
            HandleLogs.write_log('Servicio de post iniciado')
            token = request.headers.get('Authorization')
            validar_token = JWTComponent.token_validate(token)

            if not validar_token:
                response_error('Token no válido')

            # if token and token.startswith('Bearer '):
            #     token = token[7:]
            # else:
            #     return response_error('Token no válido')


            result = PostComponent.get_all_posts()

            if result['result']:
                return response_success(result['data'])
            else:
                return response_error(result['message'])

        except Exception as error:
            HandleLogs.write_log(error)
            return response_error("Error en el servicio -> " + error.__str__())

    @staticmethod
    def post(user_id):
        try:
            HandleLogs.write_log('Servicio de Creación de Publicación Iniciado')

            token = request.headers.get('token')
            if not token:
                return response_error('No se recibió ningún token')

            validar_token = JWTComponent.token_validate(token)
            if not validar_token:
                return response_error('Token inválido')

            request_data = request.get_json()
            if not request_data:
                return response_error('No se recibió contenido en la solicitud')

            post_content = request_data.get('post_content')
            if not post_content:
                return response_error('El contenido del post es obligatorio')

            result = PostComponent.create_post(user_id, post_content)
            print(result)

            if result['result']:
                return response_success(result['data'])
            else:
                return response_error(result['message'])
        except Exception as error:
            HandleLogs.write_error(error)
            return response_error(f"Error en el servicio -> {error.__str__()}")

    @staticmethod
    def put(id_post):
        try:
            HandleLogs.write_log('Servicio para actualizar un post iniciado')
            token = request.headers['token']

            validar_token = JWTComponent.token_validate(token)

            if not token:
                return response_error('No se recibió ningun token')
            elif not validar_token:
                return response_error('token invalido')

            request_data = request.get_json()
            print("datos recibidos", request_data)
            post_content = request_data['post_content']

            request_schema = UpdatePostRequest()
            error = request_schema.validate(request_data)
            if error:
                return response_error('Datos invalidos para actualizar usuario')

            result = PostComponent.updatePost(
                id_post, post_content
            )

            if result['result']:
                return response_success(result['data'])
            else:
                return response_error(result['message'])

        except Exception as error:
            HandleLogs.write_log(error)
            return response_error("Error en el servicio -> " + error.__str__())

    @staticmethod
    def delete(id_post):
        try:
            HandleLogs.write_log('Servicio de Actualizar publicación Iniciado')

            token = request.headers['token']
            validar_token = JWTComponent.token_validate(token)

            if not token:
                return response_error('No se recibió ningun token')
            elif not validar_token:
                return response_error('token invalido')

            result = PostComponent.deletePost(id_post)

            if result['result']:
                return response_success(result['result'])
            else:
                return response_error(result['message'])
        except Exception as error:
            HandleLogs.write_log(error)
            return response_error("Error en el servicio -> " + error.__str__())

class  UserPostService(Resource):
    @staticmethod
    def get(id_user):
        try:
            HandleLogs.write_log('Posts de un usuario especifico')

            token = request.headers['token']
            validar_token = JWTComponent.token_validate(token)

            if not token:
                return response_error('No se recibió ningun token')
            elif not validar_token:
                return response_error('token invalido')

            result = PostComponent.get_user_posts(id_user)

            if result['result']:
                return response_success(result['data'])
            else:
                return response_error(result['message'])

        except Exception as error:
            HandleLogs.write_error(error)
            return response_error('Error en el servicio-> ' + error.__str__())

class TrendingPost(Resource):

    @staticmethod
    def get(user_id):
        try:
            HandleLogs.write_log('Posts con más interacciones')

            token = request.headers['token']
            validar_token = JWTComponent.token_validate(token)

            if not token:
                return response_error('No se recibió ningun token')
            elif not validar_token:
                return response_error('token invalido')

            result = PostComponent.get_best_post(user_id)

            if result['result']:
                return response_success(result['data'])
            else:
                return response_error(result['message'])

        except Exception as error:
            HandleLogs.write_error(error)
            return response_error('Error en el servicio-> ' + error.__str__())