from src.api.Services.likes_service import LikesService
from src.api.Services.comments_service import CommentService

def load_routes(api):
    api.add_resource(LikesService,
                     '/likes/<int:id_post>',
                     '/likes/create/<int:user_id>/<int:post_id>',
                     '/likes/delete/<int:user_id>/<int:post_id>'
                     )

    api.add_resource(CommentService,
                     '/comments/<int:post_id>',
                     '/comments/create/<int:user_id>/<int:post_id>',
                     '/comments/delete/<int:user_id>/<int:id_comments>'
                     )