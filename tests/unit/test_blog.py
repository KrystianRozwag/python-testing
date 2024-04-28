import unittest
from blog import Blog

class TestBlog(unittest.TestCase):
    def test_create_blog(self):
        blog = Blog('Test', 'Test Author')
        
        self.assertEqual(blog.title, 'Test')
        self.assertEqual(blog.author, 'Test Author')
        self.assertListEqual(blog.posts, [])

    def test_repr(self):
        blog = Blog('Test', 'Test Author')
        blog2 = Blog('My Day', 'Krystian')
        self.assertEqual(blog.__repr__(), 'Test by Test Author (0 posts)')
        self.assertEqual(blog2.__repr__(), 'My Day by Krystian (0 posts)')

    def test_repr_multiple_posts(self):
        blog = Blog('Test', 'Test Author')
        blog.posts=['test']
        blog2 = Blog('My Day', 'Krystian')
        blog2.posts=['test','test2']

        self.assertEqual(blog.__repr__(), 'Test by Test Author (1 post)')
        self.assertEqual(blog2.__repr__(), 'My Day by Krystian (2 posts)')

