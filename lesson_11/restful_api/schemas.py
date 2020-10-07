from marshmallow import Schema, fields, validate, validates


class UserSchema(Schema):
    id = fields.String(read_only=True)
    first_name = fields.String(validate=validate.Length(min=2, max=256))
    last_name = fields.String(validate=validate.Length(min=2, max=256))
    # gender = fields.String(validate=validate.OneOf(['Male', 'Female']))
    unique_number = fields.Int()

    # @validates('unique_number')
    # def validate_unique_number(self, value):
    #     User.objects(unique=value)