from src.api.Services.friendship_service import FriendShipService, GetNumFriendsService

def load_routes(api):
    api.add_resource(FriendShipService, '/add/friend/<int:user_id>/<int:amigo_id>')
    api.add_resource(GetNumFriendsService, '/num/friends/<int:user_id>')