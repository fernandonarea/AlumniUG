from src.utils.general.logs import HandleLogs
from src.utils.database.connection_db import DataBaseHandle
from src.utils.general.response import internal_response

class FacultiesComponent:
    @staticmethod
    def get_faculties():
        try:
            data = None
            message = None
            result = True
            sql = 'SELECT * FROM faculties'

            sql_result = DataBaseHandle.getRecords(sql, 0)

            if sql_result['result']:
                data = sql_result['data']
                result = True
                message = 'Facultades obtenidas con exito'
            else:
                message = 'Error al traer los facultades'

        except Exception as error:
            HandleLogs.write_error(error)
            message = 'Error creando el usuario ' + error.__str__()
        finally:
            return internal_response(result, data, message)