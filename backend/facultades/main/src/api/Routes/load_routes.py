from src.api.Services.faculties_service import UserService

def load_routes(api):
    api.add_resource(UserService, '/facultades')