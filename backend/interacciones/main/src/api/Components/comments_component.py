from src.utils.general.logs import HandleLogs
from src.utils.database.connection_db import DataBaseHandle
from src.utils.general.response import internal_response

class CommentsComponent:
    @staticmethod
    def get_comments(post_id):
        try:
            result = False
            data = None
            message = None
            sql = """
                SELECT 
                    post_comments.id_comments AS comment_id,
                    users.name AS owner_name,
                    users.lastname AS owner_last_name,
                    post_comments.comment_text AS text
                FROM
                    post_comments
                JOIN
                    users ON post_comments.user_id = users.id_user
                WHERE
                    post_comments.post_id = %s;
            """

            record = (post_id, )

            sql_result = DataBaseHandle.getRecords(sql, 0, record)

            if sql_result['result']:
                result = True
                data = sql_result['data']
                message = 'Comentarios obtenidas con exito'
            else:
                message = 'Comentarios no obtenidos'
                HandleLogs.write_log('Error al obtener los Comentarios ' + sql_result['message'])

        except Exception as error:
            HandleLogs.write_error(error)
            message = 'No se obtuvieron los comentarios' + error.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def create_comment(user_id, post_id, comment_text):
        try:
            result = False
            data = None
            message = None
            sql = 'INSERT INTO post_comments (user_id, post_id, comment_text) VALUES (%s, %s, %s)'

            record = (user_id, post_id, comment_text)

            sql_result = DataBaseHandle.ExecuteNonQuery(sql, record)
            print(sql_result)

            if sql_result['result']:
                result = True
                data = sql_result['data']
                message = 'Comentario creado con éxito'
            else:
                message = 'Error al crear la comentario'
                HandleLogs.write_log('Error creando comentario: ' + sql_result.get('message', 'Sin detalles'))

        except Exception as error:
            HandleLogs.write_error(error)
            message = 'Error en el componente' + error.__str__()
        finally:
            return internal_response(result, data, message)


    @staticmethod
    def delete_comment(user_id, id_comments):
        try:
            result = True
            data = None
            message = None
            sql = 'DELETE FROM post_comments WHERE user_id = %s AND id_comments = %s'

            record = (user_id, id_comments)

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