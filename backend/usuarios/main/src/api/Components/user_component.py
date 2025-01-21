from src.utils.general.logs import HandleLogs
from src.utils.database.connection_db import DataBaseHandle
from src.utils.general.response import internal_response

class UserComponent:
    @staticmethod
    def get_users(user_id):
        try:
            data = []
            message = None
            result = True
            sql = """
                SELECT u.id_user, u.username, u.name, u.lastname
                FROM users u
                WHERE u.id_user NOT IN (
                    SELECT f.amigo_id
                    FROM friends f
                    WHERE f.user_id = %s
                    UNION
                    SELECT f.user_id
                    FROM friends f
                    WHERE f.amigo_id = %s
                )
                AND u.id_user != %s;
            """

            record = (user_id, user_id, user_id)
            sql_result = DataBaseHandle.getRecords(sql, 0, record)

            print("Resultado SQL:", sql_result)

            if sql_result['result']:
                user_data = sql_result['data']  # Esto debería ser una lista de diccionarios
                if user_data:
                    for user in user_data:
                        # Crear un diccionario para cada usuario
                        formatted_user = {
                            'id_user': user['id_user'],
                            'username': user['username'],
                            'name': user['name'],
                            'lastname': user['lastname']
                        }
                        data.append(formatted_user)
                    message = 'Usuarios obtenidos con éxito'
                else:
                    message = 'No hay usuarios disponibles'
            else:
                result = False
                message = 'Error al traer los usuarios'
        except Exception as error:
            HandleLogs.write_error(error)
            message = 'Error creando el usuario ' + error.__str__()
        finally:
            return internal_response(result, data, message)


    @staticmethod
    def create_user(username, password, name, lastname, id_facultad):
        try:
            data = None
            message = None
            result = False
            sql='INSERT INTO users (username, password, name, lastname, id_facultad) '\
            'VALUES (%s, %s, %s, %s, %s)'

            record = (username, password, name, lastname, id_facultad)

            sql_result =DataBaseHandle.ExecuteNonQuery(sql, record)

            if sql_result['result']:
                result = True
                data = sql_result['data']
                message = 'Usuario Creado con exito'
            else:
                message = 'Error al crear usuario '
                HandleLogs.write_log('Error creando al usuario -> ' + sql_result['message'])
        except Exception as error:
            HandleLogs.write_error(error)
            message = 'Error creando el usuario ' + error.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def update_user(user_id, username, name, lastname):
        try:
            data = None
            message = None
            result = False
            sql = 'UPDATE users SET username = %s, name = %s, lastname = %s '\
            'WHERE id_user = %s'

            record = (username, name, lastname, user_id)

            sql_result = DataBaseHandle.ExecuteNonQuery(sql, record)

            if sql_result['result']:
                result = True
                data = sql_result['data']
                message = 'Datos actualizados con exito'
            else:
                message = 'No se pudo actualizar '
                HandleLogs.write_log(sql_result['message'])

        except Exception as error:
            HandleLogs.write_error(error)
            message = 'Error al actualizar datos de usuario ' + error.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def delete_user(user_id):
        try:
            data = None
            message = None
            result = False
            sql = 'DELETE FROM users WHERE id_user = %s'

            record = (user_id,)
            delete_result = DataBaseHandle.ExecuteNonQuery(sql, record)

            if delete_result['result']:
                result = True
                message = 'Usuario eliminado con exito'
            else:
                message = 'Error al eliminar el usuario'
                HandleLogs.write_log('Error eliminando el usuario -> ' + delete_result['message'] )
        except Exception as error:
            HandleLogs.write_error(error)
            message = 'Error al eliminar usuario ' + error.__str__()
        finally:
            return internal_response(result, data, message)