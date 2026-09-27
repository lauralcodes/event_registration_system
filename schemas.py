from marshmallow import Schema, fields


class EventSchema(Schema):
    event_id = fields.Str()
    name = fields.Str()
    date = fields.Str()
    time = fields.Str()
    price = fields.Float()


class RegistrationSchema(Schema):
    name = fields.Str()
    email = fields.Str()
    eventId = fields.Str()