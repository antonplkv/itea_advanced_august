import mongoengine as me

me.connect('Users_august')


class User(me.Document):
    first_name = me.StringField(min_length=1, max_length=256)
    surname = me.StringField(min_length=1, max_length=256)
    age = me.IntField(min_value=9, max_value=99)
    interests = me.ListField(me.StringField())

    def __str__(self):
        return f'{self.first_name} {self.age} {self.interests}'

#
# obj = User(first_name='Mark', surname='Zcukerbeg',
#            age=30, interests=['Reading', 'Programming'])
#
# print(obj.id)
# print(obj.first_name, obj.surname, obj.age, obj.interests)
# obj.save()
# obj.first_name = 'Carl'
# obj.surname = 'Johnson'
# obj.save()


# for user in User.objects:
# #    print(user.id, user.interests, user.first_name, user.age)
#     print(user)
#     user.age += 3
#     user.save()

# user = User.objects.create(
#     first_name='Gianna',
#     surname='Lowson',
#     age=20,
#     interests=['Music']
# )

user = User.objects(age__lte=30)
user2 = User.objects.get(id='5f74c594c8240f389b1c5545')
user3 = User.objects(age__ne=39)
users4 = User.objects(age__gt=10, age__lt=21, )
print(users4)
