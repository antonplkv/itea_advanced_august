import mongoengine as me
import datetime

me.connect('new_author')


class News(me.Document):
    title = me.StringField(required=True, min_length=4, max_length=256)
    body = me.StringField(required=True, min_length=16, max_length=4096)
    created_at = me.DateTimeField(default=datetime.datetime.now)
    author = me.ReferenceField('Author')

    def __str__(self):
        return f'New {self.title} by author {self.author}'


class Author(me.Document):
    first_name = me.StringField(min_length=2, max_length=128, required=True)
    last_name = me.StringField(min_length=2, max_length=128)
    age = me.IntField(min_value=18)
    rating = me.IntField(min_value=0, max_value=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def news(self):
        """
        :return: Author`s news
        """
        print(self)
        return News.objects(author=self)

    def increase_rating(self, value):
        self.rating += value
        self.save()


if __name__ == '__main__':
    # new = News.objects.get(id='5f7b47d9aba741fffbf34fbc')
    # print(new.id, new.created_at)
    # print(new.author.first_name, new.author.rating)
    # john_doe = Author.objects.get(first_name='John')
    # michael_johnsons = Author.objects.create(first_name='Michael', last_name='Johnsons', rating=90, age=30)
    # n1 = News.objects.create(title='IT news', body='.' * 20, author=michael_johnsons)
    # john_doe = Author.objects.get(first_name='John')
    # john_doe.increase_rating(50)
    # print(john_doe.news)
    # michael = Author.objects.get(first_name='Michael')
    # michael.increase_rating(-30)
    # print(michael.news)

    author = {
        'first_name': 'Ginni',
        'last_name': 'Doe',
        'age': 20,
        'rating': 99
    }
    Author.objects.create(**author)


