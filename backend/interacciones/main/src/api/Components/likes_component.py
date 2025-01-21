from src.utils.general.logs import HandleLogs
from src.utils.database.connection_db import DataBaseHandle
from src.utils.general.response import internal_response

class LikesComponent:
    @staticmethod
    def get_interactions(id_post):
        try:
            result = False
            data = None
            message = None
            sql = '''SELECT posts.id_post, COUNT(likes.user_id) AS total_likes 
                            FROM posts 
                            LEFT JOIN likes ON posts.id_post = likes.post_id 
                            WHERE posts.id_post = %s 
                            GROUP BY posts.id_post'''

            record = (id_post, )

            sql_result = DataBaseHandle.getRecords(sql, 1, record)

            if sql_result['result']:
                result = True
                data = sql_result['data']
                message = 'Interacciones obtenidas con exito'
            else:
                message = 'Interacciones no obtenidas'
                HandleLogs.write_log('Error al obtener las interacciones ' + sql_result['message'])

        except Exception as error:
            HandleLogs.write_error(error)
            message = 'No se obtuvieron las interacciones' + error.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def create_interaction(user_id, post_id):
        try:
            result = False
            data = None
            message = None
            sql = 'INSERT INTO likes (post_id, user_id) VALUES (%s, %s)'

            record = (post_id, user_id)

            sql_result = DataBaseHandle.ExecuteNonQuery(sql, record)

            if sql_result['result']:
                result = True
                data = sql_result['data']
                message = 'Interaccion creada con exito'
            else:
                message = 'Interaccion no creada'
                HandleLogs.write_log('Error al crear la interaccion ' + sql_result['message'])

        except Exception as error:
            HandleLogs.write_error(error)
            message = 'No se obtuvieron las publicaciones' + error.__str__()
        finally:
            return internal_response(result, data, message)


    @staticmethod
    def delete_interaction(user_id, post_id):
        try:
            result = True
            data = None
            message = None
            sql = 'DELETE FROM likes WHERE user_id = %s AND post_id = %s'

            record = (user_id, post_id)

            sql_result = DataBaseHandle.ExecuteNonQuery(sql, record)

            if sql_result['result']:
                result = True
                data = sql_result['data']
                message = 'Interaccion eliminada con exito'
            else:
                message = 'No se pudo eliminar la interaccion'
                HandleLogs.write_log('No se pudo eliminar la interaccion')

        except Exception as error:
            HandleLogs.write_error(error)
            message = 'No se obtuvieron las publicaciones' + error.__str__()
        finally:
            return internal_response(result, data, message)


