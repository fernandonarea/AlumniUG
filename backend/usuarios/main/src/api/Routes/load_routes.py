from src.api.Services.user_service import UserService

def load_routes(api):
    api.add_resource(UserService, '/api/users', '/api/users/<int:user_id>')