from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post

# Create your tests here.

class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_post_list(self):
        # 블로그로 들어간다
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
