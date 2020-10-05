import mongoengine as me

me.connect('rest_api_users')


class User(me.Document):
    first_name = me.StringField(min_length=2, max_length=256)
    last_name = me.StringField(min_length=2, max_length=256)