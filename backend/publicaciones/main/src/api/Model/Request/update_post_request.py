from marshmallow import Schema, fields

class UpdatePostRequest(Schema):
    post_content = fields.String(required=True)