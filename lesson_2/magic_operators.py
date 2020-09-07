class Post:

    def __init__(self, title, views):
        self.title = title
        self.views = views

    def increase_likes(self, num):
        self.views += num

    def __add__(self, other):
        title = self.title + other.title
        views = self.views + other.views
        return Post(title, views)

    def __str__(self):
        return f'Post title {self.title}, post views - {self.views}'

    def __len__(self):
        return self.views


class SocialNetworkPost(Post):

    def __init__(self, title, views, likes):
        super().__init__(title, views)
        self.likes = likes

    def __add__(self, other):
        post = super().__add__(other)
        return SocialNetworkPost(post.title, post.views, self.likes + other.likes)

    def __str__(self):
        base_str = super().__str__()
        new_str = base_str + ' num of likes - ' + str(self.likes)
        return new_str


post1 = SocialNetworkPost('photo', 40, 24)
post2 = SocialNetworkPost('album', 200, 150)
result = post1 + post2



print(result)
news = Post('Breaking news', 100)
weather = Post('Weather forecast', 500)
ecologic = Post('Ecologic news', 70)

# result = news + weather
# print(result.title, result.views)
# result = result + ecologic
# print(result.title, result.views)

result = news + weather + ecologic

# news + weather == news.__add__(weather)
print(result)
print(len(result))

print(dir(result))