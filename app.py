blogs = dict()
from blog import Blog
MENU_PROMPT = 'Enter "c" to create a new blog, "l" to list blogs, "r" to read one, "p" to create a post or "q" to quit: '




def menu():
    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)

def print_blogs():
    for key, blog in blogs.items():
        print(f'{key} - {blog}')

def ask_create_blog():
    title = input(f'Enter your blog title: ')
    author = input(f'Enter your blog author: ')
    blogs[title] = Blog(title, author)

def ask_read_blog():
    title = input(f'Enter your blog title: ')

    blog = blogs[title]
    if blog is not None:
        print_posts(blog)
    else:
        print('Blog does not exist')

def print_posts(blog):
    for post in blog.posts:
        print_post(post)
def print_post(post):
    print(f"Title: {post.title}, content: {post.content}")
def ask_create_post():
    blog_name = input(f'Enter your blog title: ')

    blog = blogs[blog_name]
    if blog is not None:
        title = input(f'Enter your post title: ')
        content = input(f'Enter your post content: ')
        blog.create_post(title, content)
    else:
        print('Blog does not exist')
