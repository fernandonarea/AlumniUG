from src.utils.general.logs import HandleLogs
from src.utils.database.connection_db import DataBaseHandle
from src.utils.general.response import internal_response

class ForosComponent:
    @staticmethod
    def get_foros():
        try:
            result = False
            data = None
            message = None
            sql = "SELECT * FROM forums"

            result = DataBaseHandle.getRecords(sql, 0)

            if result['result']:
                data = result['data']
                result = True
                message = 'Foros obtenidos con exito'
            else:
                message = 'No se obtuvieron los foros'
        except Exception as error:
            HandleLogs.write_error(error)
            message = 'Error obteniendo foros ' + error.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def create_foro(forum_title, forum_description):
        try:
            result = False
            data = None
            message = None
            sql = 'INSERT INTO forums (forum_title, forum_description) '\
            'VALUES (%s, %s)'

            record = (forum_title, forum_description)

            sql_result = DataBaseHandle.ExecuteNonQuery(sql, record)

            if sql_result['result']:
                result = True
                data = sql_result['data']
                message = 'Foro Creado con exito'
            else:
                message = 'Error al crear foro '
                HandleLogs.write_log('Error creando al foro -> ' + sql_result['message'])
        except Exception as error:
            HandleLogs.write_error(error)
            message = 'Error creando foro ' + error.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def get_foro(id_forum):
        try:
            data= None
            result= False
            message= None
            sql = '''
                SELECT 
                    f.id_forum, 
                    f.forum_title, 
                    f.forum_description, 
                    m.id_message, 
                    m.user_id, 
                    u.username, 
                    CONCAT(u.name, ' ', u.lastname) AS user_full_name, 
                    m.message_content
                FROM forums f
                LEFT JOIN forum_messages m ON f.id_forum = m.forum_id
                LEFT JOIN users u ON m.user_id = u.id_user
                WHERE f.id_forum = %s;
            '''
            record = (id_forum, )

            sql_result = DataBaseHandle.getRecords(sql, 0, record)

            if sql_result['result']:
                data = sql_result['data']
                result = True
                message = 'Foro obtenido'
            else:
                message = 'Error al obtener foro '
                HandleLogs.write_log('Error obteniendo foro -> ' + sql_result['message'])

        except Exception as error:
            HandleLogs.write_error(error)
            message = 'Error obteniendo foro ' + error.__str__();
        finally:
            return internal_response(result, data, message)
