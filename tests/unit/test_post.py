from unittest import TestCase
from post import Post

class TestPost(TestCase):
    def test_create_post(self):
        post = Post('Test Title', 'Test Content')
        
        self.assertEqual(post.title, 'Test Title')
        self.assertEqual(post.content, 'Test Content')