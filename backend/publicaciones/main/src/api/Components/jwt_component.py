from src.utils.database.connection_db import DataBaseHandle
from src.utils.general.logs import HandleLogs
from src.utils.general.config import Parametros
import pytz
from datetime import timezone
import jwt

class JWTComponent:
    @staticmethod
    def token_validate(token):
        try:
            payload = jwt.decode(token, Parametros.secret_jwt, algorithms=['HS256'])

            return {
                'username': payload.get('username'),
                'user_id': payload.get('user_id')
            }

        except jwt.InvalidTokenError as err:
            HandleLogs.write_error(f"Error en la validacion: {err}")
            return None
        except Exception as error:
            HandleLogs.write_error(f"Error inesperado al validar el token: {error}")
            return None