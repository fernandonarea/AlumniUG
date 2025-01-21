from datetime import datetime
from src.utils.general.logs import HandleLogs
from src.utils.database.connection_db import DataBaseHandle
from src.utils.general.response import internal_response

class PostComponent:
    @staticmethod
    def get_all_posts():
        try:
            result = False
            data = None
            message = None
            sql = '''
                    SELECT 
                        posts.id_post AS id_post,
                        users.name AS owner_name,
                        users.lastname AS owner_lastname,
                        posts.post_content,
                        posts.image,
                        posts.date,
                        COUNT(DISTINCT likes.user_id) AS total_likes,
                        COUNT(DISTINCT post_comments.user_id) AS total_comments
                        FROM 
                            posts
                        JOIN 
                            users ON posts.user_id = users.id_user
                        LEFT JOIN 
                            likes ON posts.id_post = likes.post_id
                        LEFT JOIN 
                            post_comments ON posts.id_post = post_comments.post_id
                        GROUP BY 
                            posts.id_post, users.name, users.lastname, posts.post_content, posts.image, posts.date
                        ORDER BY 
                            posts.date DESC;
                    '''
            sql_result = DataBaseHandle.getRecords(sql, 0)
            print(sql_result)

            if sql_result['result']:
                if sql_result['data']:
                    for post in sql_result['data']:
                        post['date'] = post['date'].strftime("%Y-%m-%d %H:%M:%S")
                    data = sql_result['data']
                    result = True
                    message = 'Publicaciones obtenidas con exito'
                else:
                    message ='No hay publicaciones'
            else:
                message = 'Error al traer las publicaciones'

        except Exception as error:
            HandleLogs.write_error(error)
            message = 'No se obtuvieron las publicaciones' + error.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def get_user_posts(id_user):
        try:
            result = False
            data = None
            message = None
            sql = 'SELECT * FROM posts WHERE user_id = %s ORDER BY posts.date desc'

            record = (id_user,)

            sql_result = DataBaseHandle.getRecords(sql, 0, record)
            print(sql_result)

            if sql_result['result']:
                if sql_result['data']:
                    for post in sql_result['data']:
                        post['date'] = post['date'].strftime("%Y-%m-%d %H:%M:%S")
                    data = sql_result['data']
                    result = True
                    message = 'Publicaciones obtenidas con exito'
                else:
                    message = 'No hay publicaciones'
            else:
                message = 'Error al traer las publicaciones'

        except Exception as error:
            HandleLogs.write_error(error)
            message = 'No se obtuvieron las publicaciones' + error.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def get_best_post(user_id):
        try:
            result = False
            data = None
            message = None
            sql = ''' 
                SELECT COUNT(DISTINCT likes.id_like) AS total_likes,
                    COUNT(DISTINCT post_comments.id_comments) AS total_comments
                FROM 
                    posts
                LEFT JOIN 
                    likes ON posts.id_post = likes.post_id
                LEFT JOIN 
                    post_comments ON posts.id_post = post_comments.post_id
                WHERE 
                    posts.user_id = %s;
            '''

            record = (user_id ,)

            sql_result = DataBaseHandle.getRecords(sql, 0, record)

            if sql_result['result']:
                result = True
                data = sql_result['data']
                message = 'post con mas interacciones obtenido'
            else:
                message = 'Error al obtener la publicacion'
        except Exception as error:
            HandleLogs.write_error(error)
            message = f'Error al crear publicación: {error.__str__()}'
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def create_post(user_id, post_content):
        try:
            result = False
            data = None
            message = None
            sql = 'INSERT INTO posts (user_id, post_content) VALUES (%s, %s)'
            record = (user_id, post_content)

            sql_result = DataBaseHandle.ExecuteNonQuery(sql, record)

            if sql_result['result']:
                result = True
                data = sql_result['data']
                message = 'Publicación creada con éxito'
            else:
                message = 'Error al crear la publicación'
                HandleLogs.write_log('Error creando publicación: ' + sql_result.get('message', 'Sin detalles'))

        except Exception as error:
            HandleLogs.write_error(error)
            message = f'Error al crear publicación: {error.__str__()}'
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def updatePost(id_post, post_content):
        try:
            result = False
            data = None
            message = None
            sql='UPDATE posts SET post_content = %s WHERE id_post = %s'

            record = (post_content, id_post)

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
            message = 'Error al actualizar publicación' + error.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def deletePost(id_post):
        try:
            result = False
            data = None
            message = None
            sql = 'DELETE FROM posts WHERE id_post = %s'

            record = (id_post,)

            sql_result = DataBaseHandle.ExecuteNonQuery(sql, record)

            if sql_result['result']:
                result = True
                message ='Publicación Eliminada con Exito'
            else:
                message = 'Error al eliminar publicacion'
                HandleLogs.write_log('Error eliminando publicacion ' + sql_result['message'])

        except Exception as error:
            HandleLogs.write_error(error)
            message = 'Error al eliminar publicación' + error.__str__()
        finally:
            return internal_response(result, data, message)