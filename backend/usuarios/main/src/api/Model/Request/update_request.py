from marshmallow import Schema, fields

class UpdateUserRequest(Schema):
    username = fields.String(required=True)
    name = fields.String(required=True)
    lastname = fields.String(required=True)