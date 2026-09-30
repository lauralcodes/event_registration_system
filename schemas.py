from marshmallow import Schema, fields

class EventSchema(Schema):
    event_id = fields.Str(required=True)
    name = fields.Str(required=True)
    date = fields.Str(required=True)
    time = fields.Str(required=True)
    price = fields.Float(required=True)


class RegistrationSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    eventId = fields.Str(required=True)


class LoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)