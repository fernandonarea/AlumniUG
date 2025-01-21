from src.api.Services.foro_service import ForoService, getForoService
from src.api.Services.message_service import MessageService

def load_routes(api):
    api.add_resource(ForoService, '/foros', '/foros/create')
    api.add_resource(getForoService, '/foro/<int:id_forum>')
    api.add_resource(MessageService, '/addMessage/<int:forum_id>/<int:user_id>')