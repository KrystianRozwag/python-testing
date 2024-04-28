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
        return post

    
    def json(self):
        return {"title": self.title, "author": self.author, "posts": self.posts}