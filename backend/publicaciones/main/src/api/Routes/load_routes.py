from src.api.Services.post_service import PostService, UserPostService, TrendingPost

def load_routes(api):
    api.add_resource(PostService,
                     '/posts',
                     '/posts/create/<int:user_id>',
                     '/posts/update/<int:id_post>',
                     '/posts/delete/<int:id_post>'
    )


    api.add_resource(UserPostService, '/posts/user/<int:id_user>')

    api.add_resource(TrendingPost, '/posts/best/<int:user_id>')