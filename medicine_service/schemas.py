from marshmallow import Schema, fields


class Medicine(Schema):
    id = fields.Str(required=False)
    name = fields.Str(required=True)
    dose = fields.Int(required=True)
    dose_unit = fields.Str(required=True)