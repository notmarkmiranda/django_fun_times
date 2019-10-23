from django.test import SimpleTestCase
from unittest.mock import patch

from .services import ArticlesService

def methodStub(self, slug):
    return slug

class ArticlesIndexTest(SimpleTestCase):
    @patch.object(ArticlesService, 'find_featured_article', methodStub)
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)