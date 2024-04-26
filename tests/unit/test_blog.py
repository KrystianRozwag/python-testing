import unittest
from blog import Blog

class TestBlog(unittest.TestCase):
    def test_create_blog(self):
        blog = Blog('Test', 'Test Author')
        
        self.assertEqual(blog.title, 'Test')
        self.assertEqual(blog.author, 'Test Author')
        self.assertListEqual(blog.posts, [])