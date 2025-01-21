from src.utils.general.logs import HandleLogs
from src.utils.database.connection_db import DataBaseHandle
from src.utils.general.response import internal_response

class MessageComponent:
    @staticmethod
    def post_messages(forum_id, user_id, message_content):
        try:
            data = None
            result = False
            message = None
            sql = 'INSERT INTO forum_messages (forum_id, user_id, message_content) '\
            'VALUES (%s, %s, %s)'

            record = (forum_id, user_id, message_content)

            sql_result = DataBaseHandle.ExecuteNonQuery(sql, record)

            if sql_result['result']:
                data = sql_result['data']
                result = True
                message = 'Mensaje creado con exito'
        except Exception as error:
            HandleLogs.write_error(error)
            message = 'Error creando mensaje ' + error.__str__()
        finally:
            return internal_response(result, data, message)