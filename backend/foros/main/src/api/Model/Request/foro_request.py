from marshmallow import Schema, fields

class CreateForumRequest(Schema):
    forum_title = fields.String(required=True)
    forum_description = fields.String(required=True)