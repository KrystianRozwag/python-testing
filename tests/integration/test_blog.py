
from blog import Blog
from unittest import TestCase
from unittest.mock import patch

import app
class TestBlog(TestCase):
    def setUp(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}
    def test_create_post_in_blog(self):
        blog = app.blogs['Test']
        blog.create_post('Test Post', 'Test Content')

        self.assertEqual(len(blog.posts), 1)
        self.assertEqual(blog.posts[0].title, 'Test Post')
        self.assertEqual(blog.content, 'Test Content')

    def test_json_no_posts(self):
        blog = app.blogs['Test']
        expected = {
            'title': 'Test',
            'author': 'Test Author',
            'posts': []}
        self.assertDictEqual(blog.json(), expected)
    def test_json(self):
        blog = app.blogs['Test']
        blog.create_post('Test Post', 'Test Content')
        expected = {
            'title': 'Test',
            'author': 'Test Author',
            'posts': [
                {'title': 'Test Post',
                 'content': 'Test Content'}]}

        self.assertDictEqual(app.blogs[0].json(), expected)
    def test_delete_no_posts(self):
        blog = app.blogs['Test']
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                blog.delete_post()
                mocked_print.assert_called_with("Index out of range")
    def test_delete_existing_post(self):
        blog = app.blogs['Test']
        blog.create_post('Test Post', 'Test Content')
        with patch('builtins.input', return_value=0) as mocked_input:
            blog.delete_post()
            self.assertEqual(len(blog.posts), 0)
