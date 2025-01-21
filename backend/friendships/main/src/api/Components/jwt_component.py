from src.utils.general.logs import HandleLogs
from src.utils.general.config import Parametros
import jwt

class JWTComponent:
    @staticmethod
    def token_validate(token):
        try:
            respuesta = None
            respuesta_jwt = jwt.decode(token, Parametros.secret_jwt, algorithms=['HS256'])
            print(respuesta_jwt)

            if respuesta_jwt is not None:
                respuesta = True

        except Exception as err:
            HandleLogs.write_log('Ocurrio un error al validar el token' + str(token))
            HandleLogs.write_log(err)
        finally:
            return respuesta