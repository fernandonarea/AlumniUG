from src.api.Services.login_services import LoginServices

def load_routes(api):
    api.add_resource(LoginServices, '/api/login')