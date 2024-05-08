from post import Post
class Blog:
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []
    
    def __repr__(self):
        return (f'{self.title}'
                f' by {self.author}'
                f' ({len(self.posts)}'
                f' post{'' if len(self.posts) == 1 else 's'})')
    
    def create_post(self, title, content):
        post = Post(title, content)
        self.posts.append(post)
    def delete_post(self):
        index = int(input('Enter index of post to delete: '))
        try:
            self.posts.pop(index)
        except IndexError:
            print('Index out of range')
    
    def json(self):
        return {"title": self.title, "author": self.author, "posts": [post.json() for post in self.posts]}