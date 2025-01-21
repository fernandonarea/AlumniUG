from src.utils.general.logs import HandleLogs
from src.utils.database.connection_db import DataBaseHandle
from src.utils.general.response import internal_response

class FriendShipComponent:
    @staticmethod
    def add_friend(user_id, amigo_id):
        try:
            data = None
            message = None
            result = False

            sql_insert = 'INSERT INTO friends (user_id, amigo_id) VALUES (%s, %s)'
            record = (user_id, amigo_id)

            sql_result = DataBaseHandle.ExecuteNonQuery(sql_insert, record)

            if sql_result['result']:
                result = True
                message = 'Amigos añadidos con éxito'
            else:
                message = 'Error al añadir el amigo'
                HandleLogs.write_log('Error añadiendo amigo -> ' + sql_result['message'])

        except Exception as error:
            HandleLogs.write_error(error)
            message = 'Error al añadir amigo: ' + error.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def get_num_friends(user_id):
        try:
            result = False
            data = None
            message = None
            sql = """
                SELECT 
                    (SELECT COUNT(*) FROM friends WHERE user_id = %s) + 
                    (SELECT COUNT(*) FROM friends WHERE amigo_id = %s ) AS total_amigos;
                """

            record = (user_id, user_id)

            sql_result = DataBaseHandle.getRecords(sql, 0, record)

            if sql_result['result']:
                result = True
                data = sql_result['data']
                message = 'Numero de amigos obtenidos'
            else:
                message = 'numero de amigos no obtenidos'
        except Exception as error:
            HandleLogs.write_error(error)
            message = 'Error al añadir amigo: ' + error.__str__()
        finally:
            return internal_response(result, data, message)

