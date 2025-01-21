from flask import request
from flask_restful import Resource
from src.api.Components.login_component import LoginComponent
from src.api.Model.Request.login_request import LoginRequest
from src.utils.general.logs import HandleLogs
from src.utils.general.response import response_error, response_success

class LoginServices(Resource):
    @staticmethod
    def post():
        try:
            HandleLogs.write_log('Login Service Ejecutandose')

            rq_json= request.get_json()

            new_request= LoginRequest()
            validation_error =new_request.validate(rq_json)

            if validation_error:
                HandleLogs.write_log('Error al validar el Request' + str(validation_error))
                return response_error('Error al validar el Request' + str(validation_error))

            result_login = LoginComponent.login(rq_json['username'], rq_json['password'])
            if result_login['result']:
                print(result_login['data'])
                return response_success(result_login['data'])
            else:
                return response_error(result_login['message'])
        except Exception as error:
            HandleLogs.write_log(error)
            return response_error('Error en el Servicio Login ' + error.__str__())