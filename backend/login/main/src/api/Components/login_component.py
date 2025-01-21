from src.utils.general.logs import HandleLogs
from src.utils.database.connection_db import DataBaseHandle
from src.utils.general.response import internal_response
from src.api.Components.jwt_component import JWTComponent

class LoginComponent:
    @staticmethod
    def login(p_user, p_pass):
        try:
            data = None
            message = None
            result = False

            sql = '''
                SELECT users.id_user, users.name, users.lastname,
                faculties.nombre AS nombre_facultad
                FROM users 
                LEFT JOIN faculties ON users.id_facultad = faculties.id_facultad
                WHERE username = %s AND password = %s AND status = true
            '''
            record = (p_user, p_pass)

            login_result = DataBaseHandle.getRecords(sql, 1, record)

            if login_result['result']:
                user_data = login_result['data']
                if user_data:
                    user_id = user_data['id_user']
                    name = user_data['name']
                    lastname = user_data['lastname']
                    facultad = user_data['nombre_facultad']
                    token = JWTComponent.token_generate(p_user)
                    if token:
                        result = True
                        message = 'Login Exitoso'
                        data = {
                            'token': token,
                            'user_id': user_id,
                            'username': p_user,
                            'name': name,
                            'lastname': lastname,
                            'nombre_facultad': facultad
                        }
                    else:
                        message = 'Error al generar el TOKEN'
                else:
                    message = 'Login Inválido'
            else:
                HandleLogs.write_log('Error al ejecutar Login: ' + login_result['message'])
                message = 'Error al ejecutar Login'


        except Exception as error:
            HandleLogs.write_error(error)
            message = 'Error en el Login -> ' + error.__str__()
        finally:
            return internal_response(result, data, message)
