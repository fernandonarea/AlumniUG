from marshmallow import Schema, fields

class MessageRequest(Schema):
    message_content = fields.String(required=True)