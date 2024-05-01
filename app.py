blogs = dict()

MENU_PROMPT = 'Enter "c" to create a new blog, "l" to list blogs, "r" to read one, "p" to create a post or "q" to quit: '
def menu():
    print_blogs()
    selection = input(MENU_PROMPT)


def print_blogs():
    for key, blog in blogs.items():
        print(f'{key} - {blog}')