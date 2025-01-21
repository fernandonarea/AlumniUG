from marshmallow import Schema,fields

class CreatePostRequest(Schema):
    post_content = fields.String(required=True)

