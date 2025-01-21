from marshmallow import Schema, fields

class CreateUserRequest(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)
    name = fields.String(required=True)
    lastname = fields.String(required=True)
    id_facultad = fields.Integer(required=True)