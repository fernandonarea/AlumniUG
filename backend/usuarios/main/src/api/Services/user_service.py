from flask import request
from flask_restful import Resource
from src.api.Components.user_component import UserComponent
from src.api.Model.Request.create_request import CreateUserRequest
from src.api.Model.Request.update_request import UpdateUserRequest
from src.utils.general.logs import HandleLogs
from src.utils.general.response import response_error, response_success, response_inserted
from src.api.Components.jwt_component import JWTComponent

class UserService(Resource):
    @staticmethod
    def get(user_id):
        try:
            HandleLogs.write_log('Servicio de usuarios iniciado')
            token = request.headers['token']
            validar_token = JWTComponent.token_validate(token)

            if not token:
                return response_error('No se recibió ningun token')
            elif not validar_token:
                return response_error('token invalido')

            result = UserComponent.get_users(user_id)

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
            HandleLogs.write_log('Servicio de Creación Usuarios ejecutando')

            request_data = request.get_json()

            request_schema = CreateUserRequest()
            error = request_schema.validate(request_data)
            if error:
                return response_error('Datos incorrectos para crear usuario')

            username = request_data['username']
            password = request_data['password']
            name = request_data['name']
            lastname = request_data['lastname']
            id_facultad = request_data['id_facultad']

            result =UserComponent.create_user(
                username, password, name, lastname, id_facultad
            )

            if result['result']:
                return response_inserted(result['data'])
            else:
                return response_error(result['message'])

        except Exception as error:
            HandleLogs.write_log(error)
            return response_error("Error en el servicio -> " + error.__str__())

    @staticmethod
    def put(user_id):
        try:
            HandleLogs.write_log('Servicio de Actualización de datos iniciado')
            token = request.headers['token']

            validar_token = JWTComponent.token_validate(token)

            if not token:
                return response_error('No se recibió ningun token')
            elif not validar_token:
                return response_error('token invalido')

            request_data = request.get_json()

            request_schema = UpdateUserRequest()
            error = request_schema.validate(request_data)
            if error:
                return response_error('Datos invalidos para actualizar usuario')

            username = request_data['username']
            name = request_data['name']
            lastname = request_data['lastname']

            result = UserComponent.update_user(
                    user_id, username, name, lastname
            )

            if result['result']:
                return response_success(result['data'])
            else:
                return response_error(result['message'])

        except Exception as error:
            HandleLogs.write_error(error)
            return response_error('Error en el servicio de actualización -> ' + error.__str__())

    @staticmethod
    def delete(id_user):
        try:
            HandleLogs.write_log('Servicio Eliminar Usuario iniciado')
            token = request.headers.get('token')

            validar_token = JWTComponent.token_validate(token)

            if not token:
                return response_error('No se recibió ningun token')
            elif not validar_token:
                return response_error('token invalido')

            result = UserComponent.delete_user(id_user)

            if result['result']:
                return response_success(result['data'])
            else:
                return response_error(result['message'])

        except Exception as error:
            HandleLogs.write_error(error)
            return response_error('Error en el servicio de eliminar usuarios -> ' + error.__str__())