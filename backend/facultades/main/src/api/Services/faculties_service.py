from flask import request
from flask_restful import Resource
from src.api.Components.faculties_component import FacultiesComponent
from src.utils.general.logs import HandleLogs
from src.utils.general.response import response_error, response_success, response_inserted

class UserService(Resource):
    @staticmethod
    def get():
        try:
            HandleLogs.write_log('Servicio de facultades iniciado')

            result = FacultiesComponent.get_faculties()

            if result['result']:
                return response_success(result['data'])
            else:
                return response_error(result['message'])

        except Exception as error:
            HandleLogs.write_log(error)
            return response_error("Error en el servicio -> " + error.__str__())