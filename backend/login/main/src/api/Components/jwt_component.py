from src.utils.general.logs import HandleLogs
from src.utils.general.config import Parametros
from datetime import datetime, timedelta
import pytz
import jwt

class JWTComponent:
    @staticmethod
    def token_generate(p_user):
        try:
            timezone = pytz.timezone('America/Guayaquil')
            payload = {
                'iat': datetime.now(tz=timezone),
                'exp': datetime.now(tz=timezone) + timedelta(minutes=15),
                'username': p_user,
            }
            return jwt.encode(payload, Parametros.secret_jwt, 'HS256')
        except Exception as err:
            HandleLogs.write_error(err)
            return None
